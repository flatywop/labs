from pydub import AudioSegment
import pydub

pydub.AudioSegment.converter = 'D:/gggg/все лабы/dopolnitelnye zadanya/.exe'
f = AudioSegment.from_wav("D:/gggg/все лабы/dopolnitelnye zadanya/trek.wav")

def speed_change(sound, speed=1.0):
    s = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return s.set_frame_rate(sound.frame_rate)

i = input('Введите значение: ')

fast = speed_change(f, float(i))

fast.export("новаяверсия.wav", format="wav")