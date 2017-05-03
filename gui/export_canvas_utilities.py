#!/usr/bin/env python3


from markers.shapes import Shapes
from PIL import ImageColor, ImageDraw

class ExportCanvasUtilities:

    @staticmethod
    def place_elements(image_to_save, placed_markers, colors):
        '''
        Processes imported image, registered placed markers, adds those to export file.

        Args:
            image_to_save: instance - class of PIL.Image, image in the normal size.
            placed_markers: instance - class Samples, list of all placed markers in canvas.
            colors: instance - class Samples, dictionary of all colors used in given markers.

        Return:
             image_to_save: instance - class of PIL.Image ready to export image.
        '''
        draw = ImageDraw.Draw(image_to_save)

        for current_marker in placed_markers:
            size = current_marker.size
            qualifier = current_marker.qualifier
            color = ImageColor.getrgb(colors[current_marker.mode])
            x = current_marker.position_x
            y = current_marker.position_y
            image_scale = 1.0

            shape = Shapes.calculate_shape(qualifier, x, y, size, image_scale, False)

            if qualifier == 1:
                draw.polygon(
                    (
                        shape[0],
                        shape[1],
                        shape[2],
                        shape[3],
                        shape[4],
                        shape[5]),
                    fill=color)

            elif qualifier == 2:
                draw.ellipse(
                    (
                        shape[0],
                        shape[1],
                        shape[2],
                        shape[3]),
                    fill=color)

            elif qualifier == 3:
                draw.rectangle(
                    (
                        shape[0],
                        shape[1],
                        shape[2],
                        shape[3]),
                    fill=color)

            elif qualifier == 4:
                draw.line(
                    (
                        shape[0],
                        shape[1],
                        shape[2],
                        shape[3]),
                    width=shape[4],
                    fill=color)

        return image_to_save

    @staticmethod
    def format_export_file_name(full_path, extension):
        '''
        Check if the file_name on the end of full file path has extension present.

        Args:
            full_path: string - full path with the file name.
            extension: string - extension of the file.

        Return:
            string - full path containing file_name with only one extension attached.
        '''

        occurrences = []
        occurrences_count = 0
        end_extension = False

        for i in range(len(full_path) // 4):

            if i == 0 and full_path[-4 - 4 * i:] == extension:
                occurrences.append(i)
                occurrences_count += 1
                end_extension = True

            elif i > 0 and full_path[-4 - 4 * i:-4 - 4 * (i - 1)] == extension:
                occurrences.append(i)
                occurrences_count += 1

        if end_extension and 1 in occurrences:
            validated_full_path = full_path[:-4]
        elif not end_extension and occurrences_count > 0:
            validated_full_path = '{}{}'.format(full_path, extension)
        elif not end_extension and occurrences_count == 0:
            validated_full_path = '{}{}'.format(full_path, extension)
        else:
            validated_full_path = full_path

        return validated_full_path
