from bottle import *
from time import *
from math import floor
from os import remove
import sqlite3, csv
from json import *

HOSTNAME = 'localhost'
MASTER_PASSWORD = 'notthepassword'

#Utility functions used for gathering data for the data base, calculating finish time,
def createDatabase():
    
    database = sqlite3.connect('runners.db')
    database.execute("CREATE TABLE runners (id INTEGER PRIMARY KEY, runnerNumber INTEGER, name char(100) NOT NULL, gender char(3) NOT NULL, age char (3) NOT NULL, category INTEGER NOT NULL, hasFinished bool NOT NULL, finishTime )")
    database.commit()

def addRunners(runnerinfo):
    
    database = sqlite3.connect('runners.db')
    database.execute("INSERT INTO runners(runnerNumber, name, gender, age, category, hasFinished, finishTime) VALUES (?,?,?,?,?,?,?)",(runnerinfo[4],runnerinfo[0]+' '+runnerinfo[1],runnerinfo[2],runnerinfo[3], runnerinfo[5],0,0))
    database.commit()

def readInputFile(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            #print(row)
            addRunners(row)


def getFinishTime(finishTime):
    timeFile = open('startTime.txt','r')
    startTime = timeFile.readline()
    timeFile.close()
    finishTime = time() - float(startTime)
    minutes = finishTime/60
    seconds = (minutes - floor(minutes))*60
    return "%02d:%02d"%(minutes,seconds)

def getRunnerInfo(gender, age, hasFinished, orderBy):
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, name, category FROM runners WHERE gender LIKE '%s' AND age LIKE '%s' AND hasFinished LIKE '%s' ORDER BY %s"%(gender, age, hasFinished, orderBy))
    runners = c.fetchall()
    return runners

def getAllRunnerData(runnerID):
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, name, gender, age, category, hasFinished, finishTime  FROM runners WHERE runnerNumber LIKE '%s'"%runnerID)
    runners = c.fetchall()
    return runners


def getRunnerResults(gender, age, hasFinished, orderBy):
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, name, finishTime FROM runners WHERE gender LIKE '%s' AND age LIKE '%s' AND hasFinished LIKE '%s' ORDER BY %s"%(gender, age, hasFinished, orderBy))
    runners = c.fetchall()
    return runners

#Generates a CSV file with list items separated by semicolons  
def generateRaceResults():
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT name, gender, age, runnerNumber, category, finishTime FROM runners WHERE name NOT LIKE '' ORDER BY runnerNumber")
    runners = c.fetchall()
    print(runners[0])
    dataFile = open('raceResults.csv','w')
    for runner in runners:
        runnerInfo = str(runner[0])+';'+str(runner[1])+';'+str(runner[2])+';'+str(runner[3])+';'+str(runner[4])+';'+str(runner[5])+'\n'
        dataFile.write(runnerInfo)
    dataFile.close()
    




#These functions output the Javascript list of runners used in the simulator
def outputRunnerSim():
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, age, gender FROM runners WHERE hasFinished LIKE '0' ")
    runners = c.fetchall()
    return runners

def runSim():
    outputString = '['
    runners = outputRunnerSim()
    for runner in runners:
        
        if(runner[2]=='M'):
            if(runner[1]=='A'):
                colorCategory = 0
            elif(runner[1]=='US'):
                colorCategory = 1
            else:
                colorCategory=2
        else:
            if(runner[1]=='A'):
                colorCategory = 3
            elif(runner[1]=='US'):
                colorCategory = 4
            else:
                colorCategory = 5
        outputString+='[%s,%s],'%(runner[0],colorCategory)
    runnerSimData = open('runnersim.txt','w')
    runnerSimData.write(outputString)
    runnerSimData.close()

    
#Start of routing functions for Bottle
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root = '/Users/weinbergmath/Sites/')

@route('/main/')
@route('/')
def mainMenu():
   # runSim()
    return template('mainmenu.tpl')

@post('/admin/')
def admin():
    password = request.forms.get('password')
    adminoption = request.forms.get('adminoption')
    if(password == MASTER_PASSWORD):
        if(adminoption == '1'):
            startTime = strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
            timeFile = open('startTime.txt','w')
            timeFile.write(str(time()))
            timeFile.close()    
            return template('starttime.tpl', startTime = startTime)
        elif(adminoption=='2'):
            conn = sqlite3.connect('runners.db')
            c = conn.cursor()
            c.execute("SELECT runnerNumber, name, category FROM runners  ORDER BY runnerNumber")
            runners = c.fetchall()
            c.close()

            return template('listRunnersEdit.tpl', runners = runners)
        elif(adminoption=='3'):
 
            return template('addRunner.tpl')
        
        elif(adminoption=='4'):
            remove('runners.db')
            #remove('startTime.txt')
            createDatabase()
            readInputFile('5krunners.csv')
 
            return "Database reloaded."

        elif(adminoption=='5'):
            generateRaceResults()
            return "Race results file generated."
    else:
        return "Wrong master password!"

#Runner database operations

@get('/editRunner/')
def listAllRunners():

    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, name, category FROM runners  ORDER BY runnerNumber")
    runners = c.fetchall()
    c.close()
 
    return template('listRunnersEdit.tpl', runners = runners)



@get('/editRunner/<runnerID>')
def getEditPage(runnerID):
    runners = getAllRunnerData(runnerID)
       #runnerNumber, name, gender, age, category, hasFinished, finishTime
   
    if (len(runners)==0):
        return "No runner with that ID exists!"
    else:
        runnerList = []
        for data in runners[0]:
            runnerList.append(data)
       # print(runnerList)
        genderSelect=['','']
        ageSelect = ['','','','']
        categorySelect = ['','','','','','']
        if (runnerList[2]=='M'):
            genderSelect = ['selected','']
        else:
            genderSelect =['','selected']
 
        if(runnerList[3]=='LS'):
            ageSelect = ['selected','','','']
        elif(runnerList[3]=='MS'):
            ageSelect = ['','selected','','']
        elif(runnerList[3]=='US'):
            ageSelect = ['','','selected','']
        else:
            ageSelect = ['','','','selected']

        if(runnerList[4]==0):
            categorySelect = ['selected','','','','','']
        elif(runnerList[4]==1):
            categorySelect = ['','selected','','','','']
        elif(runnerList[4]==2):
            categorySelect= ['','','selected','','','']
        elif(runnerList[4]==3):
            categorySelect = ['','','','selected','','']
        elif(runnerList[4]==4):
            categorySelect = ['','','','','selected','']
            
        else:
            ageSelect = ['','','','','','selected']
        if(runnerList[5]==1):
            runnerList[5]='checked'
        else:
            runnerList[5]=''
        runnerList[2] = genderSelect
        runnerList[3] = ageSelect
        runnerList[4] = categorySelect
        #print(runnerList)
        return template('editRunner.tpl',runner = runnerList)

@post('/editRunner/')
def editRunner():
    runner = []
    runner.append(request.forms.get('runnerID'))
    runner.append(request.forms.get('name'))
    runner.append(request.forms.get('gender'))
    runner.append(request.forms.get('age'))
    runner.append(request.forms.get('category'))
    runner.append(request.forms.get('hasFinished'))
    runner.append(request.forms.get('finishTime'))
    if(runner[5]=='on'):
        runner[5]=1
    else:
        runner[5]=0
    print(runner)
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("UPDATE runners SET runnerNumber =?,name=?, gender=?, age=?, category=?, hasFinished = ?, finishTime = ? WHERE runnerNumber LIKE ?", (runner[0],runner[1],runner[2], runner[3],runner[4],runner[5], runner[6],runner[0]))
    conn.commit()

    return template('mainmenu.tpl')
    
@get('/addRunner/')
def addRunner():

    return template('addRunner.tpl')
@post('/addRunner/')
def confirmRunner():
    runner = []
    runner.append(request.forms.get('runnerID'))
    runner.append(request.forms.get('name'))
    runner.append(request.forms.get('gender'))
    runner.append(request.forms.get('age'))
    runner.append(request.forms.get('category'))
                  


    return template('confirmRunnerInfo.tpl',runner = runner)

@post('/insertRunner/')
def insertRunner():
    runner = []
    runner.append(request.forms.get('runnerID'))
    runner.append(request.forms.get('name'))
    runner.append(request.forms.get('gender'))
    runner.append(request.forms.get('age'))
    runner.append(request.forms.get('category'))
   
    database = sqlite3.connect('runners.db')
    database.execute("INSERT INTO runners(runnerNumber, name, gender, age, category, hasFinished, finishTime) VALUES (?,?,?,?,?,?,?)",(runner[0],runner[1],runner[2],runner[3],runner[4],0,0))
    database.commit()

    return template('mainmenu.tpl')

#Pages for stopping/restarting runners from /men/ or /women/ using a GET operation

@get('/stoptime/<runnerID>')
def stopTime(runnerID):
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, name  FROM runners WHERE runnerNumber LIKE '%s'"%runnerID)
    runners = c.fetchall()
    if (len(runners)==0):
        return "No runner with that ID exists!"
    else:
        finishTime = getFinishTime(time())
        c = conn.cursor()
        c.execute("UPDATE runners SET hasFinished = ?, finishTime = ? WHERE runnerNumber LIKE ?", (1, finishTime, runnerID))
        conn.commit()
    return template('mainmenu.tpl')       

@get('/restarttime/<runnerID>')
def restartTime(runnerID):
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, name  FROM runners WHERE runnerNumber LIKE '%s'"%runnerID)
    runners = c.fetchall()
    if (len(runners)==0):
        return "No runner with that ID exists!"
    else:
             
        c = conn.cursor()
        c.execute("UPDATE runners SET hasFinished = ?, finishTime = ? WHERE runnerNumber LIKE ?", (0, 0, runnerID))
        conn.commit()
    return template('mainmenu.tpl')       

@get('/mobile/stoptime/<runnerID>')
def stopTime(runnerID):
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, name, hasFinished  FROM runners WHERE runnerNumber LIKE '%s'"%runnerID)
    runners = c.fetchall()
    if (len(runners)==0):
        runnerID = 99998
    elif(runners[0][2]!=1):
        finishTime = getFinishTime(time())
        c = conn.cursor()
        c.execute("UPDATE runners SET hasFinished = ?, finishTime = ? WHERE runnerNumber LIKE ?", (1, finishTime, runnerID))
        conn.commit()
    else:
        runnerID = 99999
    return template('inputpad2.tpl', runnerID = runnerID, hostname = HOSTNAME)  




#Functions for stopping a runner directly through the manual input page at /stopRunner/:
@get('/stopRunner/')
def manualStopRunner():
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber FROM runners WHERE hasFinished LIKE '1' ORDER BY finishTime DESC")
    runners = c.fetchmany(10)
    lastrunners = ''
    for runner in runners[0:len(runners)-1]:
          lastrunners=lastrunners+'<td><a href = "/restartRunner/' + str(runner[0])+'/">' + str(runner[0]) + '</a></td>'
 
        

    return template('enterRunner.tpl', message = '', lastrunners = lastrunners)

@get('/stopTime/')
@post('/stopTime/')
def stopTime():
    runnerID = request.forms.get('runnerID')
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, name, hasFinished  FROM runners WHERE runnerNumber LIKE '%s'"%runnerID)
    runners = c.fetchall()
    if (len(runners)==0):
        message =  "No runner with that ID exists!"
    elif(runners[0][2]==1):
        message = "Runner %s already stopped!"%(runnerID)
    else:
        message = "Runner %s has been stopped."%(runnerID)
        finishTime = getFinishTime(time())
        c = conn.cursor()
        c.execute("UPDATE runners SET hasFinished = ?, finishTime = ? WHERE runnerNumber LIKE ?", (1, finishTime, runnerID))
        conn.commit()
        conn = sqlite3.connect('runners.db')
        c = conn.cursor()
    c.execute("SELECT runnerNumber FROM runners WHERE hasFinished LIKE '1' ORDER BY finishTime DESC")
    runners = c.fetchmany(10)
    lastrunners = ''
    for runner in runners[0:len(runners)-1]:
        lastrunners=lastrunners+'<td><a href = "/restartRunner/' + str(runner[0])+'/">' + str(runner[0]) + '</a></td>'
        
    return template('enterRunner.tpl', message = message, lastrunners = lastrunners)       

@get('/restartRunner/<runnerID>/')
def restartTime(runnerID):
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, name  FROM runners WHERE runnerNumber LIKE '%s'"%runnerID)
    runners = c.fetchall()
    if (len(runners)==0):
        message = "No runner with that ID exists!"
    else:
             
        c = conn.cursor()
        c.execute("UPDATE runners SET hasFinished = ?, finishTime = ? WHERE runnerNumber LIKE ?", (0, 0, runnerID))
        conn.commit()
        message = "Runner " + runnerID + " has been restarted."
        conn = sqlite3.connect('runners.db')
        c = conn.cursor()
        c.execute("SELECT runnerNumber FROM runners WHERE hasFinished LIKE '1' ORDER BY finishTime DESC")
        runners = c.fetchmany(10)
        lastrunners = ''
        for runner in runners[0:len(runners)-1]:
              lastrunners=lastrunners+'<td><a href = "/restartRunner/' + str(runner[0])+'/">' + str(runner[0]) + '</a></td>'
        
    return template('enterRunner.tpl', message = message, lastrunners = lastrunners)       

#A master list of all runners that have not finished the race
@route('/runners')
def listRunners():
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, name, category FROM runners WHERE hasFinished LIKE '0' ORDER BY runnerNumber")
    runners = c.fetchall()
    finished = getRunnerResults('M','A','1','finishTime')
    return template('runnerlist.tpl',runners = runners, finished = finished)

@route('/stoppedRunners/')
def listRunners():
    conn = sqlite3.connect('runners.db')
    c = conn.cursor()
    c.execute("SELECT runnerNumber, name, finishTime FROM runners WHERE hasFinished LIKE '1' ORDER BY finishTime DESC")
    runners = c.fetchall()
    return template('resultslist.tpl',runners = runners,category = 'All Runners')

#Result generating functions for each category of runner. The first set is for generating lists of runners in each category, with buttons for stopping them individually.

@route('/men/')
def listMen():
   runners = getRunnerInfo('M','A','0','runnerNumber')
   finished = getRunnerResults('M','A','1','finishTime')
   
   return template('runnerlist.tpl',runners = runners, finished = finished)


@route('/women/')
def listWomen():
    runners = getRunnerInfo('F','A','0','runnerNumber')
    finished = getRunnerResults('F','A','1','finishTime')
   
    return template('runnerlist.tpl',runners = runners, finished = finished)

@route('/HSmale/')
def listUSmale():
    runners = getRunnerInfo('M','HS','0','runnerNumber')
    finished = getRunnerResults('M','HS','1','finishTime')
   
    return template('runnerlist.tpl',runners = runners, finished = finished)

@route('/HSfemale/')
def listUSfemale():
    runners = getRunnerInfo('F','HS','0','runnerNumber')
    finished = getRunnerResults('F','HS','1','finishTime')
   
    return template('runnerlist.tpl',runners = runners, finished = finished)

@route('/MSmale/')
def listUSmale():
    runners = getRunnerInfo('M','MS','0','runnerNumber')
    finished = getRunnerResults('M','MS','1','finishTime')
   
    return template('runnerlist.tpl',runners = runners, finished = finished)

@route('/MSfemale/')
def listUSfemale():
    runners = getRunnerInfo('F','MS','0','runnerNumber')
    finished = getRunnerResults('F','MS','1','finishTime')
   
    return template('runnerlist.tpl',runners = runners, finished = finished)

@route('/LSmale/')
def listLSmale():
    runners = getRunnerInfo('M','LS','0','runnerNumber')
    finished = getRunnerResults('M','LS','1','finishTime')
   
    return template('runnerlist.tpl',runners = runners, finished = finished)

@route('/LSfemale/')
def listLSfemale():
    runners = getRunnerInfo('F','LS','0','runnerNumber')
    finished = getRunnerResults('F','LS','1','finishTime')
   
    return template('runnerlist.tpl',runners = runners, finished = finished)

#Routes corresponding to lists of finished runners for each category.

@route('/men/results/')
def menResults():
    runners = getRunnerResults('M','A','1','finishTime')

    return template('resultslist.tpl',runners = runners,category = 'Adult Men')

@route('/women/results/')
def womenResults():
    runners = getRunnerResults('F','A','1','finishTime')

    return template('resultslist.tpl',runners = runners,category = 'Adult Women')

@route('/HSmale/results/')
def USMaleResults():
    runners = getRunnerResults('M','HS','1','finishTime')

    return template('resultslist.tpl',runners = runners,category = 'HS Male')

@route('/HSfemale/results/')
def USFemaleResults():
    runners = getRunnerResults('F','HS','1','finishTime')

    return template('resultslist.tpl',runners = runners,category = 'HS Female')

@route('/MSmale/results/')
def USMaleResults():
    runners = getRunnerResults('M','MS','1','finishTime')

    return template('resultslist.tpl',runners = runners,category = 'MS Male')

@route('/MSfemale/results/')
def USFemaleResults():
    runners = getRunnerResults('F','MS','1','finishTime')

    return template('resultslist.tpl',runners = runners,category = 'MS Female')


@route('/LSmale/results/')
def LSMaleResults():
    runners = getRunnerResults('M','LS','1','finishTime')

    return template('resultslist.tpl',runners = runners,category = 'LS Boys')

@route('/LSfemale/results/')
def LSFemaleResults():
    runners = getRunnerResults('F','LS','1','finishTime')

    return template('resultslist.tpl',runners = runners,category = 'LS Girls')

#Unused functions that I don't want to totally get rid of yet:

@get('/mobile/')
def showMobile():
    return template('inputpad2.tpl', runnerID = 99997, hostname = HOSTNAME)


@route('/upload/', method = 'POST')
def uploadFile():
    upload = request.files.get('upload')
    name,ext = os.path.splitext(upload.filename)
    if (name != '5krunners'):
        return 'Incorrect input file name.'
    else:
        datafile = open('5krunners.csv')
        upload.save(datafile)
        datafile.close()
        return 'File uploaded successfully'

   
#run(host = HOSTNAME,port = 8080, debug = False)
run(host = HOSTNAME, port = 8080, server='cherrypy', debug=False)



#createDatabase()
#addRunners()
