This task was built for HouseOfApps by Ibrahim Alaybeyi


Run with docker/docker-compose
------------------------------

::

  docker-compose up --build


Run without docker
------------------

::
  
  cd nasaui
  python manage.py migrate
  python manage.py runserver

``python`` command default version must be ``3``

Then:
::
  localhost:8000
  or
  0.0.0.0:8000
 


If you want login directly (no register)::

Username: ``test``
Password: ``test``

