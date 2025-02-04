import asyncio
from bleak import BleakClient
import RPi.GPIO as GPIO
import time

# Bluetooth MAC-adres van Eco-Worthy BMS
BMS_MAC = "XX:XX:XX:XX:XX:XX"  # Vervang dit met het echte MAC-adres!

# GPIO-instellingen voor generator
GENERATOR_PIN = 17  # Pas dit aan indien nodig
GPIO.setmode(GPIO.BCM)
GPIO.setup(GENERATOR_PIN, GPIO.OUT)
GPIO.output(GENERATOR_PIN, GPIO.LOW)  # Zorgt dat generator uit blijft bij opstarten

# Instellingen die de gebruiker kan aanpassen
START_VOLTAGE = 11.5  # Wanneer generator moet starten
STOP_VOLTAGE = 13.8   # Wanneer generator moet stoppen
EVENING_CHARGE_TIME = "17:00"  # Tijd voor extra opladen

async def read_bms():
    async with BleakClient(BMS_MAC) as client:
        if not await client.is_connected():
            print("⚠ Geen verbinding met BMS!")
            GPIO.output(GENERATOR_PIN, GPIO.LOW)  # Generator uitschakelen voor veiligheid
            return None
        
        # Lees batterijvoltage (pas de UUID aan als nodig)
        battery_data = await client.read_gatt_char("00002A19-0000-1000-8000-00805f9b34fb")
        voltage = int.from_bytes(battery_data, byteorder="little") / 10.0  # Spanningswaarde
        print(f"🔋 Huidige batterijspanning: {voltage}V")
        return voltage

async def control_generator():
    while True:
        voltage = await read_bms()
        
        if voltage is None:
            print("⚠ Geen spanning uit BMS, generator uit voor veiligheid!")
            GPIO.output(GENERATOR_PIN, GPIO.LOW)

        elif voltage < START_VOLTAGE:
            print("⚠ Lage spanning! Generator AAN!")
            GPIO.output(GENERATOR_PIN, GPIO.HIGH)

        elif voltage > STOP_VOLTAGE:
            print("✅ Batterij vol, generator UIT!")
            GPIO.output(GENERATOR_PIN, GPIO.LOW)

        await asyncio.sleep(30)  # Controleer elke 30 seconden

try:
    asyncio.run(control_generator())
except KeyboardInterrupt:
    GPIO.cleanup()
    print("🔴 Script gestopt en GPIO opgeruimd.")
