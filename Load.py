from datetime import datetime
from tabulate import tabulate
import json

Token = open('Token.json', 'rt')

Token_Loader = json.load(Token)

Token_String = f"{Token_Loader['Token']}"

Token.close()

table = [['Token Loaded',f'At : {datetime.now()}']]

print(tabulate(table , tablefmt="grid"))