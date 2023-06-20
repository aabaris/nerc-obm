FROM debian

RUN apt-get update
RUN apt-get install -y curl vim python3 python3-pip git
RUN apt-get update
RUN apt-get install -y ansible
RUN apt-get install -y jq

RUN pip install omsdk

RUN ansible-galaxy collection install  dellemc.openmanage
