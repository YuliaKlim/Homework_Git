import json

# Створюємо функцію перевірки валідності json-файлів
def json_valid_or_not(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
        return True
    except FileNotFoundError:
        print(f"File not found")
        return False
    except json.JSONDecodeError as e:
        print(f"File error! Broken here: {e}")
        return False

# Робимо перевірку для файлів
if json_valid_or_not('localizations_en.json'):
    print("JSON 'localizations_en' is valid")
else:
    print("JSON 'localizations_en' is not valid")

if json_valid_or_not('localizations_ru.json'):
    print("JSON 'localizations_ru' is valid")
else:
    print("JSON 'localizations_ru' is not valid")

if json_valid_or_not('login.json'):
    print("JSON 'login' is valid")
else:
    print("JSON 'login' is not valid")

if json_valid_or_not('swagger.json'):
    print("JSON 'swagger' is valid")
else:
    print("JSON 'swagger' is not valid")