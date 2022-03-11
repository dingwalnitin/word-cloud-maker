
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from tkinter import *


def removepunc(z):
    test_str=z
    punc = '''!()-[]{};:'"'\\',<>./?@#$%^&*_~'''
    for ele in test_str:
        if ele in punc:
            test_str = test_str.replace(ele, "")
    return test_str

def removebad(f):
    print(type(f))
    badword2 = ["the", "a","in","on", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me",
    "my","we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her",
    "hers", "its", "they","them","their", "what", "which", "who", "whom", "this", "that",
    "am", "are", "was", "were", "be", "been","being","have", "has", "had", "do", "does",
    "did", "but", "at", "by", "with", "from", "here", "when", "where","how","all", "any",
    "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can",
    "will","just"]
    keep = []
    toss = []
    for w in f:
        if w in badword2:
            toss.append( w )
        else:
            keep.append( w )
    return keep
def coun(list):
    all_freq={}
    for i in list:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq
def startfn():
    a=text2
    a=a.lower()
    unqword=removepunc(a)
    ab=unqword.split()
    print(type(ab))
    unqword1=removebad(ab)
    dictionary=coun(unqword1)





    wc = WordCloud(background_color="white",width=1000,height=1000, max_words=100,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(dictionary)
    plt.imshow(wc)
    wc.to_file('wordcloud_output.png')
root= Tk()
root.title("Word cloud by nitin")
root.geometry("700x700")
text2=0
def getfn():
    global text2
    text2=e.get()

    return text2


e=Entry(root, width=100)
e.pack()

def getfn1():
    e.delete("1.0", "end")

button2= Button(root,text="initialise", command=getfn)
button4= Button(root,text="make", command=startfn)
button3= Button(root,text="clear", command=getfn1)

button2.pack()
button4.pack()
button3.pack()



root.mainloop()













def startfn():
    a=text2
    a=a.lower()
    unqword=removepunc(a)
    ab=unqword.split()
    print(type(ab))
    unqword1=removebad(ab)
    dictionary=coun(unqword1)





    wc = WordCloud(background_color="white",width=1000,height=1000, max_words=100,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(dictionary)
    plt.imshow(wc)
    wc.to_file('wordcloud_output.png')