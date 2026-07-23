from gpiozero import DistanceSensor

# Bỏ giới hạn max_distance để cảm biến dễ đọc hơn
sensor = DistanceSensor(echo=24, trigger=23)

try:
    khoang_cach = sensor.distance * 100
    print(f"{khoang_cach:.1f}")
except Exception as e:
    print("0")
