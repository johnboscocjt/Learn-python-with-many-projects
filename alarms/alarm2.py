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
            
            try:
                # play the alarm sound
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                
                # Wait for the sound to finish playing
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                    
            except pygame.error as e:
                print(f"Error playing sound: {e}")
                print("Alarm triggered but sound could not be played")
            
            is_running = False

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)