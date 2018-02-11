 
 cm1="sed - 's/SELINUX=.*/SELINUX=disabled/' /etc/selinux/config"
 cm2="systemctl stop firewalld"
 cm3="systemctl disable firewalld"
 $cm1 && $cm2 && $cm3
