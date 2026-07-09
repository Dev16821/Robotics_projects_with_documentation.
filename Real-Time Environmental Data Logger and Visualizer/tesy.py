import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configure serial connection
ser = serial.Serial('/dev/ttyACM1', 38400, timeout=1)
time.sleep(2)

# Maintain a fixed-size queue for a rolling window of 100 points
data_window = collections.deque([0]*100, maxlen=100)

fig, ax = plt.subplots()
line, = ax.plot(data_window)
ax.set_ylim(0, 1023) # Match our 10-bit ADC bounds
ax.set_xlabel("light intesity")
ax.set_ylabel("ADC Value (0-1023)")

def update(frame):
    # Consume all available data points in the serial buffer to prevent accumulation
    while ser.in_waiting > 0:
        raw_data = ser.readline().decode('utf-8').strip()
        if raw_data.isdigit():
            # Apply your exponential filter here if desired
            data_window.append(int(raw_data))
    
    line.set_ydata(data_window)
    return line,

# Pass your verified 42ms interval here
ani = animation.FuncAnimation(fig, update, interval=42, blit=True)
plt.show()