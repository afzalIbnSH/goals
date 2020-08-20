# Goals API
This repo define RESTful API to create and manage your organization's goals.

# Plans
## Free Account
* Admin can't create additional users to his organisation
* Admin can create and manage goals for his organization

## Enterprise Account
* Admin can create additional users to his organisation
* Any user from the same organisation can create goals
* All users can manage all goals of the organization


# Python version: 3.8.5

# Setup
```
python3 -m venv ~/your-python-virtualenvs/goals
source ~/your-python-virtualenvs/goals/bin/activate
pip install -r requirements.txt
# For some reason gunicorn isn't picking up the python virtualenv path without a refresh
deactivate
source ~/your-python-virtualenvs/goals/bin/activate
python3 manage.py migrate
```

# Host
Run `gunicorn --bind $HOST:$PORT enterprise_goals.wsgi --daemon`.
Eg: `gunicorn --bind localhost:8001 enterprise_goals.wsgi --daemon`.
See the APIs at `$HOST:$PORT/api/v1/swagger/`.
