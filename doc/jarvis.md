Using Jeff's fancy CAD u37 USB super-microphone, and following the
procedures outlined at:

https://www.raspberrypi.org/forms/viewtopic.php?t=63136&p=468103

I've determined:

    $ arecord --list-devices
    **** List of CAPTURE Hardware Devices ****
    card 1: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0


    $ arecord -f S16_LE -r 60000 -D hw:1,0 -d 5 test_S16_LE.wav
    Recording WAVE 'test_S16_LE.wav' : Signed 16 bit Little Endian, \
    Rate 60000 Hz, Mono
    Warning: rate is not accurate (requested = 60000Hz, got = 48000Hz)
             please, try the plug plugin 

So, maximum sampling rate is 48000.
