import numpy as np
from PyQt5 import QtGui


class DarkPalette(QtGui.QPalette):
    """Class that inherits from pyqtgraph.QtGui.QPalette and renders dark colours for the application."""

    def __init__(self):
        QtGui.QPalette.__init__(self)
        self.setup()

    def setup(self):
        self.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 50, 47))
        self.setColor(QtGui.QPalette.WindowText, QtGui.QColor(255, 255, 255))
        self.setColor(QtGui.QPalette.Base, QtGui.QColor(30, 27, 24))
        self.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 50, 47))
        self.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(255, 255, 255))
        self.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(255, 255, 255))
        self.setColor(QtGui.QPalette.Text, QtGui.QColor(255, 255, 255))
        self.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 50, 47))
        self.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255, 255, 255))
        self.setColor(QtGui.QPalette.BrightText, QtGui.QColor(255, 0, 0))
        self.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
        self.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
        self.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(0, 0, 0))
        self.setColor(
            QtGui.QPalette.Disabled, QtGui.QPalette.Text, QtGui.QColor(128, 128, 128)
        )
        self.setColor(
            QtGui.QPalette.Disabled,
            QtGui.QPalette.ButtonText,
            QtGui.QColor(128, 128, 128),
        )
        self.setColor(
            QtGui.QPalette.Disabled,
            QtGui.QPalette.WindowText,
            QtGui.QColor(128, 128, 128),
        )


COLORMAP_COLORS = np.array(
    [
        [103, 0, 31],
        [112, 0, 31],
        [121, 1, 32],
        [130, 3, 33],
        [138, 5, 34],
        [146, 8, 35],
        [154, 10, 36],
        [161, 14, 38],
        [167, 17, 40],
        [173, 20, 41],
        [178, 24, 43],
        [183, 28, 45],
        [187, 34, 47],
        [191, 40, 50],
        [195, 48, 54],
        [198, 56, 57],
        [201, 64, 61],
        [204, 72, 65],
        [208, 81, 69],
        [211, 89, 73],
        [214, 96, 77],
        [217, 103, 81],
        [221, 110, 86],
        [224, 117, 91],
        [228, 125, 96],
        [231, 132, 101],
        [235, 139, 107],
        [238, 146, 112],
        [240, 152, 118],
        [242, 159, 124],
        [244, 165, 130],
        [245, 171, 136],
        [247, 177, 143],
        [248, 183, 150],
        [249, 189, 157],
        [250, 194, 164],
        [251, 200, 172],
        [251, 205, 179],
        [252, 210, 186],
        [253, 215, 193],
        [253, 219, 199],
        [253, 224, 206],
        [254, 228, 213],
        [254, 233, 220],
        [254, 238, 228],
        [254, 242, 235],
        [255, 246, 241],
        [255, 250, 247],
        [255, 253, 251],
        [255, 254, 254],
        [255, 255, 255],
        [254, 254, 254],
        [252, 252, 252],
        [249, 249, 249],
        [246, 246, 246],
        [241, 241, 241],
        [237, 237, 237],
        [232, 232, 232],
        [228, 228, 228],
        [224, 224, 224],
        [220, 220, 220],
        [217, 217, 217],
        [213, 213, 213],
        [210, 210, 210],
        [206, 206, 206],
        [202, 202, 202],
        [198, 198, 198],
        [194, 194, 194],
        [190, 190, 190],
        [186, 186, 186],
        [182, 182, 182],
        [177, 177, 177],
        [172, 172, 172],
        [167, 167, 167],
        [162, 162, 162],
        [157, 157, 157],
        [151, 151, 151],
        [146, 146, 146],
        [140, 140, 140],
        [135, 135, 135],
        [129, 129, 129],
        [124, 124, 124],
        [118, 118, 118],
        [112, 112, 112],
        [106, 106, 106],
        [100, 100, 100],
        [94, 94, 94],
        [88, 88, 88],
        [83, 83, 83],
        [77, 77, 77],
        [72, 72, 72],
        [66, 66, 66],
        [61, 61, 61],
        [56, 56, 56],
        [51, 51, 51],
        [46, 46, 46],
        [41, 41, 41],
        [36, 36, 36],
        [31, 31, 31],
        [26, 26, 26],
    ]
)

SANITY_PLOT_COLORS = {
    "diagnostic":
        [
            [23, 41, 114],
            [24, 42, 117],
            [24, 43, 120],
            [24, 44, 123],
            [25, 45, 125],
            [25, 46, 129],
            [26, 48, 131],
            [26, 49, 134],
            [26, 50, 137],
            [27, 51, 140],
            [27, 52, 143],
            [27, 53, 146],
            [28, 54, 149],
            [28, 56, 152],
            [28, 57, 155],
            [29, 58, 158],
            [29, 59, 161],
            [29, 60, 164],
            [29, 61, 168],
            [30, 62, 171],
            [30, 63, 174],
            [30, 65, 177],
            [31, 66, 180],
            [31, 67, 183],
            [32, 68, 186],
            [32, 70, 189],
            [33, 71, 192],
            [34, 72, 194],
            [35, 73, 197],
            [36, 74, 200],
            [37, 76, 202],
            [39, 77, 205],
            [41, 78, 207],
            [43, 80, 210],
            [45, 81, 212],
            [47, 82, 214],
            [49, 84, 215],
            [52, 85, 217],
            [55, 86, 219],
            [57, 88, 220],
            [60, 89, 222],
            [63, 91, 223],
            [66, 92, 224],
            [68, 93, 225],
            [71, 95, 226],
            [74, 96, 227],
            [76, 98, 228],
            [79, 99, 229],
            [82, 101, 230],
            [85, 102, 231],
            [87, 104, 232],
            [90, 105, 233],
            [92, 107, 234],
            [95, 108, 235],
            [97, 110, 235],
            [99, 111, 236],
            [102, 113, 237],
            [104, 114, 238],
            [106, 116, 239],
            [109, 118, 239],
            [111, 119, 240],
            [113, 121, 241],
            [115, 122, 242],
            [117, 124, 243],
            [120, 125, 244],
            [122, 127, 245],
            [124, 129, 245],
            [126, 130, 246],
            [128, 132, 247],
            [130, 133, 247],
            [132, 135, 248],
            [134, 137, 249],
            [136, 138, 249],
            [138, 140, 250],
            [141, 142, 250],
            [143, 143, 251],
            [145, 145, 251],
            [147, 147, 252],
            [149, 148, 252],
            [151, 150, 252],
            [153, 152, 252],
            [155, 154, 252],
            [157, 155, 253],
            [159, 157, 253],
            [161, 159, 252],
            [163, 160, 252],
            [165, 162, 252],
            [168, 164, 252],
            [170, 166, 252],
            [171, 168, 252],
            [173, 169, 252],
            [175, 171, 251],
            [177, 173, 251],
            [179, 175, 251],
            [181, 176, 251],
            [183, 178, 251],
            [185, 180, 250],
            [187, 182, 250],
            [189, 184, 250],
            [190, 185, 250],
            [193, 187, 249],
            [194, 189, 249],
            [196, 191, 249],
            [198, 193, 249],
            [200, 195, 248],
            [201, 196, 248],
            [203, 198, 248],
            [205, 200, 247],
            [207, 202, 247],
            [208, 204, 247],
            [210, 206, 247],
            [212, 208, 246],
            [213, 209, 246],
            [215, 211, 246],
            [217, 213, 245],
            [219, 214, 245],
            [220, 216, 244],
            [222, 218, 244],
            [224, 220, 243],
            [225, 221, 243],
            [227, 222, 242],
            [228, 223, 241],
            [230, 225, 240],
            [232, 225, 239],
            [233, 226, 237],
            [235, 227, 236],
            [236, 227, 235],
            [237, 227, 233],
            [239, 227, 231],
            [240, 226, 229],
            [241, 225, 227],
            [242, 224, 225],
            [243, 223, 222],
            [244, 222, 220],
            [245, 221, 217],
            [246, 219, 214],
            [247, 217, 212],
            [247, 215, 209],
            [248, 213, 206],
            [249, 211, 203],
            [249, 209, 200],
            [250, 207, 198],
            [250, 205, 195],
            [250, 202, 192],
            [251, 200, 189],
            [251, 198, 186],
            [251, 196, 183],
            [252, 193, 181],
            [252, 191, 178],
            [252, 188, 175],
            [252, 186, 172],
            [252, 184, 169],
            [252, 182, 166],
            [253, 179, 163],
            [253, 177, 161],
            [253, 174, 158],
            [253, 172, 155],
            [253, 170, 152],
            [253, 168, 150],
            [253, 165, 147],
            [253, 163, 144],
            [253, 160, 141],
            [252, 158, 138],
            [252, 156, 136],
            [252, 153, 133],
            [252, 151, 130],
            [252, 148, 128],
            [252, 146, 125],
            [251, 144, 122],
            [251, 141, 120],
            [251, 139, 117],
            [250, 136, 114],
            [250, 134, 112],
            [249, 132, 109],
            [249, 129, 107],
            [248, 127, 105],
            [248, 124, 102],
            [247, 122, 100],
            [246, 120, 97],
            [246, 118, 95],
            [245, 116, 93],
            [244, 113, 91],
            [243, 111, 88],
            [242, 109, 86],
            [241, 107, 84],
            [240, 104, 82],
            [239, 102, 80],
            [237, 100, 78],
            [236, 98, 76],
            [235, 96, 74],
            [234, 94, 72],
            [233, 91, 70],
            [232, 89, 68],
            [230, 87, 66],
            [229, 85, 65],
            [228, 83, 62],
            [226, 80, 61],
            [225, 78, 59],
            [224, 76, 57],
            [223, 73, 55],
            [221, 71, 53],
            [220, 69, 51],
            [219, 66, 49],
            [218, 64, 47],
            [216, 61, 45],
            [215, 59, 44],
            [213, 56, 42],
            [212, 54, 40],
            [211, 51, 38],
            [209, 48, 36],
            [208, 46, 34],
            [207, 43, 33],
            [205, 40, 31],
            [203, 37, 29],
            [202, 34, 28],
            [200, 31, 26],
            [199, 28, 24],
            [197, 25, 23],
            [195, 22, 21],
            [193, 19, 20],
            [191, 16, 19],
            [189, 12, 18],
            [187, 9, 17],
            [185, 7, 16],
            [182, 5, 15],
            [180, 3, 14],
            [178, 2, 14],
            [175, 1, 13],
            [173, 1, 12],
            [170, 0, 12],
            [168, 0, 11],
            [165, 0, 11],
            [162, 1, 11],
            [159, 1, 11],
            [157, 1, 10],
            [154, 2, 10],
            [151, 2, 10],
            [149, 2, 10],
            [146, 3, 9],
            [143, 3, 9],
            [141, 4, 9],
            [138, 4, 8],
            [135, 4, 8],
            [133, 5, 8],
            [130, 5, 7],
            [128, 5, 7],
            [125, 6, 7],
            [122, 6, 6],
            [120, 6, 6],
            [117, 6, 5],
            [115, 7, 5],
            [112, 7, 4],
            [110, 7, 4],
            [107, 7, 3],
            [105, 7, 3],
            [102, 7, 2]
        ],
    "dissimilarity":
        [
            [8, 92, 248],
            [15, 95, 244],
            [19, 97, 241],
            [23, 99, 237],
            [25, 101, 233],
            [27, 103, 229],
            [28, 106, 225],
            [29, 108, 222],
            [29, 110, 218],
            [30, 112, 214],
            [29, 114, 210],
            [29, 116, 206],
            [28, 117, 203],
            [27, 119, 199],
            [25, 121, 195],
            [24, 123, 191],
            [22, 125, 187],
            [20, 126, 184],
            [19, 128, 180],
            [18, 130, 176],
            [18, 131, 172],
            [19, 133, 168],
            [20, 134, 164],
            [23, 136, 160],
            [26, 137, 156],
            [29, 138, 152],
            [32, 140, 147],
            [35, 141, 143],
            [39, 142, 139],
            [42, 143, 134],
            [45, 144, 130],
            [47, 146, 126],
            [49, 147, 121],
            [52, 148, 117],
            [53, 149, 112],
            [55, 150, 108],
            [56, 151, 103],
            [57, 152, 98],
            [58, 154, 94],
            [59, 155, 89],
            [59, 156, 84],
            [59, 157, 80],
            [60, 158, 75],
            [60, 159, 70],
            [60, 160, 66],
            [61, 161, 61],
            [61, 162, 57],
            [62, 163, 53],
            [63, 164, 49],
            [65, 165, 46],
            [66, 166, 43],
            [68, 167, 40],
            [71, 168, 38],
            [73, 168, 36],
            [76, 169, 34],
            [78, 170, 33],
            [81, 170, 32],
            [84, 171, 32],
            [87, 172, 31],
            [90, 172, 31],
            [92, 173, 30],
            [95, 174, 30],
            [98, 174, 30],
            [101, 175, 30],
            [103, 175, 29],
            [106, 176, 29],
            [108, 177, 29],
            [111, 177, 29],
            [114, 178, 29],
            [116, 178, 29],
            [119, 179, 28],
            [121, 180, 28],
            [123, 180, 28],
            [126, 181, 28],
            [128, 181, 27],
            [131, 182, 27],
            [133, 182, 27],
            [135, 183, 27],
            [138, 184, 27],
            [140, 184, 26],
            [142, 185, 26],
            [145, 185, 26],
            [147, 186, 26],
            [149, 186, 25],
            [151, 187, 25],
            [154, 187, 25],
            [156, 188, 25],
            [158, 189, 24],
            [160, 189, 24],
            [163, 190, 24],
            [165, 190, 24],
            [167, 191, 23],
            [169, 191, 23],
            [171, 192, 23],
            [174, 192, 22],
            [176, 193, 22],
            [178, 193, 22],
            [180, 194, 21],
            [182, 194, 21],
            [184, 195, 21],
            [187, 195, 20],
            [189, 196, 20],
            [191, 197, 20],
            [193, 197, 19],
            [195, 198, 19],
            [197, 198, 19],
            [199, 199, 18],
            [202, 199, 18],
            [204, 200, 18],
            [206, 200, 17],
            [208, 201, 17],
            [210, 201, 16],
            [212, 202, 16],
            [214, 202, 15],
            [216, 203, 15],
            [219, 203, 14],
            [221, 203, 14],
            [223, 204, 14],
            [225, 204, 14],
            [227, 205, 14],
            [229, 205, 14],
            [231, 205, 15],
            [233, 206, 16],
            [235, 206, 18],
            [237, 206, 20],
            [239, 205, 22],
            [241, 205, 25],
            [243, 205, 28],
            [244, 204, 31],
            [246, 203, 35],
            [247, 202, 38],
            [248, 201, 41],
            [249, 200, 45],
            [249, 199, 48],
            [250, 198, 51],
            [250, 197, 54],
            [251, 195, 57],
            [251, 194, 60],
            [252, 192, 63],
            [252, 191, 65],
            [252, 190, 68],
            [252, 188, 70],
            [252, 187, 72],
            [253, 185, 75],
            [253, 184, 77],
            [253, 182, 79],
            [253, 181, 81],
            [253, 179, 83],
            [253, 178, 85],
            [254, 176, 87],
            [254, 175, 89],
            [254, 173, 91],
            [254, 172, 93],
            [254, 170, 95],
            [254, 169, 97],
            [254, 167, 99],
            [254, 166, 101],
            [254, 164, 102],
            [254, 163, 104],
            [254, 161, 106],
            [254, 160, 108],
            [255, 158, 109],
            [255, 157, 111],
            [255, 155, 113],
            [255, 154, 114],
            [255, 152, 116],
            [255, 151, 117],
            [255, 149, 119],
            [255, 147, 121],
            [255, 146, 122],
            [255, 144, 124],
            [255, 143, 125],
            [255, 141, 127],
            [254, 139, 128],
            [254, 138, 130],
            [254, 136, 132],
            [254, 134, 133],
            [254, 133, 135],
            [254, 131, 136],
            [254, 129, 138],
            [254, 128, 139],
            [254, 126, 140],
            [254, 124, 142],
            [254, 122, 143],
            [253, 121, 145],
            [253, 119, 146],
            [253, 117, 148],
            [253, 115, 149],
            [253, 113, 151],
            [253, 112, 152],
            [253, 110, 153],
            [252, 108, 155],
            [252, 106, 156],
            [252, 104, 158],
            [252, 102, 159],
            [252, 100, 160],
            [251, 98, 162],
            [251, 96, 163],
            [251, 94, 164],
            [251, 92, 165],
            [250, 90, 166],
            [250, 88, 167],
            [250, 86, 168],
            [250, 84, 168],
            [249, 82, 168],
            [249, 80, 168],
            [249, 78, 167],
            [248, 76, 166],
            [248, 74, 165],
            [248, 73, 163],
            [247, 71, 161],
            [247, 70, 158],
            [247, 68, 156],
            [246, 67, 153],
            [246, 66, 150],
            [246, 64, 146],
            [245, 63, 143],
            [245, 62, 140],
            [244, 61, 136],
            [244, 60, 133],
            [243, 58, 130],
            [243, 57, 126],
            [242, 56, 123],
            [241, 55, 120],
            [241, 54, 116],
            [240, 52, 113],
            [240, 51, 109],
            [239, 50, 106],
            [238, 49, 103],
            [238, 47, 99],
            [237, 46, 96],
            [236, 45, 93],
            [235, 44, 89],
            [235, 42, 86],
            [234, 41, 83],
            [233, 40, 79],
            [232, 38, 76],
            [232, 37, 73],
            [231, 36, 69],
            [230, 34, 66],
            [229, 33, 63],
            [228, 32, 59],
            [227, 30, 56],
            [226, 29, 53],
            [226, 27, 49],
            [225, 26, 46],
            [224, 24, 42],
            [223, 22, 38],
            [222, 20, 35],
            [221, 19, 31],
            [220, 17, 27],
            [219, 15, 23],
            [218, 12, 18],
            [217, 10, 12],
            [216, 7, 6],
            [215, 5, 0]
        ]
}
