
import datetime , time
def get_current_datetime():
    now = datetime.datetime.now()
    
    clean_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:",clean_time)

def calculate_date_difference(date_obj2,date_obj):

    differnce = date_obj2 - date_obj

    total_days = abs(differnce.days)
    
    print(f"{total_days} Days")

def format_custom_date(date_obj, fmt_choice):
    if fmt_choice == 1:
        return date_obj.strftime("%d/%m/%Y")
    elif fmt_choice == 2:
        return date_obj.strftime("%Y-%m-%d")
    elif fmt_choice == 3:
        return date_obj.strftime("%d %B, %Y")
    elif fmt_choice == 4:
        return date_obj.strftime("%d-%m-%Y %H:%M:%S")
    else:
        return None

    
def start_stopwatch():
    input("\nPress ENTER to START the stopwatch...")
    start_time = time.time()
    print("Stopwatch started! Running...")

    input("Press ENTER to STOP the stopwatch...")
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"\nElapsed Time: {elapsed_time:.2f} seconds")

def start_countdown(seconds):
    print(f"\nCountdown started for {seconds} seconds...")
    while seconds > 0:
        print(f"Time remaining: {seconds}s", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\nTime's up! Alert! Alert! ⏰")