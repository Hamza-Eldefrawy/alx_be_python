from datetime import datetime, timedelta

def display_current_datetime():
    """
    Gets the current time, formats it, and prints it.
    """
    # 1. Save the current date inside a current_date variable
    current_date = datetime.now()
    
    # 2. Format the date to "YYYY-MM-DD HH:MM:SS"
    # We use the formatted string we learned earlier
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_date}")
    
    # We return this so other functions could use it if they wanted to
    return current_date

def calculate_future_date():
    """
    Asks the user for a number of days, adds it to the current date,
    and prints the result.
    """
    # 1. Prompt the user to enter a number of days
    # We wrap this in int() because input() returns a string by default
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Get the current date again to do the math
        current_date = datetime.now()
        
        # 2. Calculate the future date using timedelta
        # timedelta represents a "duration" or difference in time
        future_date = current_date + timedelta(days=days_to_add)
        
        # 3. Format and print the future date (YYYY-MM-DD)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
        
    except ValueError:
        # This runs if the user types text instead of a number
        print("Error: Please enter a valid whole number.")
