from api.export_report.Formats import Formats
import csv

class toCsv(Formats):
    _extension = 'csv'

    def print_to_format(self, data, filename):
        with open(f"../src/reports/csv/{filename}.{self.get_extension()}", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def get_extension(self):
        return self._extension

    def construct_report(self, data):
        row_list = []
        for sorting_method in data.keys():
            row_list.append([f"Sorting Method: {sorting_method}",f"Time: {data[sorting_method]['time']} s"])
            row_list.append(["Original Array", "Sorted Array"])
            for i, (oe, se) in enumerate(zip(data[sorting_method]['original_array'],data[sorting_method]['sorted_array'])):
                row_list.append([oe, se])
            row_list.append(["\n"])
        return row_list
