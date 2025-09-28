# create venv
python -m venv venv

# activate venv
venv\Scripts\activate

# delete venv
make sure the virtual environment venv is deactivated. Then just delete the folder.

# to deactivate
deactivate



# upgrade tooling
python -m pip install --upgrade pip setuptools wheel

# (then install your project deps if needed)
pip install -r requirement.txt

# setup mysql at following path
'cd infra\mysql'

# then go to commands.md file in this path. follow instructions there. After setting up the db, user and privilages; run below command after returning to project path in your terminal

# from folder with manage.py (venv active)
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver


# after application has stopped; to stop the docker image; again to to  commands.md file
