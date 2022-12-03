"""
Add default sd to be passed to UI object (pass by reference)
Create as executable
"""
import SensorData as SD
import UserInterface as UI

if __name__ == '__main__':
    sd = SD.sensorData('DummyData.csv', 'MetaData.csv')
    sd.compileSensor()
    gd = sd.compileGraphData()

    ui = UI.UserInterface(sd,gd)
    ui.mainloop()