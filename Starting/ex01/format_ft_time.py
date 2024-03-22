import datetime

if __name__ == "__main__":
    now = datetime.datetime.now()
    start_time = datetime.datetime(1970, 1, 1)

    formatted_time = now.strftime("%Y %m %d")

    time_elapsed = now - formatted_time
    print(time_elapsed)
    print(f'Seconds since January 1, 1970: {10} or {10} in n scientific notation')
    print(formatted_time)