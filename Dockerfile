from devopsfaith/krakend

ENV KRAKEND_CONFIG /etc/krakend/krakend.json



USER root 
COPY etc/* /etc/krakend/
RUN chown krakend:krakend -R /etc/krakend
RUN chmod 777 -R /etc/krakend
WORKDIR /

USER krakend
RUN cat /etc/krakend/krakend.json
