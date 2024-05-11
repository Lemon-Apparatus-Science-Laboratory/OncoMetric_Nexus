# Use a base image with X11 support
FROM ubuntu:20.04
# Set environment variable to avoid dialog prompts
ENV DEBIAN_FRONTEND=noninteractive
# Set the display variable
ENV DISPLAY=:0
VOLUME ["/tcia", "/tciaDownload", "/config"]
# Install required packages
RUN apt-get update && apt-get install -y wget python3 python3-pip xdg-utils
RUN pip3 install tcia_utils
COPY src/downloadTool.py ./downloadTool.py
RUN python3 ./downloadTool.py 
RUN wget https://cbiit-download.nci.nih.gov/nbia/releases/ForTCIA/NBIADataRetriever_4.4/nbia-data-retriever-4.4.2.deb
RUN mkdir /usr/share/desktop-directories/
RUN dpkg -i nbia-data-retriever-4.4.2.deb
# CMD
# ENTRYPOINT [ "/opt/nbia-data-retriever/nbia-data-retriever", "/tcia/Sample.tcia", "-d", "/tciaDownload/" ] 
ENTRYPOINT ["/opt/nbia-data-retriever/nbia-data-retriever"] 
