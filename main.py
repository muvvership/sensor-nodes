message = ""
soil = 0
humidity = 0
temp = 0
nodeId = 2
radio.set_group(99)
PlantMonitor.start_mon()
basic.pause(1000)

def on_forever():
    global temp, humidity, soil, message
    temp = PlantMonitor.read_temp()
    humidity = PlantMonitor.read_humidity()
    soil = PlantMonitor.read_wetness()
    message = "" + str(nodeId) + "," + ("" + str(temp)) + "," + ("" + str(humidity)) + "," + ("" + str(soil))
    radio.send_string(message)
    basic.pause(30000)
basic.forever(on_forever)
