def solution(phone_number):
    phone_number_list = list(phone_number)
    for i in range(len(phone_number)-4):
        phone_number_list[i] = '*'
    return "".join(phone_number_list)