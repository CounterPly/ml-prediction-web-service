FROM python:3.6-buster

MAINTAINER Pranay Chandekar "pranayc6@gmail.com"

LABEL project="ml-prediction-web-service"

EXPOSE 8080

ARG APP_HOME=/opt/deployment
ARG PROJECT_NAME="ml-prediction-web-service"

ENV APP_HOME=${APP_HOME} \
    PROJECT_NAME=${PROJECT_NAME} \
    PROJECT_HOME=${APP_HOME}/${PROJECT_NAME}

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

COPY *-server.sh ${APP_HOME}/

ADD requirements.txt /

RUN pip3 install -r requirements.txt && \
    mkdir -p ${PROJECT_HOME}/src && \
    mkdir -p ${PROJECT_HOME}/logs && \
    mkdir -p ${PROJECT_HOME}/conf && \
    mkdir -p ${PROJECT_HOME}/resources && \
    chmod a+x ${APP_HOME}/start-server.sh

COPY train.py ${PROJECT_HOME}/

COPY prediction.py ${PROJECT_HOME}/

COPY src ${PROJECT_HOME}/src

COPY conf ${PROJECT_HOME}/conf

COPY resources ${PROJECT_HOME}/resources

WORKDIR ${PROJECT_HOME}
ENTRYPOINT ["/opt/deployment/start-server.sh"]