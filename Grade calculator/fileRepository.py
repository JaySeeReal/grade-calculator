import models.grade
import re

gradeList = []
saveFile = "Grade calculator\grades.txt"

def readFromFile():
    global gradeList
    file = open(saveFile)
    gradeList = file.read()
    return None

def saveToFile():
    pass
    
def addSubject(subject, grade):
    clearSubject = str(subject)
    clearGrade = 0.0
    if "+" in grade:
        grade = re.sub("[+]","", grade)
        grade = float(grade)
        clearGrade = grade + 0.50
    elif "-" in grade:
        grade = re.sub("[-]","", grade)
        grade = float(grade)
        clearGrade = grade - 0.25
    else:

        clearGrade = float(grade)
    gradeList.append(models.grade.grade(clearSubject, clearGrade))

def shortGrade():
    for i in gradeList:
        if i.grade % 1 == 0:
            i.grade = int(i.grade)
        else:
            pass

def addTestSubjects():
    addSubject("English","5")
    addSubject("OS","4")
    addSubject("Polish","3")
    addSubject("Math", "3")
    addSubject("Deutch","5")
    addSubject("Work safety","6")
    addSubject("Biology","1")
    addSubject("Physics", "3-")
    addSubject("Geography", "2")
    addSubject("Ethics", "3+")
    addSubject("test","+1")

def searchForSubject(index):
    item = gradeList.__getitem__(index)
    return item.subject

def searchForGrade(index):
    item = gradeList.__getitem__(index)
    return item.grade