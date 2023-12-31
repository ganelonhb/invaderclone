"""A list of RGB colors produced by X11's showrgb command. The color database
    is probably from an IRIX system circa 2005"""

from pygame import Color


def _clamp(val: int, min_value=0, max_value=255) -> int:
    """Clamp a value between min and max."""
    return max(min_value, min(val, max_value))


def mult_color(scalar, color):
    """Multiply a color by a scalar"""
    return tuple(map(lambda n: _clamp(n * scalar), color))


def mult_colr(color_a, color_b):
    """Multiply a color by another color."""
    return (
        _clamp(color_a[0] * color_b[0]),
        _clamp(color_a[1] * color_b[1]),
        _clamp(color_a[2] * color_b[2]),
    )


def sum_color(color_a, color_b):
    """Sum two colors together."""
    return (
        _clamp(color_a[0] + color_b[0]),
        _clamp(color_a[1] + color_b[1]),
        _clamp(color_a[2] + color_b[2]),
    )


def diff_color(color_a, color_b):
    """Take the difference of two colors."""
    return (
        _clamp(color_a[0] - color_b[0]),
        _clamp(color_a[1] - color_b[1]),
        _clamp(color_a[2] - color_b[2]),
    )


def tuple_to_color(color_tuple):
    """return a Pygame color contructed from a tuple."""
    return Color(*color_tuple)


snow = (255, 250, 250)
ghost_white = (248, 248, 255)
ghostwhite = (248, 248, 255)
white_smoke = (245, 245, 245)
whitesmoke = (245, 245, 245)
gainsboro = (220, 220, 220)
floral_white = (255, 250, 240)
floralwhite = (255, 250, 240)
old_lace = (253, 245, 230)
oldlace = (253, 245, 230)
linen = (250, 240, 230)
antique_white = (250, 235, 215)
antiquewhite = (250, 235, 215)
papaya_whip = (255, 239, 213)
papayawhip = (255, 239, 213)
blanched_almond = (255, 235, 205)
blanchedalmond = (255, 235, 205)
bisque = (255, 228, 196)
peach_puff = (255, 218, 185)
peachpuff = (255, 218, 185)
navajo_white = (255, 222, 173)
navajowhite = (255, 222, 173)
moccasin = (255, 228, 181)
cornsilk = (255, 248, 220)
ivory = (255, 255, 240)
lemon_chiffon = (255, 250, 205)
lemonchiffon = (255, 250, 205)
seashell = (255, 245, 238)
honeydew = (240, 255, 240)
mint_cream = (245, 255, 250)
mintcream = (245, 255, 250)
azure = (240, 255, 255)
alice_blue = (240, 248, 255)
aliceblue = (240, 248, 255)
lavender = (230, 230, 250)
lavender_blush = (255, 240, 245)
lavenderblush = (255, 240, 245)
misty_rose = (255, 228, 225)
mistyrose = (255, 228, 225)
white = (255, 255, 255)
black = (0, 0, 0)
dark_slate_gray = (47, 79, 79)
darkslategray = (47, 79, 79)
dark_slate_grey = (47, 79, 79)
darkslategrey = (47, 79, 79)
dim_gray = (105, 105, 105)
dimgray = (105, 105, 105)
dim_grey = (105, 105, 105)
dimgrey = (105, 105, 105)
slate_gray = (112, 128, 144)
slategray = (112, 128, 144)
slate_grey = (112, 128, 144)
slategrey = (112, 128, 144)
light_slate_gray = (119, 136, 153)
lightslategray = (119, 136, 153)
light_slate_grey = (119, 136, 153)
lightslategrey = (119, 136, 153)
gray = (190, 190, 190)
grey = (190, 190, 190)
light_grey = (211, 211, 211)
lightgrey = (211, 211, 211)
light_gray = (211, 211, 211)
lightgray = (211, 211, 211)
midnight_blue = (25, 25, 112)
midnightblue = (25, 25, 112)
navy = (0, 0, 128)
navy_blue = (0, 0, 128)
navyblue = (0, 0, 128)
cornflower_blue = (100, 149, 237)
cornflowerblue = (100, 149, 237)
dark_slate_blue = (72, 61, 139)
darkslateblue = (72, 61, 139)
slate_blue = (106, 90, 205)
slateblue = (106, 90, 205)
medium_slate_blue = (123, 104, 238)
mediumslateblue = (123, 104, 238)
light_slate_blue = (132, 112, 255)
lightslateblue = (132, 112, 255)
medium_blue = (0, 0, 205)
mediumblue = (0, 0, 205)
royal_blue = (65, 105, 225)
royalblue = (65, 105, 225)
blue = (0, 0, 255)
dodger_blue = (30, 144, 255)
dodgerblue = (30, 144, 255)
deep_sky_blue = (0, 191, 255)
deepskyblue = (0, 191, 255)
sky_blue = (135, 206, 235)
skyblue = (135, 206, 235)
light_sky_blue = (135, 206, 250)
lightskyblue = (135, 206, 250)
steel_blue = (70, 130, 180)
steelblue = (70, 130, 180)
light_steel_blue = (176, 196, 222)
lightsteelblue = (176, 196, 222)
light_blue = (173, 216, 230)
lightblue = (173, 216, 230)
powder_blue = (176, 224, 230)
powderblue = (176, 224, 230)
pale_turquoise = (175, 238, 238)
paleturquoise = (175, 238, 238)
dark_turquoise = (0, 206, 209)
darkturquoise = (0, 206, 209)
medium_turquoise = (72, 209, 204)
mediumturquoise = (72, 209, 204)
turquoise = (64, 224, 208)
cyan = (0, 255, 255)
light_cyan = (224, 255, 255)
lightcyan = (224, 255, 255)
cadet_blue = (95, 158, 160)
cadetblue = (95, 158, 160)
medium_aquamarine = (102, 205, 170)
mediumaquamarine = (102, 205, 170)
aquamarine = (127, 255, 212)
dark_green = (0, 100, 0)
darkgreen = (0, 100, 0)
dark_olive_green = (85, 107, 47)
darkolivegreen = (85, 107, 47)
dark_sea_green = (143, 188, 143)
darkseagreen = (143, 188, 143)
sea_green = (46, 139, 87)
seagreen = (46, 139, 87)
medium_sea_green = (60, 179, 113)
mediumseagreen = (60, 179, 113)
light_sea_green = (32, 178, 170)
lightseagreen = (32, 178, 170)
pale_green = (152, 251, 152)
palegreen = (152, 251, 152)
spring_green = (0, 255, 127)
springgreen = (0, 255, 127)
lawn_green = (124, 252, 0)
lawngreen = (124, 252, 0)
green = (0, 255, 0)
chartreuse = (127, 255, 0)
medium_spring_green = (0, 250, 154)
mediumspringgreen = (0, 250, 154)
green_yellow = (173, 255, 47)
greenyellow = (173, 255, 47)
lime_green = (50, 205, 50)
limegreen = (50, 205, 50)
yellow_green = (154, 205, 50)
yellowgreen = (154, 205, 50)
forest_green = (34, 139, 34)
forestgreen = (34, 139, 34)
olive_drab = (107, 142, 35)
olivedrab = (107, 142, 35)
dark_khaki = (189, 183, 107)
darkkhaki = (189, 183, 107)
khaki = (240, 230, 140)
pale_goldenrod = (238, 232, 170)
palegoldenrod = (238, 232, 170)
light_goldenrod_yellow = (250, 250, 210)
lightgoldenrodyellow = (250, 250, 210)
light_yellow = (255, 255, 224)
lightyellow = (255, 255, 224)
yellow = (255, 255, 0)
gold = (255, 215, 0)
light_goldenrod = (238, 221, 130)
lightgoldenrod = (238, 221, 130)
goldenrod = (218, 165, 32)
dark_goldenrod = (184, 134, 11)
darkgoldenrod = (184, 134, 11)
rosy_brown = (188, 143, 143)
rosybrown = (188, 143, 143)
indian_red = (205, 92, 92)
indianred = (205, 92, 92)
saddle_brown = (139, 69, 19)
saddlebrown = (139, 69, 19)
sienna = (160, 82, 45)
peru = (205, 133, 63)
burlywood = (222, 184, 135)
beige = (245, 245, 220)
wheat = (245, 222, 179)
sandy_brown = (244, 164, 96)
sandybrown = (244, 164, 96)
tan = (210, 180, 140)
chocolate = (210, 105, 30)
firebrick = (178, 34, 34)
brown = (165, 42, 42)
dark_salmon = (233, 150, 122)
darksalmon = (233, 150, 122)
salmon = (250, 128, 114)
light_salmon = (255, 160, 122)
lightsalmon = (255, 160, 122)
orange = (255, 165, 0)
dark_orange = (255, 140, 0)
darkorange = (255, 140, 0)
coral = (255, 127, 80)
light_coral = (240, 128, 128)
lightcoral = (240, 128, 128)
tomato = (255, 99, 71)
orange_red = (255, 69, 0)
orangered = (255, 69, 0)
red = (255, 0, 0)
hot_pink = (255, 105, 180)
hotpink = (255, 105, 180)
deep_pink = (255, 20, 147)
deeppink = (255, 20, 147)
pink = (255, 192, 203)
light_pink = (255, 182, 193)
lightpink = (255, 182, 193)
pale_violet_red = (219, 112, 147)
palevioletred = (219, 112, 147)
maroon = (176, 48, 96)
medium_violet_red = (199, 21, 133)
mediumvioletred = (199, 21, 133)
violet_red = (208, 32, 144)
violetred = (208, 32, 144)
magenta = (255, 0, 255)
violet = (238, 130, 238)
plum = (221, 160, 221)
orchid = (218, 112, 214)
medium_orchid = (186, 85, 211)
mediumorchid = (186, 85, 211)
dark_orchid = (153, 50, 204)
darkorchid = (153, 50, 204)
dark_violet = (148, 0, 211)
darkviolet = (148, 0, 211)
blue_violet = (138, 43, 226)
blueviolet = (138, 43, 226)
purple = (160, 32, 240)
medium_purple = (147, 112, 219)
mediumpurple = (147, 112, 219)
thistle = (216, 191, 216)
snow1 = (255, 250, 250)
snow2 = (238, 233, 233)
snow3 = (205, 201, 201)
snow4 = (139, 137, 137)
seashell1 = (255, 245, 238)
seashell2 = (238, 229, 222)
seashell3 = (205, 197, 191)
seashell4 = (139, 134, 130)
antiquewhite1 = (255, 239, 219)
antiquewhite2 = (238, 223, 204)
antiquewhite3 = (205, 192, 176)
antiquewhite4 = (139, 131, 120)
bisque1 = (255, 228, 196)
bisque2 = (238, 213, 183)
bisque3 = (205, 183, 158)
bisque4 = (139, 125, 107)
peachpuff1 = (255, 218, 185)
peachpuff2 = (238, 203, 173)
peachpuff3 = (205, 175, 149)
peachpuff4 = (139, 119, 101)
navajowhite1 = (255, 222, 173)
navajowhite2 = (238, 207, 161)
navajowhite3 = (205, 179, 139)
navajowhite4 = (139, 121, 94)
lemonchiffon1 = (255, 250, 205)
lemonchiffon2 = (238, 233, 191)
lemonchiffon3 = (205, 201, 165)
lemonchiffon4 = (139, 137, 112)
cornsilk1 = (255, 248, 220)
cornsilk2 = (238, 232, 205)
cornsilk3 = (205, 200, 177)
cornsilk4 = (139, 136, 120)
ivory1 = (255, 255, 240)
ivory2 = (238, 238, 224)
ivory3 = (205, 205, 193)
ivory4 = (139, 139, 131)
honeydew1 = (240, 255, 240)
honeydew2 = (224, 238, 224)
honeydew3 = (193, 205, 193)
honeydew4 = (131, 139, 131)
lavenderblush1 = (255, 240, 245)
lavenderblush2 = (238, 224, 229)
lavenderblush3 = (205, 193, 197)
lavenderblush4 = (139, 131, 134)
mistyrose1 = (255, 228, 225)
mistyrose2 = (238, 213, 210)
mistyrose3 = (205, 183, 181)
mistyrose4 = (139, 125, 123)
azure1 = (240, 255, 255)
azure2 = (224, 238, 238)
azure3 = (193, 205, 205)
azure4 = (131, 139, 139)
slateblue1 = (131, 111, 255)
slateblue2 = (122, 103, 238)
slateblue3 = (105, 89, 205)
slateblue4 = (71, 60, 139)
royalblue1 = (72, 118, 255)
royalblue2 = (67, 110, 238)
royalblue3 = (58, 95, 205)
royalblue4 = (39, 64, 139)
blue1 = (0, 0, 255)
blue2 = (0, 0, 238)
blue3 = (0, 0, 205)
blue4 = (0, 0, 139)
dodgerblue1 = (30, 144, 255)
dodgerblue2 = (28, 134, 238)
dodgerblue3 = (24, 116, 205)
dodgerblue4 = (16, 78, 139)
steelblue1 = (99, 184, 255)
steelblue2 = (92, 172, 238)
steelblue3 = (79, 148, 205)
steelblue4 = (54, 100, 139)
deepskyblue1 = (0, 191, 255)
deepskyblue2 = (0, 178, 238)
deepskyblue3 = (0, 154, 205)
deepskyblue4 = (0, 104, 139)
skyblue1 = (135, 206, 255)
skyblue2 = (126, 192, 238)
skyblue3 = (108, 166, 205)
skyblue4 = (74, 112, 139)
lightskyblue1 = (176, 226, 255)
lightskyblue2 = (164, 211, 238)
lightskyblue3 = (141, 182, 205)
lightskyblue4 = (96, 123, 139)
slategray1 = (198, 226, 255)
slategray2 = (185, 211, 238)
slategray3 = (159, 182, 205)
slategray4 = (108, 123, 139)
lightsteelblue1 = (202, 225, 255)
lightsteelblue2 = (188, 210, 238)
lightsteelblue3 = (162, 181, 205)
lightsteelblue4 = (110, 123, 139)
lightblue1 = (191, 239, 255)
lightblue2 = (178, 223, 238)
lightblue3 = (154, 192, 205)
lightblue4 = (104, 131, 139)
lightcyan1 = (224, 255, 255)
lightcyan2 = (209, 238, 238)
lightcyan3 = (180, 205, 205)
lightcyan4 = (122, 139, 139)
paleturquoise1 = (187, 255, 255)
paleturquoise2 = (174, 238, 238)
paleturquoise3 = (150, 205, 205)
paleturquoise4 = (102, 139, 139)
cadetblue1 = (152, 245, 255)
cadetblue2 = (142, 229, 238)
cadetblue3 = (122, 197, 205)
cadetblue4 = (83, 134, 139)
turquoise1 = (0, 245, 255)
turquoise2 = (0, 229, 238)
turquoise3 = (0, 197, 205)
turquoise4 = (0, 134, 139)
cyan1 = (0, 255, 255)
cyan2 = (0, 238, 238)
cyan3 = (0, 205, 205)
cyan4 = (0, 139, 139)
darkslategray1 = (151, 255, 255)
darkslategray2 = (141, 238, 238)
darkslategray3 = (121, 205, 205)
darkslategray4 = (82, 139, 139)
aquamarine1 = (127, 255, 212)
aquamarine2 = (118, 238, 198)
aquamarine3 = (102, 205, 170)
aquamarine4 = (69, 139, 116)
darkseagreen1 = (193, 255, 193)
darkseagreen2 = (180, 238, 180)
darkseagreen3 = (155, 205, 155)
darkseagreen4 = (105, 139, 105)
seagreen1 = (84, 255, 159)
seagreen2 = (78, 238, 148)
seagreen3 = (67, 205, 128)
seagreen4 = (46, 139, 87)
palegreen1 = (154, 255, 154)
palegreen2 = (144, 238, 144)
palegreen3 = (124, 205, 124)
palegreen4 = (84, 139, 84)
springgreen1 = (0, 255, 127)
springgreen2 = (0, 238, 118)
springgreen3 = (0, 205, 102)
springgreen4 = (0, 139, 69)
green1 = (0, 255, 0)
green2 = (0, 238, 0)
green3 = (0, 205, 0)
green4 = (0, 139, 0)
chartreuse1 = (127, 255, 0)
chartreuse2 = (118, 238, 0)
chartreuse3 = (102, 205, 0)
chartreuse4 = (69, 139, 0)
olivedrab1 = (192, 255, 62)
olivedrab2 = (179, 238, 58)
olivedrab3 = (154, 205, 50)
olivedrab4 = (105, 139, 34)
darkolivegreen1 = (202, 255, 112)
darkolivegreen2 = (188, 238, 104)
darkolivegreen3 = (162, 205, 90)
darkolivegreen4 = (110, 139, 61)
khaki1 = (255, 246, 143)
khaki2 = (238, 230, 133)
khaki3 = (205, 198, 115)
khaki4 = (139, 134, 78)
lightgoldenrod1 = (255, 236, 139)
lightgoldenrod2 = (238, 220, 130)
lightgoldenrod3 = (205, 190, 112)
lightgoldenrod4 = (139, 129, 76)
lightyellow1 = (255, 255, 224)
lightyellow2 = (238, 238, 209)
lightyellow3 = (205, 205, 180)
lightyellow4 = (139, 139, 122)
yellow1 = (255, 255, 0)
yellow2 = (238, 238, 0)
yellow3 = (205, 205, 0)
yellow4 = (139, 139, 0)
gold1 = (255, 215, 0)
gold2 = (238, 201, 0)
gold3 = (205, 173, 0)
gold4 = (139, 117, 0)
goldenrod1 = (255, 193, 37)
goldenrod2 = (238, 180, 34)
goldenrod3 = (205, 155, 29)
goldenrod4 = (139, 105, 20)
darkgoldenrod1 = (255, 185, 15)
darkgoldenrod2 = (238, 173, 14)
darkgoldenrod3 = (205, 149, 12)
darkgoldenrod4 = (139, 101, 8)
rosybrown1 = (255, 193, 193)
rosybrown2 = (238, 180, 180)
rosybrown3 = (205, 155, 155)
rosybrown4 = (139, 105, 105)
indianred1 = (255, 106, 106)
indianred2 = (238, 99, 99)
indianred3 = (205, 85, 85)
indianred4 = (139, 58, 58)
sienna1 = (255, 130, 71)
sienna2 = (238, 121, 66)
sienna3 = (205, 104, 57)
sienna4 = (139, 71, 38)
burlywood1 = (255, 211, 155)
burlywood2 = (238, 197, 145)
burlywood3 = (205, 170, 125)
burlywood4 = (139, 115, 85)
wheat1 = (255, 231, 186)
wheat2 = (238, 216, 174)
wheat3 = (205, 186, 150)
wheat4 = (139, 126, 102)
tan1 = (255, 165, 79)
tan2 = (238, 154, 73)
tan3 = (205, 133, 63)
tan4 = (139, 90, 43)
chocolate1 = (255, 127, 36)
chocolate2 = (238, 118, 33)
chocolate3 = (205, 102, 29)
chocolate4 = (139, 69, 19)
firebrick1 = (255, 48, 48)
firebrick2 = (238, 44, 44)
firebrick3 = (205, 38, 38)
firebrick4 = (139, 26, 26)
brown1 = (255, 64, 64)
brown2 = (238, 59, 59)
brown3 = (205, 51, 51)
brown4 = (139, 35, 35)
salmon1 = (255, 140, 105)
salmon2 = (238, 130, 98)
salmon3 = (205, 112, 84)
salmon4 = (139, 76, 57)
lightsalmon1 = (255, 160, 122)
lightsalmon2 = (238, 149, 114)
lightsalmon3 = (205, 129, 98)
lightsalmon4 = (139, 87, 66)
orange1 = (255, 165, 0)
orange2 = (238, 154, 0)
orange3 = (205, 133, 0)
orange4 = (139, 90, 0)
darkorange1 = (255, 127, 0)
darkorange2 = (238, 118, 0)
darkorange3 = (205, 102, 0)
darkorange4 = (139, 69, 0)
coral1 = (255, 114, 86)
coral2 = (238, 106, 80)
coral3 = (205, 91, 69)
coral4 = (139, 62, 47)
tomato1 = (255, 99, 71)
tomato2 = (238, 92, 66)
tomato3 = (205, 79, 57)
tomato4 = (139, 54, 38)
orangered1 = (255, 69, 0)
orangered2 = (238, 64, 0)
orangered3 = (205, 55, 0)
orangered4 = (139, 37, 0)
red1 = (255, 0, 0)
red2 = (238, 0, 0)
red3 = (205, 0, 0)
red4 = (139, 0, 0)
debianred = (215, 7, 81)
deeppink1 = (255, 20, 147)
deeppink2 = (238, 18, 137)
deeppink3 = (205, 16, 118)
deeppink4 = (139, 10, 80)
hotpink1 = (255, 110, 180)
hotpink2 = (238, 106, 167)
hotpink3 = (205, 96, 144)
hotpink4 = (139, 58, 98)
pink1 = (255, 181, 197)
pink2 = (238, 169, 184)
pink3 = (205, 145, 158)
pink4 = (139, 99, 108)
lightpink1 = (255, 174, 185)
lightpink2 = (238, 162, 173)
lightpink3 = (205, 140, 149)
lightpink4 = (139, 95, 101)
palevioletred1 = (255, 130, 171)
palevioletred2 = (238, 121, 159)
palevioletred3 = (205, 104, 137)
palevioletred4 = (139, 71, 93)
maroon1 = (255, 52, 179)
maroon2 = (238, 48, 167)
maroon3 = (205, 41, 144)
maroon4 = (139, 28, 98)
violetred1 = (255, 62, 150)
violetred2 = (238, 58, 140)
violetred3 = (205, 50, 120)
violetred4 = (139, 34, 82)
magenta1 = (255, 0, 255)
magenta2 = (238, 0, 238)
magenta3 = (205, 0, 205)
magenta4 = (139, 0, 139)
orchid1 = (255, 131, 250)
orchid2 = (238, 122, 233)
orchid3 = (205, 105, 201)
orchid4 = (139, 71, 137)
plum1 = (255, 187, 255)
plum2 = (238, 174, 238)
plum3 = (205, 150, 205)
plum4 = (139, 102, 139)
mediumorchid1 = (224, 102, 255)
mediumorchid2 = (209, 95, 238)
mediumorchid3 = (180, 82, 205)
mediumorchid4 = (122, 55, 139)
darkorchid1 = (191, 62, 255)
darkorchid2 = (178, 58, 238)
darkorchid3 = (154, 50, 205)
darkorchid4 = (104, 34, 139)
purple1 = (155, 48, 255)
purple2 = (145, 44, 238)
purple3 = (125, 38, 205)
purple4 = (85, 26, 139)
mediumpurple1 = (171, 130, 255)
mediumpurple2 = (159, 121, 238)
mediumpurple3 = (137, 104, 205)
mediumpurple4 = (93, 71, 139)
thistle1 = (255, 225, 255)
thistle2 = (238, 210, 238)
thistle3 = (205, 181, 205)
thistle4 = (139, 123, 139)
gray0 = (0, 0, 0)
grey0 = (0, 0, 0)
gray1 = (3, 3, 3)
grey1 = (3, 3, 3)
gray2 = (5, 5, 5)
grey2 = (5, 5, 5)
gray3 = (8, 8, 8)
grey3 = (8, 8, 8)
gray4 = (10, 10, 10)
grey4 = (10, 10, 10)
gray5 = (13, 13, 13)
grey5 = (13, 13, 13)
gray6 = (15, 15, 15)
grey6 = (15, 15, 15)
gray7 = (18, 18, 18)
grey7 = (18, 18, 18)
gray8 = (20, 20, 20)
grey8 = (20, 20, 20)
gray9 = (23, 23, 23)
grey9 = (23, 23, 23)
gray10 = (26, 26, 26)
grey10 = (26, 26, 26)
gray11 = (28, 28, 28)
grey11 = (28, 28, 28)
gray12 = (31, 31, 31)
grey12 = (31, 31, 31)
gray13 = (33, 33, 33)
grey13 = (33, 33, 33)
gray14 = (36, 36, 36)
grey14 = (36, 36, 36)
gray15 = (38, 38, 38)
grey15 = (38, 38, 38)
gray16 = (41, 41, 41)
grey16 = (41, 41, 41)
gray17 = (43, 43, 43)
grey17 = (43, 43, 43)
gray18 = (46, 46, 46)
grey18 = (46, 46, 46)
gray19 = (48, 48, 48)
grey19 = (48, 48, 48)
gray20 = (51, 51, 51)
grey20 = (51, 51, 51)
gray21 = (54, 54, 54)
grey21 = (54, 54, 54)
gray22 = (56, 56, 56)
grey22 = (56, 56, 56)
gray23 = (59, 59, 59)
grey23 = (59, 59, 59)
gray24 = (61, 61, 61)
grey24 = (61, 61, 61)
gray25 = (64, 64, 64)
grey25 = (64, 64, 64)
gray26 = (66, 66, 66)
grey26 = (66, 66, 66)
gray27 = (69, 69, 69)
grey27 = (69, 69, 69)
gray28 = (71, 71, 71)
grey28 = (71, 71, 71)
gray29 = (74, 74, 74)
grey29 = (74, 74, 74)
gray30 = (77, 77, 77)
grey30 = (77, 77, 77)
gray31 = (79, 79, 79)
grey31 = (79, 79, 79)
gray32 = (82, 82, 82)
grey32 = (82, 82, 82)
gray33 = (84, 84, 84)
grey33 = (84, 84, 84)
gray34 = (87, 87, 87)
grey34 = (87, 87, 87)
gray35 = (89, 89, 89)
grey35 = (89, 89, 89)
gray36 = (92, 92, 92)
grey36 = (92, 92, 92)
gray37 = (94, 94, 94)
grey37 = (94, 94, 94)
gray38 = (97, 97, 97)
grey38 = (97, 97, 97)
gray39 = (99, 99, 99)
grey39 = (99, 99, 99)
gray40 = (102, 102, 102)
grey40 = (102, 102, 102)
gray41 = (105, 105, 105)
grey41 = (105, 105, 105)
gray42 = (107, 107, 107)
grey42 = (107, 107, 107)
gray43 = (110, 110, 110)
grey43 = (110, 110, 110)
gray44 = (112, 112, 112)
grey44 = (112, 112, 112)
gray45 = (115, 115, 115)
grey45 = (115, 115, 115)
gray46 = (117, 117, 117)
grey46 = (117, 117, 117)
gray47 = (120, 120, 120)
grey47 = (120, 120, 120)
gray48 = (122, 122, 122)
grey48 = (122, 122, 122)
gray49 = (125, 125, 125)
grey49 = (125, 125, 125)
gray50 = (127, 127, 127)
grey50 = (127, 127, 127)
gray51 = (130, 130, 130)
grey51 = (130, 130, 130)
gray52 = (133, 133, 133)
grey52 = (133, 133, 133)
gray53 = (135, 135, 135)
grey53 = (135, 135, 135)
gray54 = (138, 138, 138)
grey54 = (138, 138, 138)
gray55 = (140, 140, 140)
grey55 = (140, 140, 140)
gray56 = (143, 143, 143)
grey56 = (143, 143, 143)
gray57 = (145, 145, 145)
grey57 = (145, 145, 145)
gray58 = (148, 148, 148)
grey58 = (148, 148, 148)
gray59 = (150, 150, 150)
grey59 = (150, 150, 150)
gray60 = (153, 153, 153)
grey60 = (153, 153, 153)
gray61 = (156, 156, 156)
grey61 = (156, 156, 156)
gray62 = (158, 158, 158)
grey62 = (158, 158, 158)
gray63 = (161, 161, 161)
grey63 = (161, 161, 161)
gray64 = (163, 163, 163)
grey64 = (163, 163, 163)
gray65 = (166, 166, 166)
grey65 = (166, 166, 166)
gray66 = (168, 168, 168)
grey66 = (168, 168, 168)
gray67 = (171, 171, 171)
grey67 = (171, 171, 171)
gray68 = (173, 173, 173)
grey68 = (173, 173, 173)
gray69 = (176, 176, 176)
grey69 = (176, 176, 176)
gray70 = (179, 179, 179)
grey70 = (179, 179, 179)
gray71 = (181, 181, 181)
grey71 = (181, 181, 181)
gray72 = (184, 184, 184)
grey72 = (184, 184, 184)
gray73 = (186, 186, 186)
grey73 = (186, 186, 186)
gray74 = (189, 189, 189)
grey74 = (189, 189, 189)
gray75 = (191, 191, 191)
grey75 = (191, 191, 191)
gray76 = (194, 194, 194)
grey76 = (194, 194, 194)
gray77 = (196, 196, 196)
grey77 = (196, 196, 196)
gray78 = (199, 199, 199)
grey78 = (199, 199, 199)
gray79 = (201, 201, 201)
grey79 = (201, 201, 201)
gray80 = (204, 204, 204)
grey80 = (204, 204, 204)
gray81 = (207, 207, 207)
grey81 = (207, 207, 207)
gray82 = (209, 209, 209)
grey82 = (209, 209, 209)
gray83 = (212, 212, 212)
grey83 = (212, 212, 212)
gray84 = (214, 214, 214)
grey84 = (214, 214, 214)
gray85 = (217, 217, 217)
grey85 = (217, 217, 217)
gray86 = (219, 219, 219)
grey86 = (219, 219, 219)
gray87 = (222, 222, 222)
grey87 = (222, 222, 222)
gray88 = (224, 224, 224)
grey88 = (224, 224, 224)
gray89 = (227, 227, 227)
grey89 = (227, 227, 227)
gray90 = (229, 229, 229)
grey90 = (229, 229, 229)
gray91 = (232, 232, 232)
grey91 = (232, 232, 232)
gray92 = (235, 235, 235)
grey92 = (235, 235, 235)
gray93 = (237, 237, 237)
grey93 = (237, 237, 237)
gray94 = (240, 240, 240)
grey94 = (240, 240, 240)
gray95 = (242, 242, 242)
grey95 = (242, 242, 242)
gray96 = (245, 245, 245)
grey96 = (245, 245, 245)
gray97 = (247, 247, 247)
grey97 = (247, 247, 247)
gray98 = (250, 250, 250)
grey98 = (250, 250, 250)
gray99 = (252, 252, 252)
grey99 = (252, 252, 252)
gray100 = (255, 255, 255)
grey100 = (255, 255, 255)
dark_grey = (169, 169, 169)
darkgrey = (169, 169, 169)
dark_gray = (169, 169, 169)
darkgray = (169, 169, 169)
dark_blue = (0, 0, 139)
darkblue = (0, 0, 139)
dark_cyan = (0, 139, 139)
darkcyan = (0, 139, 139)
dark_magenta = (139, 0, 139)
darkmagenta = (139, 0, 139)
dark_red = (139, 0, 0)
darkred = (139, 0, 0)
light_green = (144, 238, 144)
lightgreen = (144, 238, 144)

color_dictionary = {
    "snow" : snow,
	"ghost_white" : ghost_white,
	"ghostwhite" : ghostwhite,
	"white_smoke" : white_smoke,
	"whitesmoke" : whitesmoke,
	"gainsboro" : gainsboro,
	"floral_white" : floral_white,
	"floralwhite" : floralwhite,
	"old_lace" : old_lace,
	"oldlace" : oldlace,
	"linen" : linen,
	"antique_white" : antique_white,
	"antiquewhite" : antiquewhite,
	"papaya_whip" : papaya_whip,
	"papayawhip" : papayawhip,
	"blanched_almond" : blanched_almond,
	"blanchedalmond" : blanchedalmond,
	"bisque" : bisque,
	"peach_puff" : peach_puff,
	"peachpuff" : peachpuff,
	"navajo_white" : navajo_white,
	"navajowhite" : navajowhite,
	"moccasin" : moccasin,
	"cornsilk" : cornsilk,
	"ivory" : ivory,
	"lemon_chiffon" : lemon_chiffon,
	"lemonchiffon" : lemonchiffon,
	"seashell" : seashell,
	"honeydew" : honeydew,
	"mint_cream" : mint_cream,
	"mintcream" : mintcream,
	"azure" : azure,
	"alice_blue" : alice_blue,
	"aliceblue" : aliceblue,
	"lavender" : lavender,
	"lavender_blush" : lavender_blush,
	"lavenderblush" : lavenderblush,
	"misty_rose" : misty_rose,
	"mistyrose" : mistyrose,
	"white" : white,
	"black" : black,
	"dark_slate_gray" : dark_slate_gray,
	"darkslategray" : darkslategray,
	"dark_slate_grey" : dark_slate_grey,
	"darkslategrey" : darkslategrey,
	"dim_gray" : dim_gray,
	"dimgray" : dimgray,
	"dim_grey" : dim_grey,
	"dimgrey" : dimgrey,
	"slate_gray" : slate_gray,
	"slategray" : slategray,
	"slate_grey" : slate_grey,
	"slategrey" : slategrey,
	"light_slate_gray" : light_slate_gray,
	"lightslategray" : lightslategray,
	"light_slate_grey" : light_slate_grey,
	"lightslategrey" : lightslategrey,
	"gray" : gray,
	"grey" : grey,
	"light_grey" : light_grey,
	"lightgrey" : lightgrey,
	"light_gray" : light_gray,
	"lightgray" : lightgray,
	"midnight_blue" : midnight_blue,
	"midnightblue" : midnightblue,
	"navy" : navy,
	"navy_blue" : navy_blue,
	"navyblue" : navyblue,
	"cornflower_blue" : cornflower_blue,
	"cornflowerblue" : cornflowerblue,
	"dark_slate_blue" : dark_slate_blue,
	"darkslateblue" : darkslateblue,
	"slate_blue" : slate_blue,
	"slateblue" : slateblue,
	"medium_slate_blue" : medium_slate_blue,
	"mediumslateblue" : mediumslateblue,
	"light_slate_blue" : light_slate_blue,
	"lightslateblue" : lightslateblue,
	"medium_blue" : medium_blue,
	"mediumblue" : mediumblue,
	"royal_blue" : royal_blue,
	"royalblue" : royalblue,
	"blue" : blue,
	"dodger_blue" : dodger_blue,
	"dodgerblue" : dodgerblue,
	"deep_sky_blue" : deep_sky_blue,
	"deepskyblue" : deepskyblue,
	"sky_blue" : sky_blue,
	"skyblue" : skyblue,
	"light_sky_blue" : light_sky_blue,
	"lightskyblue" : lightskyblue,
	"steel_blue" : steel_blue,
	"steelblue" : steelblue,
	"light_steel_blue" : light_steel_blue,
	"lightsteelblue" : lightsteelblue,
	"light_blue" : light_blue,
	"lightblue" : lightblue,
	"powder_blue" : powder_blue,
	"powderblue" : powderblue,
	"pale_turquoise" : pale_turquoise,
	"paleturquoise" : paleturquoise,
	"dark_turquoise" : dark_turquoise,
	"darkturquoise" : darkturquoise,
	"medium_turquoise" : medium_turquoise,
	"mediumturquoise" : mediumturquoise,
	"turquoise" : turquoise,
	"cyan" : cyan,
	"light_cyan" : light_cyan,
	"lightcyan" : lightcyan,
	"cadet_blue" : cadet_blue,
	"cadetblue" : cadetblue,
	"medium_aquamarine" : medium_aquamarine,
	"mediumaquamarine" : mediumaquamarine,
	"aquamarine" : aquamarine,
	"dark_green" : dark_green,
	"darkgreen" : darkgreen,
	"dark_olive_green" : dark_olive_green,
	"darkolivegreen" : darkolivegreen,
	"dark_sea_green" : dark_sea_green,
	"darkseagreen" : darkseagreen,
	"sea_green" : sea_green,
	"seagreen" : seagreen,
	"medium_sea_green" : medium_sea_green,
	"mediumseagreen" : mediumseagreen,
	"light_sea_green" : light_sea_green,
	"lightseagreen" : lightseagreen,
	"pale_green" : pale_green,
	"palegreen" : palegreen,
	"spring_green" : spring_green,
	"springgreen" : springgreen,
	"lawn_green" : lawn_green,
	"lawngreen" : lawngreen,
	"green" : green,
	"chartreuse" : chartreuse,
	"medium_spring_green" : medium_spring_green,
	"mediumspringgreen" : mediumspringgreen,
	"green_yellow" : green_yellow,
	"greenyellow" : greenyellow,
	"lime_green" : lime_green,
	"limegreen" : limegreen,
	"yellow_green" : yellow_green,
	"yellowgreen" : yellowgreen,
	"forest_green" : forest_green,
	"forestgreen" : forestgreen,
	"olive_drab" : olive_drab,
	"olivedrab" : olivedrab,
	"dark_khaki" : dark_khaki,
	"darkkhaki" : darkkhaki,
	"khaki" : khaki,
	"pale_goldenrod" : pale_goldenrod,
	"palegoldenrod" : palegoldenrod,
	"light_goldenrod_yellow" : light_goldenrod_yellow,
	"lightgoldenrodyellow" : lightgoldenrodyellow,
	"light_yellow" : light_yellow,
	"lightyellow" : lightyellow,
	"yellow" : yellow,
	"gold" : gold,
	"light_goldenrod" : light_goldenrod,
	"lightgoldenrod" : lightgoldenrod,
	"goldenrod" : goldenrod,
	"dark_goldenrod" : dark_goldenrod,
	"darkgoldenrod" : darkgoldenrod,
	"rosy_brown" : rosy_brown,
	"rosybrown" : rosybrown,
	"indian_red" : indian_red,
	"indianred" : indianred,
	"saddle_brown" : saddle_brown,
	"saddlebrown" : saddlebrown,
	"sienna" : sienna,
	"peru" : peru,
	"burlywood" : burlywood,
	"beige" : beige,
	"wheat" : wheat,
	"sandy_brown" : sandy_brown,
	"sandybrown" : sandybrown,
	"tan" : tan,
	"chocolate" : chocolate,
	"firebrick" : firebrick,
	"brown" : brown,
	"dark_salmon" : dark_salmon,
	"darksalmon" : darksalmon,
	"salmon" : salmon,
	"light_salmon" : light_salmon,
	"lightsalmon" : lightsalmon,
	"orange" : orange,
	"dark_orange" : dark_orange,
	"darkorange" : darkorange,
	"coral" : coral,
	"light_coral" : light_coral,
	"lightcoral" : lightcoral,
	"tomato" : tomato,
	"orange_red" : orange_red,
	"orangered" : orangered,
	"red" : red,
	"hot_pink" : hot_pink,
	"hotpink" : hotpink,
	"deep_pink" : deep_pink,
	"deeppink" : deeppink,
	"pink" : pink,
	"light_pink" : light_pink,
	"lightpink" : lightpink,
	"pale_violet_red" : pale_violet_red,
	"palevioletred" : palevioletred,
	"maroon" : maroon,
	"medium_violet_red" : medium_violet_red,
	"mediumvioletred" : mediumvioletred,
	"violet_red" : violet_red,
	"violetred" : violetred,
	"magenta" : magenta,
	"violet" : violet,
	"plum" : plum,
	"orchid" : orchid,
	"medium_orchid" : medium_orchid,
	"mediumorchid" : mediumorchid,
	"dark_orchid" : dark_orchid,
	"darkorchid" : darkorchid,
	"dark_violet" : dark_violet,
	"darkviolet" : darkviolet,
	"blue_violet" : blue_violet,
	"blueviolet" : blueviolet,
	"purple" : purple,
	"medium_purple" : medium_purple,
	"mediumpurple" : mediumpurple,
	"thistle" : thistle,
	"snow1" : snow1,
	"snow2" : snow2,
	"snow3" : snow3,
	"snow4" : snow4,
	"seashell1" : seashell1,
	"seashell2" : seashell2,
	"seashell3" : seashell3,
	"seashell4" : seashell4,
	"antiquewhite1" : antiquewhite1,
	"antiquewhite2" : antiquewhite2,
	"antiquewhite3" : antiquewhite3,
	"antiquewhite4" : antiquewhite4,
	"bisque1" : bisque1,
	"bisque2" : bisque2,
	"bisque3" : bisque3,
	"bisque4" : bisque4,
	"peachpuff1" : peachpuff1,
	"peachpuff2" : peachpuff2,
	"peachpuff3" : peachpuff3,
	"peachpuff4" : peachpuff4,
	"navajowhite1" : navajowhite1,
	"navajowhite2" : navajowhite2,
	"navajowhite3" : navajowhite3,
	"navajowhite4" : navajowhite4,
	"lemonchiffon1" : lemonchiffon1,
	"lemonchiffon2" : lemonchiffon2,
	"lemonchiffon3" : lemonchiffon3,
	"lemonchiffon4" : lemonchiffon4,
	"cornsilk1" : cornsilk1,
	"cornsilk2" : cornsilk2,
	"cornsilk3" : cornsilk3,
	"cornsilk4" : cornsilk4,
	"ivory1" : ivory1,
	"ivory2" : ivory2,
	"ivory3" : ivory3,
	"ivory4" : ivory4,
	"honeydew1" : honeydew1,
	"honeydew2" : honeydew2,
	"honeydew3" : honeydew3,
	"honeydew4" : honeydew4,
	"lavenderblush1" : lavenderblush1,
	"lavenderblush2" : lavenderblush2,
	"lavenderblush3" : lavenderblush3,
	"lavenderblush4" : lavenderblush4,
	"mistyrose1" : mistyrose1,
	"mistyrose2" : mistyrose2,
	"mistyrose3" : mistyrose3,
	"mistyrose4" : mistyrose4,
	"azure1" : azure1,
	"azure2" : azure2,
	"azure3" : azure3,
	"azure4" : azure4,
	"slateblue1" : slateblue1,
	"slateblue2" : slateblue2,
	"slateblue3" : slateblue3,
	"slateblue4" : slateblue4,
	"royalblue1" : royalblue1,
	"royalblue2" : royalblue2,
	"royalblue3" : royalblue3,
	"royalblue4" : royalblue4,
	"blue1" : blue1,
	"blue2" : blue2,
	"blue3" : blue3,
	"blue4" : blue4,
	"dodgerblue1" : dodgerblue1,
	"dodgerblue2" : dodgerblue2,
	"dodgerblue3" : dodgerblue3,
	"dodgerblue4" : dodgerblue4,
	"steelblue1" : steelblue1,
	"steelblue2" : steelblue2,
	"steelblue3" : steelblue3,
	"steelblue4" : steelblue4,
	"deepskyblue1" : deepskyblue1,
	"deepskyblue2" : deepskyblue2,
	"deepskyblue3" : deepskyblue3,
	"deepskyblue4" : deepskyblue4,
	"skyblue1" : skyblue1,
	"skyblue2" : skyblue2,
	"skyblue3" : skyblue3,
	"skyblue4" : skyblue4,
	"lightskyblue1" : lightskyblue1,
	"lightskyblue2" : lightskyblue2,
	"lightskyblue3" : lightskyblue3,
	"lightskyblue4" : lightskyblue4,
	"slategray1" : slategray1,
	"slategray2" : slategray2,
	"slategray3" : slategray3,
	"slategray4" : slategray4,
	"lightsteelblue1" : lightsteelblue1,
	"lightsteelblue2" : lightsteelblue2,
	"lightsteelblue3" : lightsteelblue3,
	"lightsteelblue4" : lightsteelblue4,
	"lightblue1" : lightblue1,
	"lightblue2" : lightblue2,
	"lightblue3" : lightblue3,
	"lightblue4" : lightblue4,
	"lightcyan1" : lightcyan1,
	"lightcyan2" : lightcyan2,
	"lightcyan3" : lightcyan3,
	"lightcyan4" : lightcyan4,
	"paleturquoise1" : paleturquoise1,
	"paleturquoise2" : paleturquoise2,
	"paleturquoise3" : paleturquoise3,
	"paleturquoise4" : paleturquoise4,
	"cadetblue1" : cadetblue1,
	"cadetblue2" : cadetblue2,
	"cadetblue3" : cadetblue3,
	"cadetblue4" : cadetblue4,
	"turquoise1" : turquoise1,
	"turquoise2" : turquoise2,
	"turquoise3" : turquoise3,
	"turquoise4" : turquoise4,
	"cyan1" : cyan1,
	"cyan2" : cyan2,
	"cyan3" : cyan3,
	"cyan4" : cyan4,
	"darkslategray1" : darkslategray1,
	"darkslategray2" : darkslategray2,
	"darkslategray3" : darkslategray3,
	"darkslategray4" : darkslategray4,
	"aquamarine1" : aquamarine1,
	"aquamarine2" : aquamarine2,
	"aquamarine3" : aquamarine3,
	"aquamarine4" : aquamarine4,
	"darkseagreen1" : darkseagreen1,
	"darkseagreen2" : darkseagreen2,
	"darkseagreen3" : darkseagreen3,
	"darkseagreen4" : darkseagreen4,
	"seagreen1" : seagreen1,
	"seagreen2" : seagreen2,
	"seagreen3" : seagreen3,
	"seagreen4" : seagreen4,
	"palegreen1" : palegreen1,
	"palegreen2" : palegreen2,
	"palegreen3" : palegreen3,
	"palegreen4" : palegreen4,
	"springgreen1" : springgreen1,
	"springgreen2" : springgreen2,
	"springgreen3" : springgreen3,
	"springgreen4" : springgreen4,
	"green1" : green1,
	"green2" : green2,
	"green3" : green3,
	"green4" : green4,
	"chartreuse1" : chartreuse1,
	"chartreuse2" : chartreuse2,
	"chartreuse3" : chartreuse3,
	"chartreuse4" : chartreuse4,
	"olivedrab1" : olivedrab1,
	"olivedrab2" : olivedrab2,
	"olivedrab3" : olivedrab3,
	"olivedrab4" : olivedrab4,
	"darkolivegreen1" : darkolivegreen1,
	"darkolivegreen2" : darkolivegreen2,
	"darkolivegreen3" : darkolivegreen3,
	"darkolivegreen4" : darkolivegreen4,
	"khaki1" : khaki1,
	"khaki2" : khaki2,
	"khaki3" : khaki3,
	"khaki4" : khaki4,
	"lightgoldenrod1" : lightgoldenrod1,
	"lightgoldenrod2" : lightgoldenrod2,
	"lightgoldenrod3" : lightgoldenrod3,
	"lightgoldenrod4" : lightgoldenrod4,
	"lightyellow1" : lightyellow1,
	"lightyellow2" : lightyellow2,
	"lightyellow3" : lightyellow3,
	"lightyellow4" : lightyellow4,
	"yellow1" : yellow1,
	"yellow2" : yellow2,
	"yellow3" : yellow3,
	"yellow4" : yellow4,
	"gold1" : gold1,
	"gold2" : gold2,
	"gold3" : gold3,
	"gold4" : gold4,
	"goldenrod1" : goldenrod1,
	"goldenrod2" : goldenrod2,
	"goldenrod3" : goldenrod3,
	"goldenrod4" : goldenrod4,
	"darkgoldenrod1" : darkgoldenrod1,
	"darkgoldenrod2" : darkgoldenrod2,
	"darkgoldenrod3" : darkgoldenrod3,
	"darkgoldenrod4" : darkgoldenrod4,
	"rosybrown1" : rosybrown1,
	"rosybrown2" : rosybrown2,
	"rosybrown3" : rosybrown3,
	"rosybrown4" : rosybrown4,
	"indianred1" : indianred1,
	"indianred2" : indianred2,
	"indianred3" : indianred3,
	"indianred4" : indianred4,
	"sienna1" : sienna1,
	"sienna2" : sienna2,
	"sienna3" : sienna3,
	"sienna4" : sienna4,
	"burlywood1" : burlywood1,
	"burlywood2" : burlywood2,
	"burlywood3" : burlywood3,
	"burlywood4" : burlywood4,
	"wheat1" : wheat1,
	"wheat2" : wheat2,
	"wheat3" : wheat3,
	"wheat4" : wheat4,
	"tan1" : tan1,
	"tan2" : tan2,
	"tan3" : tan3,
	"tan4" : tan4,
	"chocolate1" : chocolate1,
	"chocolate2" : chocolate2,
	"chocolate3" : chocolate3,
	"chocolate4" : chocolate4,
	"firebrick1" : firebrick1,
	"firebrick2" : firebrick2,
	"firebrick3" : firebrick3,
	"firebrick4" : firebrick4,
	"brown1" : brown1,
	"brown2" : brown2,
	"brown3" : brown3,
	"brown4" : brown4,
	"salmon1" : salmon1,
	"salmon2" : salmon2,
	"salmon3" : salmon3,
	"salmon4" : salmon4,
	"lightsalmon1" : lightsalmon1,
	"lightsalmon2" : lightsalmon2,
	"lightsalmon3" : lightsalmon3,
	"lightsalmon4" : lightsalmon4,
	"orange1" : orange1,
	"orange2" : orange2,
	"orange3" : orange3,
	"orange4" : orange4,
	"darkorange1" : darkorange1,
	"darkorange2" : darkorange2,
	"darkorange3" : darkorange3,
	"darkorange4" : darkorange4,
	"coral1" : coral1,
	"coral2" : coral2,
	"coral3" : coral3,
	"coral4" : coral4,
	"tomato1" : tomato1,
	"tomato2" : tomato2,
	"tomato3" : tomato3,
	"tomato4" : tomato4,
	"orangered1" : orangered1,
	"orangered2" : orangered2,
	"orangered3" : orangered3,
	"orangered4" : orangered4,
	"red1" : red1,
	"red2" : red2,
	"red3" : red3,
	"red4" : red4,
	"debianred" : debianred,
	"deeppink1" : deeppink1,
	"deeppink2" : deeppink2,
	"deeppink3" : deeppink3,
	"deeppink4" : deeppink4,
	"hotpink1" : hotpink1,
	"hotpink2" : hotpink2,
	"hotpink3" : hotpink3,
	"hotpink4" : hotpink4,
	"pink1" : pink1,
	"pink2" : pink2,
	"pink3" : pink3,
	"pink4" : pink4,
	"lightpink1" : lightpink1,
	"lightpink2" : lightpink2,
	"lightpink3" : lightpink3,
	"lightpink4" : lightpink4,
	"palevioletred1" : palevioletred1,
	"palevioletred2" : palevioletred2,
	"palevioletred3" : palevioletred3,
	"palevioletred4" : palevioletred4,
	"maroon1" : maroon1,
	"maroon2" : maroon2,
	"maroon3" : maroon3,
	"maroon4" : maroon4,
	"violetred1" : violetred1,
	"violetred2" : violetred2,
	"violetred3" : violetred3,
	"violetred4" : violetred4,
	"magenta1" : magenta1,
	"magenta2" : magenta2,
	"magenta3" : magenta3,
	"magenta4" : magenta4,
	"orchid1" : orchid1,
	"orchid2" : orchid2,
	"orchid3" : orchid3,
	"orchid4" : orchid4,
	"plum1" : plum1,
	"plum2" : plum2,
	"plum3" : plum3,
	"plum4" : plum4,
	"mediumorchid1" : mediumorchid1,
	"mediumorchid2" : mediumorchid2,
	"mediumorchid3" : mediumorchid3,
	"mediumorchid4" : mediumorchid4,
	"darkorchid1" : darkorchid1,
	"darkorchid2" : darkorchid2,
	"darkorchid3" : darkorchid3,
	"darkorchid4" : darkorchid4,
	"purple1" : purple1,
	"purple2" : purple2,
	"purple3" : purple3,
	"purple4" : purple4,
	"mediumpurple1" : mediumpurple1,
	"mediumpurple2" : mediumpurple2,
	"mediumpurple3" : mediumpurple3,
	"mediumpurple4" : mediumpurple4,
	"thistle1" : thistle1,
	"thistle2" : thistle2,
	"thistle3" : thistle3,
	"thistle4" : thistle4,
	"gray0" : gray0,
	"grey0" : grey0,
	"gray1" : gray1,
	"grey1" : grey1,
	"gray2" : gray2,
	"grey2" : grey2,
	"gray3" : gray3,
	"grey3" : grey3,
	"gray4" : gray4,
	"grey4" : grey4,
	"gray5" : gray5,
	"grey5" : grey5,
	"gray6" : gray6,
	"grey6" : grey6,
	"gray7" : gray7,
	"grey7" : grey7,
	"gray8" : gray8,
	"grey8" : grey8,
	"gray9" : gray9,
	"grey9" : grey9,
	"gray10" : gray10,
	"grey10" : grey10,
	"gray11" : gray11,
	"grey11" : grey11,
	"gray12" : gray12,
	"grey12" : grey12,
	"gray13" : gray13,
	"grey13" : grey13,
	"gray14" : gray14,
	"grey14" : grey14,
	"gray15" : gray15,
	"grey15" : grey15,
	"gray16" : gray16,
	"grey16" : grey16,
	"gray17" : gray17,
	"grey17" : grey17,
	"gray18" : gray18,
	"grey18" : grey18,
	"gray19" : gray19,
	"grey19" : grey19,
	"gray20" : gray20,
	"grey20" : grey20,
	"gray21" : gray21,
	"grey21" : grey21,
	"gray22" : gray22,
	"grey22" : grey22,
	"gray23" : gray23,
	"grey23" : grey23,
	"gray24" : gray24,
	"grey24" : grey24,
	"gray25" : gray25,
	"grey25" : grey25,
	"gray26" : gray26,
	"grey26" : grey26,
	"gray27" : gray27,
	"grey27" : grey27,
	"gray28" : gray28,
	"grey28" : grey28,
	"gray29" : gray29,
	"grey29" : grey29,
	"gray30" : gray30,
	"grey30" : grey30,
	"gray31" : gray31,
	"grey31" : grey31,
	"gray32" : gray32,
	"grey32" : grey32,
	"gray33" : gray33,
	"grey33" : grey33,
	"gray34" : gray34,
	"grey34" : grey34,
	"gray35" : gray35,
	"grey35" : grey35,
	"gray36" : gray36,
	"grey36" : grey36,
	"gray37" : gray37,
	"grey37" : grey37,
	"gray38" : gray38,
	"grey38" : grey38,
	"gray39" : gray39,
	"grey39" : grey39,
	"gray40" : gray40,
	"grey40" : grey40,
	"gray41" : gray41,
	"grey41" : grey41,
	"gray42" : gray42,
	"grey42" : grey42,
	"gray43" : gray43,
	"grey43" : grey43,
	"gray44" : gray44,
	"grey44" : grey44,
	"gray45" : gray45,
	"grey45" : grey45,
	"gray46" : gray46,
	"grey46" : grey46,
	"gray47" : gray47,
	"grey47" : grey47,
	"gray48" : gray48,
	"grey48" : grey48,
	"gray49" : gray49,
	"grey49" : grey49,
	"gray50" : gray50,
	"grey50" : grey50,
	"gray51" : gray51,
	"grey51" : grey51,
	"gray52" : gray52,
	"grey52" : grey52,
	"gray53" : gray53,
	"grey53" : grey53,
	"gray54" : gray54,
	"grey54" : grey54,
	"gray55" : gray55,
	"grey55" : grey55,
	"gray56" : gray56,
	"grey56" : grey56,
	"gray57" : gray57,
	"grey57" : grey57,
	"gray58" : gray58,
	"grey58" : grey58,
	"gray59" : gray59,
	"grey59" : grey59,
	"gray60" : gray60,
	"grey60" : grey60,
	"gray61" : gray61,
	"grey61" : grey61,
	"gray62" : gray62,
	"grey62" : grey62,
	"gray63" : gray63,
	"grey63" : grey63,
	"gray64" : gray64,
	"grey64" : grey64,
	"gray65" : gray65,
	"grey65" : grey65,
	"gray66" : gray66,
	"grey66" : grey66,
	"gray67" : gray67,
	"grey67" : grey67,
	"gray68" : gray68,
	"grey68" : grey68,
	"gray69" : gray69,
	"grey69" : grey69,
	"gray70" : gray70,
	"grey70" : grey70,
	"gray71" : gray71,
	"grey71" : grey71,
	"gray72" : gray72,
	"grey72" : grey72,
	"gray73" : gray73,
	"grey73" : grey73,
	"gray74" : gray74,
	"grey74" : grey74,
	"gray75" : gray75,
	"grey75" : grey75,
	"gray76" : gray76,
	"grey76" : grey76,
	"gray77" : gray77,
	"grey77" : grey77,
	"gray78" : gray78,
	"grey78" : grey78,
	"gray79" : gray79,
	"grey79" : grey79,
	"gray80" : gray80,
	"grey80" : grey80,
	"gray81" : gray81,
	"grey81" : grey81,
	"gray82" : gray82,
	"grey82" : grey82,
	"gray83" : gray83,
	"grey83" : grey83,
	"gray84" : gray84,
	"grey84" : grey84,
	"gray85" : gray85,
	"grey85" : grey85,
	"gray86" : gray86,
	"grey86" : grey86,
	"gray87" : gray87,
	"grey87" : grey87,
	"gray88" : gray88,
	"grey88" : grey88,
	"gray89" : gray89,
	"grey89" : grey89,
	"gray90" : gray90,
	"grey90" : grey90,
	"gray91" : gray91,
	"grey91" : grey91,
	"gray92" : gray92,
	"grey92" : grey92,
	"gray93" : gray93,
	"grey93" : grey93,
	"gray94" : gray94,
	"grey94" : grey94,
	"gray95" : gray95,
	"grey95" : grey95,
	"gray96" : gray96,
	"grey96" : grey96,
	"gray97" : gray97,
	"grey97" : grey97,
	"gray98" : gray98,
	"grey98" : grey98,
	"gray99" : gray99,
	"grey99" : grey99,
	"gray100" : gray100,
	"grey100" : grey100,
	"dark_grey" : dark_grey,
	"darkgrey" : darkgrey,
	"dark_gray" : dark_gray,
	"darkgray" : darkgray,
	"dark_blue" : dark_blue,
	"darkblue" : darkblue,
	"dark_cyan" : dark_cyan,
	"darkcyan" : darkcyan,
	"dark_magenta" : dark_magenta,
	"darkmagenta" : darkmagenta,
	"dark_red" : dark_red,
	"darkred" : darkred,
	"light_green" : light_green,
	"lightgreen" : lightgreen,
	None : None,
}
