import sys
if __name__ == "__main__":
    with open(sys.argv[1], 'rb+') as f:
        donnes = bytearray(f.read())
        donnes[0x2598] = 0x84
        donnes[0x2599] = 0x8F
        donnes[0x259A] = 0x88
        donnes[0x259B] = 0x93
        donnes[0x259C] = 0x84
        donnes[0x259D] = 0x82
        donnes[0x259E] = 0x87
        checksum = 0xff
        for i in donnes[0x2598:0x3523]:
            checksum -= i
        donnes[0x3523] = checksum & 0xFF
        f.seek(0)
        f.write(donnes)

