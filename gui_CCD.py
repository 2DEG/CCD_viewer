import wx  # type: ignore

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas  # type: ignore
from matplotlib.figure import Figure  # type: ignore


from typing import Tuple, Optional, List, Union

from configparser import ConfigParser

from utils import *
from conv_im import *

import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import os


class MyApp(wx.App):
    """Main application class."""

    def __init__(self):
        super().__init__(clearSigInt=True)

        self.mainFrame = MainFrame(None)
        self.mainFrame.Show()

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1139,724 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel61 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel65 = wx.Panel( self.m_panel61, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel70 = wx.Panel( self.m_panel65, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22.Add( self.m_panel70, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel73 = wx.Panel( self.m_panel65, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22.Add( self.m_panel73, 9, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.m_panel65, wx.ID_ANY, u"Pixels:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer22.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.coord_txt = wx.StaticText( self.m_panel65, wx.ID_ANY, u"X: 500 Y: 500", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.coord_txt.Wrap( -1 )

		bSizer22.Add( self.coord_txt, 0, wx.ALL, 5 )


		self.m_panel65.SetSizer( bSizer22 )
		self.m_panel65.Layout()
		bSizer22.Fit( self.m_panel65 )
		bSizer20.Add( self.m_panel65, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel66 = wx.Panel( self.m_panel61, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel67 = wx.Panel( self.m_panel66, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21.Add( self.m_panel67, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel68 = wx.Panel( self.m_panel66, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21.Add( self.m_panel68, 9, wx.EXPAND |wx.ALL, 5 )

		self.m_panel69 = wx.Panel( self.m_panel66, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel71 = wx.Panel( self.m_panel69, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23.Add( self.m_panel71, 1, wx.EXPAND |wx.ALL, 5 )

		self.sngl_shot_btn = wx.Button( self.m_panel69, wx.ID_ANY, u"Single Shot", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.sngl_shot_btn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.cont_shot_btn = wx.Button( self.m_panel69, wx.ID_ANY, u"Continuous Shooting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.cont_shot_btn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		self.m_panel69.SetSizer( bSizer23 )
		self.m_panel69.Layout()
		bSizer23.Fit( self.m_panel69 )
		bSizer21.Add( self.m_panel69, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel66.SetSizer( bSizer21 )
		self.m_panel66.Layout()
		bSizer21.Fit( self.m_panel66 )
		bSizer20.Add( self.m_panel66, 9, wx.EXPAND |wx.ALL, 5 )


		self.m_panel61.SetSizer( bSizer20 )
		self.m_panel61.Layout()
		bSizer20.Fit( self.m_panel61 )
		bSizer19.Add( self.m_panel61, 3, wx.EXPAND |wx.ALL, 5 )

		self.m_panel79 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook4 = wx.Notebook( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.settings_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel74 = wx.Panel( self.settings_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self.m_panel74, wx.ID_ANY, u"Exposition Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer28.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.exp_time_txtctrl = wx.TextCtrl( self.m_panel74, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.exp_time_txtctrl, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel74, wx.ID_ANY, u"Frames Count", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer28.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.frames_txtctrl = wx.TextCtrl( self.m_panel74, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.frames_txtctrl, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.m_panel74, wx.ID_ANY, u"Target Temperature", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer28.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.temp_targ_txtctrl = wx.TextCtrl( self.m_panel74, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.temp_targ_txtctrl, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self.m_panel74, wx.ID_ANY, u"Open Shutter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer28.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_checkBox1 = wx.CheckBox( self.m_panel74, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_checkBox1, 0, wx.ALL, 5 )


		self.m_panel74.SetSizer( bSizer28 )
		self.m_panel74.Layout()
		bSizer28.Fit( self.m_panel74 )
		bSizer24.Add( self.m_panel74, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel75 = wx.Panel( self.settings_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel76 = wx.Panel( self.m_panel75, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer29.Add( self.m_panel76, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self.m_panel75, wx.ID_ANY, u"Save to:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer29.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.save_to_dir_picker = wx.DirPickerCtrl( self.m_panel75, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer29.Add( self.save_to_dir_picker, 0, wx.ALL, 5 )

		self.save_dat_rad = wx.RadioButton( self.m_panel75, wx.ID_ANY, u"Save Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.save_dat_rad, 0, wx.ALL, 5 )


		self.m_panel75.SetSizer( bSizer29 )
		self.m_panel75.Layout()
		bSizer29.Fit( self.m_panel75 )
		bSizer24.Add( self.m_panel75, 1, wx.EXPAND |wx.ALL, 5 )


		self.settings_panel.SetSizer( bSizer24 )
		self.settings_panel.Layout()
		bSizer24.Fit( self.settings_panel )
		self.m_notebook4.AddPage( self.settings_panel, u"Settings", True )
		self.bwg_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel82 = wx.Panel( self.bwg_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( self.m_panel82, wx.ID_ANY, u"Black", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer33.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.slider_blk = wx.Slider( self.m_panel82, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer33.Add( self.slider_blk, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText15 = wx.StaticText( self.m_panel82, wx.ID_ANY, u"White", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer33.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.slider_wht = wx.Slider( self.m_panel82, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer33.Add( self.slider_wht, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText16 = wx.StaticText( self.m_panel82, wx.ID_ANY, u"Gamma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer33.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.slider_g = wx.Slider( self.m_panel82, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer33.Add( self.slider_g, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel82.SetSizer( bSizer33 )
		self.m_panel82.Layout()
		bSizer33.Fit( self.m_panel82 )
		bSizer31.Add( self.m_panel82, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel83 = wx.Panel( self.bwg_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31.Add( self.m_panel83, 1, wx.EXPAND |wx.ALL, 5 )


		self.bwg_panel.SetSizer( bSizer31 )
		self.bwg_panel.Layout()
		bSizer31.Fit( self.bwg_panel )
		self.m_notebook4.AddPage( self.bwg_panel, u"BWG", False )

		bSizer30.Add( self.m_notebook4, 9, wx.EXPAND |wx.ALL, 5 )

		self.m_panel80 = wx.Panel( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer30.Add( self.m_panel80, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel79.SetSizer( bSizer30 )
		self.m_panel79.Layout()
		bSizer30.Fit( self.m_panel79 )
		bSizer19.Add( self.m_panel79, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer19 )
		self.Layout()
		self.status_bar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.menu_bar = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.menu_open = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_open )

		self.menu_save = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_save )

		self.menu_save_as = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Save As", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_save_as )

		self.menu_bar.Append( self.menu_file, u"File" )

		self.m_menu2 = wx.Menu()
		self.menu_bar.Append( self.m_menu2, u"Help" )

		self.SetMenuBar( self.menu_bar )


		self.Centre( wx.BOTH )

		# Connect Events
		self.sngl_shot_btn.Bind( wx.EVT_BUTTON, self.sngl_shut )
		self.cont_shot_btn.Bind( wx.EVT_BUTTON, self.cont_shot )
		self.exp_time_txtctrl.Bind( wx.EVT_TEXT_ENTER, self.set_exp_time )
		self.frames_txtctrl.Bind( wx.EVT_TEXT_ENTER, self.set_frames_num )
		self.temp_targ_txtctrl.Bind( wx.EVT_TEXT_ENTER, self.set_temperature )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.open_shutter )
		self.save_to_dir_picker.Bind( wx.EVT_DIRPICKER_CHANGED, self.pick_dir )
		self.save_dat_rad.Bind( wx.EVT_RADIOBUTTON, self.save_dat )
		self.slider_blk.Bind( wx.EVT_SCROLL, self.chng_blk )
		self.slider_wht.Bind( wx.EVT_SCROLL, self.chng_wht )
		self.slider_g.Bind( wx.EVT_SCROLL, self.chng_g )
		self.Bind( wx.EVT_MENU, self.open_file, id = self.menu_open.GetId() )
		self.Bind( wx.EVT_MENU, self.save_file, id = self.menu_save.GetId() )
		self.Bind( wx.EVT_MENU, self.save_as_file, id = self.menu_save_as.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def sngl_shut( self, event ):
		event.Skip()

	def cont_shot( self, event ):
		event.Skip()

	def set_exp_time( self, event ):
		event.Skip()

	def set_frames_num( self, event ):
		event.Skip()

	def set_temperature( self, event ):
		event.Skip()

	def open_shutter( self, event ):
		event.Skip()

	def pick_dir( self, event ):
		event.Skip()

	def save_dat( self, event ):
		event.Skip()

	def chng_blk( self, event ):
		event.Skip()

	def chng_wht( self, event ):
		event.Skip()

	def chng_g( self, event ):
		event.Skip()

	def open_file( self, event ):
		event.Skip()

	def save_file( self, event ):
		event.Skip()

	def save_as_file( self, event ):
		event.Skip()


