from smart_home import temperature, light , security

#control light
light.turn_on()
light.turn_off


#set room temp
temperature.set_temperature(22)

#control security
security.active_alarm()
security.deactive_alarm()