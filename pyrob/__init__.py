#!/usr/bin/python3

import functools
import importlib
import logging
import sys

from pyrob import core
from pyrob import utils

tasks_to_run = []

logger = logging.getLogger(__name__)


def get_task_class(task_id):
    # TODO ge

    task = task_id[1:].replace("_", "&", 1).split("&")

    spec = importlib.util.spec_from_file_location("PYROB", f"tasks/pyrob/{'/'.join(task)}.py")
    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    # module = importlib.import_module('pyrob.tasks.' + task_id)

    return module.Task


def task(*args, **kwargs):

    def decorator(f):

        @functools.wraps(f)
        def wrapper():
            task_id = f.__name__
            clazz = get_task_class(task_id)
            passed = True

            countCompletedTasks = 0

            for i in range(clazz.CHECKS):
                core.on_position_changed = None

                _task = clazz()
                with utils.allow_internal(True):
                    _task.load_level(i)

                core.on_position_changed = viz.update_robot_position(delay)
                core.on_cell_type_changed = viz.update_cell_color

                with utils.allow_internal(True):
                    viz.render_maze(task_id)
                    core.on_position_changed(*core.get_pos())

                crashed = False
                error = False
                try:
                    f()
                except Exception as e:
                    logger.exception('Ошибка')
                    passed = False
                    error = True
                    if isinstance(e, core.RobotCrashed):
                        crashed = True

                with utils.allow_internal(True):
                    passed = passed and _task.check_solution()

                if passed:
                    logger.debug('Test #{} задание {} пройдено'.format(i + 1, task_id))
                    viz.on_task_completed(True)

                    countCompletedTasks += 1

                else:
                    logger.error('Test #{} задание {} провалено'.format(i+1, task_id))
                    if crashed:
                        viz.on_robot_crashed()
                    elif error:
                        viz.on_task_errored()
                    else:
                        viz.on_task_completed(False)

                    break

            import threading

            def send(answer):
                import socket

                try:
                    sock = socket.socket()
                    sock.connect(("localhost", 3521))
                    sock.send(str(int(answer)).encode())

                    data = sock.recv(1024)

                except Exception:
                    pass

                finally:
                    sock.close()

            # print(countCompletedTasks, clazz.CHECKS)

            thr = threading.Thread(target=lambda: send(countCompletedTasks == clazz.CHECKS))
            thr.daemon = True
            thr.start()

            return passed

        tasks_to_run.append(wrapper)
        return wrapper

    if 'delay' in kwargs:
        delay = kwargs['delay']
        return decorator
    else:
        delay = None
        return decorator(args[0])


def run_tasks(speed: int = 1, verbose=False, headless=False):
    logging.basicConfig(level=(logging.DEBUG if verbose else logging.INFO))

    global viz
    viz = importlib.import_module('pyrob.dummy_viz' if headless else 'pyrob.viz')

    viz.init(0.15 / speed if speed != 0 else 0)

    passed = 0

    for t in tasks_to_run:
        print('Задание: {}'.format(t.__name__))

        status = t()

        if status:
            passed += 1

        print(f"Задание {t.__name__} {'выполнено' if status else 'сделано с ошибкой'}")
        # logger.info('Задание {} выполнено: {}'.format(t.__name__, ('+' if status else '-')))

    print('Решено: {} / {}'.format(passed, len(tasks_to_run)))

    return passed == len(tasks_to_run)

from pyrob.core import move_left, move_right, move_up, move_down

from pyrob.core import wall_is_above, wall_is_beneath, wall_is_on_the_left, wall_is_on_the_right

from pyrob.core import fill_cell, cell_is_filled

from pyrob.core import mov
from pyrob import task
from pyrob import run_tasks

left = lt = move_left
right = rt = move_right
up = move_up
down = dn = move_down

wall_left = w_left = wlt = wall_is_on_the_left
wall_right = w_right = wrt = wall_is_on_the_right
wall_up = w_up = wup = wall_is_above
wall_down = w_down = wdn = wall_is_beneath

fill = fill_cell
filled = is_fill = cell_is_filled

run = run_tasks
