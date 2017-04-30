#!/usr/bin/env python3


from markers.shapes import Shapes
from PIL import ImageColor, ImageDraw

class ExportCanvasUtilities:

    @staticmethod
    def place_elements(image_to_save, processed_image, placed_markers, colors):
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