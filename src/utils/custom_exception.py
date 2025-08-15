import sys

class CostomException(Exception):
    def __init__(self,message:str,error_detail:Exception=None):
        self.error_message=self.get_detail_error_message(message,error_detail)
        super().__init__(self.error_message)


    def get_detail_error_message(self,message,error_detail):
        _,_,exc_tb=sys.exc_info()
        filename=exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        line_number=exc_tb.tb_lineno if exc_tb else "Unknown_line"
        return f"{message}, error:{error_detail}, filename: {filename}, line_number: {line_number}" 
    
    def __str__(self):
        return self.error_message
    
