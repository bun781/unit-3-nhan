import random
random.seed(1234)
class SEAT:
    def __init__(seat, seat_no:str, seat_type:str, car_no:int):
        seat.empty = random.randint(0,1)
        seat.seat_no = seat_no
        seat.car_no = car_no
        seat.seat_type = seat_type
    def __repr__(seat)->str:
        return f"<💺{seat.info()}>"

    def info(seat):
        status = "Empty" if seat.empty else "Occupied"
        return f"Seat No. {seat.seat_no} in car {seat.car_no} {seat.seat_type} class is {status}"

    def get_price(seat, base:int):
        classes = {"non-reserved": 1, "reserved": 1.1, "green": 1.25, "grand": 1.35}
        rate = classes[seat.seat_type]
        return int(base * rate)


################ Another Program
test_seat = SEAT(car_no = 1, seat_type = "grand", seat_no = "1A")
print(test_seat.info(), test_seat.get_price(base = 5700))

shinkansen = []
cars = [
    ('grand', 20),
    ('green', 40),('green', 40),
    ('reserved', 100),('reserved', 100),('reserved', 100),('reserved', 100),
    ('non-reserved', 200),('non-reserved', 200),('non-reserved', 200)
]

for i, car in enumerate(cars):
    car_type, num_seats = car

    car = {
        'class': car_type,
        'car_number': i + 1,
        'seats': []
    }

    for row in range(1, num_seats // 5 + 1):
        for col in "ABCDE":
            s = SEAT(seat_no = f"{row}{col}", seat_type = car_type, car_no = i+1)
            car['seats'].append(s)
    shinkansen.append(car)

def occupied_ratio(shinkansen, car_number):
    car = shinkansen[car_number-1]
    seats = car['seats']
    occupied_count = 0
    for seat in seats:
        occupied_count += 1 if seat.empty else 0
    total = len(seats)

    return occupied_count, occupied_count / total

total_profit = 0
for i,car in enumerate(shinkansen):
    sales = occupied_ratio(shinkansen, i+1)[0]
    car_type = car['class']
    classes = {"non-reserved": 1, "reserved": 1.1, "green": 1.25, "grand": 1.35}
    print(f"Car {i+1} has a total profit of {sales * 5700 * classes[car_type]:.0f} yen")
    total_profit += sales * 5700 * classes[car_type]
print(total_profit)

print(occupied_ratio(shinkansen, 4))
