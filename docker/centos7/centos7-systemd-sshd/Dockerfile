FROM centos:7

MAINTAINER "Gerben Venekamp" <gerben@venekamp.eu>

ARG ssh_pub_key

ENV container docker
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
VOLUME [ "/sys/fs/cgroup" ]

#RUN yum -y install httpd; yum clean all; systemctl enable httpd.service

RUN yum install -y openssh-server sudo vim python3 rsync

CMD ["/usr/sbin/init"]
RUN systemctl enable sshd.service

EXPOSE 22
EXPOSE 80

# Copy sshd PAM stack
COPY pam.d/sshd /etc/pam.d/sshd

# Create and configure vagrant user
RUN useradd --create-home -s /bin/bash vagrant
WORKDIR /home/vagrant

# Configure SSH access
RUN mkdir -p /home/vagrant/.ssh
COPY ssh/id_rsa.pub /home/vagrant/.ssh/authorized_keys
#RUN echo "${ssh_pub_key}" | sed -e "s/'//" >> /home/vagrant/.ssh/authorized_keys
RUN chown -R vagrant: /home/vagrant/.ssh
RUN echo -n 'vagrant:vagrant' | chpasswd

# Enable passwordless sudo for the "vagrant" user
RUN mkdir -p /etc/sudoers.d
RUN install -b -m 0440 /dev/null /etc/sudoers.d/vagrant
RUN echo 'vagrant ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers.d/vagrant
