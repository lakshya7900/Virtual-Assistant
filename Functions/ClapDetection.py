import sounddevice as sd
import numpy as np

threshold = 70
clap = False

def DetectClap(indata, frames, time, status):
    global clap

    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > threshold:
        print('clapped')
        clap = True

def ListenForClap():
    with sd.InputStream(callback=DetectClap):
        return sd.sleep(1000)
    
# if __name__ == "__main__":
#     while True:
#         ListenForClap()
#         if clap == True:
#             break

#         else:
#             pass