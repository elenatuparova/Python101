class Parser:
    @classmethod
    def parse_money_tracker_data(cls, file_name):
        try:
            with open(file_name) as file:
                data = file.readlines()
            return data
        except (OSError, IOError):
            print('Invalid file name! File not found!')