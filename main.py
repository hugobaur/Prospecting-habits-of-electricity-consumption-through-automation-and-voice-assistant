import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()


def falaai():
    engine = pyttsx3.init()
    with mic as fonte:
        r.adjust_for_ambient_noise(fonte)
        engine.say("Fale alguma coisa por favor, Hugo")
        engine.runAndWait()
        engine.stop()

        audio = r.listen(fonte)
        print("Enviando para reconhecimento")
        try:
            texto = r.recognize_google(audio, language="pt-BR")
            print("Voce disse: {}".format(texto))
            engine.say("Voce disse: {}".format(texto))
            engine.runAndWait()
            engine.stop()
        except:
            print("Não deu certo")
            engine.say("Não deu certo")
            engine.runAndWait()
            engine.stop()


if __name__ == '__main__':
    falaai()

