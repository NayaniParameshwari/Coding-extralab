# This script will generate the ranodm data

import time, datetime, traceback, random, sys, os

def generate_data(delay : int) -> (None):
    count = 1
    next_time = time.time() + delay
    while True:
    # for i in range(60):
        time.sleep(max(0, next_time - time.time()))
        try:
            current_datetime = datetime.datetime.now()
            current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            data1 = round(random.uniform(0, 10), 2)
            data2 = round(random.uniform(0, 10), 2)
        except Exception:
            traceback.print_exc()

        value_dict = {"timedate": current_datetime, "value1" : data1, "value2" : data2}

        next_time += (time.time() - next_time) // delay * delay + delay
        
        print(value_dict)
        # count += 1
        # if count == 10:
        #     break

if __name__ == '__main__':
    try:
        generate_data(1)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)