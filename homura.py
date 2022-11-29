import turtle as ttle
from typing import Tuple

WriteSteps = 500       
Speed = 2.5
Width = 666            
Height = 666        
Xh, Yh = 0, 0     


ttle.tracer(10)
ttle.setup(Width, Height, 0, 0)
ttle.setworldcoordinates(0, Height, Width, 0)
ttle.pensize(1)
ttle.speed(Speed)
ttle.penup()


def move_to(point):
    ttle.penup()
    ttle.goto(point)


def point_of_bezier(points, timestep, dimension=2):
    degree = len(points) - 1
    if(degree == 0):
        return points[0]
    else:
        new_points = []
        for idx in range(degree):
            temp = []
            for d in range(dimension):
                temp.append(points[idx][d] * (1.0 - timestep) +
                            points[idx + 1][d] * timestep)
            new_points.append(tuple(temp))
        return point_of_bezier(tuple(new_points), timestep, dimension)


def curve_of_bezier(points, dimension=None):
    if(dimension is None):
        dimension = len(points[0])

    move_to(points[0])
    ttle.pendown()
    for timestep in range(0, WriteSteps + 1):
        p = point_of_bezier(points, timestep / WriteSteps, dimension)
        ttle.goto(p)
    ttle.penup()


def bezier_curve_through(points, relative: bool = False):
    global Xh
    global Yh
    curr = ttle.position()
    points = list(points)
    if(relative):
        for i in range(len(points)):
            points[i] = tuple([c1 + c2 for c1, c2 in zip(points[i], curr)])
    points.insert(0, curr)
    curve_of_bezier(tuple(points))
    Xh = points[-1][0] - points[-2][0]
    Yh = points[-1][1] - points[-2][1]


def bezier_curve_Smooth_ver(points, relative: bool = False):
    global Xh
    global Yh
    points = list(points)
    points.insert(0, (Xh + ttle.position()[0], Yh + ttle.position()[1]))
    if(relative):
        points[0] = (points[0][0] - ttle.position()[0],
                     points[0][1] - ttle.position()[1])
    bezier_curve_through(tuple(points), relative)


def between_the_line(source, destination):
    move_to(source)
    ttle.pendown()
    ttle.goto(destination)


def displace_the_line(displacement):
    between_the_line(ttle.position(), ttle.position() + displacement)


def line_to(destination):
    between_the_line(ttle.position(), destination)


def horizontal_line_to_destination(destination_x):
    between_the_line(ttle.position(), (destination_x, ttle.ycor()))


def horizontal_displace(dx):
    between_the_line(ttle.position(), ttle.position() + (dx, 0))


def displace_the_line_vertical(dy):
    between_the_line(ttle.position(), ttle.position() + (0, dy))


def polyline(points):
    total = len(points)
    for idx in range(total - 1):
        between_the_line(points[idx], points[idx + 1])


def main():
    """
    Layer 1
    """

    # Coat
    ttle.color("violet", "#c6d5fb")
    move_to((61, 462))
    ttle.begin_fill()
    bezier_curve_Smooth_ver(((12, -41), (27, -58)), relative=True)
    bezier_curve_through(((-6, -36), (6, -118), (9, -132)), relative=True)
    bezier_curve_through(((-15, -27), (-23, -51), (-26, -74)), relative=True)
    bezier_curve_through(((4, -66), (38, -105), (65, -149)), relative=True)
    horizontal_line_to_destination(486)
    bezier_curve_through(((12, 24), (40, 99), (33, 114)), relative=True)
    bezier_curve_through(((39, 82), (55, 129), (39, 144)), relative=True)
    bezier_curve_Smooth_ver(((-31, 23), (-39, 28)), relative=True)
    bezier_curve_Smooth_ver(((-12, 37), (-12, 37)), relative=True)
    displace_the_line((50, 92))
    horizontal_line_to_destination(445)
    bezier_curve_Smooth_ver(((-29, -38), (-31, -46)), relative=True)
    bezier_curve_Smooth_ver(((78, -107), (72, -119)), relative=True)
    bezier_curve_Smooth_ver(((355, 178), (340, 176)))
    bezier_curve_Smooth_ver(((272, 63), (264, 64)))
    bezier_curve_Smooth_ver(((-29, 67), (-27, 73)), relative=True)
    bezier_curve_Smooth_ver(((99, 292), (174, 428), (173, 439)))
    bezier_curve_Smooth_ver(((-8, 23), (-8, 23)), relative=True)
    line_to((61, 462))
    ttle.end_fill()

    # Shadow
    move_to((60.5, 461.5))
    ttle.color("black", "#4a55a5")
    ttle.begin_fill()
    bezier_curve_through(((0, 0), (17, -42), (27, -59)), relative=True)
    bezier_curve_through(((-6, -33), (6, -128), (10, -133)), relative=True)
    bezier_curve_through(
        ((-15, -10), (-27, -66), (-27.285, -75)), relative=True)
    ttle.pencolor("#D3DFF0")
    bezier_curve_through(((12.285, 11), (82.963, 156),
                         (82.963, 156)), relative=True)
    ttle.pencolor("black")
    bezier_curve_Smooth_ver(((12.322, 75), (19.322, 86)), relative=True)
    bezier_curve_through(((-1, 11), (-8, 25), (-8, 25)), relative=True)
    horizontal_line_to_destination(60.5)
    ttle.end_fill()

    move_to((444.5, 464))
    ttle.begin_fill()
    bezier_curve_through(((0, 0), (-29, -36), (-31, -46)), relative=True)
    bezier_curve_Smooth_ver(((53.59, -82.337), (53.59, -82.337)), relative=True)
    ttle.pencolor("#D3DFF0")
    bezier_curve_Smooth_ver(((86.41, -47.663), (96.072, -54.85)), relative=True)
    bezier_curve_Smooth_ver(((563.5, 297.5), (570.5, 299.5), (518.5, 334)))
    ttle.pencolor("black")
    bezier_curve_through(((-2, 16), (-12, 33), (-12, 37)), relative=True)
    bezier_curve_Smooth_ver(((50, 92), (50, 93)), relative=True)
    horizontal_line_to_destination(444.5)
    ttle.end_fill()

    move_to((195, 49))
    ttle.begin_fill()
    ttle.pencolor("#D3DFF0")
    polyline(((195, 49), (175.5, 106.5), (202.522, 49)))
    ttle.pencolor("black")
    horizontal_line_to_destination(195)
    ttle.pencolor("#D3DFF0")
    ttle.end_fill()

    move_to((327.997, 49))
    ttle.begin_fill()
    ttle.pencolor("#D3DFF0")
    bezier_curve_through(
        ((0, 0), (11.503, 121.087), (13.503, 128.087)), relative=True)
    bezier_curve_through(((11, 2), (54, 37), (54, 37)), relative=True)
    displace_the_line((-40, - 165.087))
    ttle.pencolor("black")
    horizontal_line_to_destination(327.997)
    ttle.pencolor("#D3DFF0")
    ttle.end_fill()

    # Wrinkles
    ttle.pencolor("black")
    between_the_line((94.5, 397.5), (107.5, 373.5))
    between_the_line((122.5, 317.5), (95.875, 274.699))
    between_the_line((122.5, 341.5), (141.5, 402.5))
    between_the_line((141.5, 409.5), (153.5, 431.5))
    between_the_line((340.023, 49), (360.5, 144))
    between_the_line((478.5, 95.5), (518.5, 161.5))
    between_the_line((518.5, 332.5), (460.5, 359.5))
    polyline(((506.5, 369.5), (493.5, 402.5), (502.5, 443.5)))
    move_to((530, 429))
    bezier_curve_through(((4, 16), (-5, 33), (-5, 33)), relative=True)

    """
    Layer 2
    """

    # Inside of jacket
    ttle.color("black", "#3F0071")
    move_to((225, 462))
    ttle.begin_fill()
    horizontal_line_to_destination(165)
    bezier_curve_Smooth_ver(((9, -15), (8, -25)), relative=True)
    bezier_curve_through(((-47, -126), (6, -212), (12, -225)), relative=True)
    bezier_curve_Smooth_ver(((185, 305), (202, 428), (225, 462)))
    line_to((225, 462))
    ttle.end_fill()

    move_to((390, 462))
    ttle.begin_fill()
    bezier_curve_through(
        ((10, -23), (34, -180), (35, -222)), relative=True)
    bezier_curve_through(((7, 4), (54, 45), (61, 61)), relative=True)
    bezier_curve_Smooth_ver(((-73, 101), (-72, 118)), relative=True)
    bezier_curve_through(((5, 15), (31, 46), (31, 45)), relative=True)
    line_to((390, 462))
    ttle.end_fill()

    """
    Layer 3
    """

    # Inside of jacket
    ttle.color("black", "#3F0071")
    move_to((225, 462))
    ttle.begin_fill()
    bezier_curve_through(((-28, -50), (-40, -166), (-40, -250)), relative=True)
    bezier_curve_through(((6, 51), (-6, 87), (45, 106)), relative=True)
    bezier_curve_Smooth_ver(((64, 27), (89, 24)), relative=True)
    bezier_curve_Smooth_ver(((49, -18), (56, -20)), relative=True)
    bezier_curve_Smooth_ver(((50, -10), (51, -85)), relative=True)
    bezier_curve_through(((0, 29), (-25, 201), (-36, 225)), relative=True)
    line_to((225, 462))
    ttle.end_fill()

    """
    Layer 4
    """

    # Clothes
    ttle.color("black", "#7f92b3")
    move_to((225, 462))
    ttle.begin_fill()
    bezier_curve_through(((-5, -5), (-22, -53), (-23, -70)), relative=True)
    displace_the_line((32, -13))
    bezier_curve_through(((3, -25), (6, -28), (12, -36)), relative=True)
    bezier_curve_Smooth_ver(((13, -12), (16, -12)), relative=True)
    displace_the_line_vertical(-2)
    bezier_curve_through(((45, 20), (64, 14), (94, 1)), relative=True)
    displace_the_line_vertical(2)
    bezier_curve_through(((8, -2), (15, 2), (17, 4)), relative=True)
    bezier_curve_Smooth_ver(((0, 6), (-2, 9)), relative=True)
    bezier_curve_through(((10, 10), (10, 29), (11, 33)), relative=True)
    bezier_curve_Smooth_ver(((23, 4), (25, 6)), relative=True)
    bezier_curve_Smooth_ver(((-17, 83), (-17, 78)), relative=True)
    line_to((225, 462))
    ttle.end_fill()

    """
    Layer 5
    """

    # Neck
    ttle.color("black", "#f1d4d0")
    move_to((262, 329))
    ttle.begin_fill()
    displace_the_line_vertical(17)
    bezier_curve_through(((1, 2), (44, 14), (45, 15)), relative=True)
    bezier_curve_Smooth_ver(((3, 12), (3, 12)), relative=True)
    horizontal_displace(3)
    displace_the_line_vertical(-5)
    bezier_curve_through(((1, -3), (4, -6), (5, -7)), relative=True)
    displace_the_line((36, -14))
    bezier_curve_through(((1, -1), (3, -16), (2, -17)), relative=True)
    bezier_curve_Smooth_ver(((318, 348), (296, 344), (262, 329)))
    ttle.end_fill()


    """
    Layer 6
    """

    # Collar
    ttle.color("black", "#A2B8D6")
    move_to((262, 331))
    ttle.begin_fill()
    bezier_curve_through(((0, 8), (-1, 13), (0, 15)), relative=True)
    bezier_curve_Smooth_ver(((43, 14), (45, 15)), relative=True)
    displace_the_line((3, 12))
    horizontal_displace(3)
    bezier_curve_Smooth_ver(((-1, -3), (0, -5)), relative=True)
    displace_the_line((5, -7))
    displace_the_line((36, -14))
    bezier_curve_through(((1, -1), (2, -12), (2, -15)), relative=True)
    bezier_curve_Smooth_ver(((25, -2), (15, 13)), relative=True)
    bezier_curve_through(((-2, 4), (-7, 29), (-7, 32)), relative=True)
    bezier_curve_Smooth_ver(((-35, 19), (-41, 22)), relative=True)
    bezier_curve_Smooth_ver(((-9, 14), (-12, 14)), relative=True)
    bezier_curve_Smooth_ver(((-7, -12), (-14, -15)), relative=True)
    bezier_curve_through(((-19, -2), (-41, -25), (-41, -25)), relative=True)
    bezier_curve_Smooth_ver(((-10, -26), (-10, -30)), relative=True)
    bezier_curve_Smooth_ver(((255, 332), (262, 331)))
    ttle.end_fill()

    move_to((262, 346))
    displace_the_line((-12, -6))
    move_to((369, 333))
    bezier_curve_through(((2, 4), (-6, 10), (-15, 14)), relative=True)

    """
    Layer 7
    """

    # Face
    ttle.color("black", "#f1d4d0")
    move_to((185, 212))
    ttle.begin_fill()
    bezier_curve_through(((4, -9), (46, -77), (52, -75)), relative=True)
    bezier_curve_through(((-2, -17), (19, -68), (27, -73)), relative=True)
    bezier_curve_through(((16, 15), (71, 108), (76, 112)), relative=True)
    bezier_curve_Smooth_ver(((76, 53), (86, 60)), relative=True)
    bezier_curve_through(((0, 65), (-27, 75), (-31, 76)), relative=True)
    bezier_curve_through(((-50, 28), (-70, 30), (-85, 30)), relative=True)
    bezier_curve_Smooth_ver(((-77, -22), (-86, -26)), relative=True)
    bezier_curve_Smooth_ver(((180, 302), (186, 228), (185, 212)))
    ttle.end_fill()

    """
    Layer 8
    """

    # Hair
    ttle.color("black", "#d4d549")
    move_to((189, 202))
    ttle.begin_fill()
    bezier_curve_through(((-1, 22), (19, 51), (19, 51)), relative=True)
    bezier_curve_Smooth_ver(((-10, -42), (7, -92)), relative=True)
    bezier_curve_Smooth_ver(((212, 168), (196, 189), (189, 202)))
    ttle.end_fill()

    move_to((221, 155))
    ttle.begin_fill()
    bezier_curve_through(((-2, 6), (5, 48), (5, 48)), relative=True)
    bezier_curve_Smooth_ver(((18, -28), (20, -48)), relative=True)
    bezier_curve_through(((-5, 24), (4, 43), (7, 50)), relative=True)
    bezier_curve_through(((-10, -49), (3, -72), (13, -106)), relative=True)
    bezier_curve_through(((-2, -7), (-3, -32), (-3, -35)), relative=True)
    bezier_curve_through(((-17, 18), (-27, 71), (-27, 71)), relative=True)
    line_to((221, 155))
    ttle.end_fill()

    move_to((264, 64))
    ttle.begin_fill()
    bezier_curve_through(((-4, 5), (14, 100), (14, 100)), relative=True)
    bezier_curve_Smooth_ver(((-6, -79), (-5, -85)), relative=True)
    bezier_curve_through(((0, 98), (49, 139), (49, 139)), relative=True)
    bezier_curve_Smooth_ver(((8, -50), (3, -65)), relative=True)
    bezier_curve_Smooth_ver(((272, 64), (264, 64)))
    ttle.end_fill()

    move_to((342, 176))
    ttle.begin_fill()
    bezier_curve_through(((-1, 27), (-10, 57), (-10, 57)), relative=True)
    bezier_curve_Smooth_ver(((20, -33), (17, -54)), relative=True)
    line_to((342, 176))
    ttle.end_fill()

    ttle.penup()
    ttle.begin_fill()
    polyline(((349, 180), (353, 203), (361, 203)))
    polyline(((361, 203), (362, 188), (349, 180)))
    ttle.end_fill()

    """
    Layer 9
    """

    # Eyerbrows
    ttle.pensize(2)
    move_to((210, 180))
    bezier_curve_through(((5, -4), (63, 9), (63, 14)), relative=True)
    move_to((338, 193))
    bezier_curve_through(((0, -3), (18, -6), (18, -6)), relative=True)
    ttle.pensize(1)

    """
    Layer 10
    """

    # Eye 1
    ttle.color("black", "#D1D1D1")
    ttle.pensize(2)
    move_to((206, 212))
    ttle.begin_fill()
    displace_the_line((15, -7))
    bezier_curve_through(((4, -1), (26, -2), (30, 0)), relative=True)
    bezier_curve_Smooth_ver(((10, 3), (12, 7)), relative=True)
    ttle.pencolor("#D1D1D1")
    ttle.pensize(1)
    bezier_curve_Smooth_ver(((2, 27), (-1, 30)), relative=True)
    bezier_curve_Smooth_ver(((-39, 5), (-44, 1)), relative=True)
    bezier_curve_Smooth_ver(((206, 212), (206, 212)))
    ttle.end_fill()

    move_to((384, 204))
    ttle.begin_fill()
    ttle.pencolor("black")
    ttle.pensize(2)
    bezier_curve_through(((-3, -1), (-18, -1), (-28, 1)), relative=True)
    bezier_curve_Smooth_ver(((-9, 6), (-10, 9)), relative=True)
    ttle.pencolor("#D1D1D1")
    ttle.pensize(1)
    bezier_curve_Smooth_ver(((3, 18), (6, 23)), relative=True)
    bezier_curve_Smooth_ver(((38, 6), (40, 4)), relative=True)
    bezier_curve_Smooth_ver(((10, -9), (13, -22)), relative=True)
    ttle.pencolor("black")
    ttle.pensize(2)
    line_to((384, 204))
    ttle.end_fill()

    """
    Layer 11
    """

    # Eye 2
    ttle.color("#0C1631", "#0C1631")
    ttle.pensize(1)
    move_to((216, 206))
    ttle.begin_fill()
    bezier_curve_through(((-1, 5), (0, 26), (7, 35)), relative=True)
    bezier_curve_Smooth_ver(((30, 2), (33, 0)), relative=True)
    bezier_curve_Smooth_ver(((5, -31), (2, -34)), relative=True)
    bezier_curve_Smooth_ver(((219, 203), (216, 206)))
    ttle.end_fill()

    move_to((354, 207))
    ttle.begin_fill()
    bezier_curve_through(((-2, 1), (2, 29), (4, 31)), relative=True)
    bezier_curve_Smooth_ver(((30, 3), (33, 1)), relative=True)
    bezier_curve_Smooth_ver(((6, -24), (4, -27)), relative=True)
    displace_the_line((-11, -8))
    bezier_curve_Smooth_ver(((382, 204), (357, 206), (354, 207)))
    ttle.end_fill()


    # Eye line
    ttle.pencolor("black")
    ttle.pensize(3)
    move_to((225, 215))
    bezier_curve_through(((10, 28), (22, 16), (24, 6)), relative=True)
    move_to((365, 219))
    bezier_curve_through(((4, 14), (18, 24), (22, -3)), relative=True)
    ttle.pensize(2)
    between_the_line((240.5, 207.5), (227.5, 211.5))
    between_the_line((245.5, 209.5), (227.5, 214.5))
    between_the_line((247.5, 211.5), (227.5, 217.5))
    between_the_line((247.5, 214.5), (229.5, 220.5))
    between_the_line((247.5, 218.5), (230.5, 223.5))
    between_the_line((246.5, 222.5), (232.5, 226.5))
    between_the_line((244.5, 225.5), (234.5, 228.5))
    between_the_line((377.5, 207.5), (367.5, 210.5))
    between_the_line((384.5, 207.5), (366.5, 212.5))
    between_the_line((385.5, 210.5), (366.5, 215.5))
    between_the_line((384.5, 213.5), (366.5, 218.5))
    between_the_line((384.5, 215.5), (367.5, 220.5))
    between_the_line((384.5, 218.5), (368.5, 223.5))
    between_the_line((382.5, 223.5), (370.5, 227.5))

    """
    Layer 12
    """

    # Nose and mouth
    ttle.pencolor("black")
    move_to((309, 270))
    bezier_curve_through(((0, 0), (4, 7), (1, 9)), relative=True)
    between_the_line((296.5, 307.5), (303.5, 307.5))
    move_to((315, 307))
    bezier_curve_Smooth_ver(((10, -1), (10, 2)), relative=True)

    # Wait for the user to click to exit
    ttle.exitonclick()


if __name__ == '__main__':
    main()
