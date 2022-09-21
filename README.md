Starting with Django

For this case, i am using a virtualenvironment to facilitate the translation to docker:

Create a folder where the project is located
mkdir test01

go into that folder
cd test01

Now, to create a virtual environment, inside that folder we put:
virtualenv -p python3 .

With the virtual environment created, we can start it using the following command:
source bin/activate

If we want to verify that the virtual environment is working properly, try using the following command:
pip -V

It should show the path to the environment's location

Now we can install Django
pip install django

If we want to stop the virtual environment, we can use the following command:
deactivate

We can also use the following command to verify the packages we've installed in the virtual environment:
pip freeze