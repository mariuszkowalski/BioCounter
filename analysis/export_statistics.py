#!/usr/bin/env python3


import codecs
import csv


class ExportStatistics:
    '''
    Class used for exporting the created in software
    statistics.
    '''

    @staticmethod
    def export_to_csv(file_path, samples, statistics):
        '''
        Exports the basic statistics form the application to the CSV file format.

        Args:
            file_path: string - contains full file path with file name.
            samples: instance - class Samples.
            statistics: instance - class Statistics.

        Return:
            No return in method.
        '''

        header_row = [
            '',
            samples.qualifiers[1],
            samples.qualifiers[2],
            samples.qualifiers[3],
            samples.qualifiers[4]]

        #Row structure.
        #samples.names[1...8], statistics.stats[1...8][1...4]
        matrix = []

        for key, value in samples.names.items():
            temp = [value, statistics.stats[key][1], statistics.stats[key][2], statistics.stats[key][3], statistics.stats[key][4]]
            matrix.append(temp)

        with codecs.open(file_path, 'w', 'utf-8') as csv_file:

            file_writer = csv.writer(csv_file, delimiter=';')
            file_writer.writerow(header_row)

            for element in matrix:
                file_writer.writerow(element)
