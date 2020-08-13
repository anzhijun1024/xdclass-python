class MyException(Exception):
    def __init__(self,parameter):
        err = '非法入参{0}，分母不能为0'.format(parameter)
        Exception.__init__(self,err)
        self.parameter=parameter