
from pyrob import *

import traceback

@task
def ctask_task_1_1():
	try:
		pass
		dn()
		rt(2)
	except Exception as e:
		traceback.print_exc()

run(1)
