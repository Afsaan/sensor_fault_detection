import sys
import os

def error_message_detail(error, error_detail:sys):
    _,_, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error = str(error)

    error_message = f"""error has occured and the the file name is {file_name} and the line number is {line_number}
                        and error is {error}"""
    
    return error_message

class SensorException(Exception):

    def __init__(self, error_message, error_details:sys):
        super().__init__(self, error_message)
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self): # dunder method to convert the output as string
        return self.error_message
