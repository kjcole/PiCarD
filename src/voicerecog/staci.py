#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copied by Kevin Cole <kevin.cole@novawebcoop.org> 2016.06.16
# https://ggulati.wordpress.com/2016/02/24/coding-jarvis-in-python-3-in-2016/

import speech_recognition
import pyttsx
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

# See http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine = pyttsx.init("espeak")
speech_engine.setProperty("rate", 150)

def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()

def listen():
    with speech_recognition.Microphone(sample_rate=48000,
                                       chunk_size=24000) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_sphinx(audio)
        # or: return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

while True:
    speak("Say something!")  # Audible prompt
    response = listen()       # capture response
    speak("I heard you say " + response)
    print("I heard you say: {0}".format(response))
    if response == "ok stacy turn on the rear defroster":
        while True:
            GPIO.output(23, GPIO.HIGH)
            time.sleep(0.0011)
            GPIO.output(23, GPIO.LOW)
            time.sleep(0.0011)
