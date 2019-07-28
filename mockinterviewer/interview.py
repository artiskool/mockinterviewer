from gtts import gTTS
import subprocess
import time
import csv
import os


def CallGTTS_InterviewerQuestion(texttoconvert, nameoffile):
    tts = gTTS(text=texttoconvert, lang='en')
    tts.save(nameoffile)

def CallSubprocess_InterviewerSpeaks(nameoffile):    
    returncode = subprocess.call(["afplay", nameoffile])

def CallTime_InterviewerWaits(Seconds):
    time.sleep(Seconds)

if __name__ == '__main__':
    InterviewQuestions = []
    introtext = "Sorry for the Delay. Hello Maahaan! I am your Automated Interviewer. I hope you're having a great day.Lets start off the interview."
    endText = "Thanks for taking the interview."
    with open('InterviewQuestion.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for x in reader:
            InterviewQuestions = x 
    csv_file.close()
    CallGTTS_InterviewerQuestion(introtext, 'intro.mp3')
    for i in range(0,len(InterviewQuestions)):
        #print(InterviewQuestions[i])
        CallGTTS_InterviewerQuestion(InterviewQuestions[i], ('1702' + str(i)) + '.mp3')
    CallGTTS_InterviewerQuestion(endText, 'end.mp3')

    CallSubprocess_InterviewerSpeaks("intro.mp3")
    for i in range(0,len(InterviewQuestions)):
        #print(InterviewQuestions[i])
        CallSubprocess_InterviewerSpeaks('1702' + str(i) + '.mp3')
        if(len(InterviewQuestions[i]) < 35):
            CallTime_InterviewerWaits(1)
        elif(len(InterviewQuestions[i]) < 50):
            CallTime_InterviewerWaits(1)
        else:
            CallTime_InterviewerWaits(1)
        
    CallSubprocess_InterviewerSpeaks("end.mp3")

    os.remove("intro.mp3")
    for i in range(0,len(InterviewQuestions)):
        os.remove('1702' + str(i) + '.mp3')
    os.remove("end.mp3")
    
    
        


        
        
