# # """
# # Response time - single-threaded
# # """
# # 
from machine import Pin
import time
import random
import json
import urequests
import requests
import network


N: int = 10
sample_ms = 10.0
on_ms = 500

WRITE_KEY = "YLMMTXOTYLNP4Q6M"
HOTSPOT_PASS = "29032085"
SSID = "SDK"


def conn_to_wifi(ssid, passk):
    try:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, passk)
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            time.sleep(1)
#         print(wlan.ifconfig())
    except Exception as e:
        print(e)
def push(data, field, key = WRITE_KEY):
    WRITE_URL = f"http://api.thingspeak.com/update.json?api_key={key}&field{field}={data}"
    print("\n Pushing to database... ")
    request = urequests.post(WRITE_URL)
    time.sleep(15)
    print(str(data)+ " data sent to field " + str(field))



def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    json_filename: str
        The name of the file to write to. This will overwrite any existing file.

    data: dict
        Dictionary data to write to the file.
    """

    with open(json_filename, "w") as f:
        json.dump(data, f)


def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")
   

    t_good = [x for x in t if x is not None]
   

    # add key, value to this dict to store the minimum, maximum, average response time
    # and score (non-misses / total flashes) i.e. the score a floating point number
    # is in range [0..1]
    print("Your fastest time was:  " + str(min(t_good))+ "ms! \n")
    print("Your slowest time was: hold " +str(max(t_good))+ "ms! \n")
    print("Your average time was: hold " + str(sum(t_good)/len(t_good))+"ms! \n")
    
    print(t_good)
    data = {"fastest-time":(min(t_good)), "slowest-time":(max(t_good)), "average-time":(sum(t_good)/len(t_good))}

    # %% make dynamic filename and write JSON

    now: tuple[int] = time.localtime()

    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"

    print("write", filename)

    write_json(filename, data)
    return min(t_good), max(t_good), sum(t_good)/len(t_good)
    #print(write_json(filename, data))




        

if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files

    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    blinker(5, led)

    data = scorer(t)
    conn_to_wifi(SSID, HOTSPOT_PASS)
    time.sleep(1)
    push(data[0], 1) #pushing fastest speed
    push(data[1], 2) #pushing slowest speed
    push(data[2], 3) #pushing avg speed
    print("Data push complete ")
#

#     
#     request_json = request.json()
#     print(request_json)
#     
#     
    
#     #send data to database

