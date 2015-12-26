FROM ubuntu:14.04
MAINTAINER Dean Hillan <>
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-dev python-pip python-numpy python-scipy
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.6.0-cp27-none-linux_x86_64.whl
ADD ./ /opt/tensor/
WORKDIR /opt/tensor
EXPOSE 5000
CMD ["python", "app.py"]
