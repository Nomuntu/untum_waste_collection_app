
from setuptools import setup, find_packages

setup(
    name="waste_collection_app",
    version="0.1.0",
    author="Nomuntu Ndhlovu",
    description="A Flask-based web application for deployment on Heroku",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['alembic==1.6.5', 'atomicwrites==1.4.0', 'attrs==21.2.0', 'bcrypt==3.2.0', 'bidict==0.21.2', 'cachelib==0.1.1', 'certifi==2021.5.30', 'cffi==1.14.5', 'chardet==4.0.0', 'click==8.0.1', 'colorama==0.4.4', 'dnspython==1.16.0', 'eventlet==0.30.2', 'Flask==2.0.1', 'Flask-Login==0.5.0', 'Flask-Migrate==3.0.1', 'Flask-Session==0.3.2', 'Flask-SocketIO==5.1.0', 'Flask-SQLAlchemy==2.5.1', 'greenlet==1.1.0', 'gunicorn==20.1.0', 'idna==2.10', 'iniconfig==1.1.1', 'itsdangerous==2.0.1', 'Jinja2==3.0.1', 'Mako==1.1.4', 'MarkupSafe==2.0.1', 'packaging==20.9', 'Pillow==8.2.0', 'pluggy==0.13.1', 'psycopg2-binary==2.8.6', 'py==1.10.0', 'pycparser==2.20', 'PyJWT==1.7.1', 'pyparsing==2.4.7', 'pytest==6.2.4', 'python-dateutil==2.8.1', 'python-editor==1.0.4', 'python-engineio==4.2.0', 'python-socketio==5.3.0', 'pytz==2021.1', 'requests==2.25.1', 'six==1.16.0', 'SQLAlchemy==1.4.17', 'toml==0.10.2', 'urllib3==1.26.5', 'Werkzeug==2.0.1', 'twilio==6.59.1'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
