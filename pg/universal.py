import json
import random
from pg.tools import *
from pg.united_kingdom import uk_exception
import numpy as np
import os
import datetime


def vrpg_universal(font: str = None,
                   directory: str = None,
                   dpi: int = 150,
                   area: dict = None,
                   plate_type: str = 'random',
                   aabb_gen: bool = True) -> dict:
    """
    Computes the Chile Vehicle Registration Plate (text and images)

    :param aabb_gen: add aabb for every letter in the sequence
    :param font: the font for printing number in image
    :param directory: the directory for saving the 2 output images - white and yellow color images
    :param dpi: the image resolution
    :param area: list of hte plates configurations
    :param plate_type: plate type to generate or generate 'random'
    :return: dictionary with: time stamp, plate number, absolute path to image
    """
    timestamp = datetime.datetime.now().strftime("%d_%b_%Y-%H_%M_%S")

    # array of the aabb
    a_aabb = []

    serial = ''

    # select plate type
    plate = plate_selector(area=area, plate_type=plate_type)

    # estimating pixel number per 1 mm
    pnpi = dpi / 25.4
    # plate size
    plate_width = int(pnpi * plate['width'])
    plate_height = int(pnpi * plate['height'])
    # create an image
    img = PIL.Image.new(mode='RGB', size=(plate_width, plate_height), color=(255, 255, 255))
    draw = PIL.ImageDraw.Draw(img)
    # patch for UK
    img_rear = None
    draw_rear = None
    if area['country'] == 'UK' and uk_exception(plate['name']) is True:
        img_rear = PIL.Image.new(mode='RGB', size=(plate_width, plate_height), color=(255, 255, 255))
        draw_rear = PIL.ImageDraw.Draw(img_rear)
    # -- Print plate --

    # open font
    if font is None:
        font = '../fonts/' + area['font']
    free_type_compatible_font = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), font
        )
    )
    font_h = int(dpi) * 2  # quality of the font printed
    font = PIL.ImageFont.truetype(free_type_compatible_font, font_h)

    # var for plate sequence, used as part of image file name
    # plate_sequence = plate['name'].replace(' ', '-') + '-'
    plate_sequence = ''
    # - DECODE OBJECTS -
    start_x_abs = 0
    for e in plate['object']:
        if e['type'] == 'text':
            if e['random'] is 0 and e['by_letter'] is 0:
                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs
                sequence = e['letters']
                font_in_use = font
                # verify if additional font required
                if 'font' in e:
                    free_type_add_font = os.path.abspath(
                        os.path.join(
                            os.path.dirname(__file__), '../fonts/' + e['font']
                        )
                    )
                    font_h = int(dpi) * 2
                    font_add = PIL.ImageFont.truetype(free_type_add_font, font_h)
                    font_in_use = font_add

                # plate_sequence += (sequence + '-')
                print_sequence_all(img_src=img,
                                   font=font_in_use,
                                   sequence=sequence,
                                   width_mm=e['width'],
                                   height_mm=e['height'],
                                   color_bg=e['color_bg'],
                                   color_text=e['color_text'],
                                   start_x_mm=start_x,
                                   start_y_mm=e['start_y'],
                                   pnpi=pnpi
                                   )
                start_x_abs += e['width']  # absolute x coordinate
            elif e['random'] is 1 and e['by_letter'] is 0:
                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs
                sequence = random.sample(e['letters'], e['quantity'])
                sequence = ''.join(sequence)

                font_in_use = font
                # verify if additional font required
                if 'font' in e:
                    free_type_add_font = os.path.abspath(
                        os.path.join(
                            os.path.dirname(__file__), e['font']
                        )
                    )
                    font_h = int(dpi) * 2
                    font_add = PIL.ImageFont.truetype(free_type_add_font, font_h)
                    font_in_use = font_add

                # plate_sequence += (sequence + '-')
                print_sequence_all(img_src=img,
                                   font=font_in_use,
                                   sequence=sequence,
                                   width_mm=e['width'],
                                   height_mm=e['height'],
                                   color_bg=plate['color_bg'],
                                   color_text=plate['color_text'],
                                   # start_x_mm=e['start_x'],
                                   start_x_mm=start_x,
                                   start_y_mm=e['start_y'],
                                   pnpi=pnpi
                                   )
                start_x_abs += e['width']  # absolute x coordinate

            elif e['random'] is 2 and e['by_letter'] is 0:
                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs
                k, v = random.choice(list(e['letters'].items()))
                chile_capital_selected = str(k).upper()  # only for Chile
                sequence = e['text_fixed'] + v
                # plate_sequence += (sequence + '-')
                print_sequence_all(img_src=img,
                                   font=font,
                                   sequence=sequence,
                                   width_mm=e['width'],
                                   height_mm=e['height'],
                                   color_bg=plate['color_bg'],
                                   color_text=plate['color_text'],
                                   # start_x_mm=e['start_x'],
                                   start_x_mm=start_x,
                                   start_y_mm=e['start_y'],
                                   pnpi=pnpi
                                   )
                start_x_abs += e['width']  # absolute x coordinate
            if e['random'] is 3 and e['by_letter'] is 0:
                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs
                sequence = e['letters'] + chile_capital_selected  # Chile only

                # verify if additional font required
                if 'font' in e:
                    free_type_add_font = os.path.abspath(
                        os.path.join(
                            os.path.dirname(__file__), e['font']
                        )
                    )
                    font_h = int(dpi) * 2
                    font_add = PIL.ImageFont.truetype(free_type_add_font, font_h)
                    font_in_use = font_add
                # plate_sequence += (sequence + '-')
                print_sequence_all(img_src=img,
                                   font=font_in_use,
                                   sequence=sequence,
                                   width_mm=e['width'],
                                   height_mm=e['height'],
                                   color_bg=plate['color_bg'],
                                   color_text=plate['color_text'],
                                   # start_x_mm=e['start_x'],
                                   start_x_mm=start_x,
                                   start_y_mm=e['start_y'],
                                   pnpi=pnpi
                                   )
                start_x_abs += e['width']  # absolute x coordinate
            elif e['random'] is 1 and e['by_letter'] is 3:
                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs
                sequence = random.sample(e['letters'], e['quantity'])
                sequence = ''.join(sequence)
                sequence = sequence.upper()
                start_x, width = sequence_auto_center(sequence, e['width'], e['height'], e['offset_x'],
                                                      plate['width'] // 2)

                font_in_use = font
                # verify if additional font required
                if 'font' in e:
                    free_type_add_font = os.path.abspath(
                        os.path.join(
                            os.path.dirname(__file__), e['font']
                        )
                    )
                    font_h = int(dpi) * 2
                    font_add = PIL.ImageFont.truetype(free_type_add_font, font_h)
                    font_in_use = font_add
                # plate_sequence += (sequence + '-')
                print_sequence_all(img_src=img,
                                   font=font_in_use,
                                   sequence=sequence,
                                   width_mm=width,
                                   height_mm=e['height'],
                                   color_bg=plate['color_bg'],
                                   color_text=plate['color_text'],
                                   # start_x_mm=e['start_x'],
                                   start_x_mm=start_x,
                                   start_y_mm=e['start_y'],
                                   pnpi=pnpi
                                   )
                start_x_abs += e['width']  # absolute x coordinate
            elif e['random'] is 0 and e['by_letter'] is 1:
                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs
                sequence = e['letters']
                # plate_sequence += (sequence + '-')
                print_sequence_by_letter(img_src=img,
                                         font=font,
                                         sequence=sequence,
                                         width_mm=e['width'],
                                         height_mm=e['height'],
                                         color_bg=plate['color_bg'],
                                         color_text=plate['color_text'],
                                         # start_x_mm=e['start_x'],
                                         start_x_mm=start_x,
                                         start_y_mm=e['start_y'],
                                         offset_x_mm=e['offset_x'],
                                         pnpi=pnpi
                                         )
                start_x_abs += (
                        e['width'] * len(sequence) + e['offset_x'] * (len(sequence) - 1))  # absolute x coordinate
            elif e['random'] is 1 and e['by_letter'] is 2:
                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs

                i = random.randint(0, len(e['letters']) - 1)
                sequence = e['letters'][i]
                # plate_sequence += (sequence + '-')

                offset_x_min = 2  # debug
                width = by_letter_mode_2_auto_adjustment(sequence=sequence, width=e['width'], offset_x_min=offset_x_min)

                print_sequence_by_letter(img_src=img,
                                         font=font,
                                         sequence=sequence,
                                         # width_mm=e['width'],
                                         width_mm=width,
                                         height_mm=e['height'],
                                         color_bg=plate['color_bg'],
                                         color_text=plate['color_text'],
                                         # start_x_mm=e['start_x'],
                                         start_x_mm=start_x,
                                         start_y_mm=e['start_y'],
                                         # offset_x_mm=e['offset_x'],
                                         offset_x_mm=offset_x_min,
                                         pnpi=pnpi
                                         )
                start_x_abs += e['width']  # absolute x coordinate
            elif e['random'] is 4 and e['by_letter'] is 0:
                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs
                sequence = serial
                # plate_sequence += (sequence + '-')
                print_sequence_all(img_src=img,
                                   font=font,
                                   sequence=sequence,
                                   width_mm=e['width'],
                                   height_mm=e['height'],
                                   color_bg=e['color_bg'],
                                   color_text=e['color_text'],
                                   # start_x_mm=e['start_x'],
                                   start_x_mm=start_x,
                                   start_y_mm=e['start_y'],
                                   pnpi=pnpi
                                   )
                start_x_abs += e['width']  # absolute x coordinate

        elif e['type'] == 'number' and e['by_letter'] is 0:
            if e['random'] is 1:
                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs
                value = random.randint(e['number_min'], e['number_max'])
                sequence = str(value).zfill(e['number_zfil'])
                # plate_sequence += (sequence + '-')
                print_sequence_all(img_src=img,
                                   font=font,
                                   sequence=sequence,
                                   width_mm=e['width'],
                                   height_mm=e['height'],
                                   color_bg=e['color_bg'],
                                   color_text=e['color_text'],
                                   # start_x_mm=e['start_x'],
                                   start_x_mm=start_x,
                                   start_y_mm=e['start_y'],
                                   pnpi=pnpi
                                   )
                start_x_abs += e['width']  # absolute x coordinate
        elif e['type'] == 'number' and e['by_letter'] is 2:
            if e['random'] is 1:
                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs
                value = random.randint(e['number_min'], e['number_max'])
                sequence = str(value).zfill(e['number_zfil'])
                # plate_sequence += sequence

                offset_x_min = 10  # debug
                width = by_letter_mode_2_auto_adjustment(sequence=sequence,
                                                         width=e['width'],
                                                         offset_x_min=offset_x_min)

                print_sequence_by_letter(img_src=img,
                                         font=font,
                                         sequence=sequence,
                                         # width_mm=e['width'],
                                         width_mm=width,
                                         height_mm=e['height'],
                                         color_bg=plate['color_bg'],
                                         color_text=plate['color_text'],
                                         # start_x_mm=e['start_x'],
                                         start_x_mm=start_x,
                                         start_y_mm=e['start_y'],
                                         # offset_x_mm=e['offset_x'],
                                         offset_x_mm=offset_x_min,
                                         pnpi=pnpi
                                         )

                start_x_abs += e['width']  # absolute x coordinate
        elif e['type'] == 'image':
            start_x_abs = element_print_image(img=img, e=e, start_x_abs=start_x_abs, pnpi=pnpi)
        elif e['type'] == 'format':
            if e['random'] is 1:
                scaling_limit = {'I', '1'}

                sequence_format = None

                format_type = random.randint(0, len(e['obj']) - 1)
                plate_format = e['obj'][format_type]

                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs
                sequence = ''
                for pfe in plate_format:
                    if pfe['type'] == 0 and pfe['r'] == 1:
                        letter = random.sample(pfe['rnd_obj'], 1)
                        sequence += ''.join(letter)
                    if pfe['type'] == 0 and pfe['r'] == 0:
                        letter = pfe['text_obj']
                        sequence += letter
                    if pfe['type'] == 1 and pfe['r'] == 1:
                        value = random.randint(pfe['min'], pfe['max'])
                        sequence += str(value).zfill(pfe['zfil'])
                    if pfe['type'] == 3:
                        sequence_format = pfe['obj']
                    if pfe['type'] == 5:
                        scaling_limit = pfe['sl']
                    if pfe['type'] == 6 and pfe['r'] == 1:  # length cutter by using 'sequence_limit' value
                        value = random.randint(pfe['min'], pfe['max'])
                        sequence += str(value).zfill(pfe['zfil'])
                        sequence = list(sequence)
                        sequence = ''.join(sequence[:pfe['sequence_limit']])
                    if pfe['type'] == 7 and pfe['r'] == 1:  # currently in use only for Chile type 'Bomberos'
                        k, v = random.choice(list(pfe['rnd_obj'].items()))
                        chile_capital_selected = str(k).upper()  # only for Chile
                        sequence += v
                    if pfe['type'] == 8: # made for Germany, an Auto-position calculation
                        v = pfe['f']() # generate Sequence and Auto-position calculation
                        plate_format.extend(v)
                        # print(v)
                    if pfe['type'] == 9:
                        start_x_abs = element_print_image(img=img, e=pfe['obj'], start_x_abs=start_x_abs, pnpi=pnpi)

                plate_sequence += sequence
                serial = sequence

                font_in_use = font
                # verify if additional font required
                if 'font' in e:
                    free_type_add_font = os.path.abspath(
                        os.path.join(
                            os.path.dirname(__file__), '../fonts/' + e['font']
                        )
                    )
                    font_h = int(dpi) * 2
                    font_add = PIL.ImageFont.truetype(free_type_add_font, font_h)
                    font_in_use = font_add


                if sequence_format is not None:
                    r = print_sequence_by_letter_with_format(
                        img_src=img,
                        font=font_in_use,
                        sequence=sequence,
                        color_bg=e['color_bg'],
                        color_text=e['color_text'],
                        start_x_mm=start_x,
                        start_y_mm=e['start_y'],
                        sequence_format=sequence_format,
                        pnpi=pnpi,
                        scaling_limit=scaling_limit,
                        aabb_gen=aabb_gen)
                    if aabb_gen is True:
                        a_aabb.append(r)
                        # debug
                        # for er in r:
                        #     draw.rectangle(((er['xlu'], er['ylu']), (er['xlu']+er['w'], er['ylu']+er['h'])),
                        #                    outline=e['color_text'], width=1)
                else:
                    print_sequence_all(img_src=img,
                                       font=font_in_use,
                                       sequence=sequence,
                                       width_mm=e['width'],
                                       height_mm=e['height'],
                                       color_bg=e['color_bg'],
                                       color_text=e['color_text'],
                                       # start_x_mm=e['start_x'],
                                       start_x_mm=start_x,
                                       start_y_mm=e['start_y'],
                                       pnpi=pnpi
                                       )
                start_x_abs += e['width']  # absolute x coordinate
        elif e['type'] == 'format_uk':
            if e['random'] is 1:
                sequence_format = None
                scaling_limit = {'I', '1'}

                format_type = random.randint(0, len(e['obj']) - 1)
                plate_format = e['obj'][format_type]

                start_x_abs += e['start_x']  # absolute x coordinate
                start_x = e['start_x']
                if e['coord'] == 1:
                    start_x = start_x_abs
                sequence = ''
                for pfe in plate_format:
                    if pfe['type'] == 0 and pfe['r'] == 1:
                        letter = random.sample(pfe['rnd_obj'], 1)
                        sequence += ''.join(letter)
                    if pfe['type'] == 0 and pfe['r'] == 0:
                        letter = pfe['text_obj']
                        sequence += letter
                    if pfe['type'] == 1 and pfe['r'] == 1:
                        value = random.randint(pfe['min'], pfe['max'])
                        sequence += str(value).zfill(pfe['zfil'])
                    if pfe['type'] == 3:
                        sequence_format = pfe['obj']
                    if pfe['type'] == 4:
                        mnemonic_value = random.randint(0, len(pfe['obj']) - 1)
                        dvla_value = random.randint(0, len(pfe['obj'][mnemonic_value]['DVLA_office']) - 1)
                        area_letter = pfe['obj'][mnemonic_value]["letter_1"]
                        dvla_letter = random.sample(pfe['obj'][mnemonic_value]["DVLA_office"][dvla_value]["letter_2"], 1)[0]
                        sequence += (area_letter+dvla_letter)

                plate_sequence += sequence
                serial = sequence

                if sequence_format is not None:
                    r = print_sequence_by_letter_with_format(
                        img_src=img,
                        font=font,
                        sequence=sequence,
                        color_bg=e['color_bg'],
                        color_text=e['color_text'],
                        start_x_mm=start_x,
                        start_y_mm=e['start_y'],
                        sequence_format=sequence_format,
                        pnpi=pnpi,
                        scaling_limit=scaling_limit,
                        aabb_gen=aabb_gen)
                    if aabb_gen is True:
                        a_aabb.append(r)
                    r = print_sequence_by_letter_with_format(
                        img_src=img_rear,
                        font=font,
                        sequence=sequence,
                        color_bg=e['color_bg_rear'],
                        color_text=e['color_text_rear'],
                        start_x_mm=start_x,
                        start_y_mm=e['start_y'],
                        sequence_format=sequence_format,
                        pnpi=pnpi,
                        scaling_limit=scaling_limit,
                        aabb_gen=aabb_gen)
                    if aabb_gen is True:
                        a_aabb.append(r)
                else:
                    print_sequence_all(img_src=img,
                                       font=font,
                                       sequence=sequence,
                                       width_mm=e['width'],
                                       height_mm=e['height'],
                                       color_bg=e['color_bg'],
                                       color_text=e['color_text'],
                                       # start_x_mm=e['start_x'],
                                       start_x_mm=start_x,
                                       start_y_mm=e['start_y'],
                                       pnpi=pnpi
                                       )
                start_x_abs += e['width']  # absolute x coordinate
        elif e['type'] == 'rectangle':
            start_x_abs += e['start_x']  # absolute x coordinate
            start_x = e['start_x']
            if e['coord'] == 1:
                start_x = start_x_abs
            width = int(pnpi * e['border_width'])
            rect_corner_x = int(pnpi * start_x)
            rect_corner_y = int(pnpi * e['start_y'])
            rect_corner_x_end = rect_corner_x + int(pnpi * e['width'])
            rect_corner_y_end = rect_corner_y + int(pnpi * e['height'])
            draw.rectangle(((rect_corner_x, rect_corner_y), (rect_corner_x_end, rect_corner_y_end)),
                           fill=e['fill_color'], outline=e['border_color'], width=width)

            start_x_abs += e['width']  # absolute x coordinate
        elif e['type'] == 'rectangle_uk':
            start_x_abs += e['start_x']  # absolute x coordinate
            start_x = e['start_x']
            if e['coord'] == 1:
                start_x = start_x_abs
            width = int(pnpi * e['border_width'])
            rect_corner_x = int(pnpi * start_x)
            rect_corner_y = int(pnpi * e['start_y'])
            rect_corner_x_end = rect_corner_x + int(pnpi * e['width'])
            rect_corner_y_end = rect_corner_y + int(pnpi * e['height'])
            draw.rectangle(((rect_corner_x, rect_corner_y), (rect_corner_x_end, rect_corner_y_end)),
                           fill=e['fill_color'], outline=e['border_color'], width=width)
            draw_rear.rectangle(((rect_corner_x, rect_corner_y), (rect_corner_x_end, rect_corner_y_end)),
                           fill=e['fill_color_rear'], outline=e['border_color'], width=width)

            start_x_abs += e['width']  # absolute x coordinate
        elif e['type'] == 'rectangle_rounded':
            start_x_abs += e['start_x']  # absolute x coordinate
            start_x = e['start_x']
            if e['coord'] == 1:
                start_x = start_x_abs
            width = int(pnpi * e['border_width'])
            rect_corner_x = int(pnpi * start_x)
            rect_corner_y = int(pnpi * e['start_y'])
            rect_corner_x_end = rect_corner_x + int(pnpi * e['width'])
            rect_corner_y_end = rect_corner_y + int(pnpi * e['height'])
            radius = int(pnpi * e['border_radius'])
            fill_color = None
            if 'fill_color' in e:
                fill_color = e['fill_color']
            draw.rounded_rectangle((rect_corner_x, rect_corner_y, rect_corner_x_end, rect_corner_y_end),
                                   fill=fill_color,
                                   outline=e['border_color'],
                                   width=width,
                                   radius=radius)

            start_x_abs += e['width']  # absolute x coordinate
        elif e['type'] == 'sine_wave':
            start_x = int(pnpi * e['start_x'])
            end_x = int(pnpi * e['end_x'])
            wave_width = int(pnpi * e['wave_width'])
            amplitude = int(pnpi * e['wave_amplitude'])
            wave_period = int(pnpi * e['wave_period'])
            wave_phase = pnpi * e['wave_phase']
            offset = pnpi * e['start_y']  # Vertical offset
            wave_step = (2 * math.pi) / wave_period
            # Draw the sine wave
            frequency = 0
            for x in range(start_x, end_x):
                y = int(amplitude * math.sin(frequency + (wave_step * wave_phase)) + offset)
                frequency += wave_step
                if frequency >= wave_period:
                    frequency = 0
                for i in range(-wave_width // 2, wave_width // 2 + 1):
                    draw.point((x, y + i), fill=e['fill_color'])

    # remove spaces fro sequence
    plate_sequence = plate_sequence.replace(' ', '')
    # create dir for saving image
    os.makedirs(os.path.dirname(directory), exist_ok=True)
    images = []
    # patch for UK
    if area['country'] == 'UK' and uk_exception(plate['name']) is True:
        img_name = os.path.join(directory,
                                area['country'] + '-Front-'
                                + area['rfy'] + '-' + plate_sequence + '-' + timestamp + '.png')
        # save front image
        img.save(img_name, dpi=(dpi, dpi))
        images.append(img_name)
        img_name = os.path.join(directory,
                                area['country'] + '-Rear-'
                                + area['rfy'] + '-' + plate_sequence + '-' + timestamp + '.png')
        # save rear image
        img_rear.save(img_name, dpi=(dpi, dpi))
        images.append(img_name)
    else:
        img_name = os.path.join(directory,
                                area['country'] + '-' + area['rfy'] + '-' + plate_sequence + '-' + timestamp + '.png')
        # save image
        img.save(img_name, dpi=(dpi, dpi))
        images = [img_name]

    return {'timestamp': timestamp,
            'country': area['country'],
            'type': plate['name'],
            'plate': plate_sequence,
            'aabb': a_aabb,
            'images': images}
