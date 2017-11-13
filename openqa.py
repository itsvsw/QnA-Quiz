#openqa --- used to open a filehandle, read and delimit "questions and answers"
#openqa --- based off '-' started 9NOV17 0730
import random # random is used when determining what question should be asked
print("Attempting to open file 'qatest.txt' in curdir...\n")
inFile = open("qatest.txt",'r')
q = []
a = []
for l in inFile:
    i = l.find('-') #seperate questions and answers based of offset of '-' which divides Q from A
    if i is -1:
        continue #if line doesn't contain '-', then it must not be a question, because there is no answer. Adding formatting markers in future iterations.
    q.append(l[0:i]) #from beginning up to, but not including the loc of '-'
    a.append(l[i+1:-1]) #skips the '-' with i+1, to end of line
if len(q) == len(a): #questions should equal answers, need error handling in case of not equal. Future debugging
    print("Number of questions EQUALS number of answers. Stripping both\n")
    x=0;
    while x < len(q):
        q[x] = q[x].strip()
        a[x] = a[x].strip()
        x += 1
totalQ = len(q)
reply = input(str(len(q)) + " questions found \nWould you like to proceed with quiz? (Y/N)")
if reply[0].lower() == 'y':
    print("YES")
else:
    print("NO")
def startQ():
    qAsked = 0
    while True:
        qNum = qOrder[0]
        qAsked += 1
        print("Question #", str(qAsked), ":", q[qNum])        
        qOrder.pop(0)
        userAnswer = input()
        def checkA():
            if userAnswer.lower() == a[qNum].lower():
                print("CORRECT")
        checkA()
        if qAsked == totalQ: break
        

qOrder = list(range(totalQ))
random.shuffle(qOrder)
print(qOrder)
startQ()
