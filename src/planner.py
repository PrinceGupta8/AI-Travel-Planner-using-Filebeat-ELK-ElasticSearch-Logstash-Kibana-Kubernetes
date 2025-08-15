from src import config
from src.itinary_chain import generate_itinary
from src.utils.logger import get_logger
from src.utils.custom_exception import CostomException
from langchain_core.messages import HumanMessage,AIMessage

logger=get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages=[]
        self.itinary=[]
        self.city=""
        self.interests=""

    def set_city(self,city):
        try:
            self.city=city
            self.messages.append(HumanMessage(content=city))
            logger.info("city set successfuly")
        except Exception as e:
            logger.error(msg=f"error while setting city :{e}")
            raise CostomException("failed to set city",e)


    def set_interests(self,interests):
        try:
            self.interests=interests
            self.messages.append(HumanMessage(content=interests))
            logger.info("interests set successfuly")
        except Exception as e:
            logger.error(msg=f"error while setting interests :{e}")
            raise CostomException("failed to set interests",e)
        
    def create_itinary(self):
        try:
            itinary=generate_itinary(city=self.city,interests=self.interests)
            self.itinary=itinary
            self.messages.append(AIMessage(content=self.itinary))
            logger.info("itinary generated successfuly")
        except Exception as e:
            logger.error(msg=f"error while generated itinary :{e}")
            raise CostomException("failed to generated itinary",e)


