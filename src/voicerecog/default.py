#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

MODELDIR = "model"
DATADIR  = "data"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string("-hmm",  path.join(MODELDIR, "en-us/en-us"))
config.set_string("-lm",   path.join(MODELDIR, "en-us/en-us.lm.bin"))
config.set_string("-dict", path.join(MODELDIR, "en-us/cmudict-en-us.dict"))
decoder = Decoder(config)

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()

if len(sys.argv) > 1:
    speech = sys.argv[1]
else:
    speech = input("\nSpeech file name [default.raw]: ")
if speech == "":
    speech = "default.raw"

stream = open(path.join(DATADIR, speech), "rb")
while True:
    buf = stream.read(1024)
    if buf:
        print("decoding in progress")
        decoder.process_raw(buf, False, False)
    else:
        print("boop")
        break

decoder.end_utt()
print ("Best hypothesis segments: ", [seg.word for seg in decoder.seg()])
