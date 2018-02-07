Installations：
--------------------------
1. 安装python2.7和firefox浏览器
2. 把geckodriver.exe放到firefox安装目录下。
3. 双击运行install.bat

Usage：
--------------------------
1. 修改config.py文件中的保存路径，改为实际的结果保存路径。	
2. 此文件夹内按住shift并右击鼠标，选择在此处打开命令窗口。
3. cmd下输入：python reboot_time_test_NewUI.py + 重启次数。
    如：测试5次重启： python reboot_time_test_NewUI.py 5
4. 运行完成后，打开保存路径可以看到测试结果excel和每次重启后页面截图。


Checkpoint：
--------------------------
1. 页面点击立即重启开始计算本次重启时间（T0)
2. 线程1计算ping通网关时间（T1 = Tc - T0）
3. 线程2计算ping通internet时间（baidu.com；外网地址可选）（T2 = Tc -T0)
4. 线程3计算页面跳转到登录界面的时间（T3 = Tc - T0）