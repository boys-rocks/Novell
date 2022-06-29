FROM python:3.9

WORKDIR /novell

COPY ./  /novell/

RUN apt-get update
RUN apt-get install ffmpeg opus-tools libopus0 -y
RUN pip3 install pipenv

RUN pipenv sync
CMD pipenv run python bot.py
