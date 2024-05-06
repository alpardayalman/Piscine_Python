import datetime
import time

def format_float_with_commas(number):
    """Formats a float number with commas every 3 decimals.

    Args:
        number: The float number to format.

    Returns:
        A string representation of the formatted number with commas.
    """

    formatted_number = f"{number:.4f}"
    parts = formatted_number.split(".")

    integer_part = parts[0][::-1]
    formatted_integer = ",".join(integer_part[i:i+3] for i in range(0, len(integer_part), 3))[::-1]

    return f"{formatted_integer}.{parts[1]}"

if __name__ == "__main__":
    now = datetime.datetime.now()

    formatted_time = now.strftime("%b %d %Y")
    current_time = time.time()
    epoch_start_time = time.mktime((1970, 1, 1, 0, 0, 0, 0, 0, 0))

    time_since_epoch = current_time - epoch_start_time
    t = format_float_with_commas(time_since_epoch)
    print(f'Seconds since January 1, 1970: {t} or {time_since_epoch:.2e} in scientific notation')
    print(formatted_time)
