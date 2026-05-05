
from pyrob import *

import traceback

@task
def ctask_task_8_18():
	try:
		pass
		
	except Exception as e:
		traceback.print_exc()

run(2)
