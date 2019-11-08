
import argparse



parser = argparse.ArgumentParser(description='Unpack npk file')
parser.add_argument("INPUT_NAME", help='input file')
parser.add_argument("OUTPUT_DIR", help='output dir')
args = parser.parse_args()

###文件夹//判断 

try:
    f = open(args.INPUT_NAME,'rb')
    s_file = f.read()
    f.close()
except:
    print 'Open file failed!'
    exit()

if args.OUTPUT_DIR[-1:-2] != '/':
    args.OUTPUT_DIR = args.OUTPUT_DIR + '/'


def byte_to_int(ss):
    try:
        a = ord(ss[0])
        b = ord(ss[1])
        c = ord(ss[2])
        d = ord(ss[3])
    except:
        return None

    return  a | b << 8 | c << 16 | d << 24



s_size = s_file[4:8]
s_size = byte_to_int(s_size)

s_size = (s_size * 8 - s_size) * 4

s_offset = s_file[0x14:0x18]
s_offset = byte_to_int(s_offset)



# s_file = byte(s_file, encoding = "utf8")
s_list = s_file[s_offset:s_offset + s_size]

try:
    cur_off = 0
    for i in range(s_size / (4 * 7)):
        cur_off = i * 4 * 7
        s_data_off = s_list[cur_off + 4: cur_off + 8]
        s_data_off = byte_to_int(s_data_off)

        s_size_off = s_list[cur_off + 8: cur_off + 12]
        s_size_off = byte_to_int(s_size_off)

        f = open(args.OUTPUT_DIR + "npkdump-" + str(i),'wb')
        f.write(s_file[s_data_off:s_data_off + s_size_off])
        f.close()
except:
    print 'Decode error'

 