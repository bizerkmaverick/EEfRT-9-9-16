#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.0),
    on September 09, 2016, at 09:45
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'eefrt 2.0'  # from the Builder filename that created this script
expInfo = {u'Handedness': u'r/l', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\dime-lab\\Desktop\\new eefrt test\\new-eefrt.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.0,0.0,0.0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instrpractice"
instrpracticeClock = core.Clock()
Inst_txt = visual.TextStim(win=win, name='Inst_txt',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
#EEfRT (Treadway et al., 2009) 
#organized and developed for Psychopy by Erick Rogers 08/15/16
#bizerkmaverick@gmail.com


dhand = "bob"
ndhand = "jim"
if expInfo['Handedness'].lower().startswith("r") == True:
    dhand = "right"
    ndhand = "left"
elif expInfo['Handedness'].lower().startswith("l") == True:
    dhand = "left"
    ndhand = "right"
else:
    dhand = "JimBob"
    ndhand = "JimBob"
instr_msg = "You will complete multiple rounds of a game.\n\nIn each round, you may choose the rounds difficulty.\n\nEasy rounds require you to use your %s index finger to push the SPACEBAR multiple times to fill the meter.\n\nHard rounds require you to use your %s pinky finger to push the SPACEBAR multiple times to fill the meter.\n\nEasy rounds are worth 1 point.\n\nHard rounds are worth 2 to 4 points.\n\nFor each round, you must fill the meter to earn points and you will have a high, medium, or low chance of earning points in each round.\n\nIf you do not choose the round difficulty within 5 seconds, the difficulty will be chosen randomly for you.\n\nDo you have any questions?\n\nPress ENTER to continue." %(dhand, ndhand)

bar_textE = "Use your %s index finger." %dhand
bar_textH = "Use your %s pinky finger." %ndhand

# Initialize components for Routine "Pract_Instr"
Pract_InstrClock = core.Clock()
Prac_Instr = visual.TextStim(win=win, name='Prac_Instr',
    text='You will now complete 4 practice trials. \n\nSelect the easy task first and the hard task second. \n\nThen choose either task difficulty for the remaining rounds. \n\nPoints are not earned on the practice trials.  \n\nPress ENTER to begin the practice.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "cross_pract"
cross_practClock = core.Clock()
text2_2 = visual.TextStim(win=win, name='text2_2',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "pract_Select"
pract_SelectClock = core.Clock()
#EEfRT (Treadway et al., 2009) 
#organized and developed for Psychopy by Erick Rogers 08/15/16
#bizerkmaverick@gmail.com


dhand = "bob"
ndhand = "jim"
if expInfo['Handedness'] == "right":
    dhand = "right"
    ndhand = "left"
elif expInfo['Handedness'] == "left":
    dhand = "left"
    ndhand = "right"
else:
    dhand = "JimBob"
    ndhand = "JimBob"

#hand = expInfo['Handedness']
instrText_2 = visual.TextStim(win=win, name='instrText_2',
    text='Choose Your Task:\n\nPress A for Easy Task\n\nPress B for Hard Task',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Ready?',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "pract_A"
pract_AClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, .5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

balloonSize=0.00
countdownStarted = False
background_2 = visual.Rect(
    win=win, name='background_2',
    width=[0.2, .55][0], height=[0.2, .55][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
barBody_2 = visual.Rect(
    win=win, name='barBody_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[0.553,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[0.553,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
feedbackText=""
feedbackMsg = visual.TextStim(win=win, name='feedbackMsg',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "pract_B"
pract_BClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=(0, .5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


countdownStarted = False
backgroundB_2 = visual.Rect(
    win=win, name='backgroundB_2',
    width=[0.2, .55][0], height=[0.2, .55][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
barBodyB_2 = visual.Rect(
    win=win, name='barBodyB_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[0.553,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[0.553,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
feedbackText=""
feedbackMsg = visual.TextStim(win=win, name='feedbackMsg',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial_instr"
trial_instrClock = core.Clock()
instr_text2 = visual.TextStim(win=win, name='instr_text2',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
dhand = "bob"
ndhand = "jim"
if expInfo['Handedness'].lower().startswith("r") == True:
    dhand = "right"
    ndhand = "left"
elif expInfo['Handedness'].lower().startswith("l") == True:
    dhand = "left"
    ndhand = "right"
else:
    dhand = "JimBob"
    ndhand = "JimBob"
instr_msg = "You will complete multiple rounds of a game.\n\nIn each round, you may choose the rounds difficulty.\n\nEasy rounds require you to use your %s index finger to push the SPACEBAR multiple times to fill the meter.\n\nHard rounds require you to use your %s pinky finger to push the SPACEBAR multiple times to fill the meter.\n\nEasy rounds are worth 1 point.\n\nHard rounds are worth 2 to 4 points.\n\nFor each round, you must fill the meter to earn points and you will have a high, medium, or low chance of earning points in each round.\n\nIf you do not choose the round difficulty within 5 seconds, the difficulty will be chosen randomly for you.\n\nDo you have any questions?\n\nPress ENTER to continue." %(dhand, ndhand)

bar_textE = "Use your %s index finger." %dhand
bar_textH = "Use your %s pinky finger." %ndhand

instr_msg2 = "Do you have any questions?\n\nYou will now complete 20 minutes worth of rounds. Your goal is to earn as many points as possible.\n\nREMEMBER:\nEasy rounds take less time BUT earn only 1 point.\nHard rounds take more time BUT earn more points.\n\nOn easy rounds, use your %s index finger.\nOn hard rounds, use your %s pinky finger.\n\nPress ENTER to begin." %(dhand, ndhand)

# Initialize components for Routine "cross"
crossClock = core.Clock()
#Count Frames for all trials/rewards
ExpTime = -1

text2 = visual.TextStim(win=win, name='text2',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
from psychopy import visual
import random
#initialize scoring variables
#round score
rscore = 0
#total score
tscore = 0
instrText = visual.TextStim(win=win, name='instrText',
    text='Choose Your Task:\n\nProbability of win:\n\nPress A for Easy Task\n1 point',
    font='Arial',
    pos=[0, .3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
percentText = visual.TextStim(win=win, name='percentText',
    text='default text',
    font='Arial',
    pos=[-.14, .25], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
moneyText = visual.TextStim(win=win, name='moneyText',
    text='default text',
    font='Arial',
    pos=[0, -.2], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Ready?',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=(0, .5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

balloonSize=0.00
countdownStarted = False
background = visual.Rect(
    win=win, name='background',
    width=[0.2, .55][0], height=[0.2, .55][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
barBody = visual.Rect(
    win=win, name='barBody',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[0.553,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[0.553,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
feedbackText=""
feedbackMsg = visual.TextStim(win=win, name='feedbackMsg',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "rFeedback"
rFeedbackClock = core.Clock()
rFeedbackText=""
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trialB"
trialBClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='default text',
    font='Arial',
    pos=(0, .5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


countdownStarted = False
backgroundB = visual.Rect(
    win=win, name='backgroundB',
    width=[0.2, .55][0], height=[0.2, .55][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
barBodyB = visual.Rect(
    win=win, name='barBodyB',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[0.553,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[0.553,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
feedbackText=""
feedbackMsg = visual.TextStim(win=win, name='feedbackMsg',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "rFeedbackH"
rFeedbackHClock = core.Clock()
rHardFeedbackText=""
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "FinalScore"
FinalScoreClock = core.Clock()

finalscore = visual.TextStim(win=win, name='finalscore',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instrpractice"-------
t = 0
instrpracticeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Inst_txt.setText(instr_msg)
Inst_Key = event.BuilderKeyResponse()

# keep track of which components have finished
instrpracticeComponents = [Inst_txt, Inst_Key]
for thisComponent in instrpracticeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instrpractice"-------
while continueRoutine:
    # get current time
    t = instrpracticeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Inst_txt* updates
    if t >= 0.0 and Inst_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        Inst_txt.tStart = t
        Inst_txt.frameNStart = frameN  # exact frame index
        Inst_txt.setAutoDraw(True)
    
    # *Inst_Key* updates
    if t >= 0.0 and Inst_Key.status == NOT_STARTED:
        # keep track of start time/frame for later
        Inst_Key.tStart = t
        Inst_Key.frameNStart = frameN  # exact frame index
        Inst_Key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Inst_Key.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrpracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrpractice"-------
for thisComponent in instrpracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "instrpractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Pract_Instr"-------
t = 0
Pract_InstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Prac_InstrKey = event.BuilderKeyResponse()
# keep track of which components have finished
Pract_InstrComponents = [Prac_Instr, Prac_InstrKey]
for thisComponent in Pract_InstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Pract_Instr"-------
while continueRoutine:
    # get current time
    t = Pract_InstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Prac_Instr* updates
    if t >= 0.0 and Prac_Instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        Prac_Instr.tStart = t
        Prac_Instr.frameNStart = frameN  # exact frame index
        Prac_Instr.setAutoDraw(True)
    
    # *Prac_InstrKey* updates
    if t >= 0.0 and Prac_InstrKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        Prac_InstrKey.tStart = t
        Prac_InstrKey.frameNStart = frameN  # exact frame index
        Prac_InstrKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Prac_InstrKey.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Pract_InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pract_Instr"-------
for thisComponent in Pract_InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Pract_Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsP = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trialsP')
thisExp.addLoop(trialsP)  # add the loop to the experiment
thisTrialsP = trialsP.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsP.rgb)
if thisTrialsP != None:
    for paramName in thisTrialsP.keys():
        exec(paramName + '= thisTrialsP.' + paramName)

for thisTrialsP in trialsP:
    currentLoop = trialsP
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsP.rgb)
    if thisTrialsP != None:
        for paramName in thisTrialsP.keys():
            exec(paramName + '= thisTrialsP.' + paramName)
    
    # ------Prepare to start Routine "cross_pract"-------
    t = 0
    cross_practClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    cross_practComponents = [text2_2]
    for thisComponent in cross_practComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "cross_pract"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = cross_practClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text2_2* updates
        if t >= 0.0 and text2_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text2_2.tStart = t
            text2_2.frameNStart = frameN  # exact frame index
            text2_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text2_2.status == STARTED and t >= frameRemains:
            text2_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cross_practComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cross_pract"-------
    for thisComponent in cross_practComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "pract_Select"-------
    t = 0
    pract_SelectClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    resp_pract = event.BuilderKeyResponse()
    # keep track of which components have finished
    pract_SelectComponents = [resp_pract, instrText_2]
    for thisComponent in pract_SelectComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pract_Select"-------
    while continueRoutine:
        # get current time
        t = pract_SelectClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *resp_pract* updates
        if t >= 0.0 and resp_pract.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_pract.tStart = t
            resp_pract.frameNStart = frameN  # exact frame index
            resp_pract.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp_pract.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp_pract.status == STARTED:
            theseKeys = event.getKeys(keyList=['a', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp_pract.keys = theseKeys[-1]  # just the last key pressed
                resp_pract.rt = resp_pract.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *instrText_2* updates
        if t >= 0.0 and instrText_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instrText_2.tStart = t
            instrText_2.frameNStart = frameN  # exact frame index
            instrText_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pract_SelectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pract_Select"-------
    for thisComponent in pract_SelectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #Press A for easy, B for hard
    if resp_pract.keys=='a': 
        nRepsPE=1
        nRepsPH=0
    elif resp_pract.keys=='b':
        nRepsPE=0
        nRepsPH=1
    
    # check responses
    if resp_pract.keys in ['', [], None]:  # No response was made
        resp_pract.keys=None
    trialsP.addData('resp_pract.keys',resp_pract.keys)
    if resp_pract.keys != None:  # we had a response
        trialsP.addData('resp_pract.rt', resp_pract.rt)
    # the Routine "pract_Select" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Ready"-------
    t = 0
    ReadyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ReadyComponents = [text]
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Ready"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ReadyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready"-------
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    nRepsPE = data.TrialHandler(nReps=nRepsPE, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='nRepsPE')
    thisExp.addLoop(nRepsPE)  # add the loop to the experiment
    thisNRepsPE = nRepsPE.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNRepsPE.rgb)
    if thisNRepsPE != None:
        for paramName in thisNRepsPE.keys():
            exec(paramName + '= thisNRepsPE.' + paramName)
    
    for thisNRepsPE in nRepsPE:
        currentLoop = nRepsPE
        # abbreviate parameter names if possible (e.g. rgb = thisNRepsPE.rgb)
        if thisNRepsPE != None:
            for paramName in thisNRepsPE.keys():
                exec(paramName + '= thisNRepsPE.' + paramName)
        
        # ------Prepare to start Routine "pract_A"-------
        t = 0
        pract_AClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_4.setText(bar_textE)
        npumps=0
        maxPumps=1
        #balloon image's starting size
        balloonSize=0.00
        popped=False
        
        if not countdownStarted:
            countdownClock = core.CountdownTimer(7)
            countdownStarted = True
        #7 second timer
        # keep track of which components have finished
        pract_AComponents = [text_4, background_2, barBody_2]
        for thisComponent in pract_AComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "pract_A"-------
        while continueRoutine:
            # get current time
            t = pract_AClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            if t >= 0.0 and text_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_4.tStart = t
                text_4.frameNStart = frameN  # exact frame index
                text_4.setAutoDraw(True)
            if event.getKeys(['space']):
                npumps+=1
                if npumps>=maxPumps:
                    popped=True
                    continueRoutine=False
            balloonSize=npumps*0.0184
            timeRemaining = countdownClock.getTime()
            
            if timeRemaining <= 0.0:
                continueRoutine = False # end this trial immediately
                countdownStarted = False
            
            # *background_2* updates
            if t >= 0.0 and background_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                background_2.tStart = t
                background_2.frameNStart = frameN  # exact frame index
                background_2.setAutoDraw(True)
            
            # *barBody_2* updates
            if t >= 0.0 and barBody_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                barBody_2.tStart = t
                barBody_2.frameNStart = frameN  # exact frame index
                barBody_2.setAutoDraw(True)
            if barBody_2.status == STARTED:  # only update if drawing
                barBody_2.setPos([0, 0], log=False)
                barBody_2.setSize([.2, balloonSize], log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pract_AComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pract_A"-------
        for thisComponent in pract_AComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        countdownStarted = False
        # the Routine "pract_A" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback"-------
        t = 0
        FeedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if popped==True:
            feedbackText="You completed the task!"
        else:
            feedbackText="You failed to complete the task."
        feedbackMsg.setText(feedbackText)
        # keep track of which components have finished
        FeedbackComponents = [feedbackMsg]
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *feedbackMsg* updates
            if t >= 0.0 and feedbackMsg.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedbackMsg.tStart = t
                feedbackMsg.frameNStart = frameN  # exact frame index
                feedbackMsg.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedbackMsg.status == STARTED and t >= frameRemains:
                feedbackMsg.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed nRepsPE repeats of 'nRepsPE'
    
    
    # set up handler to look after randomisation of conditions etc
    nRepsPH = data.TrialHandler(nReps=nRepsPH, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='nRepsPH')
    thisExp.addLoop(nRepsPH)  # add the loop to the experiment
    thisNRepsPH = nRepsPH.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNRepsPH.rgb)
    if thisNRepsPH != None:
        for paramName in thisNRepsPH.keys():
            exec(paramName + '= thisNRepsPH.' + paramName)
    
    for thisNRepsPH in nRepsPH:
        currentLoop = nRepsPH
        # abbreviate parameter names if possible (e.g. rgb = thisNRepsPH.rgb)
        if thisNRepsPH != None:
            for paramName in thisNRepsPH.keys():
                exec(paramName + '= thisNRepsPH.' + paramName)
        
        # ------Prepare to start Routine "pract_B"-------
        t = 0
        pract_BClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_5.setText(bar_textH)
        npumps=0
        maxPumps=100
        #balloon image's starting size
        balloonSize=0.00
        popped=False
        
        if not countdownStarted:
            countdownClock = core.CountdownTimer(21)
            countdownStarted = True
        #21 second timer
        # keep track of which components have finished
        pract_BComponents = [text_5, backgroundB_2, barBodyB_2]
        for thisComponent in pract_BComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "pract_B"-------
        while continueRoutine:
            # get current time
            t = pract_BClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if t >= 0.0 and text_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_5.tStart = t
                text_5.frameNStart = frameN  # exact frame index
                text_5.setAutoDraw(True)
            if event.getKeys(['space']):
                npumps+=1
                if npumps>=maxPumps:
                    popped=True
                    continueRoutine=False
            balloonSize=npumps*0.015
            timeRemaining = countdownClock.getTime()
            
            if timeRemaining <= 0.0:
                continueRoutine = False # end this trial immediately
                countdownStarted = False
            
            # *backgroundB_2* updates
            if t >= 0.0 and backgroundB_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                backgroundB_2.tStart = t
                backgroundB_2.frameNStart = frameN  # exact frame index
                backgroundB_2.setAutoDraw(True)
            
            # *barBodyB_2* updates
            if t >= 0.0 and barBodyB_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                barBodyB_2.tStart = t
                barBodyB_2.frameNStart = frameN  # exact frame index
                barBodyB_2.setAutoDraw(True)
            if barBodyB_2.status == STARTED:  # only update if drawing
                barBodyB_2.setPos([0, 0], log=False)
                barBodyB_2.setSize([.2, balloonSize/2.75], log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pract_BComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pract_B"-------
        for thisComponent in pract_BComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        countdownStarted = False
        # the Routine "pract_B" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback"-------
        t = 0
        FeedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if popped==True:
            feedbackText="You completed the task!"
        else:
            feedbackText="You failed to complete the task."
        feedbackMsg.setText(feedbackText)
        # keep track of which components have finished
        FeedbackComponents = [feedbackMsg]
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *feedbackMsg* updates
            if t >= 0.0 and feedbackMsg.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedbackMsg.tStart = t
                feedbackMsg.frameNStart = frameN  # exact frame index
                feedbackMsg.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedbackMsg.status == STARTED and t >= frameRemains:
                feedbackMsg.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed nRepsPH repeats of 'nRepsPH'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trialsP'


# ------Prepare to start Routine "trial_instr"-------
t = 0
trial_instrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instr_text2.setText(instr_msg2)
key_resp_3 = event.BuilderKeyResponse()

# keep track of which components have finished
trial_instrComponents = [instr_text2, key_resp_3]
for thisComponent in trial_instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial_instr"-------
while continueRoutine:
    # get current time
    t = trial_instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_text2* updates
    if t >= 0.0 and instr_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_text2.tStart = t
        instr_text2.frameNStart = frameN  # exact frame index
        instr_text2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_instr"-------
for thisComponent in trial_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "trial_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.xlsx'),
    seed=None, name='trials1')
thisExp.addLoop(trials1)  # add the loop to the experiment
thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
if thisTrials1 != None:
    for paramName in thisTrials1.keys():
        exec(paramName + '= thisTrials1.' + paramName)

for thisTrials1 in trials1:
    currentLoop = trials1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1.keys():
            exec(paramName + '= thisTrials1.' + paramName)
    
    # ------Prepare to start Routine "cross"-------
    t = 0
    crossClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    #Set ExpTime variable to 0 on the first loop only
    if trials1.thisN == 0:
        ExpTime = globalClock.getTime()
    # keep track of which components have finished
    crossComponents = [text2]
    for thisComponent in crossComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "cross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = crossClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #End trials1 if 20 minutes have passed
        if globalClock.getTime() - ExpTime >= 1200.0:
            trials1.finished = True
        
        # *text2* updates
        if t >= 0.0 and text2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text2.tStart = t
            text2.frameNStart = frameN  # exact frame index
            text2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text2.status == STARTED and t >= frameRemains:
            text2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cross"-------
    for thisComponent in crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "Instructions"-------
    t = 0
    InstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    prob=randint(1,(probability)) #probability for earning points
    
    selectBlock=randint(1,3) #randomly selects easy or hard trial 
    
    theProbText=(probText)
    
    hardMoney=randint(2,5) #earn 2-4 points on hard trials
    
    hardMoneyText=hardMoney 
    
    hardMoneyText="""Press B for Hard Task\n%s Points""" %hardMoney
    
    if not countdownStarted:
        countdownClock = core.CountdownTimer(5)
        countdownStarted = True
    #5 second timer
    trial_select = event.BuilderKeyResponse()
    percentText.setText(theProbText)
    moneyText.setText(hardMoneyText)
    # keep track of which components have finished
    InstructionsComponents = [trial_select, instrText, percentText, moneyText]
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        timeRemaining = countdownClock.getTime()
        
        if timeRemaining <= 0.0:
            continueRoutine = False
            countdownStarted = False
        
        # *trial_select* updates
        if t >= 0.0 and trial_select.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_select.tStart = t
            trial_select.frameNStart = frameN  # exact frame index
            trial_select.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(trial_select.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if trial_select.status == STARTED:
            theseKeys = event.getKeys(keyList=['a', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                trial_select.keys = theseKeys[-1]  # just the last key pressed
                trial_select.rt = trial_select.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *instrText* updates
        if t >= 0.0 and instrText.status == NOT_STARTED:
            # keep track of start time/frame for later
            instrText.tStart = t
            instrText.frameNStart = frameN  # exact frame index
            instrText.setAutoDraw(True)
        
        # *percentText* updates
        if t >= 0.0 and percentText.status == NOT_STARTED:
            # keep track of start time/frame for later
            percentText.tStart = t
            percentText.frameNStart = frameN  # exact frame index
            percentText.setAutoDraw(True)
        
        # *moneyText* updates
        if t >= 0.0 and moneyText.status == NOT_STARTED:
            # keep track of start time/frame for later
            moneyText.tStart = t
            moneyText.frameNStart = frameN  # exact frame index
            moneyText.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #Press A for easy, B for hard, otherwise chosen randomly after 5 secs
    if trial_select=='a': 
        nRepsA=1
        nRepsB=0
    elif trial_select=='b':
        nRepsA=0
        nRepsB=1
    elif selectBlock==1:
        nRepsA=0
        nRepsB=1
    else:
        nRepsA=1
        nRepsB=0
    #
    countdownStarted = False
    # check responses
    if trial_select.keys in ['', [], None]:  # No response was made
        trial_select.keys=None
    trials1.addData('trial_select.keys',trial_select.keys)
    if trial_select.keys != None:  # we had a response
        trials1.addData('trial_select.rt', trial_select.rt)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Ready"-------
    t = 0
    ReadyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ReadyComponents = [text]
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Ready"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ReadyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready"-------
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    repsA = data.TrialHandler(nReps=nRepsA, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='repsA')
    thisExp.addLoop(repsA)  # add the loop to the experiment
    thisRepsA = repsA.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRepsA.rgb)
    if thisRepsA != None:
        for paramName in thisRepsA.keys():
            exec(paramName + '= thisRepsA.' + paramName)
    
    for thisRepsA in repsA:
        currentLoop = repsA
        # abbreviate parameter names if possible (e.g. rgb = thisRepsA.rgb)
        if thisRepsA != None:
            for paramName in thisRepsA.keys():
                exec(paramName + '= thisRepsA.' + paramName)
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_6.setText(bar_textE)
        #reset round score to 0
        rscore = 0
        winE=rscore+1
        npumps=0
        maxPumps=30 #max presses to complete a trial
        #balloon image's starting size
        balloonSize=0.00
        popped=False
        nPumps=0
        if not countdownStarted:
            countdownClock = core.CountdownTimer(7)
            countdownStarted = True
        #7 second timer
        # keep track of which components have finished
        trialComponents = [text_6, background, barBody]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            if t >= 0.0 and text_6.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_6.tStart = t
                text_6.frameNStart = frameN  # exact frame index
                text_6.setAutoDraw(True)
            if event.getKeys(['space']):
                npumps+=1
                if npumps>=maxPumps:
                    popped=True
                    continueRoutine=False
            balloonSize=npumps*0.0184
            timeRemaining = countdownClock.getTime()
            
            if timeRemaining <= 0.0:
                continueRoutine = False # end this trial immediately
                countdownStarted = False
            
            # *background* updates
            if t >= 0.0 and background.status == NOT_STARTED:
                # keep track of start time/frame for later
                background.tStart = t
                background.frameNStart = frameN  # exact frame index
                background.setAutoDraw(True)
            
            # *barBody* updates
            if t >= 0.0 and barBody.status == NOT_STARTED:
                # keep track of start time/frame for later
                barBody.tStart = t
                barBody.frameNStart = frameN  # exact frame index
                barBody.setAutoDraw(True)
            if barBody.status == STARTED:  # only update if drawing
                barBody.setPos([0, 0], log=False)
                barBody.setSize([.2, balloonSize], log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #probability 3 is 50%, 26 is 88%, 51 is 12% chance to earn points
        if (probability)==3:
            if prob==1:
                if npumps>=maxPumps:
                    rscore=rscore+1
        
        elif (probability)==26:
            if prob>3:
                if npumps>=maxPumps:
                    rscore=rscore+1
        
        elif (probability)==51:
            if prob<7:
                if npumps>=maxPumps:
                    rscore=rscore+1
        #add current round score to total score
        tscore += rscore
        
        repsA.addData('# of presses', npumps)
        repsA.addData('round score', rscore)
        
        countdownStarted = False
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback"-------
        t = 0
        FeedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if popped==True:
            feedbackText="You completed the task!"
        else:
            feedbackText="You failed to complete the task."
        feedbackMsg.setText(feedbackText)
        # keep track of which components have finished
        FeedbackComponents = [feedbackMsg]
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *feedbackMsg* updates
            if t >= 0.0 and feedbackMsg.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedbackMsg.tStart = t
                feedbackMsg.frameNStart = frameN  # exact frame index
                feedbackMsg.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedbackMsg.status == STARTED and t >= frameRemains:
                feedbackMsg.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # ------Prepare to start Routine "rFeedback"-------
        t = 0
        rFeedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if rscore==winE:
                rFeedbackText="You win!\n1 point"
        else:
            rFeedbackText="No points on this trial."
        text_2.setText(rFeedbackText)
        # keep track of which components have finished
        rFeedbackComponents = [text_2]
        for thisComponent in rFeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "rFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rFeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_2* updates
            if t >= 0.0 and text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_2.tStart = t
                text_2.frameNStart = frameN  # exact frame index
                text_2.setAutoDraw(True)
            frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_2.status == STARTED and t >= frameRemains:
                text_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rFeedback"-------
        for thisComponent in rFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed nRepsA repeats of 'repsA'
    
    
    # set up handler to look after randomisation of conditions etc
    repsB = data.TrialHandler(nReps=nRepsB, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='repsB')
    thisExp.addLoop(repsB)  # add the loop to the experiment
    thisRepsB = repsB.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRepsB.rgb)
    if thisRepsB != None:
        for paramName in thisRepsB.keys():
            exec(paramName + '= thisRepsB.' + paramName)
    
    for thisRepsB in repsB:
        currentLoop = repsB
        # abbreviate parameter names if possible (e.g. rgb = thisRepsB.rgb)
        if thisRepsB != None:
            for paramName in thisRepsB.keys():
                exec(paramName + '= thisRepsB.' + paramName)
        
        # ------Prepare to start Routine "trialB"-------
        t = 0
        trialBClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_7.setText(bar_textH)
        #reset round score to 0
        rscore = 0
        winH=rscore+hardMoney
        npumps=0
        maxPumps=100
        #balloon image's starting size
        balloonSize=0.00
        popped=False
        nPumps=0
        if not countdownStarted:
            countdownClock = core.CountdownTimer(21)
            countdownStarted = True
        #21 second timer
        # keep track of which components have finished
        trialBComponents = [text_7, backgroundB, barBodyB]
        for thisComponent in trialBComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trialB"-------
        while continueRoutine:
            # get current time
            t = trialBClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_7* updates
            if t >= 0.0 and text_7.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_7.tStart = t
                text_7.frameNStart = frameN  # exact frame index
                text_7.setAutoDraw(True)
            if event.getKeys(['space']):
                npumps+=1
                if npumps>=maxPumps:
                    popped=True
                    continueRoutine=False
            balloonSize=npumps*0.015
            timeRemaining = countdownClock.getTime()
            
            if timeRemaining <= 0.0:
                continueRoutine = False # end this trial immediately
                countdownStarted = False
            
            # *backgroundB* updates
            if t >= 0.0 and backgroundB.status == NOT_STARTED:
                # keep track of start time/frame for later
                backgroundB.tStart = t
                backgroundB.frameNStart = frameN  # exact frame index
                backgroundB.setAutoDraw(True)
            
            # *barBodyB* updates
            if t >= 0.0 and barBodyB.status == NOT_STARTED:
                # keep track of start time/frame for later
                barBodyB.tStart = t
                barBodyB.frameNStart = frameN  # exact frame index
                barBodyB.setAutoDraw(True)
            if barBodyB.status == STARTED:  # only update if drawing
                barBodyB.setPos([0, 0], log=False)
                barBodyB.setSize([.2, balloonSize/2.75], log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialBComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trialB"-------
        for thisComponent in trialBComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #probability 3 is 50%, 26 is 88%, 51 is 12% chance to earn points
        if (probability)==3:
            if prob==1:
                if npumps>=maxPumps:
                    rscore=rscore+hardMoney
        
        elif (probability)==26:
            if prob>3:
                if npumps>=maxPumps:
                    rscore=rscore+hardMoney
        
        elif (probability)==51:
            if prob<7:
                if npumps>=maxPumps:
                    rscore=rscore+hardMoney
        #
        #add current round score to total score
        tscore += rscore
        
        repsB.addData('# of presses', npumps)
        repsB.addData('round score', rscore)
        trials1.addData('total score', tscore)
        
        countdownStarted = False
        # the Routine "trialB" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback"-------
        t = 0
        FeedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if popped==True:
            feedbackText="You completed the task!"
        else:
            feedbackText="You failed to complete the task."
        feedbackMsg.setText(feedbackText)
        # keep track of which components have finished
        FeedbackComponents = [feedbackMsg]
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *feedbackMsg* updates
            if t >= 0.0 and feedbackMsg.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedbackMsg.tStart = t
                feedbackMsg.frameNStart = frameN  # exact frame index
                feedbackMsg.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedbackMsg.status == STARTED and t >= frameRemains:
                feedbackMsg.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # ------Prepare to start Routine "rFeedbackH"-------
        t = 0
        rFeedbackHClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if rscore==winH:
                rHardFeedbackText="""You win!\n%s Points""" %hardMoney
        else:
            rHardFeedbackText="No points on this trial."
        text_3.setText(rHardFeedbackText)
        # keep track of which components have finished
        rFeedbackHComponents = [text_3]
        for thisComponent in rFeedbackHComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "rFeedbackH"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rFeedbackHClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_3* updates
            if t >= 0.0 and text_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_3.tStart = t
                text_3.frameNStart = frameN  # exact frame index
                text_3.setAutoDraw(True)
            frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_3.status == STARTED and t >= frameRemains:
                text_3.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rFeedbackHComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rFeedbackH"-------
        for thisComponent in rFeedbackHComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed nRepsB repeats of 'repsB'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials1'


# ------Prepare to start Routine "FinalScore"-------
t = 0
FinalScoreClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
finalScore="""Thank-you!\nYou earned a total of %s Point(s)""" %tscore
finalscore.setText(finalScore)
DoneKey = event.BuilderKeyResponse()
# keep track of which components have finished
FinalScoreComponents = [finalscore, DoneKey]
for thisComponent in FinalScoreComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "FinalScore"-------
while continueRoutine:
    # get current time
    t = FinalScoreClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *finalscore* updates
    if t >= 0.0 and finalscore.status == NOT_STARTED:
        # keep track of start time/frame for later
        finalscore.tStart = t
        finalscore.frameNStart = frameN  # exact frame index
        finalscore.setAutoDraw(True)
    
    # *DoneKey* updates
    if t >= 0.0 and DoneKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        DoneKey.tStart = t
        DoneKey.frameNStart = frameN  # exact frame index
        DoneKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if DoneKey.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinalScoreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FinalScore"-------
for thisComponent in FinalScoreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "FinalScore" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
























# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
