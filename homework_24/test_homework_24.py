import pytest
import logging
from flask import Flask, jsonify, request
from requests.auth import HTTPBasicAuth
import requests

logger = logging.getLogger('cars_search_logger')
logger.setLevel(logging.INFO)
logger.handlers.clear()

logger.propagate = True

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('test_cars_search.log', mode='w', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

BASE_URL = "http://127.0.0.1:8080"

class TestCarsSearch:
    # Authorization fixture
    @pytest.fixture(scope='class', autouse=True)
    def session(self):
        logger.info(f'Authorization in the system')
        s = requests.Session()
        auth_data = HTTPBasicAuth('test_user', 'test_pass')

        try:
            response = s.post(f'{BASE_URL}/auth', auth=auth_data)
            if response.status_code == 200:
                token = response.json().get('access_token')
                s.headers.update({'Authorization': f'Bearer {token}'})
                logger.info(f'The token has been successfully received and added to the Session')
                yield s
            else:
                logger.error(f'Authorization failed! Status: {response.status_code}')
                pytest.fail(f'Could not authenticate user')
        finally:
            logger.info(f'The session is closed')
            s.close()

    # Parameterized test
    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 10),
        ("engine_volume", 3),
        ("brand", 25),
        (None, 5)
    ])
    def test_cars_query(self, session, sort_by, limit):
        logger.info(f'Running the test: sort_by={sort_by}, limit={limit}')

        params = {}
        if sort_by: params['sort_by'] = sort_by
        if limit: params['limit'] = limit

        response = session.get(f'{BASE_URL}/cars', params=params)
        data = response.json()

        logger.info(f'API response: status {response.status_code}, records received: {len(data)}')

        # Verifications
        assert response.status_code == 200
        assert isinstance(data, list), 'API should return a list'

        expected_limit = min(limit, 25)
        assert len(data) == expected_limit, f'Expected {expected_limit} entries, received {len(data)}'

        # If we sorted by price, we'll check that the first item is cheaper than the last one
        if sort_by == "price" and len(data) > 1:
            assert data[0]['price'] <= data[-1]['price'], "Sorting by price didn't work"

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])