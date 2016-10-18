# cnroute
Add the route, so that the domestic (china) IP address does not across the VPN

- 程序利用来自 
http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest
的国内IP数据，在连接VPN前执行，添加路由使得国内IP仍通过原默认网关访问，从而实现仅国外地址通过VPN访问的目的

- 因使用了windowsAPI添加路由，本程序只能在Windows下使用

- 关于思路及部分代码参考了
https://github.com/fivesheep/chnroutes
中的内容，因原脚本需要生成bat文件然后执行，执行速度太慢，因此利用以前写的 winroute 调用windowsAPI（iphlpapi.dll）进行添加路由，速度较快

- 在连接VPN前使用，需管理员权限

- 提供了exe文件，可不安装Python直接使用

- 安全考虑，添加路由为非永久方式，所有添加的路由重启后丢失

- 关于winroute，参考
https://github.com/Shinlor/WinRoute
