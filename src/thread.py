#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide.QtCore import *

def thread(job):
    workerThread = WorkerThread(len(self.workerThreads) + 1, job)
    self.workerThreads.append(workerThread)    # Add new thread to queue
    self.workerThreads[-1].talk.connect(self.threadDone)       # int
    self.workerThreads[-1].talk[str].connect(self.threadDone)  # str
    self.workerThreads[-1].start()             # Start the new thread
    print(job,"is running")


