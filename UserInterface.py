from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import SensorData as SD
from click import command
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sys
sys.setrecursionlimit(10**5)


matplotlib.use('TKAgg')


class UserInterface(tk.Tk):

    def __init__(self, sd, gd):
        self.root = Tk()
        self.root.geometry('1920x1080')
        self.root.title('Sensor Data')
        self.sd = sd
        self.gd = gd
        self.gdTemp = gd
        self.timeShift = False

        window_frame = Frame(self.root)
        window_frame.pack(expand=True, fill=BOTH)

        tempFrame = Frame(window_frame, width=100, height=200)

        label1 = Label(tempFrame, text="Temperature")
        label1.pack()

        tempFrame.grid(row=0, column=0, padx=10, pady=5)

        figure1 = plt.figure(figsize=(3, 2), dpi=100)

        tempFigure_canvas = FigureCanvasTkAgg(figure1, tempFrame)

        toolbar = NavigationToolbar2Tk(tempFigure_canvas, tempFrame)
        toolbar.update()
        tempFigure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        temp_summarize = Button(
            tempFrame, text='Summarize', command=self.temp_summarize)
        temp_summarize.pack(side=RIGHT)
        self.axTemp = figure1.add_subplot()
        self.gd.dfTemp.plot(x='DateTime', y='Temp', ax=self.axTemp)

        acc_magFrame = Frame(window_frame, width=100, height=200)

        label1 = Label(acc_magFrame, text="Acc Magnitude Average")
        label1.pack()

        acc_magFrame.grid(row=1, column=0, padx=10, pady=5)

        figure2 = plt.figure(figsize=(3, 2), dpi=100)

        acc_magFrame_canvas = FigureCanvasTkAgg(figure2, acc_magFrame)
        toolbar = NavigationToolbar2Tk(acc_magFrame_canvas, acc_magFrame)
        toolbar.update()
        acc_magFrame_canvas.get_tk_widget().pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)
        acc_summarize = Button(
            acc_magFrame, text='Summarize', command=self.acc_mag_summarize)
        acc_summarize.pack(side=RIGHT)
        self.axACC = figure2.add_subplot()
        self.gd.dfAcc.plot(x='DateTime', y='ACC Magnitude', ax=self.axACC)

        on_wrist_Frame = Frame(window_frame, width=100, height=200)

        label1 = Label(on_wrist_Frame, text="On Wrist")
        label1.pack()

        on_wrist_Frame.grid(row=2, column=0, padx=10, pady=5)

        figure3 = plt.figure(figsize=(3, 2), dpi=100)

        on_wrist_Frame_canvas = FigureCanvasTkAgg(figure3, on_wrist_Frame)
        toolbar = NavigationToolbar2Tk(on_wrist_Frame_canvas, on_wrist_Frame)
        toolbar.update()
        on_wrist_Frame_canvas.get_tk_widget().pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)
        on_wrist_summarize = Button(
            on_wrist_Frame, text='Summarize', command=self.on_wrist_summarize)
        on_wrist_summarize.pack(side=RIGHT)
        self.axOnWrist = figure3.add_subplot()
        self.gd.dfOnWrist.plot(x='DateTime', y='On Wrist', ax=self.axOnWrist)

        step_count_Frame = Frame(window_frame, width=100, height=200)

        label1 = Label(step_count_Frame, text="Step Count")
        label1.pack()

        step_count_Frame.grid(row=0, column=2, padx=10, pady=5)

        figure4 = plt.figure(figsize=(3, 2), dpi=100)

        step_count_Frame_canvas = FigureCanvasTkAgg(figure4, step_count_Frame)
        toolbar = NavigationToolbar2Tk(
            step_count_Frame_canvas, step_count_Frame)
        toolbar.update()
        step_count_Frame_canvas.get_tk_widget().pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)
        step_count_summarize = Button(
            step_count_Frame, text='Summarize', command=self.step_count_summarize)
        step_count_summarize.pack(side=RIGHT)
        self.axStepCt = figure4.add_subplot()
        self.gd.dfStepCt.plot(x='DateTime', y='Step Count', ax=self.axStepCt)

        rest_Frame = Frame(window_frame, width=100, height=200)

        label1 = Label(rest_Frame, text="Rest")
        label1.pack()

        rest_Frame.grid(row=0, column=1, padx=10, pady=5)

        figure5 = plt.figure(figsize=(3, 2), dpi=100)

        rest_Frame_canvas = FigureCanvasTkAgg(figure5, rest_Frame)
        toolbar = NavigationToolbar2Tk(rest_Frame_canvas, rest_Frame)
        toolbar.update()
        rest_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        rest_summarize = Button(
            rest_Frame, text='Summarize', command=self.rest_summarize)
        rest_summarize.pack(side=RIGHT)
        self.axRest = figure5.add_subplot()
        self.gd.dfRest.plot(x='DateTime', y='Rest', ax=self.axRest)

        EDA_Frame = Frame(window_frame, width=100, height=200)

        label1 = Label(EDA_Frame, text="EDA Average")
        label1.pack()

        EDA_Frame.grid(row=1, column=1, padx=10, pady=5)

        figure6 = plt.figure(figsize=(3, 2), dpi=100)

        EDA_Frame_canvas = FigureCanvasTkAgg(figure6, EDA_Frame)
        toolbar = NavigationToolbar2Tk(EDA_Frame_canvas, EDA_Frame)
        toolbar.update()
        EDA_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        EDA_summarize = Button(EDA_Frame, text='Summarize',
                               command=self.EDA_summarize)
        EDA_summarize.pack(side=RIGHT)
        self.axEDA = figure6.add_subplot()
        self.gd.dfEDA.plot(x='DateTime', y='EDA', ax=self.axEDA)

        Movement_Frame = Frame(window_frame, width=100, height=200)
        label1 = Label(Movement_Frame, text="Movement Intensity")
        label1.pack()
        Movement_Frame.grid(row=2, column=1, padx=10, pady=5)

        figure7 = plt.figure(figsize=(3, 2), dpi=100)

        Movement_Frame_canvas = FigureCanvasTkAgg(figure7, Movement_Frame)
        toolbar = NavigationToolbar2Tk(Movement_Frame_canvas, Movement_Frame)
        toolbar.update()
        Movement_Frame_canvas.get_tk_widget().pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)
        Movement_summarize = Button(
            Movement_Frame, text='Summarize', command=self.Movement_summarize)
        Movement_summarize.pack(side=RIGHT)
        self.axMovInten = figure7.add_subplot()
        self.gd.dfMovInten.plot(x='DateTime', y='Movement Intensity', ax=self.axMovInten)

        QueryFrame = Frame(window_frame, width=100, height=200)

        label1 = Label(QueryFrame, text="Query:")
        label1.pack()
        QueryFrame.grid(row=1, column=2, padx=10, pady=5)

        self.inputtxt1 = tk.Text(QueryFrame,
                                 height=2,
                                 width=20)
        self.inputtxt1.pack()
        self.inputtxt2 = tk.Text(QueryFrame,
                                 height=2,
                                 width=20)
        self.inputtxt2.pack()
        self.inputtxt3 = tk.Text(QueryFrame,
                                 height=2,
                                 width=20)
        self.inputtxt3.pack()
        self.inputtxt4 = tk.Text(QueryFrame,
                                 height=2,
                                 width=20)
        self.inputtxt4.pack()

        aggregate = Button(QueryFrame, text='Aggregate',
                           command=self.aggregateData)
        aggregate.pack(side=TOP)

        Compile_Frame = Frame(window_frame, width=100, height=200)
        Compile_Frame.grid(row=2, column=2, padx=10, pady=5)

        label1 = Label(Compile_Frame, text="Menu:", padx=10, pady=5)
        label1.pack()

        Browse = Button(Compile_Frame, text="Browse", padx=20, pady=10)
        Browse.pack(padx=10, pady=10)

        Compile = Button(Compile_Frame, text="Compile", padx=10, pady=10)
        Compile.pack(side=TOP)

        def close():
            self.quit()

        Quit = Button(Compile_Frame, text="Quit",
                      padx=10, pady=10, command=close)

        Quit.pack(side=BOTTOM, padx=10, pady=10)

        plt.show()

    def addNewData(self, summaryFile, metaDataFile):
        # add window for compiling new data with two fields
        # fields open a browse window for file explorer to specify files
        # compile button calls method
        self.sd = SD.sensorData(summaryFile, metaDataFile)
        self.sd.compileSensor()
        self.sd.compileMeta()
        self.gd = self.sd.compileGraphData()
        # self.callback()

    def switchTimeSeries(self):
        if self.timeShift == True:
            self.gdTemp = self.gd
            self.gd.compileGraph()
            self.timeShift = False
        else:
            self.gdTemp = self.gd
            self.gd.compileGraphTS()
            self.timeShift = True

    def aggregateData(self):
        DateS = self.inputtxt1.get('1.0','end-1c')
        DateE = self.inputtxt2.get('1.0','end-1c')
        TimeS = self.inputtxt3.get('1.0','end-1c')
        TimeE = self.inputtxt4.get('1.0','end-1c')
        print(DateS, DateE, TimeS, TimeE)
        returnData = self.sd.aggregate(DateS, DateE, TimeS, TimeE, self.timeShift)

        self.callback()

        self.gd.dfTemp.plot(x='DateTime', y='Temp', ax=self.axTemp)
        returnData.plot(x='DateTime', y='TempAvrg', ax=self.axTemp)

        self.gd.dfAcc.plot(x='DateTime', y='ACC Magnitude', ax=self.axACC)
        returnData.plot(x='DateTime', y='ACCAvrg', ax=self.axACC)

        self.gd.dfEDA.plot(x='DateTime', y='EDA', ax=self.axEDA)
        returnData.plot(x='DateTime', y='EDAAvrg', ax=self.axOnWrist)

        self.gd.dfOnWrist.plot(x='DateTime', y='On Wrist', ax=self.axOnWrist)
        returnData.plot(x='DateTime', y='OnWristAvrg', ax=self.axStepCt)

        self.gd.dfMovInten.plot(x='DateTime', y='Movement Intensity', ax=self.axMovInten)
        returnData.plot(x='DateTime', y='MoveIntenAvrg', ax=self.axRest)

        self.gd.dfStepCt.plot(x='DateTime', y='Step Count', ax=self.axStepCt)
        returnData.plot(x='DateTime', y='StepCtAvrg', ax=self.axEDA)

        self.gd.dfRest.plot(x='DateTime', y='Rest', ax=self.axRest)
        returnData.plot(x='DateTime', y='RestAvrg', ax=self.axMovInten)
        plt.show()

    def queryData(self):
        # add window to query based on timeframe
        # window needs start date, end date, start time, and end time
        # add start button on window
        DateS = self.inputtxt1.get('1.0','end-1c')
        DateE = self.inputtxt2.get('1.0','end-1c')
        TimeS = self.inputtxt3.get('1.0','end-1c')
        TimeE = self.inputtxt4.get('1.0','end-1c')
        self.gd = self.sd.queryGraph(DateS, DateE, TimeS, TimeE)
        # self.callback()

    def switchGraphData(self):
        # switches between query graphs and full graphs
        gdq = self.gd
        self.gd = self.gdTemp
        self.gdTemp = gdq
        # self.callback()

    def temp_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('Temp')
        # somehow plot the return data over graphs

        # self.callback()
    def acc_mag_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('ACCMagnitude')
        # somehow plot the return data over graphs
        # self.callback()

    def on_wrist_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('OnWrist')
        # somehow plot the return data over graphs
        # self.callback()

    def step_count_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('StepCount')
        # somehow plot the return data over graphs
        # self.callback()

    def rest_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('Rest')
        # somehow plot the return data over graphs
        # self.callback()

    def EDA_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('EDA')
        # somehow plot the return data over graphs
        # self.callback()

    def Movement_summarize(self):
        #returnData = [sum, highest, lowest]
        returnData = self.sd.summarize('MovInten')
        # somehow plot the return data over graphs
        # self.callback()

    def callback(self):
        self.axTemp.cla()
        self.axACC.cla()
        self.axOnWrist.cla()
        self.axStepCt.cla()
        self.axRest.cla()
        self.axEDA.cla()
        self.axMovInten.cla()

def browseFiles():
    # Add this to main project
    filename = filedialog.askopenfilename(
        initialdir="/", title='Choose a file', filetypes=[('CSV Files', '.*csv')])
    file = open(filename, "r")
    # Also add this
    if file:
        DummyData = file.read()
        file.close()




