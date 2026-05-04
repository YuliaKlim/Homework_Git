import logging
from datetime import datetime

def analyze_hb_log(input_file, log_file, key):
    filtered_log = []
    with open(input_file, 'r') as f:
        for line in f:
            if key in line:
                filtered_log.append(line.strip())

    # Setting up the logger
    logging.basicConfig(filename=log_file, filemode='w', format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)

    # Analysis of filtered rows
    last_ts = None

    with open(log_file, 'w') as log_file:
        for line in filtered_log:

            # Extracting time
            ts_pos = line.find('Timestamp ')
            ts_str = line[ts_pos + 10: ts_pos + 18]
            current_ts = datetime.strptime(ts_str, '%H:%M:%S')

            if last_ts:
                # Let's calculate the difference
                diff_ts = (current_ts - last_ts).total_seconds() % 86400

                # Logging via special conditions
                if 31 < diff_ts < 33:
                    logging.warning(f'WARNING: Heartbeat delay {diff_ts}s at {ts_str}\n')
                elif diff_ts >= 33:
                    logging.error(f'ERROR: Heartbeat delay {diff_ts}s at {ts_str}\n')

            # Save the current time as "previous" for the next lap
            last_ts = current_ts

analyze_hb_log('hblog.txt', 'hb_test.log', 'Key TSTFEED0300|7E3E|0400')

