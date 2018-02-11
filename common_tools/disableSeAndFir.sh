sed -i 's/SELINUX=.*/SELINUX=disabled/' /etc/selinux/config && systemctl stop firewalld && systemctl disable firewalld
