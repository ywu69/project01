__author__ = 'Yuefeng WU'

import sys

class HammingParity(object):

    def count_parity(self, data):
        sum = 0
        for d in data:
            if d == '1':
                sum += 1
        return str(sum % 2)

    def get_parity(self, binary_str):
        postion_1 = binary_str[0] + binary_str[1] + binary_str[3] + binary_str[4] + binary_str[6]
        parity_bit1 = self.count_parity(postion_1)
        postion_2 = binary_str[0] + binary_str[2] + binary_str[3] + binary_str[5] + binary_str[6]
        parity_bit2 = self.count_parity(postion_2)
        postion_4 = binary_str[1] + binary_str[2] + binary_str[3] + binary_str[7]
        parity_bit4 = self.count_parity(postion_4)
        postion_8 = binary_str[4] + binary_str[5] + binary_str[6] + binary_str[7]
        parity_bit8 = self.count_parity(postion_8)
        hamming_parity = parity_bit1 + parity_bit2 + binary_str[0] + parity_bit4 + binary_str[1] + binary_str[2] \
                         + binary_str[3] + parity_bit8 + binary_str[4] + binary_str[5] + binary_str[6] + binary_str[7]
        return hamming_parity

class HammingBinary(object):

    def encode(self, char):
        hamming_code = ''
        for t in char:
            binary_str = "{0:08b}".format(ord(t))
            hamming_str = HammingParity().get_parity(binary_str)
            hamming_code += hamming_str

        ascii_code = ''
        for x in range(0, int(len(hamming_code)/8)):
            ascii_str = chr(int(hamming_code[8*x:8*x+8], 2))
            ascii_code += ascii_str
        if len(hamming_code) % 8 != 0:
            last_postion = int(len(hamming_code)/8)
            last_ascii = chr(int(hamming_code[8*last_postion:8*last_postion+4] + '0000', 2))
            ascii_code += last_ascii
        return ascii_code

    def decode(self, code):
        binary_code = self.to_binary(code)

        origin_code = ''
        for x in range(0, int(len(binary_code)/12)):
            each_hammingcode = binary_code[12*x:12*x+12]
            each_origin_binary = each_hammingcode[2] + each_hammingcode[4] + each_hammingcode[5] + each_hammingcode[6] \
                                 + each_hammingcode[8] + each_hammingcode[9] + each_hammingcode[10] + each_hammingcode[11]
            each_origin_code = chr(int(each_origin_binary, 2))
            origin_code += each_origin_code
        return origin_code

    def chk(self, code):
        binary_code = self.to_binary(code)

        error_position_array = []
        for x in range(0, int(len(binary_code)/12)):
            each_hammingcode = binary_code[12*x:12*x+12]
            each_origin_binary = each_hammingcode[2] + each_hammingcode[4] + each_hammingcode[5] + each_hammingcode[6] \
                                 + each_hammingcode[8] + each_hammingcode[9] + each_hammingcode[10] + each_hammingcode[11]
            each_origin_parity = HammingParity().get_parity(each_origin_binary)

            error_position = 0
            has_error = False
            for y in range(0, 12):
                if each_origin_parity[y] != each_hammingcode[y]:
                    has_error = True
                    error_position += y + 1
            if has_error:
                error_position_array.append(x * 12 + error_position)
        for e in error_position_array:
            print('There is an error bit in position: ' + str(e))
        return error_position_array

    def fix(self, code):
        binary_code = self.to_binary(code)
        binary_list = list(binary_code)
        error_position_array = self.chk(code)
        for e in error_position_array:
            if binary_list[e-1] == '0':
                binary_list[e-1] = '1'
            elif binary_list[e-1] == '1':
                binary_list[e-1] = '0'
            print('Fix the error bit in position: ' + str(e))
        correct_code = ''.join(binary_list)
        origin_code = ''
        for x in range(0, int(len(correct_code)/12)):
            each_hammingcode = correct_code[12*x:12*x+12]
            each_origin_binary = each_hammingcode[2] + each_hammingcode[4] + each_hammingcode[5] + each_hammingcode[6] \
                                 + each_hammingcode[8] + each_hammingcode[9] + each_hammingcode[10] + each_hammingcode[11]
            each_origin_code = chr(int(each_origin_binary, 2))
            origin_code += each_origin_code
        return origin_code

    def err(self, pos, code):
        binary_code = self.to_binary(code)
        binary_list = list(binary_code)
        if binary_list[int(pos)-1] == '0':
            binary_list[int(pos)-1] = '1'
        elif binary_list[int(pos)-1] == '1':
            binary_list[int(pos)-1] = '0'
        new_binary = ''.join(binary_list)
        error_code = ''
        for x in range(0, int(len(new_binary)/8)):
            each_error_str = chr(int(new_binary[8*x:8*x+8], 2))
            error_code += each_error_str
        print('Insert a error bit in position: ' + str(pos))
        return error_code

    def to_binary(self, code):
        binary_code = ''
        for c in code:
            binary_str = "{0:08b}".format(ord(c))
            binary_code += binary_str
        return binary_code

class HammingAscii(object):

    def encode(self, char):
        binary_code = ''
        for t in char:
            binary_str = "{0:08b}".format(ord(t))
            hamming_str = HammingParity().get_parity(binary_str)
            binary_code += hamming_str
        return binary_code

    def decode(self, code):
        origin_code = ''
        for x in range(0, int(len(code)/12)):
            each_hammingcode = code[12*x:12*x+12]
            each_origin_binary = each_hammingcode[2] + each_hammingcode[4] + each_hammingcode[5] + each_hammingcode[6] \
                                 + each_hammingcode[8] + each_hammingcode[9] + each_hammingcode[10] + each_hammingcode[11]
            each_origin_code = chr(int(each_origin_binary, 2))
            origin_code += each_origin_code
        return origin_code

    def chk(self, code):
        error_position_array = []
        for x in range(0, int(len(code)/12)):
            each_hammingcode = code[12*x:12*x+12]
            each_origin_binary = each_hammingcode[2] + each_hammingcode[4] + each_hammingcode[5] + each_hammingcode[6] \
                                 + each_hammingcode[8] + each_hammingcode[9] + each_hammingcode[10] + each_hammingcode[11]
            each_origin_parity = HammingParity().get_parity(each_origin_binary)

            error_position = 0
            has_error = False
            for y in range(0, 12):
                if each_origin_parity[y] != each_hammingcode[y]:
                    has_error = True
                    error_position += y + 1
            if has_error:
                error_position_array.append(x * 12 + error_position)
        for e in error_position_array:
            print('There is an error bit in position: ' + str(e))
        return error_position_array

    def fix(self, code):
        binary_list = list(code)
        error_position_array = self.chk(code)
        for e in error_position_array:
            if binary_list[e-1] == '0':
                binary_list[e-1] = '1'
            elif binary_list[e-1] == '1':
                binary_list[e-1] = '0'
            print('Fix the error bit in position: ' + str(e))
        correct_code = ''.join(binary_list)
        origin_code = ''
        for x in range(0, int(len(correct_code)/12)):
            each_hammingcode = correct_code[12*x:12*x+12]
            each_origin_binary = each_hammingcode[2] + each_hammingcode[4] + each_hammingcode[5] + each_hammingcode[6] \
                                 + each_hammingcode[8] + each_hammingcode[9] + each_hammingcode[10] + each_hammingcode[11]
            each_origin_code = chr(int(each_origin_binary, 2))
            origin_code += each_origin_code
        return origin_code

    def err(self, pos, code):
        binary_list = list(code)
        if binary_list[int(pos)-1] == '0':
            binary_list[int(pos)-1] = '1'
        elif binary_list[int(pos)-1] == '1':
            binary_list[int(pos)-1] = '0'
        new_binary = ''.join(binary_list)
        print('Insert a error bit in position: ' + str(pos))
        return new_binary

class HammingFile():

    def file_read(self, input_filename):
        infile = open(input_filename)
        text = infile.read()
        infile.close()
        return text

    def file_write(self, output_filename, result_data):
        outfile = open(output_filename, 'w')
        outfile.write(result_data)


if __name__ == '__main__':

    type = sys.argv[1]
    command = sys.argv[2]

    if type == 'asc':
        if command == 'enc':
            text = HammingFile().file_read(sys.argv[3])
            result_data = HammingAscii().encode(text)
            HammingFile().file_write(sys.argv[4], result_data)

        elif command == 'dec':
            text = HammingFile().file_read(sys.argv[3])
            result_data = HammingAscii().decode(text)
            HammingFile().file_write(sys.argv[4], result_data)

        elif command == 'chk':
            text = HammingFile().file_read(sys.argv[3])
            HammingAscii().chk(text)

        elif command == 'fix':
            text = HammingFile().file_read(sys.argv[3])
            result_data = HammingAscii().fix(text)
            HammingFile().file_write(sys.argv[4], result_data)

        elif command == 'err':
            text = HammingFile().file_read(sys.argv[4])
            result_data = HammingAscii().err(sys.argv[3], text)
            HammingFile().file_write(sys.argv[5], result_data)

    elif type == 'bin':
        if command == 'enc':
            text = HammingFile().file_read(sys.argv[3])
            result_data = HammingBinary().encode(text)
            HammingFile().file_write(sys.argv[4], result_data)

        elif command == 'dec':
            text = HammingFile().file_read(sys.argv[3])
            result_data = HammingBinary().decode(text)
            HammingFile().file_write(sys.argv[4], result_data)

        elif command == 'chk':
            text = HammingFile().file_read(sys.argv[3])
            HammingBinary().chk(text)

        elif command == 'fix':
            text = HammingFile().file_read(sys.argv[3])
            result_data = HammingBinary().fix(text)
            HammingFile().file_write(sys.argv[4], result_data)

        elif command == 'err':
            text = HammingFile().file_read(sys.argv[4])
            result_data = HammingBinary().err(sys.argv[3], text)
            HammingFile().file_write(sys.argv[5], result_data)