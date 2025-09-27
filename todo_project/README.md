# create & activate venv
python -m venv venv
venv\Scripts\activate

# upgrade tooling
python -m pip install --upgrade pip setuptools wheel

# (then install your project deps if needed)
pip install -r requirements.txt

# from folder with manage.py (venv active)
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver

