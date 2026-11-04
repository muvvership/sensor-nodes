let message = ""
let soil = 0
let humidity = 0
let temp = 0
let nodeId = 5
radio.setGroup(99)
PlantMonitor.startMon()
basic.pause(1000)
PlantMonitor.monitor_led_off()
basic.forever(function () {
    temp = PlantMonitor.readTemp()
    humidity = PlantMonitor.readHumidity()
    soil = PlantMonitor.readWetness()
    message = "" + nodeId + "," + temp + "," + humidity + "," + soil
    radio.sendString(message)
    basic.pause(30000)
})
