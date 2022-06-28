import time

class TrafficLight:
    color = 'цвет'

    def running(self):
        print('Светофор включен:')
        while True:
            print('красный')
            time.sleep(7)
            print('жёлтый')
            time.sleep(2)
            print('зелёный')
            time.sleep(7)
            print('жёлтый')
            time.sleep(2)

tl = TrafficLight()
tl.running()