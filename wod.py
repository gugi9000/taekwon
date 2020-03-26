from datetime import datetime
from random import seed, choice


def get_workout():
    workout = ['10 ap-chagi', '10 squats', '5 armstrækkere', '10 dolyo-chagi', '5 rygbøjninger', '10 momtong-makki', '10 arae-makki','30 sekunder i planke', '10 an-chagi', '10 bakat-chagi', '10 naeryo-chagi', '10 momtong-jireugi', '10 yeop-chagi', '10 sonnal eolgul bakat-chagi', '10 dwit-chagi', '10 sonnal momtong-makki', '10 jebipoom mok-chigi', '10 momtong-anmakki', '10 arae hecho-makki', '10 jump sqauts', '10 bandal-chagi', '10 eolgul-makki','30 sekunder side-planke', '5 mom-dollyo-chagi']
    seed(datetime.strftime(datetime.now(), '%Y%m%d'))
    return [choice(workout) for x in range(20)]


if __name__ == '__main__':
    for x in get_workout(): print(x)
