import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess as sp


engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
   
    print("  I am Joyboy. What can i do for you sir ")
    speak(" I am Joyboy. What can i do for you sir ")
   

def takeCommand():
    r=sr.Recognizer() #recognizer is class

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.2)
            r.pause_threshold = 1
            audio= r.listen(source,None,5)

            print("Recongnizing....")
            text =r.recognize_google(audio, language="en-in")
            text=text.lower()
            print(f"user said: {text}")
            return text
        
    except Exception as e:
                print("sorry about that i didnt here anything please speak again")
                return "sorry about that i didnt here anything please speak again"
            
    
if __name__ == '__main__':
  
    wishme()
    while(True):
        print("Listening.......")
        text=takeCommand().lower()
        speak(text)

        if "open youtube" in text:
            speak("do you want to search on youtube")
            print("listening...")
            t=takeCommand().lower()
            
            if 'yes' in t:
                  speak("what do want to search sir")
                  print("Listening...")
                  yt=takeCommand().lower()
                  webbrowser.open("https://www.youtube.com/results?search_query="+yt)
            elif 'no' in t:
                 speak("Opening youtube")
                 webbrowser.open("https://youtube.com")
            
           
        elif 'open notepad' in text:
            speak("Opening notepad")
            programname="Notepad.exe"
            sp.Popen(programname)
           

        elif'who are you'in text:
            speak("I am Joyboy. personal assistant of shrinu sir")

        elif "open google" in text:
            speak("what should i search on google")
            search=takeCommand().lower()
            webbrowser.open(f"{search}")

        elif "no wait" and "no" in text:
             speak("Ok sir")
             break
        
        else:
            speak("What else can i do for you sir")

