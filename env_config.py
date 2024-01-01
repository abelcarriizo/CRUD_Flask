from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['USER']
password = os.environ['PASSWORD']
host = os.environ['HOST']
database = os.environ['DATABASE']

DATABASE_CONNECTION_URI = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'