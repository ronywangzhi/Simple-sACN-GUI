import wx 
import sacn
import time
from datetime import datetime

from wx.core import PAPER_FANFOLD_LGL_GERMAN

#import the newly created GUI file 
import gui

class sacnBrightness(gui.MyFrame1): 

    def __init__(self,parent): 
        gui.MyFrame1.__init__(self,parent)
    
    def DMXsent(self,universe,address,channel):
        address = 1
        channel = 4
        sender = sacn.sACNsender()  # provide an IP-Address to bind to if you are using Windows and want to use multicast
        # sender.source_name = "rony_test"
        sender.start()  # start the sending thread
        sender.activate_output(universe)  # start sending out data in the 1st universe
        sender[1].multicast = True  # set multicast to True
        # sender[1].destination = "20.0.0.130"  # or provide unicast information.
        sender[1].destination = self.m_textCtrlIP.GetValue() # or provide unicast information.
        # # Keep in mind that if multicast is on, unicast is not used
        sender[1].dmx_data = (50, 100, 200, 255)  # some test DMX data
        
        #time.sleep(10)  # send the data for 10 second.
        sender.stop()  # do not forget to stop the sender
        print(sender[1].destination)


    def Timer(self,event):
        #now = wx.Now()
        #self.m_statusBar1.SetStatusText("\t\t" + now)
        now = wx.DateTime.Now()
        self.m_statusBar1.SetStatusText("\t\t" + str(now))
        
        #time check
        NowTime = (datetime.now().hour,datetime.now().minute,datetime.now().second)
        
        self.DMXsent(self.m_spinCtrlUniverse.GetValue())

    #time-base brightness
        if self.m_toggleBtn1.GetValue():
            self.m_textCtrlOnOff.SetValue("ON")

            while self.m_timePicker1.GetTime() == NowTime and self.m_checkBox1.GetValue: 
                self.m_textCtrlBrightness.SetValue(str(NowTime)+" "+str(self.m_spinCtrl1.GetValue()))
                Brightness = str(self.m_spinCtrl1.GetValue())
               
                break
                
            while self.m_timePicker2.GetTime() == NowTime and self.m_checkBox2.GetValue: 
                self.m_textCtrlBrightness.SetValue(str(NowTime)+" "+str(self.m_spinCtrl2.GetValue()))
                Brightness = str(self.m_spinCtrl2.GetValue())
                
                break

            while self.m_timePicker3.GetTime() == NowTime and self.m_checkBox3.GetValue: 
                self.m_textCtrlBrightness.SetValue(str(NowTime)+" "+str(self.m_spinCtrl3.GetValue()))
                Brightness = str(self.m_spinCtrl3.GetValue())
                break

            while self.m_timePicker4.GetTime() == NowTime and self.m_checkBox4.GetValue: 
                self.m_textCtrlBrightness.SetValue(str(NowTime)+" "+str(self.m_spinCtrl4.GetValue()))
                Brightness = str(self.m_spinCtrl4.GetValue())
                
                break

            while self.m_timePicker5.GetTime() == NowTime and self.m_checkBox5.GetValue: 
                self.m_textCtrlBrightness.SetValue(str(NowTime)+" "+str(self.m_spinCtrl5.GetValue()))
                Brightness = str(self.m_spinCtrl5.GetValue())
                
                break   

        else:
            self.m_textCtrlOnOff.SetValue("OFF")
            self.m_textCtrlBrightness.SetValue("")


app = wx.App(False) 
frame = sacnBrightness(None) 
frame.Show(True) 
#start the applications 
app.MainLoop() 