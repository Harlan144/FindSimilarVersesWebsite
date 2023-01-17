import pandas as pd
import re

df = pd.read_csv('static/bomForWebsite')

def findVerseInDF(book, chapter, verseNum):
    try:
        index = df.index[(df['Book'] == book) & (df['Chapter'] == int(chapter)) & (df["VerseNum"]== int(verseNum))]
        row = df.iloc[index[0]]
        rowNum  = index[0]
        book = row['Book']
        chapter = row["Chapter"]
        verseNum = row["VerseNum"]
        verse  = row["Verse"]
        return {'index': rowNum,'book': book, 'chapter': chapter, 'verseNum': verseNum, 'verse': verse}
    except:
        return -1

def findSimilarVerses(index):
    with open("static/mostSimilarVerses") as file:
        for i, line in enumerate(file):
            if i== index:
                regex = '\'index\': (\d+)'
                similarVerses = re.findall(regex, line) 
    listOfDic = []
    for i in similarVerses:
        row = df.iloc[int(i)]
        rowNum  = int(i)
        book = row['Book']
        chapter = row["Chapter"]
        verseNum = row["VerseNum"]
        verse  = row["Verse"]
        listOfDic.append({'index': rowNum,'book': book, 'chapter': chapter, 'verseNum': verseNum, 'verse': verse})
    return listOfDic
    