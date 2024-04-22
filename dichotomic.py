
def dichotomic(input_list,val):

    if len(input_list)==1:
        if input_list[0]==val:
            return True
        else:
            return False
    else:
        i = len(input_list)//2
