from datetime import datetime, date, timedelta


def display_current_datetime():
    now = datetime.now()
    print("Current date and time: ", now.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date():
    number_of_days = input("Enter the number of days to add to the current date: ")
    future_date = (datetime.now() + timedelta(days = number_of_days)).strftime("%Y-%m-%d")
    print("Future date: ", future_date)
