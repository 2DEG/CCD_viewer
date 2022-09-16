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

        self.mainFrame = MyFrame(None)
        self.mainFrame.Show()


class MyFrame(wx.Frame):
    """Class which generates a frame.

    All of the visual positioning of the blocks are described here.
    """

    def __init__(self, parent, title="Wafer Processor", pos=(100, 100), style=wx.DEFAULT_FRAME_STYLE | wx.FULL_REPAINT_ON_RESIZE) -> None:

        super().__init__(parent, title=title, pos=pos)
        self.init_frame()
        self.SetBackgroundColour("white")

    def init_frame(self) -> None:
        """Initializes all the panels and set sizers.

        There are 3 panels: control panel for control buttons, graph panel
        for raw data visualization and preparation and graphs panel which
        switches from graph panel and shows stages of data process.

        Args:
            None

        Returns:
            None
        """

        # Sizers
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.graphSizer = wx.BoxSizer()
        self.controlSizer = wx.BoxSizer(wx.VERTICAL)

        # Panels
        self.control = MyPanel(self)
        self.control.show_buttons()
        self.nb = wx.Notebook(self)

        tabs_names = [
            "Хорошие/Плохие",
            "Карта RES",
            "Карта SNR",
            "Гистограмма RES",
            "Гистограмма SNR",
            "Корреляции",
        ]
        self.tabs = [None] * len(tabs_names)

        for idx, val in enumerate(tabs_names):
            self.tabs[idx] = Tab(self.nb)
            self.tabs[idx].draw_graph()
            self.nb.AddPage(self.tabs[idx], val)

        self.tabs.append(Tab(self.nb))
        self.tabs[-1].make_text_panel()
        self.nb.AddPage(self.tabs[-1], "Список")

        self.control.tabs = self.tabs
        # print(type(self.control.tabs[0]))

        self.graphSizer.Add(self.nb, 0, wx.EXPAND | wx.GROW)
        self.controlSizer.Add(self.control, 0, wx.ALL, 5)
        self.mainSizer.Add(self.graphSizer, 0, wx.LEFT, 5)
        self.mainSizer.Add(self.controlSizer, 0, wx.RIGHT, 5)
        self.SetSizer(self.mainSizer)
        self.Fit()
        

    


class MyPanel(wx.Panel):
    """Custom panel class."""

    def __init__(self, parent: MyFrame) -> None:
        super().__init__(parent=parent)

    def show_buttons(self) -> None:
        """Initializes all of the buttons.

        Buttons are placed at control panel. All the buttons use event-handlers
        to react on user activity and make an appropriate functions call.

        Args:
            None

        Returns:
            None
        """
        
        hbox = wx.BoxSizer(wx.VERTICAL)
        self.btn = wx.Button(self, label="Выбрать директорию")
        self.btn.Bind(wx.EVT_BUTTON, self.on_open)

        # -----------------

        self.st = wx.StaticText(self, label="")
        self.st.SetLabel("Имя директории")
        self.st.Bind(wx.EVT_SIZE, self.on_size)
        # -----------------

        self.config_object = ConfigParser()
        self.config_object.read("wafer.conf")
        self.choice = self.config_object[self.config_object.sections()[0]]
        # for key in self.choice:
        #     print(key, self.choice[key])
        # ------------------

        self.rbox = wx.RadioBox(
            self,
            label="Тип пикселей",
            choices=self.config_object.sections(),
            majorDimension=1,
            style=wx.RA_SPECIFY_COLS,
        )
        self.rbox.Enable(False)
        self.rbox.Bind(wx.EVT_RADIOBOX, self.on_radio_box)
        # ------------------

        self.calc_btn = wx.Button(self, label="Обработать")
        self.calc_btn.Enable(False)
        self.calc_btn.Bind(wx.EVT_BUTTON, self.calc_choice)
        # ------------------


        hbox.Add(self.btn, 0, wx.CENTER, 5)
        hbox.Add(self.st, 0, wx.CENTER | wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.rbox, 0, wx.CENTER, 5)
        hbox.Add(self.calc_btn, 0, wx.CENTER | wx.BOTTOM, 5)
        # self.Bind(wx.EVT_SIZE, self.on_size)

        self.SetSizer(hbox)
        

    def on_size(self, event: wx.Event):
        # try:
        #     self.snr_proc
        # except AttributeError:
        #     print(self.Parent.GetClientSize(), self.Parent.GetClientSize() - (100, 100))
        # else:
        #     self.drop_pics()
        #     print('Exist ', self.Parent.GetClientSize(), self.Parent.GetClientSize() - (100, 100))
        
        # print()
        return

    def on_select(self, event: wx.Event) -> None:
        """Updates refractive index data due to chosen source.

        When the user selects an item in the drop-down menu, the new refractive index data is read from the selected file.

        Args:
            event: wx.EVT_BUTTON. Checks that user have picked a member of the list.

        Returns:
            None
        """

        i = event.GetString()
        self.choice = self.config_object[i]
        # for key in self.choice:
        #     print(key, float(self.choice[key]))

    def on_radio_box(self, event: wx.Event) -> None:
        i = self.rbox.GetStringSelection()
        self.choice = self.config_object[i]
        # for key in self.choice:
        #     print(key, self.choice[key])
        self.is_linear = is_linear(self.choice["linear"])

    def on_open(self, event: wx.Event) -> None:
        """Open a raw data to process.

        When user clicks on "Open Text File" and find an appropriate file,
        this function imports the data to `self.data` and plots it on graph
        panel.

        Args:
            event: wx.EVT_COMBOBOX. Checks that user have clicked on button.

        Returns:
            None
        """

        wildcard = "TXT files (*.txt)|*.txt"

        dialog = wx.DirDialog(
            self,
            "Choose input directory",
            "",
            wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,
        )

        if dialog.ShowModal() == wx.ID_CANCEL:
            return

        self.dir_path = dialog.GetPath()
        self.st.SetLabel(
            "Директория: " + os.path.basename(os.path.normpath(self.dir_path))
        )
        self.rbox.Enable(True)
        i = self.rbox.GetStringSelection()
        self.choice = self.config_object[i]
        self.is_linear = is_linear(self.choice["linear"])
        self.tabs[-1].text_panel.SetValue("")

        self.calc_btn.Enable(True)

        self.Parent.Layout()
        self.Parent.Fit()

    def calc_choice(self, event: wx.Event) -> None:
        """Executes calculation based on checked/unchecked box.

        If the Checkbox is marked then calculations are launched with detailed
        information about each step. Otherwise a dialog box appears with thickness
        information.

        Args:
            event: wx.EVT_BUTTON

        Returns:
            None
        """
        self.rbox.Enable(False)
        # self.clear_graphs()

        self.path = self.dir_path

        self.res_arr, self.snr_arr = read_data_from_dir(
            folder=self.path,
            wafer=os.path.basename(os.path.normpath(self.path)),
            linear=self.is_linear,
        )
        self.gb, self.n_good, self.n_bad = good_bad_map(
            display_obj = self.tabs[-1],
            folder=self.path,
            wafer=os.path.basename(os.path.normpath(self.path)),
            minSNR=float(self.choice["minSNR"]),
            maxR=float(self.choice["maxR"]),
            minR=float(self.choice["minR"]),
            threshold=float(self.choice["threshold"]),
        )
        self.res_proc, self.snr_proc = make_snr_res(
            self.res_arr, self.snr_arr, folder=self.path, linear=self.is_linear
        )
        self.summary = make_summary(
            self.res_arr, self.snr_arr, folder=self.path, linear=self.is_linear
        )

        # draw_map(
        #     self.tabs[2],
        #     data=self.snr_proc,
        #     min_val=0.0,
        #     max_val=5 * float(self.choice["minSNR"]),
        #     path=path,
        #     name="SNR",
        #     linear=self.is_linear,
        #     pixel_nx=len(self.res_arr[0][0]),
        # )
        # draw_map(
        #     self.tabs[1],
        #     data=self.res_proc,
        #     min_val=float(self.choice["minR"]),
        #     max_val=float(self.choice["maxR"]),
        #     path=path,
        #     name="RES",
        #     linear=self.is_linear,
        #     pixel_nx=len(self.res_arr[0][0]),
        # )
        # draw_map(
        #     self.tabs[0],
        #     data=self.gb,
        #     path=path,
        #     text="good crystals/pixels: {:d}/{:d}\nbad crystals:{:d}".format(
        #         self.n_good, self.n_good * self.gb.shape[1], self.n_bad
        #     ),
        # )
        # draw_hist(
        #     self.tabs[3],
        #     data=self.summary[::, 0],
        #     min_val=float(self.choice["minR"]),
        #     max_val=float(self.choice["maxR"]),
        #     path=path,
        #     name="RES",
        # )
        # draw_hist(
        #     self.tabs[4],
        #     data=self.summary[::, 1],
        #     min_val=0.0,
        #     max_val=5 * float(self.choice["minSNR"]),
        #     path=path,
        #     name="SNR",
        # )
        # draw_corr(
        #     self.tabs[5],
        #     data=self.summary,
        #     minSNR=float(self.choice["minSNR"]),
        #     maxR=float(self.choice["maxR"]),
        #     minR=float(self.choice["minR"]),
        #     path=path,
        # )
        self.drop_pics()

    def showProgress(self):
        self.progress = wx.ProgressDialog("Происходит обработка данных", "Пожалуйста, подождите", maximum=100, parent=self, style=wx.PD_SMOOTH|wx.PD_AUTO_HIDE)

    def destoryProgress(self):
        self.progress.Destroy()
    
    def drop_pics(self):
        self.showProgress()
        self.clear_graphs()
        draw_map(
            self.tabs[2],
            data=self.snr_proc,
            min_val=float(0.0),
            # max_val=5 * float(self.choice["minSNR"]),
            max_val=float(self.choice["maxSNR"]),
            path=self.path,
            name="SNR",
            linear=self.is_linear,
            pixel_nx=len(self.res_arr[0][0]),
        )
        self.progress.Update(20)
        draw_map(
            self.tabs[1],
            data=self.res_proc,
            # min_val=float(self.choice["minR"]),
            # max_val=float(self.choice["maxR"]),
            min_val=float(0.0),
            max_val=float(self.choice["R_max_axis"]),
            path=self.path,
            name="RES",
            linear=self.is_linear,
            pixel_nx=len(self.res_arr[0][0]),
        )
        self.progress.Update(40)
        draw_map(
            self.tabs[0],
            data=self.gb,
            path=self.path,
            text="good crystals/pixels: {:d}/{:d}\nbad crystals:{:d}".format(
                self.n_good, self.n_good * self.gb.shape[1], self.n_bad
            ),
        )
        self.progress.Update(60)
        draw_hist(
            self.tabs[3],
            data=self.summary[::, 0],
            # min_val=float(self.choice["minR"]),
            # max_val=float(self.choice["maxR"]),
            min_val=float(0.0),
            max_val=float(self.choice["R_max_axis"]),
            path=self.path,
            name="RES",
        )
        self.progress.Update(80)
        draw_hist(
            self.tabs[4],
            data=self.summary[::, 1],
            min_val=0.0,
            max_val=5 * float(self.choice["minSNR"]),
            path=self.path,
            name="SNR",
        )
        self.progress.Update(100)
        draw_corr(
            self.tabs[5],
            data=self.summary,
            minSNR=float(self.choice["minSNR"]),
            maxSNR=float(self.choice["maxSNR"]),
            maxR=float(self.choice["maxR"]),
            minR=float(self.choice["minR"]),
            path=self.path,
        )
        self.destoryProgress()


    def draw_graph(
        self,
        fig_size: Tuple[float, float] = (6.0, 5.0),
        is_special: bool = True,
        dpi: int = 100,
    ) -> None:
        """Creates plot.

        Prepare canvas and define figures.

        Args:
            fig_size: sets figure size

            is_special: flag for different kind of navigation tools on figure

            dpi: dpi

        Returns:
            None
        """
        # print(self.GetClientSize(), self.GetClientSize() - (100, 100))
        self.figure = Figure(figsize=fig_size, dpi=dpi)
        self.axes = self.figure.add_subplot()
        # self.cursor = Cursor(self.axes, useblit=True, color="red")
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        # self.sizer.Add(self.canvas, 0, wx.LEFT | wx.TOP | wx.GROW)
        self.sizer.Add(self.canvas, 0, wx.EXPAND | wx.GROW)

        self.SetSizer(self.sizer)
        self.Fit()

    def make_text_panel(
        self,
        fig_size = (600, 500),
        # is_special: bool = True,
        # dpi: int = 100,
    ) -> None:
    
        self.text_panel = wx.TextCtrl(self, size = (600,500), style = wx.TE_MULTILINE)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        # self.sizer.Add(self.canvas, 0, wx.LEFT | wx.TOP | wx.GROW)
        self.sizer.Add(self.text_panel, 0, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)

        self.SetSizer(self.sizer)
        self.Fit()

    def clear_graphs(self) -> None:
        for each in self.tabs[:-1]:
            plt.close(each.figure)
            # each.draw_graph(fig_size=(self.Parent.GetClientSize()-(100, 100))/100.0)
            each.draw_graph()
        # self.tabs[-1].make_text_panel(fig_size=(self.Parent.GetClientSize()-(100, 100))/100.0)



class Tab(MyPanel):
    def __init__(self, parent: MyPanel):
        wx.Panel.__init__(self, parent)
