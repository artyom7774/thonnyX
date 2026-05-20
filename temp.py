
from pyrob import *

import traceback

@task
def c7upr_upr_12_6():
	try:
		pass
		exec(open('code.py', 'r', encoding='utf-8').read())
	except Exception as e:
		traceback.print_exc()

run(1)
