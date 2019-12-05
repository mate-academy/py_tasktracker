# py_tasktracker

In this exercise you should implement a simple task tracker. There are two kinds of tasks: fixed payment task and hourly
payment task. Any task can be assigned to a worker. The worker has a name and can confirm task completion to the
log. The log should be able to produce reports with worker's names and payment for completed tasks.
You should offer your own design for class relationships in this exercise.

To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

To run all style checkers and tests use commands:

`pytest `

`flake8 tasks`

`pylint tasks`

`mypy --ignore-missing-imports .`
