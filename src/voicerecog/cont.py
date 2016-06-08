#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import pyaudio

modeldir = "model"
datadir = "data"
hmdir = "modeldir, 'en-us'"
lmd = "modeldir, 'en-us.lm.dmp'"
dictd = "modeldir, 'cmudict'"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
config.set_string('-lm', os.path.join(modeldir, 'en-us/en-us.lm.bin'))
config.set_string('-dict', os.path.join(modeldir, 'en-us/cmudict-en-us.dict'))
config.set_string('-keyphrase', 'hello' )
config.set_float('-kws_threshold', 1e+20)

# Open file to read the data
#stream = open(os.path.join(datadir, "goforward.raw"))

# Alternatively you can read from microphone
import pyaudio

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()

# Process audio chunk by chunk. On keyword detected perform action and restart search
decoder = Decoder(config)
decoder.start_utt()
while True:
    buf = stream.read(1024)
    if not buf:
        break
    decoder.process_raw(buf, False, False)
    if decoder.hyp() != None and decoder.hyp().hypstr == 'forward':
        print("Detected keyword, restarting search")
    decoder.end_utt()
    decoder.start_utt()
