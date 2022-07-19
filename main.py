import datetime as dt
from application.salary import calculate_salary as cal_sal
from application.people import get_employees as get_empl



if __name__ == '__main__':
    print(dt.datetime.now())
    cal_sal()
    get_empl()
    
    