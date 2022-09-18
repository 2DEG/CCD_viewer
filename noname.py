# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-88b0f50)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 864,692 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.menu_open = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_open )

		self.menu_close = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Close", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_close )

		self.menu_save_as = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Save As", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_save_as )

		self.m_menubar2.Append( self.menu_file, u"File" )

		self.menu_help = wx.Menu()
		self.m_menubar2.Append( self.menu_help, u"Help" )

		self.SetMenuBar( self.m_menubar2 )

		self.status_bar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel314 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		File = wx.FlexGridSizer( 2, 2, 0, 0 )
		File.AddGrowableCol( 0, 1 )
		File.AddGrowableCol( 1, 6 )
		File.AddGrowableRow( 0, 1 )
		File.AddGrowableRow( 1, 6 )
		File.SetFlexibleDirection( wx.BOTH )
		File.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.btns_panel = wx.Panel( self.m_panel314, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		btns_sizer = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_start = wx.BitmapButton( self.btns_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn_start.SetBitmap( wx.Bitmap( u"png/002-play.png", wx.BITMAP_TYPE_ANY ) )
		btns_sizer.Add( self.btn_start, 0, wx.EXPAND, 5 )

		self.btn_stop = wx.BitmapButton( self.btns_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn_stop.SetBitmap( wx.Bitmap( u"png/001-stop.png", wx.BITMAP_TYPE_ANY ) )
		btns_sizer.Add( self.btn_stop, 0, wx.EXPAND, 5 )

		self.btn_pause = wx.BitmapButton( self.btns_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn_pause.SetBitmap( wx.Bitmap( u"png/003-pause.png", wx.BITMAP_TYPE_ANY ) )
		btns_sizer.Add( self.btn_pause, 0, wx.EXPAND, 5 )

		self.btn_contin = wx.BitmapButton( self.btns_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn_contin.SetBitmap( wx.Bitmap( u"png/004-shooting.png", wx.BITMAP_TYPE_ANY ) )
		btns_sizer.Add( self.btn_contin, 0, wx.EXPAND, 5 )


		self.btns_panel.SetSizer( btns_sizer )
		self.btns_panel.Layout()
		btns_sizer.Fit( self.btns_panel )
		File.Add( self.btns_panel, 1, wx.EXPAND, 5 )

		self.hslice_panel = wx.Panel( self.m_panel314, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		hslice_sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self.hslice_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		hslice_sizer.Add( self.m_button5, 1, wx.EXPAND, 5 )


		self.hslice_panel.SetSizer( hslice_sizer )
		self.hslice_panel.Layout()
		hslice_sizer.Fit( self.hslice_panel )
		File.Add( self.hslice_panel, 1, wx.EXPAND, 5 )

		self.vslice_panel = wx.Panel( self.m_panel314, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		vslice_sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_button4 = wx.Button( self.vslice_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		vslice_sizer.Add( self.m_button4, 1, wx.EXPAND, 5 )


		self.vslice_panel.SetSizer( vslice_sizer )
		self.vslice_panel.Layout()
		vslice_sizer.Fit( self.vslice_panel )
		File.Add( self.vslice_panel, 1, wx.EXPAND, 5 )

		self.image_panel = wx.Panel( self.m_panel314, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		image_sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self.image_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		image_sizer.Add( self.m_bitmap1, 1, wx.ALL|wx.EXPAND, 5 )


		self.image_panel.SetSizer( image_sizer )
		self.image_panel.Layout()
		image_sizer.Fit( self.image_panel )
		File.Add( self.image_panel, 1, wx.EXPAND, 5 )


		self.m_panel314.SetSizer( File )
		self.m_panel314.Layout()
		File.Fit( self.m_panel314 )
		bSizer16.Add( self.m_panel314, 4, wx.EXPAND, 5 )

		self.m_panel315 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.notebook = wx.Notebook( self.m_panel315, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.settings_panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel323 = wx.Panel( self.settings_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.static_exp_time = wx.StaticText( self.m_panel323, wx.ID_ANY, u"Exposition Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.static_exp_time.Wrap( -1 )

		bSizer21.Add( self.static_exp_time, 0, wx.ALL, 5 )

		self.text_exp_time = wx.TextCtrl( self.m_panel323, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer21.Add( self.text_exp_time, 0, wx.ALL, 5 )

		self.static_frames = wx.StaticText( self.m_panel323, wx.ID_ANY, u"Frames Count:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.static_frames.Wrap( -1 )

		bSizer21.Add( self.static_frames, 0, wx.ALL, 5 )

		self.text_frames = wx.TextCtrl( self.m_panel323, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer21.Add( self.text_frames, 0, wx.ALL, 5 )

		self.static_targ_temp = wx.StaticText( self.m_panel323, wx.ID_ANY, u"Target Temp.:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.static_targ_temp.Wrap( -1 )

		bSizer21.Add( self.static_targ_temp, 0, wx.ALL, 5 )

		self.text_targ_temp = wx.TextCtrl( self.m_panel323, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer21.Add( self.text_targ_temp, 0, wx.ALL, 5 )

		self.chk_shutter = wx.CheckBox( self.m_panel323, wx.ID_ANY, u"Open Shutter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.chk_shutter, 0, wx.ALL, 5 )


		self.m_panel323.SetSizer( bSizer21 )
		self.m_panel323.Layout()
		bSizer21.Fit( self.m_panel323 )
		bSizer20.Add( self.m_panel323, 1, wx.EXPAND, 5 )

		self.m_panel322 = wx.Panel( self.settings_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20.Add( self.m_panel322, 1, wx.EXPAND, 5 )

		self.static_save_to = wx.StaticText( self.settings_panel, wx.ID_ANY, u"Save to:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.static_save_to.Wrap( -1 )

		bSizer20.Add( self.static_save_to, 0, wx.ALL, 5 )

		self.pick_dir = wx.DirPickerCtrl( self.settings_panel, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer20.Add( self.pick_dir, 0, wx.ALL, 5 )

		self.rad_save_data = wx.RadioButton( self.settings_panel, wx.ID_ANY, u"Save Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.rad_save_data, 0, wx.ALL, 5 )


		self.settings_panel.SetSizer( bSizer20 )
		self.settings_panel.Layout()
		bSizer20.Fit( self.settings_panel )
		self.notebook.AddPage( self.settings_panel, u"Settings", True )
		self.bwg_panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.text_black = wx.StaticText( self.bwg_panel, wx.ID_ANY, u"Black", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_black.Wrap( -1 )

		bSizer22.Add( self.text_black, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.slider_black = wx.Slider( self.bwg_panel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer22.Add( self.slider_black, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_white = wx.StaticText( self.bwg_panel, wx.ID_ANY, u"White", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_white.Wrap( -1 )

		bSizer22.Add( self.text_white, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.slider_white = wx.Slider( self.bwg_panel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer22.Add( self.slider_white, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_gamma = wx.StaticText( self.bwg_panel, wx.ID_ANY, u"Gamma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_gamma.Wrap( -1 )

		bSizer22.Add( self.text_gamma, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.slider_gamma = wx.Slider( self.bwg_panel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer22.Add( self.slider_gamma, 0, wx.ALL|wx.EXPAND, 5 )


		self.bwg_panel.SetSizer( bSizer22 )
		self.bwg_panel.Layout()
		bSizer22.Fit( self.bwg_panel )
		self.notebook.AddPage( self.bwg_panel, u"BWG", False )

		bSizer19.Add( self.notebook, 1, wx.EXPAND, 5 )


		self.m_panel315.SetSizer( bSizer19 )
		self.m_panel315.Layout()
		bSizer19.Fit( self.m_panel315 )
		bSizer16.Add( self.m_panel315, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.on_open, id = self.menu_open.GetId() )
		self.Bind( wx.EVT_MENU, self.on_close, id = self.menu_close.GetId() )
		self.Bind( wx.EVT_MENU, self.on_save_as, id = self.menu_save_as.GetId() )
		self.btn_start.Bind( wx.EVT_BUTTON, self.on_start )
		self.btn_stop.Bind( wx.EVT_BUTTON, self.on_stop )
		self.btn_pause.Bind( wx.EVT_BUTTON, self.on_pause )
		self.btn_contin.Bind( wx.EVT_BUTTON, self.on_contin )
		self.text_exp_time.Bind( wx.EVT_TEXT_ENTER, self.on_exp_time )
		self.text_frames.Bind( wx.EVT_TEXT_ENTER, self.on_frames )
		self.text_targ_temp.Bind( wx.EVT_TEXT_ENTER, self.on_targ_temp )
		self.chk_shutter.Bind( wx.EVT_CHECKBOX, self.on_chk_shutter )
		self.pick_dir.Bind( wx.EVT_DIRPICKER_CHANGED, self.on_pick_dir )
		self.rad_save_data.Bind( wx.EVT_RADIOBUTTON, self.on_save_data )
		self.slider_black.Bind( wx.EVT_SCROLL, self.on_black )
		self.slider_white.Bind( wx.EVT_SCROLL, self.on_white )
		self.slider_gamma.Bind( wx.EVT_SCROLL, self.on_gamma )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_open( self, event ):
		event.Skip()

	def on_close( self, event ):
		event.Skip()

	def on_save_as( self, event ):
		event.Skip()

	def on_start( self, event ):
		event.Skip()

	def on_stop( self, event ):
		event.Skip()

	def on_pause( self, event ):
		event.Skip()

	def on_contin( self, event ):
		event.Skip()

	def on_exp_time( self, event ):
		event.Skip()

	def on_frames( self, event ):
		event.Skip()

	def on_targ_temp( self, event ):
		event.Skip()

	def on_chk_shutter( self, event ):
		event.Skip()

	def on_pick_dir( self, event ):
		event.Skip()

	def on_save_data( self, event ):
		event.Skip()

	def on_black( self, event ):
		event.Skip()

	def on_white( self, event ):
		event.Skip()

	def on_gamma( self, event ):
		event.Skip()


