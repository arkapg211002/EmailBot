'''ARKAPRATIM GHOSH'''
import smtplib
import speech_recognition as sr
import pyttsx3 as ts
listen=sr.Recognizer()
eng=ts.init()
def talk(text):
    eng.say(text)
    eng.runAndWait()
def getin():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listen.listen(source)
            info=listen.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass
def email(receiver,msg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('arkapg2002@gmail.com','arkapg21')
    server.sendmail('arkapg2002@gmail.com',receiver,msg)

def getemailin():
    el={'arka':'arkapratimghosh2002@gmail.com','deb':'dkb@gmail.com','yoyo':'yoyo@gmail.com'}
    a=1
    while a==1:
        talk('To whom do u want to send your email')
        name =getin()
        receiver=el[name]
        talk('what is the subject of your email')
        sub=getin()
        talk('tell something')
        msg=getin()
        email(receiver,msg)
        talk('do u want anyone else in your list?')
        confirm=getin()
        if 'no' in confirm:
            talk('ok sir')
            talk('would u like to send any more mail')
            response1 = getin()
            if 'no' in response1:
                print('ok sir')
                a=0

        else:
            f=1
            while f==1:
                talk('tell name')
                n=getin()
                talk('tell email address')
                e=getin()
                el.update(e,n)
                talk('next')
                nextin=getin()
                if 'no' in nextin:
                    f=0
                    talk('would u like to send any more mail')
                    response=getin()
                    if 'no' in response:
                        print('ok sir')
                        a=0
getemailin()