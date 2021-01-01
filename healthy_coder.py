from pygame import mixer
from datetime import datetime
from time import time

def musicloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        input_user  = input()
        if input_user == stopper:
            mixer.music.stop()
            break

# for writing into the file the exact date and time into file.
def user_act(msg):
    with open("myactivity.txt",'a') as f:
        f.write(f"{msg} {datetime.now()}\n\n")


#main function
if __name__ == '__main__':
    init_water = time() # for drinking water
    init_tsleep = time() #for taking sleep
    init_social = time()# for using relaxing or using social media

    a=int(input(" Hello sir enter at what interval do you prefer to drink water (please enter in minutes) "))
    b=int(input("Hello sir enter at what interval do you prefer to chill or use social media app (please enter in minutes) "))
    c=int(input("Hello sir enter at what interval do you prefer to sleep (please enter in minutes)"))

    # give the time for each alarm
    water = a*60
    social = b*60
    sleep = c*60


    while True:
        if time() - init_water>water:
            print("Hey Ansh !! it's time have some water and to stop the music press enter 'done'")
            musicloop("water.mp3.mp3",'done')
            init_water=time()
            user_act("Ansh drank the water  -- ")

        if time()-init_social>social:
            print("Lets check some social media or chill , and to stop the music enter 'done'")
            musicloop("water.mp3.mp3",'done')
            init_social=time()
            user_act("Ansh took a chill break at  -- ")

        if time()-init_tsleep>sleep:
            print("Let's sleep bro for some time and to stop the music enter 'done'")
            musicloop("water.mp3.mp3",'done')
            init_tsleep=time()
            user_act("Ansh slept at -- ")

