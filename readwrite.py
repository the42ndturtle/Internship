import Adafruit_PN532 as PN532
import binascii

CS = 18
MOSI = 23
MISO = 24
SCLK = 25

pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.SAM_configuration()

print('Waiting for MiFare card...')

while 1:
    uid = pn532.read_passive_target()
    if uid is None:
        continue
    print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
    data = pn532.mifare_classic_read_block(4)
    if data is None:
        print('Failed to read block 4!')
        continue
    print('Read block 4: 0x{0}'.format(binascii.hexlify(data[:4])))
