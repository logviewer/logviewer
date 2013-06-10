install:
	mkdir /opt/logviewer
	virtualenv --no-site-packages /opt/logviewer/venv
	/opt/logviewer/venv/bin/easy_install -U distribute
	/opt/logviewer/venv/bin/easy_install django==1.4.3
	/opt/logviewer/venv/bin/easy_install django-bootstrap-toolkit
	/opt/logviewer/venv/bin/easy_install django-static
	/opt/logviewer/venv/bin/easy_install pyes
	/opt/logviewer/venv/bin/easy_install MySQL-python
	/opt/logviewer/venv/bin/easy_install thrift
	wget --directory-prefix=/opt/logviewer/ https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.1.tar.gz
	tar xvzf /opt/logviewer/elasticsearch-0.90.1.tar.gz -C /opt/logviewer/
	mv /opt/logviewer/elasticsearch-0.90.1 /opt/logviewer/elasticsearch
	rm /opt/logviewer/elasticsearch-0.90.1.tar.gz
	sed -i 's@^# path\.@path\.@g' /opt/logviewer/elasticsearch/config/elasticsearch.yml
	sed -i 's@/path/to/@/opt/logviewer/elasticsearch/@g' /opt/logviewer/elasticsearch/config/elasticsearch.yml
	cp -r src /opt/logviewer
	/opt/logviewer/elasticsearch/bin/plugin -install elasticsearch/elasticsearch-transport-thrift/1.5.0
	/opt/logviewer/elasticsearch/bin/plugin -install mobz/elasticsearch-head
	echo '## Logviewer ##' >> /etc/syslog-ng/syslog-ng.conf
	echo '## START ##' >> /etc/syslog-ng/syslog-ng.conf
	echo 'template t_rewritetime { template("$${YEAR}$${MONTH}$${DAY}$${HOUR}$${MIN}$${SEC} $${MSG}\\n");  template_escape(no); };' >> /etc/syslog-ng/syslog-ng.conf
	echo 'destination d_network { unix-stream("/var/log/network.sock" template(t_rewritetime)); };' >> /etc/syslog-ng/syslog-ng.conf
	echo 'destination d_sshd { unix-stream("/var/log/sshd.sock" template(t_rewritetime)); };' >> /etc/syslog-ng/syslog-ng.conf
	echo 'filter f_iptables { facility(kern) and match(".*(ACCEPT|DROP) IN.*" value("MESSAGE")) };' >> /etc/syslog-ng/syslog-ng.conf
	echo 'filter f_sshd { facility(auth, authpriv) and match(".*(Accepted|Failed) password.*" value("MESSAGE")); };' >> /etc/syslog-ng/syslog-ng.conf
	echo 'log { source(s_src); filter(f_iptables); destination(d_network); };' >> /etc/syslog-ng/syslog-ng.conf
	echo 'log { source(s_src); filter(f_sshd); destination(d_sshd); };' >> /etc/syslog-ng/syslog-ng.conf
	echo '## END ##' >> /etc/syslog-ng/syslog-ng.conf
