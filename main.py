from flask import Flask, render_template, request, escape
from functions import *
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Print the form data to the console
        otherVerses = [{'book': "Alma", 'chapter': 1, 'verseNum':1, 'verse': "and it..."}]
        book = request.form['book'].lower()
        chapter = request.form['chapter']
        verseNum = request.form['verseNum']
        returnedRow = findVerseInDF(book, chapter, verseNum)
        if returnedRow!= -1:
            index= returnedRow['index']
            listOfOtherVerses = findSimilarVerses(index)
        else: 
            return render_template("index.html", verse = "Not Found", foundVerses = [])
        
        print(len(listOfOtherVerses))
        return render_template("index.html", verse =returnedRow, foundVerses = listOfOtherVerses)
    else:
        return render_template("index.html")

    
if __name__ == "__main__":
    app.run(debug=True)