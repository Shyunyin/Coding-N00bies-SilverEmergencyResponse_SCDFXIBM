# RMS is the root-mean-square of forces acceleration in all axis of a body which the accelerometer will measure
RMS = float(input("RMS value"))
#input is from the accelerometer 
if float(RMS)>8.0000:
    print("\nElderly could have fallen")
#activate severity.py in watson assistant to run
    def time():
        print("Elderly could have fallen")
    t=Timer(1800.0,time)
    t.start()
elif float(RMS)>0.0000:
#if there is inactivity for a certain amount of time when the elderly is in the toilet
    print("\nElderly is not moving and may be unconscious")
elif float(RMS)<1.0000:
    print("\nElderly is not moving and may be unconscious")
else: 
    print("\nNormal")
