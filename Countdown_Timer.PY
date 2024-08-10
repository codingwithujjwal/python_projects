

import time


def countdown(user_time):
   while user_time >= 0:
       mins, secs = divmod(user_time, 60) # Convert seconds to minutes and seconds
       timer = '{:02d}:{:02d}'.format(mins, secs) # Format the time as MM:SS
       print(timer, end='\r') # Print the time, use '\r' overwrite the same line
       time.sleep(1) # Wait for 1 second 
       user_time -= 1 # Decrement the time by 1 second
   print('Lift off!') # Print the message when the countdown is complete


if __name__ == '__main__':
   user_time = int(input("Enter a time in seconds: ")) # Get the user input
   countdown(user_time) # Call the coundown function
