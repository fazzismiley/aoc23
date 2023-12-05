import string



class Solution:

    def __init__(self, file: str):
        self.file = file
    
    @staticmethod
    def read_file(file):
        with open(file, 'r') as f:
            data = f.read()
        return data

class Day1(Solution):

    def __init__(self, file: str):
        super().__init__(file)
        self.data = Day1.read_file(self.file).splitlines()
        self.numeral_map = {
                'one': '1',
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9'
            }

    @staticmethod
    def find_first_last_digit(text: str) -> str:

        first = '0'
        last = '0'
        for i in text:
            if i.isdigit():
                first = i
                break
        for i in text[-1::-1]:
            if i.isdigit():
                last = i
                break
        return int(first+last)

    def map_word_to_digit(self, text: str, depth=0) ->str:
        """replaces all word numerals with digits using a map

        Args:
            text (str): str to update

        Returns:
            str: updated str
        """
        # lower text and make hard copy
        new_text = text.lower()[0:]
        # get keys of numeral_map as list of written numerals
        word_nums = list(self.numeral_map.keys()) 
        # get lowest ix of each word num
        word_num_ix = [(new_text.find(word_num), word_num) for word_num in word_nums]
        # sort tuples
        word_num_ix_ordered = sorted(word_num_ix)
        # loop over ordered ix, word_num tuples
        # if greater than -1 (exists) replace it
        # break and search the new string. This ensures all
        # word nums are replaced in order ensuring
        # overlaps are not mapped incorrectly
        for word_num_ix, word_num in word_num_ix_ordered:
            if word_num_ix > -1:
                new_text = new_text.replace(
                    word_num,
                    self.numeral_map.get(word_num),
                    1
                    )[0:]
                break
        if any(x > -1 for x in list(map(new_text.find,word_nums))):
            new_text = self.map_word_to_digit(new_text)[0:]
        return new_text[0:]

    def solve_day1a(self):
        return sum(list(map(Day1.find_first_last_digit,self.data)))
    
    def solve_day1b(self):
        clean_data = list(map(self.map_word_to_digit, self.data[:]))
        return sum(list(map(Day1.find_first_last_digit,clean_data)))

solver_1 = Day1('./data/1.txt')
print("Day 1A Solution:", solver_1.solve_day1a())  
print("Day 1B Solution:", solver_1.solve_day1b()) 
