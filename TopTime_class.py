__author__ = 'ZeeCee'


def sanitize(time_string):      # to Format all splitter to '.'
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter= ':'
    else:
        return(time_string)     # do nonthing to the rest splitter
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

# def get_coach_data(filename):       #open file and remove the excessive spaces in the string; seperate each item into list
#     try:
#         with open(filename) as f:
#             data = f.readline()
#         return(data.strip().split(','))
#     except IOError as ioerr:
#         print('File error: ' + str(ioerr) )
#         return (none)


class Athlete:                  # Creating a Class with 3 attributes
    def __init__(self, a_name, a_dob =None, a_times =[]):
        self.name=a_name
        self.dob= a_dob
        self.times =a_times
    def top3(self):                # the function is definded within the class, and applied to the class directly
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
    def add_time(self, time_value):     # takes a single element and append it to list self.times
        self.times.append(time_value)
    def add_times(self, list_of_times):     # takes a list of element and concatenate the list with list - self.times
        self.times.extend(list_of_times)



def get_coach_data(filename):       # Return Class
    try:
        with open(filename) as f:
            data = f.readline()
            temp = data.strip().split(',')
            return(Athlete(temp.pop(0), temp.pop(0), temp))         # Sort the elements before assigning to the Keys
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

'''
def get_coach_data(filename):       # Return a Dictionary with 3 keys
    try:
        with open(filename) as f:
            data = f.readline()
            temp = data.strip().split(',')
            return({'Name':temp.pop(0),
                    'DOB':temp.pop(0),
                    'Time':str(sorted(set([sanitize(t) for t in temp]))[0:3])})
    except IOError as ioerr:
        print('File error: ' + str(ioerr) )
        return (none)
'''

sarah = get_coach_data('sarah2.txt')
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')

print((sarah.name + "'s fastest times are : ").ljust(36)  + str(sarah.top3()))
print((james.name + "'s fastest times are : ").ljust(36)  + str(james.top3()))
print((julie.name + "'s fastest times are : ").ljust(36)  + str(julie.top3()))
print((mikey.name + "'s fastest times are : ").ljust(36)  + str(mikey.top3()))
