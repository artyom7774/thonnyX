
from pyrob import *

import traceback

@task
def c7upr_upr_12_1():
	try:
		pass
		dn(2)
		rt(4)
		up(2)
	except Exception as e:
		traceback.print_exc()

run(1)
