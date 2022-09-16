#! python3
import math
import numpy as np
import struct
import os, shutil
import sys, time
import getopt
from typing import Tuple, Optional, List, Union


def read_data_from_dir(
    folder: str = "", wafer: str = "", linear: bool = False
) -> Tuple[np.ndarray, np.ndarray]:

    i = 0
    # print("Linear: ", linear)
    res_arr = []
    snr_arr = []
    while True:
        try:
            res = None
            snr = None
            # print("SNR_{:s}_{:03d}.dat".format(wafer, i))
            with open(
                os.path.join(folder, "SNR_{:s}_{:03d}.dat".format(wafer, i))
            ) as f:
                for line in f:
                    if line[0] == "#":
                        continue
                    else:
                        x = np.array([list(map(float, line.split("\t")))])
                        if linear:
                            if snr is None:
                                snr = np.ndarray((0, x.shape[1]), dtype=np.float32)
                            snr = np.concatenate((snr, x))

                        else:
                            if snr is None:
                                snr = np.ndarray((0, x.shape[1] // 2), dtype=np.float32)
                            snr = np.concatenate((snr, x[:, 0 : x.shape[1] // 2]))
                            snr = np.concatenate((snr, x[:, x.shape[1] // 2 :]))

            snr_arr.append(snr)
            # print("SNR: ", snr)
            # snr_arr = np.append(snr_arr, snr, axis=0)
            # print("RES_{:s}_{:03d}.dat".format(wafer,i))
            with open(
                os.path.join(folder, "RES_{:s}_{:03d}.dat".format(wafer, i))
            ) as f:
                for line in f:
                    if line[0] == "#":
                        continue
                    else:
                        x = np.array([list(map(float, line.split("\t")))])
                        if linear:
                            if res is None:
                                res = np.ndarray((0, x.shape[1]), dtype=np.float32)
                            res = np.concatenate((res, x))
                        else:
                            if res is None:
                                res = np.ndarray((0, x.shape[1] // 2), dtype=np.float32)
                            res = np.concatenate((res, x[:, 0 : x.shape[1] // 2]))
                            res = np.concatenate((res, x[:, x.shape[1] // 2 :]))

            res_arr.append(res)
            # res_arr = np.append(res_arr, res, axis=0)
            i += 1
        except IOError as e:
            print(e)
            break

    # print(res_arr)
    # print(np.array(res_arr).flatten())
    # np.savetxt(os.path.join(folder,"res_arr_view.dat"), np.array(res_arr), delimiter="\t")
    return res_arr, snr_arr


def make_summary(
    res_arr: np.array = np.array([]),
    snr_arr: np.array = np.array([]),
    linear: bool = False,
    folder: str = os.getcwd(),
) -> np.ndarray:

    ans = np.ndarray((0, 2))

    for each in zip(res_arr, snr_arr):
        # print(np.array(list(zip(each[0].flatten(), each[1].flatten()))))
        # ans = np.append(ans, np.array(list(zip(each[0].flatten(), each[1].flatten()))), axis=0)
        ans = np.append(
            ans,
            np.array(
                list(
                    zip(
                        each[0][np.logical_not(np.isneginf(each[0]))],
                        each[1][np.logical_not(np.isneginf(each[1]))],
                    )
                )
            ),
            axis=0,
        )

    np.savetxt(os.path.join(folder, "sum_test.dat"), ans, delimiter="\t", fmt="%1.4e")

    return ans


def make_snr_res(
    res_arr: np.array = np.array([]),
    snr_arr: np.array = np.array([]),
    linear: bool = False,
    folder: str = os.getcwd(),
):
    d = snr_arr[0].shape[1]
    a = len(snr_arr) * d
    b = max(snr_arr, key=(lambda x: x.shape[0])).shape[0]
    # print("A and B: ", a, b)
    # print("Arrays shapes: ", snr_arr.shape, res_arr.shape)
    snr = np.full((b, a), np.NaN)
    res = np.full((b, a), np.NaN)
    for i in range(len(snr_arr)):

        x = snr_arr[i].shape[0]
        dx = 0 if linear or (b - x) // 4 == (b - x) / 4 else 1
        snr[(b - x) // 2 - dx : (b + x) // 2 - dx, i * d : (i + 1) * d] = snr_arr[i]

        x = res_arr[i].shape[0]
        dx = 0 if linear or (b - x) // 4 == (b - x) / 4 else 1
        res[(b - x) // 2 - dx : (b + x) // 2 - dx, i * d : (i + 1) * d] = res_arr[i]

    np.savetxt(os.path.join(folder, "snr_test.dat"), snr, delimiter="\t")
    np.savetxt(os.path.join(folder, "res_test.dat"), res, delimiter="\t")

    # with open(os.path.join(folder,"snr.dat"),"w") as f:
    #     for i in range(snr.shape[0]):
    #         s="\t".join(map(str,snr[i,:]))
    #         f.write(s+"\n")

    # with open(os.path.join(folder,"res.dat"),"w") as f:
    #     for i in range(res.shape[0]):
    #         s="\t".join(map(str,res[i,:]))
    #         f.write(s+"\n")
    return (res, snr)


def make_pic(
    res_arr: np.array = np.array([]),
    snr_arr: np.array = np.array([]),
    linear: bool = False,
):
    return


def good_bad_map(
    display_obj = None,
    folder: str = "",
    wafer: str = "",
    threshold: int = 0,
    minSNR: float = 0,
    minR: float = 0,
    maxR: float = 0,
) -> Tuple[np.ndarray, int, int]:

    i = 0
    res_arr = []
    snr_arr = []
    while True:
        try:
            res = None
            snr = None

            with open(
                os.path.join(folder, "SNR_{:s}_{:03d}.dat".format(wafer, i))
            ) as f:
                for line in f:
                    if line[0] == "#":
                        continue
                    else:
                        x = np.array([list(map(float, line.split("\t")))])
                        if snr is None:
                            snr = x
                        else:
                            snr = np.concatenate((snr, x))

            snr_arr.append(snr)
            with open(
                os.path.join(folder, "RES_{:s}_{:03d}.dat".format(wafer, i))
            ) as f:
                for line in f:
                    if line[0] == "#":
                        continue
                    else:
                        x = np.array([list(map(float, line.split("\t")))])
                        if res is None:
                            res = x

                        else:
                            res = np.concatenate((res, x))

            res_arr.append(res)
            i += 1
        except IOError as e:
            print(e)
            break
    d = snr_arr[0].shape[1]
    a = len(snr_arr)
    b = max(snr_arr, key=(lambda x: x.shape[0])).shape[0]
    # print(a, b)
    snr = np.full((b, a), np.NaN)

    bad_count = 0
    total = 0
    list_file = open(os.path.join(folder, "list_bad.dat"), "w")
    for i in range(len(snr_arr)):
        x, y = snr_arr[i].shape
        
        if display_obj != None:
            display_obj.text_panel.write("\ncolumn {:d} :\n".format(i))
        else:
            print("\ncolumn", i, ":")
        
        print("\ncolumn", i, ":", file=list_file)
        for j in range(x):
            bad = 0
            for k in range(y):
                if (
                    snr_arr[i][j, k] < minSNR
                    or res_arr[i][j, k] < minR
                    or res_arr[i][j, k] > maxR
                ):
                    bad += 1

            snr[(b - x) // 2 + j, i] = 0 if bad > threshold else 1
            if bad > threshold:
                if display_obj != None:
                    display_obj.text_panel.write("{:d}, ".format(j+1))
                else:
                    print(j + 1, end=", ")
                print(j + 1, end=", ", file=list_file)

    good = int(np.sum(np.where(snr == 1, 1, 0)))
    bad = int(np.sum(np.where(snr == 0, 1, 0)))
    if display_obj != None:
        display_obj.text_panel.write("\n\ngood crystals/pixels: {:d}/{:d}\nbad crystals:{:d}".format(
            good, good * y, bad
        ))
    else:
        print(
        "\n\ngood crystals/pixels: {:d}/{:d}\nbad crystals:{:d}".format(
            good, good * y, bad
        )
        )
    
    print(
        "\n\ngood crystals/pixels: {:d}/{:d}\nbad crystals:{:d}".format(
            good, good * y, bad
        ),
        file=list_file,
    )
    # print(snr.shape)
    with open(os.path.join(folder, "good_bad.dat"), "w") as f:
        for i in range(snr.shape[0]):
            s = "\t".join(map(str, snr[i, :]))
            f.write(s + "\n")
    # print(snr.shape)
    # np.savetxt(os.path.join(folder,"snr_test.dat"), snr,delimiter="\t")
    return (snr, good, bad)
