#!/bin/bash

now=$(date +"%m-%d-%Y--%H:%M")
fswebcam -r 1280x1024 --subtitle="test" --title="TEST" pics/WebcamPic$now.jpg
