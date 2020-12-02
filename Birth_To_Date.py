from datetime import date

today = date.today()

print("¿Cuántos días han pasado desde que naciste hasta hoy?")
birth_year = int(input("Ingresa tu año de nacimiento: \n"))
birth_month = int(input("Ingresa tu mes de nacimiento (1 al 12): \n"))
birth_day = int(input("Ingresa tu día de nacimiento: \n"))

new_date = date(birth_year, birth_month, birth_day)
delta_days = today - new_date
delta_months = (delta_days.days / 30)

print("Han pasado", delta_months, "meses desde que naciste!")