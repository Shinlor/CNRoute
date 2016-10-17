# cnroute
Add the route, so that the domestic (china) IP address does not across the VPN

##脚本主要利用来自 http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest 的数据生成路由命令脚本, 在连接VPN前执行，通过脚本, 可以让用户在使用vpn作为默认网络网关的时候, 不使用vpn进行对中国国内ip的访问, 从而减轻vpn的负担, 和增加访问国内网站的速度.

##只在Windows下使用
##关于思路及部分代码使用了https://github.com/fivesheep/chnroutes 中的内容，因原脚本需要生成bat文件执行，执行速度太慢，这里利用以前写的 winroute 调用windowsAPI（iphlpapi.dll）进行，速度较快。

##使用前阅读https://github.com/fivesheep/chnroutes 说明，在连接VPN前执行本脚本。 

##关于winroute，参考https://github.com/Shinlor/WinRoute
