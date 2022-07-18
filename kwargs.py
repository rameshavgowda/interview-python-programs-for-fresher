def arg_list(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
arg_list(arg1="argument1",arg2="argument2")