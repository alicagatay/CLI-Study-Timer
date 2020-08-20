import time
import os


# The notifier function
def notify(title, message):
    t = '-title {!r}'.format(title)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t])))



def pomodoro():
    t = 30
    count = int(input("How many pomodoro sessions do you wanna do: "))

    while(count > 0):
        print("Work for 25 minutes.")
        notify(title = 'Session Change', message  = 'Get into work!')
        print()
        print()
        while(t > -1):
            t = t - 1
            time.sleep(60)

            if(t == 5):
                print("Take a break for 5 minutes.")
                notify(title = 'Session Change', message  = 'Take a break')
                print()
                print()

        count = count - 1
        t = 30
    print("Pomodoro session finished.")
    notify(title = 'Work session finished', message  = 'Congratulations!')









def fiftytwoseventeen():
    t = 69
    c = int(input("How many sessions do you want to use 5217 method with: "))

    while(c > 0):
        print("Work for 52 minutes")
        notify(title = 'Session Change', message  = 'Get into work!')
        print()
        print()
        while(t > -1):
            t = t - 1
            time.sleep(60)


            if(t == 17):
                print("Take a break for 17 minutes.")
                notify(title = 'Session Change', message  = 'Take a break')
                print()
                print()
            
    
        c = c - 1
        t = 69
    print("5217 session finished.")
    notify(title = 'Work session finished', message  = 'Congratulations!')



choice = input("Which study timer do you want to use, pomodoro or 5217? ")

if(choice == "pomodoro"):
    pomodoro()
elif(choice == "5217"):
    fiftytwoseventeen()
else:
    print("Error")