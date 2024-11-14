#! /bin/bash

# change to the root directory of the project
cd ..

# run black on the taskmanager package
black taskmanager

# run flake8 on the taskmanager package
flake8 taskmanager

# run bandit on the taskmanager package
bandit -r taskmanager
