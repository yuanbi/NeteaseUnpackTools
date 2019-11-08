import zlib
import argparse  

def init_rotor():
    asdf_dn = 'j2h56ogodh3se'
    asdf_dt = '=dziaq.'
    asdf_df = '|os=5v7!"-234'
    asdf_tm = asdf_dn * 4 + (asdf_dt + asdf_dn + asdf_df) * 5 + '!' + '#' + asdf_dt * 7 + asdf_df * 2 + '*' + '&' + "'"
    import rotor
    rot = rotor.newrotor(asdf_tm)
    return rot


def _reverse_string(s):
    l = list(s)
    l = map(lambda x: chr(ord(x) ^ 154), l[0:128]) + l[128:]
    l.reverse()
    return ''.join(l)


parser = argparse.ArgumentParser(description='Decode npk ')
parser.add_argument("INPUT_NAME", help='input file')
parser.add_argument("OUTPUT_NAME", help='output file')
args = parser.parse_args()

fp = None
data = None
try:
    fp = open(args.INPUT_NAME,'rb')
    data = fp.read()
    fp.close()
except:
    print "File read error"
    exit()
rotor = init_rotor()
data = rotor.decrypt(data)
data = zlib.decompress(data)
data = _reverse_string(data)

fp = open(args.OUTPUT_NAME,'wb')
data = fp.write(data)
fp.close()

#data = marshal.loads(data)