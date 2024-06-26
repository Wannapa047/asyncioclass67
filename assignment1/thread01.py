# running a function in another thread
from time import sleep, ctime
from threading import Thread

#a custom funtion that blocks for a moment
def task():
    #block for a moment
    sleep(1)
    #display a message
    print(f'{ctime()} This is from another thread')
    
#Create a Thread
thread = Thread(target=task)
#run the thread
thread.start()
#wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()