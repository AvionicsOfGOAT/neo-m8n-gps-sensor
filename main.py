import serial
from pyubx2 import UBXReader

stream = serial.Serial("/dev/ttyAMA2", baudrate=9600, timeout=50)
ubr = UBXReader(stream)
file =  open("gps_data.txt", "a")
while True:
    (raw_data, parsed_data) = ubr.read()
    lines = str(raw_data).split('$')
    gngll_data = ""
    for line in lines:
        if line.startswith('GNGLL'):
            gngll_data = line
            break
    gngll_data = gngll_data.replace(',,', ',')
    parts = gngll_data.split(',')

    if len(parts) > 5:  # 유효성 확인
        try:
            latitude = float(parts[1][:2]) + float(parts[1][2:]) / 60
            longitude = float(parts[3][:3]) + float(parts[3][3:]) / 60
            file.write(f"{{ lat: {location['lat']}, lng: {location['lng']} }},\n")
        except ValueError:
            continue
