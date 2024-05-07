# imagen con python
FROM python:3

# label del maintainer
LABEL maintainer="edwin.taquichiri@jalasoft.com"

# copy the code to /opt/app folder
COPY . /opt/app
WORKDIR /opt/app

# update system
RUN apt-get update

# install java always add -y option
RUN apt-get install -y default-jre
RUN java -version

# install allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb
RUN dpkg -i allure_2.18.1-1_all.deb

# install/upgrade pip
RUN python3 -m pip install --upgrade pip

# install virtualenv librarary/package
RUN python3 -m pip install --user virtualenv

# create virtualenv for the framework
RUN python3 -m venv env

# activate virtual environment
RUN . env/bin/activate

# install requirements
RUN python3 -m pip install -r requirements.txt

# execute tests
RUN python3 -m behave

#comand line on terminal
#docker install - need have docker
#$docker build -t -auto_framework_b . #cualquier nombre
#$docker run -ti -auto_framework_b bash  #para ver reportes
#app#allure serve reports/allure/

