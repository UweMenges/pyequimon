#!/bin/bash
# bootstrapper for virtual django environment
# to be run after checkout. this will create the
# virtual environment and install the required
# packages from requirements.txt

REALPATH=$(readlink -f "$0")
BASEDIR=`dirname ${REALPATH}`
cd ${BASEDIR}

if [ ! -f requirements.txt ]; then
  echo "$0: requirements.txt missing - are you in root folder of the project?"
fi 

# check if virtualenv is already there, 
# initialize it if not
if [ ! -f bin/activate ]; then
  echo "setting up virtualenv..."
  virtualenv .
fi

# activate virtualenv
echo "activating virtualenv"
source bin/activate

# install requirements
echo "installing requirements"
pip -E . install -r requirements.txt

# create media folder, if necessary 
if [ ! -d media ]; then
  mkdir media
fi

# the django dir may be different with different python versions,
# better glob it and recreate id every time
ADMIN_MEDIA_DIR=`dirname ./lib/python*/site-packages/django/contrib/admin/media/`
cd media
rm -f admin-media
ln -s .${ADMIN_MEDIA_DIR}/media admin-media
cd ..

# create log folder, if necessary
if [ ! -d log ]; then
  mkdir log
fi 
# check if the django project is already there.
# if not, this is the first run and it should be
# created
if [ ! -d proj ]; then
  echo "creating django project pyequimon"
  mkdir proj
  cd proj
  django-admin.py startproject pyequimon
  
  # apply the patches from ../../patches to project
  cd pyequimon
  for i in ../../patches/*.patch; do
    patch -p3 < $i
  done
  
  # convenience is everything
  chmod a+x manage.py

fi

# finished
echo "virtualenv was successfully created. please note that you must"
echo " source bin/activate"
echo "this virtualenv before working with it (the script can't do it for you)."
