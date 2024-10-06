import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

import random
import math
from pg.geometry import coord_to_2daabb
from enum import Enum


class Glyph(Enum):
    LET = 0  # 1 letter
    NUM = 1  # number
    IMG = 2  # image


# -- Items
#
# TEXT
# coordinates: 0 - absolute value, 1 - relative value
# random:
#            0 - False,
#            1 - True,
#            2 - Text + random Text made from dictionary ( capital: abreviatura) -- ONLY FOR CHILE ?! --
#            3 - Text + Text
#            4 - Serial to be printed after serial is ready. Do it after serial is calculated.
#            5 - only for UK

# by_letter: 0 - print all sequence at once,
#            1 - print sequence letter by letter with predefined width,
#            2 - print sequence letter by letter with auto adjustment
#            3 - print sequence with auto center estimation

def sequence_auto_center(sequence, width, height, offset_x_min, center_x):
    w = len(sequence) * height + (offset_x_min * (len(sequence) - 1))
    if w < width:
        start_x = center_x - (w // 2)
        return start_x, w
    else:
        start_x = center_x - (width // 2)
        return start_x, width


def by_letter_mode_2_auto_adjustment(sequence, width, offset_x_min):
    if len(sequence) == 1:  # debug
        w = width // 2
    else:
        a = (len(sequence) - 1) * offset_x_min
        w = int((width - a) / len(sequence))
    return w


def print_sequence(img, font, color_bg, color_text, sequence, offset_x, offset_y, x_offset_a, x_offset_b, letter_width,
                   letter_height) -> int:
    for e in sequence:
        text_width = font.getmask(e).getbbox()[2]
        text_height = font.getmask(e).getbbox()[3]
        img_temp = PIL.Image.new(mode='RGB', size=(text_width, text_height), color=color_bg)
        draw_temp = PIL.ImageDraw.Draw(img_temp)
        draw_temp.text((0, 0), e, font=font, fill=color_text, anchor="lt")
        img_temp = img_temp.resize((letter_width, letter_height))
        img.paste(img_temp, (offset_x, offset_y))
        offset_x += (x_offset_a + x_offset_b)
    return offset_x


def print_letter(
        img_src,
        font,
        letter,
        width_mm,
        height_mm,
        color_bg,
        color_text,
        start_x_mm,
        start_y_mm,
        pnpi) -> None:
    sequence_width = font.getmask(letter).getbbox()[2]
    sequence_height = font.getmask(letter).getbbox()[3]

    width = int(pnpi * width_mm)
    height = int(pnpi * height_mm)
    start_x = int(pnpi * start_x_mm)
    start_y = int(pnpi * start_y_mm)

    img_temp = PIL.Image.new(mode='RGB', size=(sequence_width, sequence_height), color=color_bg)
    draw_temp = PIL.ImageDraw.Draw(img_temp)
    draw_temp.text((0, 0), letter, font=font, fill=color_text, anchor="lt")
    img_temp = img_temp.resize((width, height))
    img_src.paste(img_temp, (start_x, start_y))


def print_letter_avoid_ovescaling(width_old, width_new, height_old, height_new) -> tuple:
    a = width_new / width_old
    b = height_new / height_old
    if a < b:
        return width_new, int(a * height_old)
    else:
        return int(b * width_old), height_new


def fe_shrift_correction(letter: str = 'A'):
    offset = {
        '0': 2.8, '1': 3.2, '2': 2.8, '3': 3.2, '4': 2.8, '5': 3.2, '6': 2.8, '7': 3.2, '8': 2.8, '9': 2.8,
        'A': 1.9, 'B': 1.9, 'C': 1.9, 'D': 1.5, 'E': 2.4, 'F': 1.9, 'G': 1.9, 'H': 1.9, 'I': 5,
        'J': 1.4, 'K': 1.9, 'L': 2.5, 'M': 1.9, 'N': 1.9, 'O': 1.9, 'P': 1.9, 'Q': 1.9, 'R': 1.9,
        'S': 1.9, 'T': 1.9, 'U': 2.3, 'V': 1.9, 'W': 2.3, 'X': 1.9, 'Y': 1.9, 'Z': 1.9, '-': 1.2
    }
    return offset[letter]


def print_sequence_by_letter_with_format(
        img_src,
        font,
        sequence,
        color_bg,
        color_text,
        start_x_mm,
        start_y_mm,
        sequence_format,
        pnpi,
        scaling_limit,
        aabb_gen) -> list:
    r = []
    # array of aabb
    a_aabb = []

    start_x = int(pnpi * start_x_mm)
    start_y = int(pnpi * start_y_mm)
    # a = dict()
    # ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # for e in ascii_uppercase:
    #     text_width = font.getmask(e).getbbox()[2]
    #     text_height = font.getmask(e).getbbox()[3]
    #     a[e] = [text_width, text_height]
    e = list(sequence)
    sf = sequence_format

    x = start_x
    y = start_y
    for i in range(len(sf)):
        width = int(pnpi * sf[i]['w'])
        height = int(pnpi * sf[i]['h'])
        letter_width = font.getmask(e[i]).getbbox()[2]
        letter_height = font.getmask(e[i]).getbbox()[3]
        img_temp = PIL.Image.new(mode='RGBA', size=(letter_width, letter_height), color=color_bg)
        draw_temp = PIL.ImageDraw.Draw(img_temp)
        draw_temp.text((0, 0), e[i], font=font, fill=color_text, anchor="lt")
        # check if coordinates is relative to previous ones, if coordinate is absolute X = 0, and Y = 0
        if 'r' in sf[i] and sf[i]['r'] is False:
            x = 0
            y = 0
        offset_x = int(pnpi * sf[i]['ox'])
        offset_y = int(pnpi * sf[i]['oy'])
        x += offset_x
        y += offset_y
        if e[i] in scaling_limit:
            width_limit, height_limit = print_letter_avoid_ovescaling(letter_width, width, letter_height, height)
        else:
            width_limit = width
            height_limit = height
        # debug offset for cropping
        if font.getname()[0] == 'Euro Plate':
            offset_crop = int(pnpi * fe_shrift_correction(letter=e[i]))
            img_temp = img_temp.crop((offset_crop, 0, letter_width, letter_height))
        img_temp = img_temp.resize((width_limit, height_limit))
        # img_temp = img_temp.resize((width, height))
        img_src.paste(img_temp, (x, y), img_temp)
        if aabb_gen is True:
            aabb = coord_to_2daabb(letter=e[i], xlu=x, ylu=y, w=width_limit, h=height_limit)
            a_aabb.append(aabb)

        x += width_limit
        # print(int(x / pnpi))
    r = a_aabb
    # x_mm = int(x / pnpi)
    # y_mm = int(y / pnpi)
    return r


def print_sequence_by_letter(
        img_src,
        font,
        sequence,
        width_mm,
        height_mm,
        color_bg,
        color_text,
        start_x_mm,
        start_y_mm,
        offset_x_mm,
        pnpi) -> int:
    width = int(pnpi * width_mm)
    height = int(pnpi * height_mm)
    start_x = int(pnpi * start_x_mm)
    start_y = int(pnpi * start_y_mm)

    offset_x = int(pnpi * offset_x_mm)

    x = start_x
    for e in sequence:
        text_width = font.getmask(e).getbbox()[2]
        text_height = font.getmask(e).getbbox()[3]
        img_temp = PIL.Image.new(mode='RGB', size=(text_width, text_height), color=color_bg)
        draw_temp = PIL.ImageDraw.Draw(img_temp)
        draw_temp.text((0, 0), e, font=font, fill=color_text, anchor="lt")
        if e in {'I', 'J', '1'}:
            width_limit, height_limit = print_letter_avoid_ovescaling(text_width, width, text_height, height)
        else:
            width_limit = width
            height_limit = height
        img_temp = img_temp.resize((width_limit, height_limit))
        img_src.paste(img_temp, (x, start_y))
        x += (width + offset_x)

    x_mm = int(x / pnpi)
    return x_mm


def print_sequence_all(
        img_src,
        font,
        sequence,
        width_mm,
        height_mm,
        color_bg,
        color_text,
        start_x_mm,
        start_y_mm,
        pnpi) -> None:
    sequence_width = font.getmask(sequence).getbbox()[2]
    sequence_height = font.getmask(sequence).getbbox()[3]

    width = int(pnpi * width_mm)
    height = int(pnpi * height_mm)
    start_x = int(pnpi * start_x_mm)
    start_y = int(pnpi * start_y_mm)

    img_temp = PIL.Image.new(mode='RGBA', size=(sequence_width, sequence_height), color=color_bg)
    draw_temp = PIL.ImageDraw.Draw(img_temp)
    draw_temp.text((0, 0), sequence, font=font, fill=color_text, anchor="lt")
    img_temp = img_temp.resize((width, height))
    img_src.paste(img_temp, (start_x, start_y), img_temp)


def print_image(
        img_src,
        img_paste,
        width_mm,
        height_mm,
        start_x_mm,
        start_y_mm,
        pnpi) -> None:
    img_width = int(pnpi * width_mm)
    img_height = int(pnpi * height_mm)
    start_x = int(pnpi * start_x_mm)
    start_y = int(pnpi * start_y_mm)

    img = PIL.Image.open(img_paste)
    img = img.resize((img_width, img_height))
    # merge image
    img_src.paste(img, (start_x, start_y), img)


def element_print_image(img, e, start_x_abs, pnpi) -> int:
    start_x_abs += e['start_x']  # absolute x coordinate
    start_x = e['start_x']
    if e['coord'] == 1:
        start_x = start_x_abs
    print_image(
        img_src=img,
        img_paste=e["image"],
        width_mm=e['width'],
        height_mm=e['height'],
        start_x_mm=start_x,
        start_y_mm=e['start_y'],
        pnpi=pnpi)
    start_x_abs += e['width']  # absolute x coordinate
    return start_x_abs


def plate_format_to_random(plate_format, text_set, number_min, number_max):
    sequence = ''

    plate_formats_type_0 = {'ABC-123', 'AB1-234', 'A1B-234', 'AB-1234', 'A-123'}

    if plate_format in plate_formats_type_0:
        plate_format = list(plate_format)
        for i in range(len(plate_format)):
            if plate_format[i].isalpha() is True:
                j = random.randint(0, len(text_set - 1))
                a = text_set[i]
            elif plate_format[i].isnumeric() is True:
                value = random.randint(number_min, number_max)
            elif plate_format[i] == '-':
                break

        value = random.randint(number_min, number_max)
        sequence = str(value).zfill(3)

    return sequence


# def print_text_non_random


def plate_selector(area: dir = None, plate_type: str = 'random'):
    plate = None
    if plate_type == 'random':
        # select random plate type
        plate_type = random.randint(0, len(area['plates']) - 1)
        plate = area['plates'][plate_type]
    else:
        for e in area['plates']:
            if e['name'] == plate_type:
                plate = e
                break
    return plate
