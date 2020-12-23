# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Time-Based Brightness Control via sACN for Brompton & MVR", pos = wx.DefaultPosition, size = wx.Size( 562,685 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Enter the IP of the processor.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrlIP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrlIP, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		m_radioBox1Choices = [ u"Brompton", u"MVR" ]
		self.m_radioBox1 = wx.RadioBox( self.m_panel1, wx.ID_ANY, u"Processing Platform", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer2.Add( self.m_radioBox1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"For Brompton, Set Live Control to [sACN] and Control Profile to [Colour].", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"For MVR, Enable sACN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer2.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Info" ), wx.VERTICAL )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Universe", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_spinCtrlUniverse = wx.SpinCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 1, 5, 1 )
		gSizer1.Add( self.m_spinCtrlUniverse, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Start Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_spinCtrlStartAddress = wx.SpinCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 1, 5, 1 )
		gSizer1.Add( self.m_spinCtrlStartAddress, 0, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Channel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		gSizer1.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_spinCtrlChannel = wx.SpinCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 5, 4 )
		gSizer1.Add( self.m_spinCtrlChannel, 0, wx.ALL, 5 )


		sbSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Brompton" ), wx.VERTICAL )

		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText5 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Channel 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gSizer8.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Red Gain: 0~100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Channel 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Green Gain: 0~100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer8.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Channel 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gSizer8.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Blue Gain: 0~100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer8.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Channel 4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer8.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Intensity Gain: 0~100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer8.Add( self.m_staticText12, 0, wx.ALL, 5 )


		sbSizer11.Add( gSizer8, 1, wx.EXPAND, 5 )


		sbSizer1.Add( sbSizer11, 0, wx.EXPAND, 5 )

		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MVR" ), wx.VERTICAL )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText51 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Channel 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		gSizer11.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_staticText61 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Blackout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		gSizer11.Add( self.m_staticText61, 0, wx.ALL, 5 )

		self.m_staticText71 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Channel 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		gSizer11.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Freeze", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		gSizer11.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.m_staticText91 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Channel 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		gSizer11.Add( self.m_staticText91, 0, wx.ALL, 5 )

		self.m_staticText101 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Brightness", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		gSizer11.Add( self.m_staticText101, 0, wx.ALL, 5 )

		self.m_staticText111 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Channel 4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		gSizer11.Add( self.m_staticText111, 0, wx.ALL, 5 )

		self.m_staticText121 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Gamma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		gSizer11.Add( self.m_staticText121, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Channel 5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		gSizer11.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Enable Test Pattern", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		gSizer11.Add( self.m_staticText36, 0, wx.ALL, 5 )


		sbSizer12.Add( gSizer11, 1, wx.EXPAND, 5 )


		sbSizer1.Add( sbSizer12, 0, wx.EXPAND, 5 )


		gSizer7.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Brightness Control" ), wx.VERTICAL )

		self.m_staticText37 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Set Time and Brightness", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		sbSizer2.Add( self.m_staticText37, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_textCtrlOnOff = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer9.Add( self.m_textCtrlOnOff, 0, wx.ALL, 5 )

		self.m_textCtrlBrightness = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer9.Add( self.m_textCtrlBrightness, 0, wx.ALL, 5 )


		sbSizer2.Add( gSizer9, 0, wx.EXPAND, 5 )

		self.m_toggleBtn1 = wx.ToggleButton( sbSizer2.GetStaticBox(), wx.ID_ANY, u"On/Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_toggleBtn1, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox1 = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer2.Add( self.m_checkBox1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_timePicker1 = wx.adv.TimePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.TP_DEFAULT  )
		fgSizer2.Add( self.m_timePicker1, 0, wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 255, 0 )
		fgSizer2.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer2.Add( self.m_checkBox2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_timePicker2 = wx.adv.TimePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.TP_DEFAULT  )
		fgSizer2.Add( self.m_timePicker2, 0, wx.ALL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 255, 0 )
		fgSizer2.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer2.Add( self.m_checkBox3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_timePicker3 = wx.adv.TimePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.TP_DEFAULT  )
		fgSizer2.Add( self.m_timePicker3, 0, wx.ALL, 5 )

		self.m_spinCtrl3 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 255, 0 )
		fgSizer2.Add( self.m_spinCtrl3, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer2.Add( self.m_checkBox4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_timePicker4 = wx.adv.TimePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.TP_DEFAULT  )
		fgSizer2.Add( self.m_timePicker4, 0, wx.ALL, 5 )

		self.m_spinCtrl4 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 255, 0 )
		fgSizer2.Add( self.m_spinCtrl4, 0, wx.ALL, 5 )

		self.m_checkBox5 = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer2.Add( self.m_checkBox5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_timePicker5 = wx.adv.TimePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.TP_DEFAULT  )
		fgSizer2.Add( self.m_timePicker5, 0, wx.ALL, 5 )

		self.m_spinCtrl5 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 255, 0 )
		fgSizer2.Add( self.m_spinCtrl5, 0, wx.ALL, 5 )


		sbSizer2.Add( fgSizer2, 0, wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer2.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Brightness Slider (Pending)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		sbSizer2.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.m_slider1 = wx.Slider( sbSizer2.GetStaticBox(), wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		sbSizer2.Add( self.m_slider1, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer7.Add( sbSizer2, 1, wx.EXPAND, 5 )


		bSizer2.Add( gSizer7, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Brightness Control", True )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText40 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Rony Wang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		bSizer9.Add( self.m_staticText40, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer9 )
		self.m_panel3.Layout()
		bSizer9.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"Author", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_timer1.Start( 1000 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_TIMER, self.Timer, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Timer( self, event ):
		event.Skip()


