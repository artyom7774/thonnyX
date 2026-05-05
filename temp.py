
from pyrob import *

import traceback

@task
def ctask_task_8_30():
	try:
		pass
		rt(10)
	except Exception as e:
		traceback.print_exc()

run(1)
