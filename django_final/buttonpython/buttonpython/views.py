from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage
import wave
#import keras
#import numpy as np
#import librosa

def button(request):
    return render(request,'index.html')

def external(request):
    #inp = request.POST.get('wavFile')
    wavInput = request.FILES["wavInput"]
    #print("Song name is "+ wavInput)
    fs = FileSystemStorage()
    fileName = fs.save(wavInput.name,wavInput)
    fileurl = fs.open(fileName)
    templateurl = fs.url(fileName)

    out = run([sys.executable, 'C:\\Users\\drkdfr\\Desktop\\django_final\\predictEmotion.py',fileurl,fileName],shell=False,stdout=PIPE)
    print(out.stdout)
    return render(request, 'index.html',{'data':out.stdout})



