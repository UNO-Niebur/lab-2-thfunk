#FutureTime.py
#Name: Taran Funk
#Date: 2/1/2026
#Assignment: Lab 2 - Future Time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  #TODO:
  #Ask user for hours
  inputHours = int(input("Enter number of hours to add: "))

  #Ask user for minutes
  inputMinutes = int(input("Enter number of minutes to add: "))

  #Calculate the time after the user-supplied time has passed.
  futureHour = (currentHour + ((currentMinute + inputMinutes) // 60) + inputHours) % 24
  futureMinute = (currentMinute + (inputMinutes % 60)) % 60

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print("In " + str(inputHours) + " hours and " + str(inputMinutes) + " minutes the time will be " + str(futureHour).zfill(2) + ":" + str(futureMinute).zfill(2))


if __name__ == '__main__':
  main()
