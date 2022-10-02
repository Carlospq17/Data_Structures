from api.export_report.Formats import Formats

class toTxt(Formats):
    _extension = 'txt'

    def print_to_format(self, data, filename):
        with open(f"../src/reports/txt/{filename}.{self.get_extension()}", 'w', newline='') as file:
            for line in data:
                print(line)
                file.write(line)
                file.write('\n')

    def get_extension(self):
        return self._extension

    def construct_report(self, data):
        row_list = []
        for sorting_method in data.keys():
            row_list.append(f"Sorting Method: {sorting_method} Time: {data[sorting_method]['time']} s")
            row_list.append(f"Original Array: {data[sorting_method]['original_array']}" )
            row_list.append(f"Original Array: {data[sorting_method]['sorted_array']}" )
            row_list.append("\n")
        return row_list
