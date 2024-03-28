import Adafruit_DHT
import time
from threading import Thread
import busio  # For I2C communication with MQ-9 sensor
import board  # For I2C communication with MQ-9 sensor
import adafruit_gas  # Library for MQ-9 sensor

# Sensor pin numbers (replace with your actual pin numbers)
dht_pin = 4
pir_pin = 17  # Example pin for PIR sensor (adjust based on your wiring)
mq9_adc = busio.I2C(board.SCL, board.SDA)  # I2C connection for MQ-9 sensor

# Create an instance of the MQ-9 gas sensor (adjust gain as needed)
mq9 = adafruit_gas.MQ9(mq9_adc, gain=1000)  # 1000 is a common gain value, adjust based on your sensor

def read_dht():
    while True:
        try:
            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, dht_pin)
            if humidity is not None and temperature is not None:
                print(f"DHT: Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%")
            else:
                print("DHT sensor error!")
        except RuntimeError as e:
            print(f"DHT sensor error: {e}")
        time.sleep(5)

def detect_movement():
    while True:
        try:
            # Replace this with your PIR sensor reading logic
            # (e.g., using a GPIO library to read the pin state)
            movement_detected = True  # Simulate movement detection (replace with actual logic)
            if movement_detected:
                print("Movement detected!")
        except Exception as e:  # Catch any exception for robustness
            print(f"Movement sensor error: {e}")
        time.sleep(1)  # Adjust sleep time based on your sensor's requirements

def read_gas():
    while True:
        try:
            # Read gas resistance value from MQ-9 sensor
            resistance = mq9.resistance
            # Convert resistance to voltage (assuming a voltage divider circuit)
            # You might need to adjust the conversion based on your circuit setup
            voltage = 3.3 / (1 + resistance / 10000)
            # Calculate gas concentration using a sensor-specific formula
            # (replace this with the formula for your MQ-9 sensor and gas type)
            gas_concentration = voltage * 200  # Example formula, replace with actual calculation

            print(f"MQ-9: Gas concentration: {gas_concentration:.2f}")
        except RuntimeError as e:
            print(f"MQ-9 sensor error: {e}")
        time.sleep(2)  # Adjust sleep time based on your sensor reading frequency

# Create and start sensor threads
dht_thread = Thread(target=read_dht)
pir_thread = Thread(target=detect_movement)
mq9_thread = Thread(target=read_gas)
dht_thread.start()
pir_thread.start()
mq9_thread.start()

# Main program loop (can be used for other tasks while sensors run in the background)
while True:
    # Add your main program logic here (e.g., processing data from other sensors)
    time.sleep(3)