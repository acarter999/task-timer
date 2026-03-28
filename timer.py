import time


def start_timer(minutes):
    total_seconds = minutes * 60

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("\nTime is up!")


def main():
    try:
        minutes = int(input("Enter countdown time in minutes: "))

        if minutes <= 0:
            print("Please enter a number greater than 0.")
            return

        start_timer(minutes)

    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
