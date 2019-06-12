import logging


fmt = '%(asctime)s : [Line: %(lineno)d]s:%(levelname)s - %(message)s'
logging.basicConfig(filename="inform.log", filemode='a', level=logging.DEBUG, format=fmt)



class RomanNumber(int):

    def __init__(self, number, cod=10):

        self.number = number
        self.cod = cod
        self.arg = int(self.number, self.cod)

    def convert(data):
        logging.debug('convert start')
        if not 1 <= data <= 3999:
            logging.critical(u'FATAL!!!')
            raise ValueError("Argument must be between 1 and 3999")

        one = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hund = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thou = ["", "M", "MM", "MMM", "MMMM"]

        t = thou[data // 1000]
        h = hund[data // 100 % 10]
        te = ten[data // 10 % 10]
        o = one[data % 10]
        return t + h + te + o
        # logging.debug(f'def convert return (t + h + te + o)')
        logging.debug(t + h + te + o)
    convert = property(convert)

    def __str__(self):
        return self.convert

    def __add__(self, value):
        return RomanNumber(str(self.arg + value))

    def __sub__(self, value):
        return RomanNumber(str(self.arg - value))

    def __floordiv__(self, value):
        return RomanNumber(str(self.arg // value))

    def __mul__(self, value):
        return RomanNumber(str(self.arg * value))

    def __eq__(self, value):
        return self.arg == value

    def __lt__(self, value):
        return self.arg < value


a = RomanNumber('27', 8)
b = RomanNumber('3015', 10)


logging.debug(a)
logging.debug(b)
logging.debug("added %s and %s to get %s" % (a, b, a+b))
logging.info("DONE!")

