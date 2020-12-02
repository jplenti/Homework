PI = 3.1416
Wheel_Diameter = 50
Circumference = PI * Wheel_Diameter

Distance_In_CM = 100000 # 1 KM

In_Km = Circumference / Distance_In_CM
Total_Turns = 1 / In_Km
print("La llanta da un total de", Total_Turns, "vueltas en 1 km.")
