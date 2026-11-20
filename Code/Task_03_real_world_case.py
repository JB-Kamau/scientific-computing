import numpy as np
import timeit

# REAL-WORLD CASE: RMS (effective) value of a vibration/AC sensor signal.
# A sensor output is sampled by a microcontroller ADC. We need the RMS value
# of the signal, which means squaring every sample, averaging, and taking the
# square root. The sine function is applied to a whole array at once.
#
# ASSUMPTIONS
#  - The sensor output is a 50 Hz sine wave of amplitude 1.5 V
#    centred on 1.65 V (the middle of a 3.3 V ADC range).
#  - Sampling rate is 100,000 samples per second for 10 seconds
#    (1,000,000 samples).
#  - Random noise with standard deviation 0.05 V is added.
#  - The signal is simulated, not measured from a real sensor.

fs = 100_000          # sampling rate (samples per second)
duration = 10         # seconds
freq = 50             # signal frequency (Hz)
amplitude = 1.5       # volts
offset = 1.65         # volts (DC level)
noise_std = 0.05      # volts

rng = np.random.default_rng(42)
t = np.arange(fs * duration) / fs                       # time of every sample
signal = offset + amplitude * np.sin(2 * np.pi * freq * t) \
         + rng.normal(0, noise_std, t.size)

def rms_loop(x):
    total = 0.0
    for value in x:
        centred = value - offset
        total += centred ** 2
    return (total / len(x)) ** 0.5

def rms_vectorized(x):
    centred = x - offset
    return np.sqrt(np.mean(centred ** 2))

loop_time = timeit.timeit(lambda: rms_loop(signal), number=1)
vector_time = timeit.timeit(lambda: rms_vectorized(signal), number=3) / 3

expected = np.sqrt(amplitude**2 / 2 + noise_std**2)

print(f"Number of samples: {signal.size:,}")
print(f"RMS (loop): {rms_loop(signal):.4f} V")
print(f"RMS (vectorized): {rms_vectorized(signal):.4f} V")
print(f"RMS expected from theory: {expected:.4f} V")
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")