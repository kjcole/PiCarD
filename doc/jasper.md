Jasper
======

Start with the [Jasper documentation](http://jasperproject.github.io/).

/etc/modprobe.d/alsa-base.conf is now /usr/share/alsa/alsa.conf

Nope. Don't mess with that.  Instead, configure audio using Raspbian's
audio configuration menu. Preferences -> Audio Device Settings. This
will create ~/.asoundrc.  Copy ~/.asoundrc to /etc/asound.conf and
reboot.

    $ arecord -D plughw:1,0 -f cd test.wav
    [talk into the microphone]
	^C
	$ aplay test.wav

Playback:  Make sure your Playback is set to Analog!

And... we run into our old friend Python2 vs. Python3... Make sure the
pip is installing to Python2's library directory.  Try pip2 instead of
merely pip.

When you get a message about unknown public keys, the following will
fix that:

    $ gpg --recv-key 8B48AD6246925553
    $ gpg --recv-key 7638D0442B90D010

    $ gpg --export --armor 8B48AD6246925553 | sudo apt-key add -
    $ gpg --export --armor 7638D0442B90D010 | sudo apt-key add -

