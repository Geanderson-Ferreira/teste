from os import environ
from dotenv import load_dotenv

load_dotenv()

print(environ['MYCREDENTIAL'])