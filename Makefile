install:
	mkdir /opt/logviewer
	virtualenv --no-site-packages /opt/logviewer/venv
	/opt/logviewer/venv/bin/easy_install django==1.4.3
	/opt/logviewer/venv/bin/easy_install django-bootstrap-toolkit
	/opt/logviewer/venv/bin/easy_install django-static
	/opt/logviewer/venv/bin/easy_install pyes
	/opt/logviewer/venv/bin/easy_install MySQL-python
	/opt/logviewer/venv/bin/easy_install thrift
	wget --directory-prefix=/opt/logviewer/ https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.1.tar.gz
	tar xvzf /opt/logviewer/elasticsearch-0.90.1.tar.gz -C /opt/logviewer/
	mv /opt/logviewer/elasticsearch-0.90.1 /opt/logviewer/elasticsearch
	cp -r src /opt/logviewer
	/opt/logviewer/elasticsearch/bin/plugin -install elasticsearch/elasticsearch-transport-thrift/1.5.0
