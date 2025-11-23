from datetime import datetime, date, timedelta
def display_current_datetime():
    current_date = date.today()
    print("Current date and time: ", datetime.now())

def calculate_future_date():
    number_of_days = input("Enter the number of days to add to the current date: ")
    print("Future date: ", timedelta(days = number_of_days))
