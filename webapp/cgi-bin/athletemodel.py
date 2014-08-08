__author__ = 'ZC'

import pickle
from athletelist import AthleteList

def get_coach_data(filename):       # Return Class
    try:
        with open(filename) as f:
            data = f.readline()
            temp = data.strip().split(',')
            return(AthleteList(temp.pop(0), temp.pop(0), temp))         # Sort the elements before assigning to the Keys
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

def put_to_store(files_list):
    all_athletes={}
    # code here: the function is called with a list of filenames as its sole argument
    for each_file in files_list:
        ath=get_coach_data(each_file)
        all_athletes[ath.name]=ath      # ath.name -- key ;  ath -- the value of the AthleteList object instance
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File Error (put_to_store): ' +str(ioerr) )
    return(all_athletes)

def get_from_store():
    all_athletes={}
    # code here: the function is called to get the dictionary from the file, so that it can be returned to the caller
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File Error (get_from_store): ' +str(ioerr) )
    return(all_athletes)
