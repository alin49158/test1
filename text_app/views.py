from django.shortcuts import render, redirect
from django.http import HttpResponse
import subprocess
import os
import csv

# Create your views here.

def home(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        return redirect('result', text=text)
    return render(request, 'text_app/home.html')

def result(request, text):
    #script_path = "F://Desktop//11//Senti4SD//ClassificationTask//classificationTask.sh"
    #param1 = "F://Desktop//11//Senti4SD//ClassificationTask//Sample.csv"
    #param2 = "World"
    
    data = [
    [text],   # Header row
    ]
    with open("F:/Desktop/11/Senti4SD/ClassificationTask/Sample.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    os.system(" cd F:/Desktop/11/Senti4SD/ClassificationTask && sh classificationTask.sh Sample.csv")
    predict_text=""
    with open('F:/Desktop/11/Senti4SD/ClassificationTask/predictions.csv', mode='r', newline='') as file:
        #reader = csv.reader(file)
        #for row in reader:
        #    predict_text = str(row) + predict_text
            
        reader = csv.DictReader(file)    
        for row in reader:
            predict_text = str(row['Predicted']) + predict_text
    
    result_text = ""

    result_text = text + ":" + predict_text
            
    return render(request, 'text_app/result.html', {'text': result_text})
