import wx  # type: ignore
from picam import PICam
from picam.picam_types import PicamReadoutControlMode, PicamAdcQuality, PicamAdcAnalogGain, PicamTriggerDetermination
from picam.picam_types import PicamTriggerResponse
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas  # type: ignore
from matplotlib.widgets import Cursor
from matplotlib.transforms import Affine2D
from matplotlib.figure import Figure  # type: ignore



from typing import Tuple, Optional, List, Union

from configparser import ConfigParser

from utils import *
from conv_im import *

import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import os


FILLER = np.linspace(1023.0, 0.0, 1024)

class MyApp(wx.App):
    """Main application class."""

    def __init__(self):
        super().__init__(clearSigInt=True)

        self.mainFrame = MyFrame(None)
        self.mainFrame.Show()


###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.background = None
		# self.Bind(wx.EVT_SIZE, self.on_resize)
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

		self.status_bar = self.CreateStatusBar( 4, wx.STB_SIZEGRIP, wx.ID_ANY )
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
		

		self.btn_start.SetBitmap( wx.Bitmap( os.path.join('png', '002-play.png'), wx.BITMAP_TYPE_ANY ) )
		btns_sizer.Add( self.btn_start, 0, wx.EXPAND, 5 )

		self.btn_stop = wx.BitmapButton( self.btns_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn_stop.SetBitmap( wx.Bitmap( os.path.join('png', '001-stop.png'), wx.BITMAP_TYPE_ANY ) )
		btns_sizer.Add( self.btn_stop, 0, wx.EXPAND, 5 )

		self.btn_pause = wx.BitmapButton( self.btns_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn_pause.SetBitmap( wx.Bitmap( os.path.join('png', '003-pause.png'), wx.BITMAP_TYPE_ANY ) )
		btns_sizer.Add( self.btn_pause, 0, wx.EXPAND, 5 )

		self.btn_contin = wx.BitmapButton( self.btns_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn_contin.SetBitmap( wx.Bitmap( os.path.join('png', '004-shooting.png'), wx.BITMAP_TYPE_ANY ) )
		btns_sizer.Add( self.btn_contin, 0, wx.EXPAND, 5 )


		self.btns_panel.SetSizer( btns_sizer )
		self.btns_panel.Layout()
		btns_sizer.Fit( self.btns_panel )
		File.Add( self.btns_panel, 1, wx.EXPAND, 5 )

		self.hslice_panel = wx.Panel( self.m_panel314, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		hslice_sizer = wx.BoxSizer( wx.VERTICAL )

		# self.m_button5 = wx.Button( self.hslice_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		# hslice_sizer.Add( self.m_button5, 1, wx.EXPAND, 5 )


		self.hslice_figure = Figure(tight_layout=True, figsize=(1,1))
		self.hslice_axes = self.hslice_figure.add_subplot(111)
		self.hslice_axes.tick_params(axis='x', labelsize='xx-small')
		self.hslice_axes.tick_params(axis='y', labelsize='xx-small')
		self.hslice_axes.grid(color='grey', linestyle='-', linewidth=0.1)


		# self.hslice_axes.set_aspect('equal', adjustable='box')
        # self.cursor = Cursor(self.axes, useblit=True, color="red")
		self.hslice_canvas = FigureCanvas(self.hslice_panel, wx.ID_ANY, self.hslice_figure)
		# self.hslice_axes.invert_xaxis()

		# self.m_button5 = wx.Button( self.hslice_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		hslice_sizer.Add( self.hslice_canvas, 1, wx.ALL|wx.EXPAND, 5)


		self.hslice_panel.SetSizer( hslice_sizer )
		self.hslice_panel.Layout()
		hslice_sizer.Fit( self.hslice_panel )
		File.Add( self.hslice_panel, 1, wx.EXPAND, 5 )

		self.vslice_panel = wx.Panel( self.m_panel314, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		vslice_sizer = wx.BoxSizer( wx.VERTICAL )

		self.vslice_figure = Figure(tight_layout=True, figsize=(1,1))
		self.vslice_axes = self.vslice_figure.add_subplot(111)
		self.vslice_axes.tick_params(axis='x', rotation=90, labelsize='xx-small')
		self.vslice_axes.tick_params(axis='y', labelsize='xx-small')
		self.vslice_axes.grid(color='grey', linestyle='-', linewidth=0.1)

		# self.hslice_axes.set_aspect('equal', adjustable='box')
        # self.cursor = Cursor(self.axes, useblit=True, color="red")
		self.vslice_canvas = FigureCanvas(self.vslice_panel, wx.ID_ANY, self.vslice_figure)

		# self.m_button4 = wx.Button( self.vslice_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		vslice_sizer.Add( self.vslice_canvas, 1, wx.ALL|wx.EXPAND, 5 )


		self.vslice_panel.SetSizer( vslice_sizer )
		self.vslice_panel.Layout()
		vslice_sizer.Fit( self.vslice_panel )
		File.Add( self.vslice_panel, 1, wx.EXPAND, 5 )

		self.image_panel = wx.Panel( self.m_panel314, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		image_sizer = wx.BoxSizer( wx.VERTICAL )

		self.image_figure = Figure(tight_layout=True)
		self.image_axes = self.image_figure.add_subplot()
		self.image_axes.set_aspect('equal', adjustable='box')
		self.image_axes.invert_yaxis()
        # self.cursor = Cursor(self.axes, useblit=True, color="red")
		self.image_canvas = FigureCanvas(self.image_panel, wx.ID_ANY, self.image_figure)
		self.image_canvas.mpl_connect('motion_notify_event', self.update_status_bar)
		self.image_canvas.mpl_connect(
            "button_press_event", self.on_press
        )
		self.image_canvas.Bind(wx.EVT_ENTER_WINDOW, self.change_cursor_coordinates)

		# self.m_bitmap1 = wx.StaticBitmap( self.image_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		image_sizer.Add( self.image_canvas, 1, wx.ALL|wx.EXPAND, 5 )


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
		self.btn_pause.Bind( wx.EVT_BUTTON, self.on_refresh )
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

		self.cam = None
		self.cam = init_camera()
		if self.cam != None:
			self.status_bar.SetStatusText('Controller Status: Connected', 3)

	def __del__( self ):
		destroy_camera(self.cam)


	# Virtual event handlers, override them in your derived class
	def on_open( self, event ):
		# event.Skip()
		"""Open a raw data to process.
    
        When user clicks on "Open Text File" and find an appropriate file, 
        this function imports the data to `self.data` and plots it on graph
        panel.
        Args:
            event: wx.EVT_COMBOBOX. Checks that user have clicked on button.
        Returns:
            None
        """
		wildcard = "TSV files (*.tsv)|*.tsv"
		dialog = wx.FileDialog(
            self,
            "Open Text Files",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        )
		if dialog.ShowModal() == wx.ID_CANCEL:
			return
			
		path = dialog.GetPath()
		
		if os.path.exists(path):
			self.single_frame = np.loadtxt(path)
			
		self.draw_data()
		# self.calc_btn.Enable(False)
		
		# draw_data(self.graph, self.data[:, 0], self.data[:, 1], name="Spectrum")
		
		# self.auto.Enable(True)
		# self.calibration.Enable(True)
		# self.auto_cal.Enable(True)
		
		# if self.graphs.IsShown():
		# 	self.graphs.Hide()
		# 	self.graph.Show()
			
		# self.Parent.Layout()
		# self.Parent.Fit()

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

	def draw_data(self) -> None:
		self.image_axes.clear()
		self.image_axes.imshow(self.single_frame, origin='upper')
		self.image_axes.invert_yaxis()
		# self.vslice_axes.invert_yaxis()
		# self.cursor = Cursor(self.image_axes, color='black', linewidth=2)
		self.image_canvas.draw()
		self.background = self.image_canvas.copy_from_bbox(self.image_axes.bbox)
		# print(self.background)

	def update_status_bar(self, event) -> None:
		if event.inaxes:
			x, y = event.xdata, event.ydata
			self.status_bar.SetStatusText("x= "+str(round(x))+"  y="+str(round(y)), 0)
			
	def change_cursor_coordinates(self, event) -> None:
		self.image_canvas.SetCursor(wx.Cursor(wx.CURSOR_CROSS))

	def on_press(self, event) -> None:
		if event.inaxes:
			x, y = event.xdata, event.ydata
			self.draw_vslice(round(x))
			self.draw_hslice(round(x))
			self.image_canvas.restore_region(self.background)
			vline = self.image_axes.axvline(x=x, color='black')
			hline = self.image_axes.axhline(y=y, color='black')
			self.image_axes.draw_artist(vline)
			self.image_axes.draw_artist(hline)
			self.image_canvas.blit(vline.axes.bbox)
			self.image_canvas.blit(hline.axes.bbox)
			# self.image_axes.axvline(x=x, color='black')
			# self.image_axes.axhline(y=y, color='black')
			# self.image_canvas.draw()

	def draw_hslice(self, y) -> None:
		self.hslice_axes.clear()
		self.hslice_axes.plot(self.single_frame[:, y])
		self.hslice_axes.tick_params(axis='x', labelsize='xx-small')
		self.hslice_axes.tick_params(axis='y', labelsize='xx-small')
		self.hslice_axes.grid(color='grey', linestyle='-', linewidth=0.1)
		self.hslice_canvas.draw()

	def draw_vslice(self, x):
		self.vslice_axes.clear()
		self.vslice_axes.plot(self.single_frame[x, :], FILLER)
		self.vslice_axes.tick_params(axis='x', rotation=90, labelsize='xx-small')
		self.vslice_axes.tick_params(axis='y', labelsize='xx-small')
		self.vslice_axes.grid(color='grey', linestyle='-', linewidth=0.1)
		self.vslice_axes.invert_xaxis()
		self.vslice_canvas.draw()

	def on_refresh(self, event) -> None:
		if self.background != None:
			self.draw_data()



