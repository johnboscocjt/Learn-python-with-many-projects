# alarm clock
import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    # Use a default sound file path, you can modify this to your actual sound file path
    sound_file = "alarms/myalarm.mp3"  
    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        # time to update every second
        time.sleep(1)
        
        # prevent the infinite loop
        # is_running = False
        
        # if current time is equal to alarm time, trigger the alarm
        if current_time == alarm_time:
            print("Wake Up! 😴")
            
            # play the alarm sound, initialize mixer module for playing sounds
            pygame.mixer.init()
            # load the sound file
            pygame.mixer.music.load(sound_file)
            # play the alarm mp3
            pygame.mixer.music.play()
            
            
            # Add a small delay to let the sound play
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            
            is_running = False

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)