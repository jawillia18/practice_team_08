import datetime
import time

def get_username(username):

    if isinstance(username, int):
        return False
    try:
        username = username.lower()
    except:
        pass   
    for i in username:
        try:
            int(i)
            return False
        except:
            pass
        if i >= 'a' and i <= 'z':
            pass
        else:
            return(False)
    if len(username) > 0:
        return True
    else:
        return False

def get_date(date_input): 
    """
    Validate date input in this format DD/MM/YYYY 
    """

    #split input date
    try:
        input_date = date_input.split("/")
        print(input_date)
    except:
        print("Invalid date format")
        return False

    #check if input format is valid
    try:
        datetime.date(int(input_date[2]), int(input_date[1]), int(input_date[0]))
    except:
        print("invalid date")
        return False
      
    #split current date
    current_date = str(datetime.date.today())
    current_date = current_date.split("-")

    # print(current_date, "current date")
    # print(input_date)

    #compare dates
    if current_date[0] <= input_date[2]:
        if current_date[1] <= input_date[1] :
            if current_date[2] <= input_date[0]:
                return True
        if current_date[1] >= input_date[1]:
            if current_date[0] < input_date[2]:
                return True
    print("Date has passed")
    return False

def get_time(time_in, date):
    """
    Validate time in this format HH:MM over 24h circle
    """

    import time

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    input_time = time_in.split(":")
    try:
        if int(input_time[0]) >=0 and int(input_time[0]) <= 24:
            if int(input_time[1]) >= 0 and int(input_time[1]) <= 59: 
                pass
            else:
                return False
        else:
            return False   
    except:
        return False
    current_time = current_time.split(":")
    print("time now now", current_time)
    
<<<<<<< HEAD
    #split input date
    try:
        input_date = date.split("/")
    except:
        return False

    #check if input format is valid
    try:
        datetime.date(int(input_date[2]), int(input_date[1]), int(input_date[0]))
    except:
        return False
    
    
    #split current date
    current_date = str(datetime.date.today())
    current_date = current_date.split("-")
    print("input date", input_date, "current date", current_date)
    #compare dates
    if (current_date[0] == input_date[2]):
        if (current_date[1] == input_date[1]):
            if current_date[2] == input_date[0]:
                if time[0] >= input_time[0]:
                    if time[1] > input_time[1]:
                        return True
                    else:
                        return False
                else:
                    return False
    else:
        return True
    print("here too")
    return False
=======
    # if date == 
    #     if time[0] >= input_time[0]:
    #         if time[1] > input_time[1]:
    #             return True
>>>>>>> 928fd927026a245119f09121c5ab0cd6ed64716c

def get_email(get_email):
    return True

def get_password(get_password):
    return True

