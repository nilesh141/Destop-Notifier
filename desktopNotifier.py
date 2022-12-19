from plyer import notification 
import time


if __name__=='__main__':
    while True:
        notification.notify(
          title="***Take Rest***",
          message="Rest is vital for better mental health, increased concentration and memory, a healthier immune system, reduced stress, improved mood and even a better metabolism.",
          #app_icon="D:/Libraries/Documents/Visual studio 22 project/PythonProjects/restIcon.jpg", #this line not working saying could not load icon
          timeout=5) #notification will wait for 5 sec then disappear
        time.sleep(10) #notification will come in every 10 sec #takes input in seconds only
        #to make it run automatically in background go to folder through command prompt and
        #write pythonw desktopNotifier.py #i.e file name
        #to stop from background process go to task manager then process then check for filename and
        #end task 
