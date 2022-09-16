import numpy as np  # type: ignore

from typing import Tuple, Optional, List, Union
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
from matplotlib.patches import Rectangle
import matplotlib.ticker as ticker
import matplotlib.cm as cm


import os


def draw_corr(
    graphNum,
    data: np.ndarray,
    path: Optional[str] = os.getcwd(),
    style="-",
    text: Optional[str] = None,
    scatter_x: Union[np.ndarray, List[float]] = None,
    scatter_y: Union[np.ndarray, List[float]] = None,
    name: Optional[str] = None,
    label_l: str = "Peaks",
    size: int = 9,
    clear: bool = True,
    x_label: str = r"Wavelength $[\AA]$",
    y_label: str = "Intensity",
    minSNR: float = 1.5e5,
    maxSNR: float = 7.5e5,
    minR: float = 0,
    maxR: float = 1,
    dpi: int = 200,
) -> None:
    """Draws data.

    Draws data that it takes on the figure that is takes.

    Args:
        graphNum: shows on which particular canvas to draw

        x: data for axis-X

        y: data for axis-Y

        style: sets a style of plot

        text: text that would be written on plot

        scatter_x: data for axis-X (scatter style)

        scatter_y: data for axis-Y (scatter style)

        name: name of the plot

        label_l: labels if any

        size: fontsize

        clear: one may want to clear the plot

        x_label: str = Label to the axis-X

        y_label: str = Label to the axis-X

    Returns:
        None
    """

    if clear:
        graphNum.axes.clear()

    graphNum.axes.set_title("Wafer" + " " + os.path.basename(os.path.normpath(path)))

    graphNum.axes.grid(which="major", color="#AAAAAA", linewidth=0.8)
    graphNum.axes.grid(which="minor", color="#DDDDDD", linestyle=":", linewidth=0.5)
    # graphNum.axes.grid(which='minor', color='#AAAAAA', linewidth=0.8)
    graphNum.axes.minorticks_on()

    graphNum.axes.scatter(data[::, 0], data[::, 1], s=4)
    graphNum.axes.set_xscale("log")
    graphNum.axes.set_xlabel(r"R, $\Omega$", fontsize=15)
    graphNum.axes.set_xlim(100, 100 * 10 ** 3)
    graphNum.axes.add_patch(
        Rectangle(
            (minR, minSNR),
            width=(maxR - minR),
            height=(maxSNR - minSNR),
            fill=False,
            hatch="\\",
            color="red",
        )
    )

    # graphNum.axes.set_ylim(1.0, minSNR * 5)
    graphNum.axes.set_ylim(0.0, maxSNR)
    graphNum.axes.set_ylabel(r"SNR", fontsize=15)
    graphNum.axes.ticklabel_format(
        axis="y", style="sci", useMathText=True, scilimits=(0, 0)
    )

    graphNum.canvas.draw()
    graphNum.figure.savefig(os.path.join(path, os.path.basename(os.path.normpath(path)) + "_correlation"+".png"), dpi=dpi, format='png'
        # path + "//" + os.path.basename(os.path.normpath(path)) + "_correlation", dpi=dpi
    )


def draw_hist(
    graphNum,
    data: np.ndarray,
    path: Optional[str] = os.getcwd(),
    style="-",
    text: Optional[str] = None,
    scatter_x: Union[np.ndarray, List[float]] = None,
    scatter_y: Union[np.ndarray, List[float]] = None,
    name: Optional[str] = "SNR",
    label_l: str = "Peaks",
    size: int = 9,
    clear: bool = True,
    x_label: str = r"Wavelength $[\AA]$",
    y_label: str = "Intensity",
    n_bins: int = 50,
    min_val: float = 1.5e5,
    max_val: float = 0,
    dpi: int = 200,
) -> None:

    if clear:
        graphNum.axes.clear()
    graphNum.axes.set_title(
        name + " " + "Wafer" + " " + os.path.basename(os.path.normpath(path))
    )

    # graphNum.axes.spines['left'].set_position(('data', 0))
    # graphNum.axes.spines['bottom'].set_position(('data', 0))

    graphNum.axes.grid(which="major", color="#AAAAAA", linewidth=0.8)
    graphNum.axes.grid(which="minor", color="#DDDDDD", linestyle=":", linewidth=0.5)
    # graphNum.axes.grid(which='minor', color='#AAAAAA', linewidth=0.8)
    graphNum.axes.hist(
        data[(data > min_val) & (data < max_val)],
        bins=n_bins,
        edgecolor="black",
        linewidth=1.2,
    )
    
    graphNum.axes.minorticks_on()

    if name == "SNR":
        graphNum.axes.set_xlabel(r"SNR", fontsize=15)
    elif name == "RES":
        graphNum.axes.set_xlabel(r"R, $\Omega$", fontsize=15)

    graphNum.axes.set_ylabel(r"Count", fontsize=15)

    graphNum.axes.ticklabel_format(style="sci", useMathText=True, scilimits=(0, 0))
    graphNum.canvas.draw()
    graphNum.figure.savefig(os.path.join(path, os.path.basename(os.path.normpath(path)) + "_" + name +"_hist"+".png"), dpi=dpi, format='png'
        # path + "//" + os.path.basename(os.path.normpath(path)) + "_" + name + "_hist",
        # dpi=dpi,
    )


def fmt(x, pos):
    a, b = "{:.2e}".format(x).split("e")
    b = int(b)
    return r"${} \times 10^{{{}}}$".format(a, b)


def draw_map(
    graphNum,
    data: np.ndarray,
    path: Optional[str] = os.getcwd(),
    style="-",
    text: Optional[str] = None,
    scatter_x: Union[np.ndarray, List[float]] = None,
    scatter_y: Union[np.ndarray, List[float]] = None,
    name: str = "Good-Bad",
    label_l: str = "Peaks",
    size: int = 9,
    clear: bool = True,
    x_label: str = r"Wavelength $[\AA]$",
    y_label: str = "Intensity",
    pixel_nx: int = 8,
    pixel_ny: int = 2,
    min_val: float = 0,
    max_val: float = 1,
    linear: bool = None,
    dpi: int = 200,
) -> None:
    """Draws data.

    Draws data that it takes on the figure that is takes.

    Args:
        graphNum: shows on which particular canvas to draw

        x: data for axis-X

        y: data for axis-Y

        style: sets a style of plot

        text: text that would be written on plot

        scatter_x: data for axis-X (scatter style)

        scatter_y: data for axis-Y (scatter style)

        name: name of the plot

        label_l: labels if any

        size: fontsize

        clear: one may want to clear the plot

        x_label: str = Label to the axis-X

        y_label: str = Label to the axis-X

    Returns:
        None
    """

    if clear:
        graphNum.axes.clear()

    graphNum.axes.set_title(
        name + " " + "Wafer" + " " + os.path.basename(os.path.normpath(path))
    )

    # masked_array = np.ma.array(data, mask=np.isnan(data))
    # cmap = cm.get_cmap("coolwarm").copy()
    # cmap.set_bad('green')
    # # ax.imshow(masked_array, interpolation='nearest', cmap=cmap)
    # c = graphNum.axes.pcolor(masked_array, cmap=cmap,  vmin=min_val, vmax=max_val)

    # c = graphNum.axes.pcolor(data, cmap='coolwarm', edgecolors='k',  vmin=min_val, vmax=max_val)
    c = graphNum.axes.pcolor(data, cmap="coolwarm", vmin=min_val, vmax=max_val)
    graphNum.axes.grid(which="major", color="black", linewidth=0.8)
    graphNum.axes.grid(which="minor", color="black", linewidth=0.8)
    # graphNum.axes.grid(which='minor', color='#DDDDDD', linestyle=':', linewidth=0.5)
    graphNum.axes.minorticks_on()

    if (min_val == 0) & (max_val == 1):
        graphNum.figure.colorbar(c, ax=graphNum.axes)
    else:
        graphNum.figure.colorbar(c, ax=graphNum.axes, format=ticker.FuncFormatter(fmt))

    graphNum.axes = graphNum.figure.gca()
    graphNum.axes.set_ylim(graphNum.axes.get_ylim()[::-1])
    graphNum.axes.xaxis.tick_top()
    graphNum.axes.yaxis.tick_left()

    if linear == True:
        graphNum.axes.xaxis.set_major_locator(MultipleLocator(pixel_nx))
        graphNum.axes.xaxis.set_minor_locator(MultipleLocator(pixel_nx))
    else:
        graphNum.axes.xaxis.set_major_locator(MultipleLocator(pixel_nx))
        graphNum.axes.xaxis.set_minor_locator(MultipleLocator(pixel_nx))
        graphNum.axes.yaxis.set_minor_locator(MultipleLocator(pixel_ny))

    if linear == None:
        # graphNum.axes.xaxis.set_major_locator(MultipleLocator(1))
        graphNum.axes.xaxis.set_minor_locator(MultipleLocator(1))
        graphNum.axes.yaxis.set_minor_locator(MultipleLocator(1))
        # graphNum.axes.yaxis.set_major_locator(MultipleLocator(1))

    if text is not None:

        # these are matplotlib.patch.Patch properties
        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)

        # place a text box in upper left in axes coords
        graphNum.axes.text(
            0.00,
            -0.1,
            text,
            transform=graphNum.axes.transAxes,
            fontsize=size,
            # verticalalignment="top",
            bbox=props,
        )

    graphNum.canvas.draw()
    graphNum.figure.savefig(os.path.join(path, os.path.basename(os.path.normpath(path)) + "_"+name+"_map"+".png"), dpi=dpi, format='png'
        # path + "//" + os.path.basename(os.path.normpath(path)) + "_" + name + "_map",
        # dpi=dpi,
    )


def is_linear(word: str = "True") -> bool:
    return True if word == "True" else False
