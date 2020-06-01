import speech_recognition as sr
import webbrowser as wb

def Youtube():
    print("Do you want to search a video")
    with sr.Microphone() as source:
        audio = r2.listen(source)
        try:
            output = r2.recognize_google(audio)
            print("You said {}".format(output))
        except:
            print("Cannot recognize the voice")
        if "yes" in r2.recognize_google(audio):

            url = 'https://www.youtube.com/results?search_query='
            with sr.Microphone() as source:
                print("Search For video")
                audio = r2.listen(source)
                try:
                    get = r2.recognize_google(audio)
                    print(get)
                    wb.get().open_new_tab(url + get)
                except sr.UnknownValueError:
                    print("Error")
                except sr.RequestError as e:
                    print("Failed to get Result as {}".format(e))
        else:
            url = 'https://www.youtube.com/'
            wb.get().open_new_tab(url)

        try:
            output = r.recognize_google(audio)
            print("your said {}".format(output))
        except:
            print("Cannot recognize the voice")

def FaceBook():
    url = 'https://www.Facebook.com/'
    wb.get().open_new_tab(url)
def Instagram():
    url = 'https://www.Instagram.com/'
    wb.get().open_new_tab(url)
def Twitter():
    url = 'https://www.twitter.com/'
    wb.get().open_new_tab(url)
def Google():
    print(" Do you want to search something")
    with sr.Microphone() as source:
        audio = r2.listen(source)
        try:
            output = r2.recognize_google(audio)
            # print("You asked for {}".format(output))
        except:
            print("Cannot recognize the voice")
        if "yes" in r2.recognize_google(audio):

            url = 'https://www.google.com/search?q='
            with sr.Microphone() as source:
                print("What do you want to search")
                audio = r2.listen(source)
                try:
                    get = r2.recognize_google(audio)
                    print(get)
                    wb.get().open_new_tab(url + get)
                except sr.UnknownValueError:
                    print("Error")
                except sr.RequestError as e:
                    print("Failed to get Result as {}".format(e))
        else:
            url = 'https://www.google.com/'
            wb.get().open_new_tab(url)


if __name__=='__main__':
    r = sr.Recognizer()
    r2 = sr.Recognizer()
    r3 = sr.Recognizer()

    with sr.Microphone() as source:
        print("How may I help you")
        audio = r3.listen(source)

        try:
            output = r3.recognize_google(audio)
        except:
            print("Cannot recognize the voice")

        if 'YouTube' in r2.recognize_google(audio):
            print("Opening YouTube")
            Youtube()
        elif 'Facebook' in r2.recognize_google(audio):
            print("Opening Facebook")
            FaceBook()
        elif 'Instagram' in r2.recognize_google(audio):
            print("Opening Instagram")
            Instagram()
        elif 'Google' in r2.recognize_google(audio):
            print("Opening Google")
            Google()
        elif 'Twitter' in r2.recognize_google(audio):
            print("Opening Twitter")
            Twitter()
        else:
            print("Sorry I am not prepared for your request")