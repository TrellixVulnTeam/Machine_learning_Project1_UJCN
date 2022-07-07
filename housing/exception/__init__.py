import os
import sys

class HousingException(Exception):
    def __init__(self, error_message:Exception, error_details:sys) -> None:
        super().__init__(error_message)
        self.error_message = HousingException.get_detailled_error_message(error_message=error_message,
                                                                            error_details= error_details)
    
    
    @staticmethod
    def get_detailled_error_message(error_message:Exception, error_details:sys)->str:
        '''
        error_message: Exception Object
        error_details:obj of sys module
        '''

        _,_ ,exec_tb = error_details.exc_info()
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        try_block_line_number = exec_tb.tb_lineno
        error_message = f"""error occured in script:[ {file_name} ] 
        at try block line number:[ {try_block_line_number} ] 
        and exeption block line number:[ {exception_block_line_number} ] 
        error message:[ {error_message} ]"""
        return error_message
    
    def __str__(self):
        return self.error_message

    def __repr__(self)-> str:
        return HousingException.__name__.str()