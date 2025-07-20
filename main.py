import keyboard
import pyautogui as p
import time
import pyperclip


def safe_type(text):
    # Release modifiers and type character-by-character
    keyboard.release('shift')
    keyboard.release('ctrl')
    keyboard.release('alt')

    for char in text:
        # Force lowercase version of character
        p.press(char.lower())
        time.sleep(0.005)  # Small delay to mimic human typing



buffer = ""
el = ""
paused = False
def everything(event):
    global buffer
    global el
    global paused

    if paused:
        return
    
    if event.event_type == "down":
        
        if event.name != '>':
            if len(event.name) == 1:
                buffer += event.name.lower()
            elif event.name == "backspace":
                buffer = buffer[:-1]

            if buffer[-4:] == "<div" and el == "":
                el = "div"
            elif buffer[-5:] == "<span" and el == "":
                el = "span"
            elif buffer[-2:] == "<a" and el == "":
                el = "a"
            elif buffer[-3:] == "<h1" and el == "":
                el = "h1"
            elif buffer[-3:] == "<h2" and el == "":
                el = "h2"
            elif buffer[-3:] == "<ul" and el == "":
                el = "ul"
            elif buffer[-3:] == "<ol" and el == "":
                el = "ol"
            elif buffer[-3:] == "<li" and el == "":
                el = "li"
            elif buffer[-6:] == "<table" and el == "":
                el = "table"
            elif buffer[-3:] == "<tr" and el == "":
                el = "tr"
            elif buffer[-2:] == "<p" and el == "":
                el = "p"
            elif buffer[-3:] == "<td" and el == "":
                el = "td"
            elif buffer[-3:] == "<th" and el == "":
                el = "th"
            elif buffer[-7:] == "<button" and el == "":
                el = "button"
            elif buffer[-6:] == "<label" and el == "":
                el = "label"
            elif buffer[-9:] == "<textarea" and el == "":
                el = "textarea"
            elif buffer[-7:] == "<option" and el == "":
                el = "option"
            elif buffer[-8:] == "<section" and el == "":
                el = "section"
            elif buffer[-4:] == "<nav" and el == "":
                el = "nav"
            elif buffer[-7:] == "<footer" and el == "":
                el = "footer"
            elif buffer[-5:] == "<main" and el == "":
                el = "main"
            elif buffer[-5:] == "<body" and el == "":
                el = "body"
            elif buffer[-5:] == "<head" and el == "":
                el = "head"

        else:
            if el!="":

                keyboard.release('shift')
                keyboard.release('ctrl')
                keyboard.release('alt')
                paused = True 

                closing_tag = f"</{el}>"
                pyperclip.copy(closing_tag)
                p.hotkey("ctrl", "v")

                #safe_type("</" + el + ">")
                #p.write("</"+el+">")
                el = ""
               # time.sleep(0.01)

                p.hotkey("ctrl", "left")
               # time.sleep(0.01)

                p.press("left")
                p.press("left")
                #time.sleep(0.01)

                p.press("enter")

                buffer = ""
                paused = False

keyboard.hook(everything)
keyboard.wait()  


