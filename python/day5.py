with open("../input/day5_1.txt") as f:
    lines = f.readlines()


ROWS_INITIAL = list(range(0, 128))
COLS_INITIAL = list(range(0, 8))


def get_val(val_info, vals):
    if not val_info:
        return vals[0]
    r = val_info[0]
    len_vals_div_2 = int(len(vals)/2)
    if r in ("F", "L"):
        vals = vals[0:len_vals_div_2]
    elif r in ("B", "R"):
        vals = vals[len_vals_div_2::]
    return get_val(val_info[1::], vals)


def get_row(row_info, rows=ROWS_INITIAL):
    return get_val(row_info, rows)


def get_col(col_info, cols=COLS_INITIAL):
    return get_val(col_info, cols)


def get_seat_id(row, col):
    return row * 8 + col


test_row = 'FBFBBFF'
assert get_row(test_row) == 44
test_col = 'RLR'
assert get_col(test_col) == 5

seat_ids = []

for line in lines:
    row = get_row(line[0:7])
    col = get_col(line[7::])
    seat_ids.append(get_seat_id(row, col))
print(max(seat_ids))


# Part 2

all_seats_ids = [
    get_seat_id(r, c)
    for r in ROWS_INITIAL[11:-16]  # Some rows @back and front are unused.
    for c in COLS_INITIAL
]
front_seats_ids = [
    get_seat_id(0, c)
    for c in COLS_INITIAL
]
back_seats_ids = [
    get_seat_id(127, c)
    for c in COLS_INITIAL
]
# print(all_seats)
unused_seats = sorted(list(set(all_seats_ids) - set(seat_ids)))
print(unused_seats[1])

