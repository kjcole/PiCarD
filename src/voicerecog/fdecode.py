#!/usr/bin/env python3
from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

MODELDIR = "model"
DATADIR = "data"
DICT = input("full or limited dictionary?(full/limited)[limited]: ")
AFILE = input("file location from '"'{0}'"': ".format(DATADIR))

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
if DICT == "full":
    config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
elif DICT == "limited" or "":
    config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us-new.dict'))
else:
    print("Wrong input")
    exit(1)
decoder = Decoder(config)

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()
stream = open(path.join(DATADIR, AFILE), 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    print("decoding in progress")
    decoder.process_raw(buf, False, False)
  else:
    break
    print('boop')
decoder.end_utt()
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])

