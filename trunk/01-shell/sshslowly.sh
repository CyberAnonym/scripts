sed -i 's/GSSAPIAuthentication.*/GSSAPIAuthentication no/' /etc/ssh/sshd_config && sed -i 's/.UseDNS.*/UseDNS no/' /etc/ssh/sshd_config && service sshd reload
