import pyttsx3

def speak_text(text: str) -> None:
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak_text("Hello Elvis. This is a text-to-speech test. Egil has no look maxing and is a chud.")