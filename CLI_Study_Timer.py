import time
import os


# The notifier function
def notify(title, message):
    t = '-title {!r}'.format(title)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t])))


#This is a method for the pomodoro studying method. A pomodoro consists of 25 minutes work and 5 minutes break.
def pomodoro():
    #t stands for the total time required for 1 pomodoro, which is 30 minutes.(25 minutes of work + 5 minutes of break.)
    t = 30
    #count stands for the number of sessions that we want use the pomodoro method.
    count = int(input("How many pomodoro sessions do you wanna do: "))

    while(count > 0):
        print("Work for 25 minutes.")
        #Using the notify method we created at the start.
        notify(title = 'Session Change', message  = 'Get into work!')
        print()
        print()
        while(t > -1):
            t = t - 1
            time.sleep(60)

            if(t == 5):
                print("Take a break for 5 minutes.")
                #Using the notify method we created at the start.
                notify(title = 'Session Change', message  = 'Take a break')
                print()
                print()

        count = count - 1
        t = 30
    print("Pomodoro session finished.")
    #Using the notify method we created at the start.
    notify(title = 'Work session finished', message  = 'Congratulations!')








#5217 method consists of working for 52 minutes and having a break for 17 minutes.
def fiftytwoseventeen():
    #t stands for the total time required for 1 pomodoro, which is 30 minutes.(25 minutes of work + 5 minutes of break.)
    t = 69
    #c stands for the number of sessions that we want use the 5217 method.
    c = int(input("How many sessions do you want to use 5217 method with: "))

    while(c > 0):
        print("Work for 52 minutes")
        #Using the notify method we created at the start.
        notify(title = 'Session Change', message  = 'Get into work!')
        print()
        print()
        while(t > -1):
            t = t - 1
            time.sleep(60)


            if(t == 17):
                print("Take a break for 17 minutes.")
                #Using the notify method we created at the start.
                notify(title = 'Session Change', message  = 'Take a break')
                print()
                print()
            
    
        c = c - 1
        t = 69
    print("5217 session finished.")
    #Using the notify method we created at the start.
    notify(title = 'Work session finished', message  = 'Congratulations!')





#Asking to the user which method they want to use to help them study, pomodoro or 5217. 
choice = input("Which study timer do you want to use, pomodoro or 5217? ")

#There are 2 possible answers. The user will either choose pomodoro or 5217 method. Any other answers will cause an error and the app will close itself.
if(choice == "pomodoro"):
    pomodoro()
elif(choice == "5217"):
    fiftytwoseventeen()
else:
    print("Error")
