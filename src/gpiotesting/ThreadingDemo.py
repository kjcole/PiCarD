#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

# dummy code to experiment with multithreading.  The WorkerThread will
# evolve into our GPIO pin listener thread.

from __future__ import print_function, absolute_import

from PySide.QtCore import *
from PySide.QtGui  import *

import time
import dummy


class MainDialog(QDialog, dummy.UI):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        self.setupUi(self)
        self.threadStarter.clicked.connect(self.startThread)
        self.workerThreads = []

    # startThread creates a new "worker" thread which runs in the
    # background.  The new thread is initialized with its own thread
    # number, and saved in a list of worker threads. Threads can send
    # "signals" in the same way that buttons can send signals, except
    # the developer must create a signal, since there is no built-in
    # signal. startThread connects connects each worker thread's
    # developer-created signal named "talk" to a "slot" method named
    # "threadDone". The talk signal can be sent two different ways --
    # as a string and as an integer. startThread connects both.
    # Finally, it starts the thread and notifies the user in the
    # terminal window.

    # If the button is pressed multiple times within the 10 second
    # time frame, those presses would normally be LOST. However, by
    # instantiating a thread each time the "Start thread" button is
    # pressed, and SAVING IT INTO A LIST, we effectively have created
    # a queue of threads. (Without saving it in a list, we would
    # overwrite the previous thread after it had started running.

    def startThread(self):
        workerThread = WorkerThread(len(self.workerThreads) + 1)
        self.workerThreads.append(workerThread)    # Add new thread to queue
        self.workerThreads[-1].talk.connect(self.threadDone)       # int
        self.workerThreads[-1].talk[str].connect(self.threadDone)  # str
        self.workerThreads[-1].start()             # Start the new thread
        print("This is printed immediately after the button press")
        print("Some text: {0}".format(self.someText.text()))

    @Slot(int)  # Accept talk signals that are integers
    @Slot(str)  # Accept talk signals that are strings
    def threadDone(self, threadNum):
        self.someText.setText(str(threadNum))  # set text to signal's text


class WorkerThread(QThread):
    # IMPORTANT! The worker thread CANNOT directly change contents in
    # the main thread.  So, the worker thread must use signals and
    # slots.  All QObjects, including QThreads are capable of emitting
    # custom signals created by the developer.

    talk = Signal((int,), (str,))  # creates a signal that accepts ints & strs

    def __init__(self, threadNumber, parent=None):
        super(WorkerThread, self).__init__(parent)
        self.threadNumber = threadNumber  # Know your place

    def run(self):  # Must override the default run method of QThread
        time.sleep(10)
        print("Thread number {0} finishing 10 seconds after the {0}th button press"
              .format(self.threadNumber))

        # When finished (after sleeping and printing to the terminal),
        # "emit" either an integer signal [commented out] or a string
        # signal, that is picked up by the main thread and handled by
        # the main thread's "slot".

#       self.talk.emit(self.threadNumber)                                 # int
        self.talk[str].emit("Thread {0} done".format(self.threadNumber))  # str

    # IMPORTANT! Since run() isn't in an infinite loop, the thread
    # STOPS and the thread DISAPPEARS after the 10 seconds are up.

    # Explore .wait() method and .stop() method of QThread
    # There is also a rude .terminate() method. Avoid.


def main():
    import sys
    app = QApplication(sys.argv)
    dummyWindow = MainDialog()
    dummyWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
