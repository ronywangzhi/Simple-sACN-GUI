import wx 
import sacn
import time
from datetime import datetime
import threading


#import the newly created GUI file 
import gui

class sacnBrightness(gui.MyFrame1): 

    def __init__(self,parent): 
        gui.MyFrame1.__init__(self,parent)
    
    def PlatformChange(self, event):
        #judge procesing platform
        while not self.m_radioBox1.GetSelection():
            #Brompton selected
            self.m_textCtrlChannel.SetValue("4")
            break
        else:
            #MVR selcted
            self.m_textCtrlChannel.SetValue("3")

        
    
    def DMXsent(self,IP,universe,Brightness):

        #universe = self.m_spinCtrlUniverse.GetValue()
        #startaddress = self.m_spinCtrlStartAddress.GetValue()
        #channel = self.m_textCtrlChannel.GetValue()
        #IP = self.m_textCtrlIP.GetValue()

        #judge procesing platform
        while not self.m_radioBox1.GetSelection():
            #Brompton selected
            
            sender = sacn.sACNsender()
            sender.start()
            sender.activate_output(universe)
            sender[universe].destination = IP
            sender[universe].dmx_data = (255, 255, 255, Brightness)
            #time.sleep(5)
            sender.stop()

            break
        else:
            #MVR selcted
            sender = sacn.sACNsender()
            sender.start()
            sender.activate_output(universe)
            sender[universe].destination = IP
            sender[universe].dmx_data = (0, 0, Brightness)
            #time.sleep(5)
            sender.stop()
            

        print(sender[universe].destination)
        print(Brightness)


    def Timer(self,event):
        #now = wx.Now()
        #self.m_statusBar1.SetStatusText("\t\t" + now)
        now = wx.DateTime.Now()
        self.m_statusBar1.SetStatusText("\t\t" + str(now))
        
        #time check
        NowTime = (datetime.now().hour,datetime.now().minute,datetime.now().second)

        IP = self.m_textCtrlIP.GetValue()
        universe = self.m_spinCtrlUniverse.GetValue()
        #startaddress = self.m_spinCtrlStartAddress.GetValue()
        #channel = self.m_textCtrlChannel.GetValue()
        
        #max brightness
        Brightness = "255"
 
        #get slided value and display it.
        #Brightness = self.m_slider1.GetValue()
        #self.m_textCtrlSlider.SetValue(str(Brightness))
        
        #self.DMXsent(IP,universe,Brightness)


        #judge brightness control method
        if not self.m_radioBox2.GetSelection():
            self.m_textCtrlSlider.SetValue("")
            #Time-based selected. time-base brightness
            if self.m_toggleBtn1.GetValue():
                self.m_textCtrlOnOff.SetValue("ON")

                while self.m_timePicker1.GetTime() == NowTime and self.m_checkBox1.GetValue:
                    self.m_textCtrlBrightness.SetValue(str(NowTime)+" "+str(self.m_spinCtrl1.GetValue()))
                    Brightness = str(self.m_spinCtrl1.GetValue())
                    self.DMXsent(IP,universe,int(Brightness))
                    break

                while self.m_timePicker2.GetTime() == NowTime and self.m_checkBox2.GetValue:
                    self.m_textCtrlBrightness.SetValue(str(NowTime)+" "+str(self.m_spinCtrl2.GetValue()))
                    Brightness = str(self.m_spinCtrl2.GetValue())
                    self.DMXsent(IP,universe,int(Brightness))
                    break

                while self.m_timePicker3.GetTime() == NowTime and self.m_checkBox3.GetValue:
                    self.m_textCtrlBrightness.SetValue(str(NowTime)+" "+str(self.m_spinCtrl3.GetValue()))
                    Brightness = str(self.m_spinCtrl3.GetValue())
                    self.DMXsent(IP,universe,int(Brightness))
                    break

                while self.m_timePicker4.GetTime() == NowTime and self.m_checkBox4.GetValue:
                    self.m_textCtrlBrightness.SetValue(str(NowTime)+" "+str(self.m_spinCtrl4.GetValue()))
                    Brightness = str(self.m_spinCtrl4.GetValue())
                    self.DMXsent(IP,universe,int(Brightness))
                    break

                while self.m_timePicker5.GetTime() == NowTime and self.m_checkBox5.GetValue:
                    self.m_textCtrlBrightness.SetValue(str(NowTime)+" "+str(self.m_spinCtrl5.GetValue()))
                    Brightness = str(self.m_spinCtrl5.GetValue())
                    self.DMXsent(IP,universe,int(Brightness))
                    break

            else:
                self.m_textCtrlOnOff.SetValue("OFF")
                self.m_textCtrlBrightness.SetValue("")
                

        else:
            #brightness slider selected
            Brightness = self.m_slider1.GetValue()
            self.m_textCtrlSlider.SetValue(str(Brightness))
            self.DMXsent(IP,universe,Brightness)


app = wx.App(False) 
frame = sacnBrightness(None) 
frame.Show(True) 

#start the applications 
app.MainLoop() 


"""
import sacn
import time

sender = sacn.sACNsender()  # provide an IP-Address to bind to if you are using Windows and want to use multicast
# sender.source_name = "rony_test"
sender.start()  # start the sending thread
sender.activate_output(1)  # start sending out data in the 1st universe
# sender[1].multicast = True  # set multicast to True
# sender[1].destination = "20.0.0.130"  # or provide unicast information.
# Keep in mind that if multicast is on, unicast is not used

sender[1].dmx_data = (255, 255, 255, 255)  # some test DMX data
time.sleep(10)  # send the data for 10 seconds
sender.stop()  # do not forget to stop the sender
"""