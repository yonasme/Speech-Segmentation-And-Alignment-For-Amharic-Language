import re
import os
import sys
import hm
from sys import argv
from tkinter import *
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.title("Speech Segmentation System")
textpath=""
speechpath=""
entryText=tk.StringVar()
entryspeech=tk.StringVar()
tk.Label(root,text="Choose Text File").grid(row=0)
tk.Label(root,text="Choose Speech File").grid(row=1)
e1=tk.Entry(root,width=70,textvariable=entryText)
e1.grid(row=0,column=1)
e2=tk.Entry(root,width=70,textvariable=entryspeech)
e2.grid(row=1,column=1)

def opentext():
    root.textfilename=filedialog.askopenfilename(initialdir="C:/",title="select File")
    textpath=root.textfilename
    entryText.set(textpath)
    #e1.insert(50,str(textpath))

def openwav():
    root.speechfilename=filedialog.askopenfilename(initialdir="C:/",title="select File")
    speechpath=root.speechfilename
    entryspeech.set(speechpath)
    #e2.insert(50,str(speechpath))
    
def g2p():

    path1=e1.get()
    print(path1)
    path2='converted.txt'
    file = open(str(path1), "r", encoding='utf-8')
    out =  open(path2, "w+", encoding='utf-8')
    count=1
    lines=file.readlines()
    for line in lines:
     line= line.replace('\n','')
     w=str(hm.phon_word('am',line,return_string=True))
     print(str(count)+"=>"+w)
     count=count+1
     words=str(w[2:len(w)-2])
     for analyzedword in words.split():             
                        word=analyzedword
                        type(word)
                        matchnum=re.match('\W[0-9]',word)
                        if( word.find('?')==0):
                            word=word[1:]
                            letter=0
                            new=''
                            while(letter<len(word)):
                                if word[letter]=='_':
                                    new=new+""
                                    letter=letter+1
                                elif word[letter]=='e':
                                    new=new+'e'
                                    letter=letter+1
                                elif word[letter]=='a':
                                    new=new+'a'
                                    letter=letter+1
                                elif word[letter]=='o':
                                    new=new+'o'
                                    letter=letter+1
                                elif word[letter]=='u':
                                    new=new+'u'
                                    letter=letter+1 
                                elif word[letter]=='i':
                                    new=new+'i'
                                    letter=letter+1     
                                elif word[letter]=="'":
                                    if(len(word)-1==letter):
                                        new=new+''
                                        letter=letter+1
                                    else:
                                        if(word[letter+1]=='a' or word[letter+1]=='E' or word[letter+1]=='i' or word[letter+1]=='o' or word[letter+1]=='u' or word[letter+1]=='e'):
                                            new=new+''
                                            letter=letter+1
                                        else:
                                            new=new+'I'
                                            letter=letter+1
                                elif word[letter]=='E':
                                    new=new+'E'
                                    letter=letter+1
                                elif word[letter]=='I':
                                    new=new+'I'
                                    letter=letter+1
                                elif word[letter]=='፡':
                                    new=new+''
                                    letter=letter+1                                      
                                elif word[letter]=='W' and word[letter+1]=='e':
                                    new=new+'o'
                                    letter=letter+2 
                                else:
                                  new=new+word[letter]
                                  letter=letter+1
                               
                            type(new)
                            out.write(new+" ")
                         
                        else:
                            letter=0
                            new=""
                            while(letter<len(word)):
                                if word[letter]=='_':
                                    new=new+""
                                    letter=letter+1
                                elif word[letter]=='e':
                                    new=new+'e'
                                    letter=letter+1
                                elif word[letter]=='a':
                                    new=new+'a'
                                    letter=letter+1
                                elif word[letter]=='o':
                                    new=new+'o'
                                    letter=letter+1
                                elif word[letter]=='u':
                                    new=new+'u'
                                    letter=letter+1    
                                elif word[letter]=='i':
                                    new=new+'i'
                                    letter=letter+1    
                                elif word[letter]=="'":
                                    if(len(word)-1==letter):
                                        new=new+''
                                        letter=letter+1
                                    else:
                                        if(word[letter+1]=='a' or word[letter+1]=='E' or word[letter+1]=='i' or word[letter+1]=='o' or word[letter+1]=='u' or word[letter+1]=='e'):
                                            new=new+''
                                            letter=letter+1
                                        else:
                                            new=new+'I'
                                            letter=letter+1
                                elif word[letter]=='E':
                                    new=new+'E'
                                    letter=letter+1
                                elif word[letter]=='I':
                                    new=new+'I'
                                    letter=letter+1
                                elif word[letter]=='፡':
                                    new=new+''
                                    letter=letter+1
                                elif word[letter]=='W' and word[letter+1]=='e':
                                    new=new+'o'
                                    letter=letter+2 
                                else:
                                    new=new+word[letter]
                                    letter=letter+1
                                        

                            out.write(new+" ")
     out.write("\n")        

    file.close()
    out.close()

    path1='converted.txt'
    path2='prompt.txt'

    file = open(path1, "r", encoding='utf-8')
    out =  open(path2, "w+", encoding='utf-8')
    num=1
    lines=file.readlines()
    for line in lines:
     out.write("*/"+str(num)+" "+line)
     num=num+1

    file.close()
    out.close()

    path1='prompt.txt'
    path2='words.mlf'

    file = open(path1, "r", encoding='utf-8')
    out =  open(path2, "w+", encoding='utf-8')
    lines=file.readlines()
    out.write("#!MLF!#\n")
    for line in lines:
        word=line.split()
        out.write('"'+word[0]+'.lab"\n')
        for i in range (1,len(word)):
           out.write(word[i]+"\n")
        out.write(".\n")
    file.close()
    out.close()
    filename=os.path.basename(speechpath)
    my_label=Label(root, text="Grapheme-to-Phoneme Conversion Done"+filename+" ")
    my_label.grid(row=4,column=1)

def makedic():
    print(os.popen("perl prompts2wlist prompt.txt wordlist").read())
    file = open("wordlist", "r", encoding='utf-8')
    out =  open("dicts", "w+", encoding='utf-8')

    lines=file.readlines()
    for line in lines:
      letter=0 
      new=''
      word=line

      while(letter<len(word)):
         if word[letter]=='e' or word[letter]=='u' or word[letter]=='i' or word[letter]=='a' or word[letter]=='E' or word[letter]=='I' or word[letter]=='o':
             new=new+word[letter]+" "
             letter=letter+1
         else:
             if(letter<(len(word)-1)):
                if((word[letter]!='e' or word[letter]!='u' or word[letter]!='i' or word[letter]!='a' or word[letter]!='E' or word[letter]!='I' or word[letter]!='o') and (word[letter+1]=='W' and (word[letter+2]=='a' or word[letter+2]=='i' or word[letter+2]=='E' )) ):
                  new=new+word[letter]+word[letter+1]+word[letter+2]+" "
                  letter=letter+3
                elif(word[letter]=='g' or word[letter]=='n' or word[letter]=='y' ) and (word[letter+1]=='I' ):                                                                                      
                  new=new+word[letter]+" "
                  letter=letter+1
                elif((word[letter]!='e' or word[letter]!='u' or word[letter]!='i' or word[letter]!='a' or word[letter]!='E' or word[letter]!='I' or word[letter]!='o') and (word[letter+1]=='e' or word[letter+1]=='u' or word[letter+1]=='i' or word[letter+1]=='a' or word[letter+1]=='E' or word[letter+1]=='I' or word[letter+1]=='o')):                                                                                      
                  new=new+word[letter]
                  letter=letter+1
                else:
                  new=new+word[letter]+" "
                  letter=letter+1
             else:
                break;
             
      #print(new)          
      out.write((word.replace('\n','')).ljust(30)+new+"sp\n")
    silence="silence"
    out.write((silence.replace('\n','')).ljust(30)+"silence\n")
    file.close()
    out.close()
    my_label=Label(root, text="Dictionary File Created")
    my_label.grid(row=5,column=1)
    
def toTG():
    tname=e1.get()
    size=len(tname)
    path=tname[:size-4]
    file=open(path+".rec",'r')
    out=open(path+".TextGrid",'a',encoding='utf-8')
    linelist=file.readlines()
    count=0
    for line in linelist:
        lineword=line.split()
        if(lineword[2]=="sp" and lineword[0]==lineword[1]):
            count=count+1
        
    out.write('''File type = "ooTextFile"
    Object class = "TextGrid"\n
    xmin = 0\n''')
    line=linelist[-1]
    w=line.split()
    xmax=int(w[1])/10000000
    out.write("xmax= "+str(xmax)+'''
    tiers? <exists> 
    size = 3
    item []:
    \titem[1]:
    \t\tclass= "IntervalTier"
    \t\tname = "phones"
    \t\txmin = 0 
    \t\txmax = '''+str(xmax)+"\n")
    numberoflines=len(linelist)-count
    out.write("\t\tintervals: size = "+str(numberoflines)+"\n")
    num=1
    for line in linelist:
        word=line.split()
        if(word[2]=="sp" and word[0]== word[1]):
            continue
        else:
            out.write("\t\tintervals ["+str(num)+"]:\n")
            out.write("\t\t\txmin= "+str(int(word[0])/10000000)+"\n")                
            out.write("\t\t\txmax= "+str(int(word[1])/10000000)+"\n")
            out.write('\t\t\ttext= "'+word[2]+'"\n')
            num=num+1
    out.write("\titem [2]:\n")
    out.write('\t\tclass = "IntervalTier"\n')
    out.write('\t\tname = "words"\n')
    out.write('\t\txmin = 0\n')
    out.write('\t\txmax = '+str(xmax)+'\n')
    count=0
    for line in linelist:
        word=line.split()
        if(len(word)==4):
            count=count+1
    out.write("\t\tintervals: size = "+str(count)+"\n")
    sentence=""
    num=1
    linecount=1
    for line in linelist:
        word=line.split()
        if(len(word)==4):
            out.write("\t\tintervals ["+str(num)+"]:\n")
            num=num+1
            out.write("\t\t\txmin= "+str(int(word[0])/10000000)+"\n")
            if(linecount<len(linelist)):
                while(linecount<=len(linelist)-1):
                    wo=linelist[linecount]
                    xmaximum=wo.split()
                    if(len(xmaximum)==4):
                        out.write("\t\t\txmax= "+str(int(xmaximum[0])/10000000)+"\n")
                        linecount=linecount+1
                        break
                    else:
                        linecount=linecount+1       
            else:
                   out.write("\t\t\txmax= "+str(xmax)+"\n")
            out.write('\t\t\ttext= "'+word[3]+'"\n')
            if word[3] != "silence":
               sentence=sentence+word[3]+" "
    out.write("\titem [3]:\n")
    out.write('\t\tclass = "IntervalTier"\n')
    out.write('\t\tname = "ortho"\n')
    out.write('\t\txmin = 0\n')
    out.write('\t\txmax = '+str(xmax)+'\n')
    out.write('\t\tintervals: size = 1\n')
    out.write('\t\tintervals [1]:\n')
    out.write('\t\t\txmin = 0\n')
    out.write('\t\t\txmax = '+str(xmax)+'\n')
    out.write('\t\t\ttext= "'+sentence+'"\n')                     

    file.close()
    out.close()
    intext=e1.get()
    inwav=e2.get()
    size=len(intext)
    tname=inwav[:size-3]+"TextGrid"
    filename=os.path.basename(e2.get())
    my_label=Label(root, text="Multi-Tier TextGrid File Generated for "+filename+" ")
    my_label.grid(row=6,column=1)
    print(os.popen('"C:/Program Files/Praat.exe" --open '+inwav+' '+tname+' ').read())
    
def speechenhancment():
   inwav=e2.get()
   fname=os.path.basename(inwav)
   outwav=e2.get()    
   size=len(inwav)
   temp=inwav[:size-5]+"temp.wav"
   print(os.popen("ctucopy4 -preset exten -fs 16000 -format_in wave -format_out wave -i "+inwav+" -o "+temp+" -v").read())
   print(os.popen("rm "+inwav+" ").read())
   print(os.popen("mv "+temp+" "+inwav+" ").read())
   my_label=Label(root, text="Speech Enhancment Performed On"+fname+" ")
   my_label.grid(row=7,column=1)
   
def featurevector():
    inwav=e2.get()
    fname=os.path.basename(inwav)
    size=len(inwav)
    mfc=inwav[:size-3]+"mfc"
    print(os.popen("HCopy -T 1 -C config "+inwav+" "+mfc+" ").read())
    my_label=Label(root, text="MFCC Feature Vectors Extracted from"+fname+" ")
    my_label.grid(row=8,column=1)
    
def forcedalignment():
    inwav=e2.get()
    fname=os.path.basename(inwav)
    size=len(inwav)
    mfc=inwav[:size-3]+"mfc"
    print(os.popen("HVite -a -b silence -m -o S -I words.mlf -H c:/Users/Yonas/Desktop/Research/train/mono2/hmmdefs dicts c:/Users/Yonas/Desktop/Research/train/monophones1 "+mfc+" ").read())
    my_label=Label(root, text="Speech Segmentation Tasked Performed On"+fname+" Succesfully")
    my_label.grid(row=9,column=1)
    
def performsegmentation():
    print(textpath)
    g2p()
    makedic()
    speechenhancment()
    featurevector()
    forcedalignment()
    toTG()

myButton1=Button(root,text="Open File",command=opentext).grid(row=0,column=2)
myButton2=Button(root,text="Open File",command=openwav).grid(row=1,column=2)
myButton3=Button(root,text="Get Segmented Boundaries",command=performsegmentation).grid(row=2,column=1)


root.mainloop()

