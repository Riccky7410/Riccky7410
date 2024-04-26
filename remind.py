import subprocess
def send_notification():
    # Replace this line with your actual notification message
    notification_message = "This is your custom notification message."

    # Use curl to send the notification
    try:
        subprocess.run(["curl", "-d", "Vo Cua U Bi Ngo Do U Biet Ko" , "66-228-52-70.ip.linodeusercontent.com/First"])
        print("Reminder sent successfully!")
    except FileNotFoundError:
        print("curl is not installed. Please install it.")

if __name__ == "__main__":
    send_notification()
