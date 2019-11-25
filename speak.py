import pyttsx3
import speech_recognition as sr
import re

while True:

    r = sr.Recognizer()
    mic = sr.Microphone()
    engine = pyttsx3.init()
    with mic as fonte:
        r.adjust_for_ambient_noise(fonte)
        engine.say("Pode falar mestre, Hugo")
        engine.runAndWait()
        engine.stop()

        audio = r.listen(fonte)
        print("Enviando para reconhecimento")
        try:
            texto = r.recognize_google(audio, language="pt-BR")
            print("Você disse: {}".format(texto))
            # engine.say("Entendi mestre Hugo, você falou: {}".format(texto))
            if re.search('Ana', texto, re.IGNORECASE):
                engine.say("Chamou mestre?")
            if re.search('Ana, tudo bem?', texto, re.IGNORECASE):
                engine.say("Tudo ótimo comigo, obrigada!")
            if re.search('Ana, ligar luz', texto, re.IGNORECASE):
                engine.say("É pra já mestre! Ligando")
            if re.search('Ana, desligar luz', texto, re.IGNORECASE):
                engine.say("Agora mesmo. Desligando")

            # engine.say("OK, ligando!")
            engine.runAndWait()
            engine.stop()
        except:
            print("Não deu certo")
            engine.say("Fala alguma coisa logo, eu não tenho o dia todo.")
            engine.runAndWait()
            engine.stop()
