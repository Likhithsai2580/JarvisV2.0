from Jarvis import *
import re
import os
import random
import pprint
import datetime
import requests
import sys
import wikipedia
import pyjokes
import time
import pyautogui
import pywhatkit
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
import wolframalpha
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Jarvis.features.gui import Ui_MainWindow
import pyfirmata
import pyttsx3
import webbrowser
from bs4 import BeautifulSoup

app_id = ""#enter your appid from wolframalpha website
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#Seting test to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def subscribe():
    webbrowser.open("https://www.youtube.com/channel/UC5N_8t5SzEyJrTx1bC66Kpw?sub_confirmation=1")
    speak("Sorry Sir Owner will make it automatically soon for any other feature contact on email")
    webbrowser.open("mailto:semalalikithsai@gmail.com")
def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Jarvis is online")
    speak("Sir or Mamdam Please Subscribe To Owner Channel To support Owner Do you Want Subscribe")
    Answer = obj.mic_input()
    if "yes" in Answer:
        speak("thank you sir")
        subscribe()
        startExecution.start()
    else:
        speak("sorry sir, if you want you can by saying i am satisfied")
        startExecution.start()



obj = JarvisAssistant()

#Memory
GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there", "hey there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

EMAIL_DIC = {
    'myself': 'semalalikith@gmail.com',
    'my official email': 'semalalikith@gmail.com',
    'my second email': 'semalalikith@gmail.com',
    'my official mail': 'semalalikith@gmail.com',
    'my second mail': 'semalalikith@gmail.com'
}

#Memory

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        startup()

        while True:
            command = obj.mic_input()


            if re.search('date', command):
                date = obj.tell_me_date()
                print(date)
                speak(date)

            elif "i am satisfied" in command:
                speak("Thank you sir")
                subscribe()
                startExecution.start()

            elif "time" in command:
                time_c = obj.tell_time()
                print(time_c)
                speak(f"Sir the time is {time_c}")

            elif "weather" in command:
                speak("what is your city name")
                city = obj.mic_input()
                fullcommand = "temperature in"+city
                url = f"www.google.com/search?q={fullcommand}"
                r = requests.get(url)
                data = BeautifulSoup(r.txt,"html.parser")
                temp = data.find("div",class_="BNewe").txt
                speak(f"current {fullcommand} is {temp}")
            elif re.search('launch', command):
                dict_app = {
                    'chrome': 'C:/Program Files/Google/Chrome/Application/chrome'
                }

                app = command.split(' ', 1)[1]
                path = dict_app.get(app)

                if path is None:
                    speak('Application path not found')
                    print('Application path not found')

                else:
                    speak('Launching: ' + app + 'for you sir!')
                    obj.launch_any_app(path_of_app=path)

            elif command in GREETINGS:
                speak(random.choice(GREETINGS_RES))

            elif re.search('open', command):
                domain = command.split(' ')[-1]
                open_result = obj.website_opener(domain)
                speak(f'Alright sir !! Opening {domain}')
                print(open_result)

            elif re.search('tell me about', command):
                topic = command.split(' ')[-1]
                if topic:
                    wiki_res = obj.tell_me(topic)
                    print(wiki_res)
                    speak(wiki_res)
                else:
                    speak(
                        "Sorry sir. I couldn't load your query from my database. Please try again")

            elif "buzzing" in command or "news" in command or "headlines" in command:
                news_res = obj.news()
                speak('Source: The Times Of India')
                speak('Todays Headlines are..')
                for index, articles in enumerate(news_res):
                    pprint.pprint(articles['title'])
                    speak(articles['title'])
                    if index == len(news_res)-2:
                        break
                speak('These were the top headlines, Have a nice day Sir!!..')

            elif 'search google for' in command:
                obj.search_anything_google(command)
            
            elif "play music" in command or "hit some music" in command:
                music_dir = "F://Songs//Imagine_Dragons"
                songs = os.listdir(music_dir)
                for song in songs:
                    os.startfile(os.path.join(music_dir, song))

            elif 'youtube' in command:
                video = command.split(' ')[1]
                speak(f"Okay sir, playing {video} on youtube")
                pywhatkit.playonyt(video)

            if "note" in command or "write" in command or "remember" in command:
                speak("What Hint do you want to put for note")
                speak("for Example to make a note on car keys")
                nameoffile = obj.mic_input()
                f = open(nameoffile + ".txt",'w')
                note = obj.mic_input()
                speak("Sir is this right if yes say right")
                speak(note)
                answerfornote = obj.mic_input
                if "right" in answerfornote:
                    speak("Trying to save")
                    f.write(note)
                    f.close()
                    speak("Saved Sir")
                else:
                    speak("i will try again to understand")
                    speak("What Hint do you want to put for note")
                    speak("for Example to make a note on car keys")
                    nameoffile = obj.mic_input()
                    f = open(nameoffile + ".txt",'w')
                    note = obj.mic_input()

            elif "close the note" in command or "close notepad" in command:
                speak("Okay sir, closing notepad")
                os.system("taskkill /f /im notepad++.exe")

            if "joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "system" in command:
                sys_info = obj.system_info()
                print(sys_info)
                speak(sys_info)

            elif "search in google" in command:
                speak("What do you want to search")
                searchforgoogle = obj.mic_input()
                urlforgoogle = f"www.google.com/search?q={searchforgoogle}"
                webbrowser.open(urlforgoogle)

            elif "where is" in command:
                place = command.split('where is ', 1)[1]
                current_loc, target_loc, distance = obj.location(place)
                city = target_loc.get('city', '')
                state = target_loc.get('state', '')
                country = target_loc.get('country', '')
                time.sleep(1)
                try:

                    if city:
                        res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                    else:
                        res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                except:
                    res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                    speak(res)

            elif "ip address" in command:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

            elif "switch the window" in command or "switch window" in command:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "where i am" in command or "current location" in command or "where am i" in command:
                try:
                    city, state, country = obj.my_location()
                    print(city, state, country)
                    speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak(
                        "Sorry sir, I coundn't fetch your current location. Please try again")

            elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                import pyautogui
                im = pyautogui.screenshot()
                speak("what name do you want to name the screenshot")
                screenshot = obj.mic_input()
                im.save(screenshot + ".jpg")

            elif "show me the screenshot" in command:
                try: 
                    img = Image.open('E:/Jarvis-Made-By-Me/' + screenshot + ".jpg")
                    img.show(img)
                    speak("Here it is sir")
                    time.sleep(2)

                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")

            elif "hide all files" in command or "hide this folder" in command:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden")

            elif "visible" in command or "make files visible" in command:
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

            # if "calculate" in command or "what is" in command:
            #     query = command
            #     answer = computational_intelligence(query)
            #     speak(answer)

            

            elif "goodbye" in command or "offline" in command or "bye" in command:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()

            elif "what is" in command or "who is" in command or "explain" or "how to" in command:
                try:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print("According to Wikipedia")
                    print(results)
                    speak(results)
                    startExecution.start()

                except:
                    speak("Sorry Sir Data Not Found")
                    startExecution.start()

            elif "on light" in command:
                board = pyfirmata.Arduino('COM4')
                board.digital[9].write(1)
                speak("Turning on Light")

            elif "off light" in command:
                board = pyfirmata.Arduino('COM4')
                board.digital[9].write(0)
                speak("Turning off Light")

            elif 'lic' in command:
                try:
                    webbrowser.open("www.licindia.in")
                    speak("opening lic india")
                except:
                    speak("sorry sir I am not able to do so")

            elif 'youtube channel' in command:
                speak("opening youtube channel hackers are here where are you")
                webbrowser.open("https://www.youtube.com/channel/UC5N_8t5SzEyJrTx1bC66Kpw?sub_confirmation=1")

            elif 'email to owner of project' in command:
                speak("ok sir")
                webbrowser.open("mailto:semalalikithsai@gmail.com")

            elif 'prime minister of india' in command:
                speak("narendra modi is prime minester of india") 
                
            else:
                try:
                    client = wolframalpha.Client(app_id)
                    res = client.query(command)
                    answer = next(res.results).text
                    speak(answer)
                except:
                    try:
                        notepadfile = command+"txt"
                        subprocess.Popen("notepad"+notepadfile)
                    except:
                        speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to Wikipedia")
                        print("According to Wikipedia")
                        print(results)
                        speak(results)
                        startExecution.start()

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
