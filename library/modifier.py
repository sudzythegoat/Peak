import pymem

class Peak:
    @staticmethod
    def modify(process, address, amount):
        pm = pymem.Pymem(process)
        pm.write_int(address, amount)

modify = Peak.modify
