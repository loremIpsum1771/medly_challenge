# Medly challenge

This project features a backend implemented in the Python Django Rest Framework

## Quickstart/Setup:

1. Download the .zip file/clone repository
2. Install the python package manager Pip if it's not already installed using the instructions [here](https://pip.pypa.io/en/stable/installing/)
3. Next, install [pipenv](https://docs.python-guide.org/dev/virtualenvs/) with the command `pip install --user pipenv`
4. Once these are installed, `cd giant_machines_challenge`
5. Run `pipenv install --ignore-pipfile` to install pacakage dependencies and activate virtual environment
6. Run `python manage.py makemigrations` followed by `python manage.py migrate` (make sure to be in the same directory with `manage.py`)
7. Start the Django api server by running: `python manage.py runserver`

#### Additional:

- The virtual environment shell can be ended with the command `exit`
- To restart the virtual environment use `pipenv shell`
- API tests can be run with `python manage.py test`
