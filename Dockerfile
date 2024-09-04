FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install build-essential wget git vim curl zip

RUN apt-get -y install python3 python-is-python3
RUN apt-get -y install python3-pip

RUN apt-get install -y npm
RUN npm install -g aws-cdk
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

# Install Maven
RUN apt-get install -y openjdk-8-jdk
RUN curl -O https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-common/apache-maven-3.6.0-bin.tar.gz
RUN tar -xf apache-maven-3.6.0-bin.tar.gz
RUN rm apache-maven-3.6.0-bin.tar.gz
RUN echo "export PATH=$PATH:/apache-maven-3.6.0/bin" >> ~/.bashrc

# https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-libraries.html#develop-using-etl-library
RUN curl -O https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-4.0/spark-3.3.0-amzn-1-bin-3.3.3-amzn-0.tgz
RUN tar -xf spark-3.3.0-amzn-1-bin-3.3.3-amzn-0.tgz
RUN rm spark-3.3.0-amzn-1-bin-3.3.3-amzn-0.tgz
RUN echo "export SPARK_HOME=/spark" >> ~/.bashrc

# Install AWS CLI
RUN apt-get install -y unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip" 
RUN unzip awscliv2.zip
RUN ./aws/install
RUN rm -rf awscliv2.zip aws