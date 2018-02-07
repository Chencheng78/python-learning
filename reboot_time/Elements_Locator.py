# -*- coding: UTF-8 -*-
import K2P_MTK_Spec
#-----------------------------------------------------------------------
#                      登录页面
#-----------------------------------------------------------------------
#密码输入框
LI_EditBox_Password = 'id=Pwd'
#登录按钮
LI_Button_Login = 'id=Save'
#密码明码或加密显示按钮
LI_Button_PwdDisplay = '//div[@id="LoginCon"]/div[4]/ul/li/i[2]'

#-----------------------------------------------------------------------
#                      快速向导页面
#-----------------------------------------------------------------------
AP_button_welcome='id=Start'
QG_UserAgree='//i[@data-value="1"]'
QG_UserUnagree='//i[@data-value="0"]'
QG_EditBox_NewPwd = 'id=PwdNew'
QG_EditBox_CfmPwd = 'id=PwdCfm'
QG_Button_Next = 'id=Save'
QG_Button_Back = 'id=PreviousStep'
QG_Option_NetType='//span[@id="WanType"]/i'
QG_Option_DHCP='//*[@id="sel-opts-ulWanType"]/li[1]'
QG_Option_PPPoE='//*[@id="sel-opts-ulWanType"]/li[2]'
QG_Option_StaticIp='//*[@id="sel-opts-ulWanType"]/li[3]'
QG_EditBox_PPPoE_UserName = 'id=PppoeUser'
QG_EditBox_PPPoE_PassWord = 'id=PppoePwd'
QG_EditBox_WAN_StaticIPaddr = 'id=WanIpaddr'
QG_EditBox_WAN_StaticMask = 'id=WanMask'
QG_EditBox_WAN_StaticGateWay = 'id=WanGw'
QG_EditBox_WAN_StaticDNS = 'id=PrimDns'
QG_EditBox_SSIDBind_On='id=Two2One'
QG_EditBox_SSIDBind_Off='//span/i'
QG_EditBox_SSID_2G='id=Ssid2G'
QG_EditBox_SSID_2G_PassWord = 'id=Pwd2G'
QG_EditBox_SSID_Bind=QG_EditBox_SSID_2G
QG_EditBox_SSID_Bind_Pwd=QG_EditBox_SSID_2G_PassWord
QG_EditBox_SSID_5G = 'id=Ssid5G'
QG_EditBox_SSID_5G_PassWord = 'id=Pwd5G'
QG_Button_Save='id=SaveReboot'
QG_Button_SaveAgain='//input[@value="确定"]'
QG_Option_Retry='id=Retry'
QG_Button_MoreSet='id=MoreSet'


#-----------------------------------------------------------------------
#                      首页
#-----------------------------------------------------------------------
#帮助
AP_Help='id=HelpIcon'
AP_Phone=u'服务热线'
AP_PhoneNum=K2P_MTK_Spec.S_AP_PhoneNum
#AP_UserAgreement='//div[@id="Con"]/*/*/div[2]/a'
AP_UserAgreement='//*[@id="ShowAgreement"]'
#'//div[@id="Con"]/div[3]/div[3]/a'
#AP_MAC= u'MAC地址:'+K2P_BCM_Spec.S_DHCP_Mac
AP_MAC= K2P_MTK_Spec.S_DHCP_Mac
AP_CompanyInfo=u'版权所有©上海斐讯数据通信技术有限公司'
##################################################
#网络状态
AP_NetState='//*[contains(text(),"网络状态")]'
#无线设置
AP_WirelessSetPage = '//*[@id="Con"]/div[1]/ul[1]/a[3]/li/p'
#个人中心
AP_PersonalSet = 'id=Tool'
#功能设置
AP_FunctionSet = '//div[@id="Con"]/div/ul/a[4]/li/p'
#终端管理
AP_DeviceManage = '//div[@id="Con"]/div/ul/a[2]/li/p'
#
AP_UpgradeLater='id=Later'
AP_UpgradeNow = '//*[@id="UpgradeNow"]'
#-----------------------------------------------------------------------
#                      个人中心
#-----------------------------------------------------------------------
#退出
AP_Logout = '//div[@id="Con"]/div/ul[2]/li/ul/li[4]'#'//li[3]'
#重启
AP_Reboot = '//li/ul/li'
AP_RebootConfirm = '//input[2]'
AP_RebootCancel = '//input[1]'
#管理员密码
AP_AdminPwdPage = '//div[@id="Con"]/div/ul[2]/li/ul/li[3]'
AP_AdminOldPwd = 'id=PwdOld'
AP_AdminNewPwd = 'id=PwdNew'
AP_AdminCheckNewPwd = 'id=PwdCfm'
AP_AdminSave = 'id=SavePwd'
AP_AdminCancel='//div[@id="ModifyPwd"]/i'
AP_Reboot_Progress='//div[@id="Pop"]/div/p[1]'
#AP_AdminEye1='//div[@id="Content"]/div[2]/ul/li/i'
#AP_AdminEye2='//div[@id="Content"]/div[2]/ul[2]/li/i'
#AP_AdminEye3='//div[@id="Content"]/div[2]/ul[3]/li/i'
#-----------------------------------------------------------------------
#                      网络状态
#-----------------------------------------------------------------------
#设备名称
NS_OnLineList_DeviceName='//div[@id="onlineList"]/ul/li[1]/span'
#设备上行速率
NS_OnLineList_DeviceNowSpeed_Up='//div[@id="onlineList"]/ul/li[3]/p'
#设备下行速率
NS_OnLineList_DeviceNowSpeed_Down='//div[@id="onlineList"]/ul/li[4]/p'
#设备接入方式
NS_OnLineList_DeviceAccessMode = '//div[@id="onlineList"]/ul/li[5]/p'
#设备上网权限
NS_OnLineList_DeviceAccessStatus = '//div[@id="onlineList"]/ul/li[6]/p/span'
NS_OnlineList_Switch_Allow='//*[@id="onlineList"]/ul[1]/li[6]/p/span[@data-switch="1"]'
NS_OnlineList_Switch_Deny='//*[@id="onlineList"]/ul[1]/li[6]/p/span[@data-switch="0"]'


#-----------------------------------------------------------------------
#                      终端管理
#-----------------------------------------------------------------------
#######################在线列表所用参数############################
#终端名称
DM_OnLineList_DeviceName =  '//div[@id="onlineList"]/ul[1]/li[1]/div/p[1]'
#终端名称输入框
DM_OnLineList_DeviceName_Input = '//div[@id="onlineList"]/ul/li[1]/div/p[1]/input'
#终端IP
DM_OnLineList_DeviceIP = '//div[@id="onlineList"]/ul[1]/li[2]/p[1]'
#终端MAC
DM_OnLineList_DeviceMac ='//*[@id="onlineList"]/ul/li[2]/p[2]'#'//div[@id="onlineList"]/ul/li[2]/p[2]'
DM_OnLineList_DeviceMac_Second = '//div[@id="onlineList"]/ul[2]/li[2]/p[2]'
#终端当前速度-上行
DM_OnLineList_DeviceNowSpeed_Up = '//div[@id="onlineList"]/ul/li[3]/p[1]'
#终端当前速度-下行
DM_OnLineList_DeviceNowSpeed_Down = '//div[@id="onlineList"]/ul/li[3]/p[2]'
#终端初次限速-上行
DM_OnLineList_DeviceSpeedUnlimit_Up = '//div[@id="onlineList"]/ul/li[4]/p[1]/input'
#终端初次限速-下行
DM_OnLineList_DeviceSpeedUnlimit_Down = '//div[@id="onlineList"]/ul/li[4]/p[2]/input'
#终端修改限速-上行
DM_OnLineList_DeviceSpeedLimited_Up = '//*[@id="onlineList"]/ul/li[4]/p[1]/span'
DM_OnLineList_DeviceSpeedLimited_Up_Input = '//*[@id="onlineList"]/ul/li[4]/p[1]/input'
#终端修改限速-下行
DM_OnLineList_DeviceSpeedLimited_Down = '//*[@id="onlineList"]/ul/li[4]/p[2]/span'
DM_OnLineList_DeviceSpeedLimited_Down_Input = '//div[@id="onlineList"]/ul/li[4]/p[2]/input'
#终端接入方式
DM_OnLineList_DeviceAccessMode = '//div[@id="onlineList"]/ul/li[5]/p'
#终端上网权限
DM_OnLineList_DeviceNetStatus_EnableImg = '//div[@id="onlineList"]/ul/li[6]/p/span'
DM_OnLineList_DeviceNetStatus_Enable = '//div[@id="onlineList"]/ul[1]/li[6]/p/span[@data-value="1"]'
DM_OnLineList_DeviceNetStatus_DisableImg = '//div[@id="forbidList"]/ul/li[6]/p/span'
DM_OnLineList_DeviceNetStatus_Disable = '//div[@id="forbidList"]/ul/li[6]/p/span[@data-value="0"]'
#终端保存防呆提示
DM_OnLineList_DeviceNet_SaveConfirm = '//div[@id="Pop"]/div/div/input'
DM_OnLineList_DeviceNet_SaveAlert = '//div[@id="Pop"]/div/p[2]'

##########################禁止上网列表所用参数#################################
#禁止终端列表
DM_ForbidList = '//*[@id="Forbid"]'
#终端名称
DM_ForbidList_DeviceName = '//div[@id="forbidList"]/ul/li[1]/div/p'
#终端MAC
DM_ForbidList_DeviceMac = '//div[@id="forbidList"]/ul/li[2]/p'
#终端当前速度-上行
DM_ForbidList_DeviceNowSpeed_Up = '//div[@id="forbidList"]/ul/li[3]/p[1]'
#终端当前速度-下行
DM_ForbidList_DeviceNowSpeed_Down = '//div[@id="forbidList"]/ul/li[3]/p[2]'
#终端限速-上行
DM_ForbidList_DeviceSpeedLimi_Up = '//div[@id="forbidList"]/ul/li[4]/p[1]'
#终端限速-下行
DM_ForbidList_DeviceSpeedLimi_Down = '//div[@id="forbidList"]/ul/li[4]/p[2]'
#终端接入方式
DM_ForbidList_DeviceAccessMode = '//div[@id="forbidList"]/ul/li[5]/p'
#终端上网权限
DM_OnLineList_DeviceNetStatus_DisableImg = '//div[@id="forbidList"]/ul/li[6]/p/span'
DM_OnLineList_DeviceNetStatus_Disable = '//div[@id="forbidList"]/ul/li[6]/p/span[@data-value="0"]'
##########################离线设备列表所用参数#################################
#终端名称
DM_OfflineList_DeviceName = '//*[@id="offlineList"]/ul[1]/li[1]/div/p'
#终端MAC
DM_OfflineList_DeviceMac = '//*[@id="offlineList"]/ul[1]/li[2]/p'
#终端当前速度-上行
DM_OfflineList_DeviceNowSpeed_Up = '//*[@id="offlineList"]/ul[1]/li[3]/p[1]'
#终端当前速度-下行
DM_OfflineList_DeviceNowSpeed_Down = '//*[@id="offlineList"]/ul[1]/li[3]/p[2]'
#终端限速-上行
DM_OfflineList_DeviceSpeedLimi_Up = '//*[@id="offlineList"]/ul[1]/li[4]/p[1]'
#终端限速-下行
DM_OfflineList_DeviceSpeedLimi_Down = '//*[@id="offlineList"]/ul[1]/li[4]/p[2]'
#终端接入方式
DM_OfflineList_DeviceAccessMode = '//*[@id="offlineList"]/ul[1]/li[5]/p'
#终端上网权限
DM_OfflineList_DeviceNetStatus_EnableImg = '//*[@id="offlineList"]/ul[1]/li[6]/p/span'
DM_OfflineList_DeviceNetStatus_Enable = '//*[@id="offlineList"]/ul[1]/li[6]/p/span[@data-value="1"]'

#-----------------------------------------------------------------------
#                      无线设置
#-----------------------------------------------------------------------
#双频合一按钮
WLS_DoubleFreCombine = 'id=Two2One'
WLS_DoubleFreCombine_Enable = '//span[@id="Two2One"][@data-value="1"]'
WLS_DoubleFreCombine_Disable = '//span[@id="Two2One"][@data-value="0"]'
#无线设置保存按钮
WLS_SaveButton = 'id=Save'
WLS_SaveConfirm = '//input[2]'
WLS_SaveCancel = '//input[1]'
#2.4G无线
WLS_2G_Switch = '//span[@id="Switch2G"]'
WLS_2G_Switch_Enable = '//span[@id="Switch2G"][@data-value="1"]'
WLS_2G_Switch_Disable = '//span[@id="Switch2G"][@data-value="0"]'
WLS_2G_Ssid = 'id=Ssid2G'
WLS_2G_Password = 'id=Pwd2G'
#2.4G无线密码明码或加密显示按钮
#WLS_2G_PswDisplay = '//div[@id="Content"]/div/ul[4]/li/i'
#WLS_2G_PswDisplay_Enable = '//div[@id="Content"]/div/ul[4]/li/i[@data-value="1"]'
#WLS_2G_PswDisplay_Disable = '//div[@id="Content"]/div/ul[4]/li/i[@data-value="0"]'
WLS_2G_PswDisplay = '//*[@id="Content"]/div[2]/ul[3]/li/i'
WLS_2G_PswDisplay_Enable = '//*[@id="Content"]/div[2]/ul[3]/li/i[@data-value="1"]'
WLS_2G_PswDisplay_Disable = '//*[@id="Content"]/div[2]/ul[3]/li/i[@data-value="0"]'
#2.4G无线SSID隐藏
WLS_2G_SsidHide = 'id=HideSsid2G'
WLS_2G_SsidHide_Enable = '//span[@id="HideSsid2G"][@data-value="1"]'
WLS_2G_SsidHide_Disable = '//span[@id="HideSsid2G"][@data-value="0"]'
#5G无线
WLS_5G_Switch = 'id=Switch5G'
WLS_5G_Switch_Enable = '//span[@id="Switch5G"][@data-value="1"]'
WLS_5G_Switch_Disable = '//span[@id="Switch5G"][@data-value="0"]'
WLS_5G_Ssid = 'id=Ssid5G'
WLS_5G_Password = 'id=Pwd5G'
#5G无线密码明码或加密显示按钮
WLS_5G_PswDisplay = '//div[@id="Wifi5G"]/ul[4]/li/i'
WLS_5G_PswDisplay_Enable = '//div[@id="Wifi5G"]/ul[4]/li/i[@data-value="1"]'
WLS_5G_PswDisplay_Disable = '//div[@id="Wifi5G"]/ul[4]/li/i[@data-value="0"]'
#5G无线SSID隐藏
WLS_5G_SsidHide = 'id=HideSsid5G'
WLS_5G_SsidHide_Enable = '//span[@id="HideSsid5G"][@data-value="1"]'
WLS_5G_SsidHide_Disable = '//span[@id="HideSsid5G"][@data-value="0"]'
#无线设置-定时开关
WLS_TimeSwitch = '//*[@id="TimeSwitch"]'
WLS_TimeSwitch_Enable = '//span[@id="TimeSwitch"][@data-value="1"]'
WLS_TimeSwitch_Disable = '//span[@id="TimeSwitch"][@data-value="0"]'
WLS_CloseHour = '//*[@id="CloseHour"]'
WLS_CloseHour_Options = '//*[@id="sel-opts-ulCloseHour"]/li'
WLS_CloseMin = '//*[@id="CloseMin"]'
WLS_CloseMin_Options = '//*[@id="sel-opts-ulCloseMin"]/li'
WLS_OpenHour = '//*[@id="OpenHour"]'
WLS_OpenHour_Options = '//*[@id="sel-opts-ulOpenHour"]/li'
WLS_OpenMin = '//*[@id="OpenMin"]'
WLS_OpenMin_Options = '//*[@id="sel-opts-ulOpenMin"]/li'
WLS_Timer_Hour_Values = ['[@title="00"]','[@title="01"]','[@title="02"]','[@title="03"]','[@title="04"]','[@title="05"]','[@title="06"]'\
						,'[@title="07"]','[@title="08"]','[@title="09"]','[@title="10"]','[@title="11"]','[@title="12"]','[@title="13"]','[@title="14"]','[@title="15"]'\
						,'[@title="16"]','[@title="17"]','[@title="18"]','[@title="19"]','[@title="20"]','[@title="21"]','[@title="22"]','[@title="23"]']
WLS_Timer_Min_Values = ['[@title="00"]','[@title="05"]','[@title="10"]','[@title="15"]','[@title="20"]','[@title="25"]','[@title="30"]'\
						,'[@title="35"]','[@title="40"]','[@title="45"]','[@title="50"]','[@title="55"]']
#无线高级设置按钮
WLS_AdvanceSet = '//span[@id="SeniorSet"]'
#2.4G无线高级设置
#2.4G无线模式设置
WLS_2G_Mode = '//span[@id="WifiMode2G"]/i'
WLS_2G_Mode_Get = '//*[@id="BandWidth2G"]/span'
WLS_2G_Mode_11bgn = '//ul[@id="sel-opts-ulWifiMode2G"]/li[1]'
WLS_2G_Mode_11bg = '//ul[@id="sel-opts-ulWifiMode2G"]/li[2]'
WLS_2G_Mode_11n = '//ul[@id="sel-opts-ulWifiMode2G"]/li[3]'
WLS_2G_Mode_Value = [WLS_2G_Mode_11bgn,WLS_2G_Mode_11bg,WLS_2G_Mode_11n]
#2.4G无线信道设置
WLS_2G_Channel = '//span[@id="Channel2G"]/i'
WLS_2G_ChlManual = '//ul[@id="sel-opts-ulChannel2G"]/li'
Wls_2G_Chl_Value=[u'[@title="自动"]','[@title="1"]','[@title="2"]','[@title="3"]','[@title="4"]','[@title="5"]','[@title="6"]','[@title="7"]','[@title="8"]','[@title="9"]','[@title="10"]','[@title="11"]','[@title="12"]','[@title="13"]']

#2.4G无线频宽设置
WLS_2G_Bandwidth = '//ul[3]/li/span/i'
WLS_2G_Bandwidth_20M = '//ul[@id="sel-opts-ulBandWidth2G"]/li[1]'
WLS_2G_Bandwidth_20Mor40M = '//ul[@id="sel-opts-ulBandWidth2G"]/li[2]'
WLS_2G_Bandwidth_40M = '//ul[@id="sel-opts-ulBandWidth2G"]/li[3]'

#2.4G无线隔离设置
WLS_2G_Isolate = 'id=WifiIsolation2G'
WLS_2G_Isolate_Enable = '//span[@id=WifiIsolation2G][@data-value="1"]'
WLS_2G_Isolate_Disable = '//span[@id=WifiIsolation2G][@data-value="0"]'
#5G无线高级设置
#5G无线模式设置
WLS_5G_Mode = '//span[@id="WifiMode5G"]/i'
WLS_5G_Mode_Get = '//*[@id="BandWidth5G"]/span'

WLS_5G_Mode_11nac = '//ul[@id="sel-opts-ulWifiMode5G"]/li[2]'
WLS_5G_Mode_11anac = '//ul[@id="sel-opts-ulWifiMode5G"]/li'
#WLS_5G_Mode_value = [WLS_5G_mode_11nac,WLS_5G_mode_11anac]
#5G无线信道设置
WLS_5G_Channel = '//span[@id="Channel5G"]/i'
WLS_5G_ChlManual='//ul[@id="sel-opts-ulChannel5G"]/li'
#Wls_5G_Chl_Value=[u'[@title="自动"]','[@title="36"]','[@title="40"]','[@title="44"]','[@title="48"]','[@title="52"]','[@title="56"]','[@title="60"]','[@title="64"]','[@title="149"]','[@title="153"]','[@title="157"]','[@title="161"]','[@title="165"]']
Wls_5G_Chl_Value=[u'[@title="自动"]','[@title="36"]','[@title="40"]','[@title="44"]','[@title="48"]','[@title="149"]','[@title="153"]','[@title="157"]','[@title="161"]','[@title="165"]']
#5G无线频宽设置
WLS_5G_Bandwidth = '//span[@id="BandWidth5G"]/i'
WLS_5G_Bandwidth_20M = '//ul[@id="sel-opts-ulBandWidth5G"]/li[1]'
WLS_5G_Bandwidth_40M = '//ul[@id="sel-opts-ulBandWidth5G"]/li[2]'
WLS_5G_Bandwidth_80M = '//ul[@id="sel-opts-ulBandWidth5G"]/li[3]'
WLS_5G_Bandwidth_20Mor40Mor80M = '//ul[@id="sel-opts-ulBandWidth5G"]/li[4]'
#5G无线隔离
WLS_5G_Isolate = 'id=WifiIsolation5G'
WLS_5G_Isolate_Enable = '//span[@id=WifiIsolation5G][@data-value="1"]'
WLS_5G_Isolate_Disable = '//span[@id=WifiIsolation5G][@data-value="0"]'
#关闭无线开关，弹出提示框，点击确认
WLS_Alert_Ok = 'css=input.confirm-btn.confirm-btn-r'
#关闭无线开关，弹出提示框，点击取消
WLS_Alert_Close = 'css=input.confirm-btn.confirm-btn-l'
#防呆出现提示信息
WLS_Message = '//div[@id="Content"]/div[2]/div[2]/p'
#出现提示信息
WLS_Prompt = '//div[@id="Pop"]/div/p[2]'
#MU-MIMO
WLS_MU_MIMO = '//*[@id="WifiMuMimo"]'
#Beamforming
WLS_Beamforming = '//*[@id="WifiBeamForming"]'
#-----------------------------------------------------------------------
#                      功能设置
#-----------------------------------------------------------------------
#打开系统状态（按表搜索）
FS_SystemManage = '//*[contains(text(),"系统状态")]'
#打开上网设置（按字搜索）
FS_NetWorkSet = '//*[contains(text(),"上网设置")]'
#打开家长控制
FS_ParentControl = '//*[contains(text(),"家长控制")]'
#打开一键体检
FS_Diagnose = '//*[contains(text(),"一键体检")]'
#打开健康节能
FS_SignalSet = '//*[contains(text(),"健康节能")]'
#打开无线扩展
FS_Wisp = '//*[contains(text(),"无线扩展")]'
#打开备份恢复
FS_Button_BackupRestore = '//*[contains(text(),"备份恢复")]'
#LAN设置按钮
FS_LanSet = '//*[contains(text(),"LAN设置")]'
#DHCP服务
FS_DHCPService = '//*[contains(text(),"DHCP服务")]'
#端口转发
FS_PortForward='//*[contains(text(),"端口转发")]'
#DMZ主机
FS_DMZ='//*[contains(text(),"DMZ主机")]'
#动态DNS
FS_DDNS='//*[contains(text(),"动态DNS")]'
#手动升级
FS_UpgradeByManual='//*[contains(text(),"手动升级")]'
#UPNP
FS_UPNP='//*[contains(text(),"UPnP")]'
#-----------------------------------------------------------------------
#                      系统状态
#-----------------------------------------------------------------------
#系统状态
ST_Label_SysInfo_RunTime = '//div[2]/ul[1]/li[1]/p[1]/span'
ST_Label_SysInfo_EquipType = '//div[2]/ul[1]/li[1]/p[2]/span'
ST_Label_SysInfo_SoftVer = '//*[@id="Content"]/div[3]/ul[1]/li[2]/p[1]/span'
ST_Label_SysInfo_HardVer = '//*[@id="Content"]/div[3]/ul[1]/li[2]/p[2]/span'
#WAN口状态
ST_Label_WanStatus_Mode = '//div[3]/ul[2]/li[1]/p[1]/span'
ST_Label_WanStatus_IP = 'id=WanIp'
ST_Label_WanStatus_Mask = 'id=WanNetmask'
ST_Label_WanStatus_Gateway = 'id=WanGateway'
ST_Label_WanStatus_DNS = 'id=WanDns'
ST_Label_WanStatus_Mac = 'id=WanMac'
#LAN口状态
ST_Label_LanStatus_IP = '//div[2]/ul[2]/li[2]/p[1]/span'
ST_Label_LanStatus_Mask = '//div[2]/ul[2]/li[2]/p[2]/span'
ST_Label_LanStatus_Mac = '//div[2]/ul[2]/li[2]/p[3]/span'
#2.4G无线状态
ST_Label_2G_Status = 'id=WlanSwitch'
ST_Label_2G_SSID = 'id=WlanSsid'
ST_Label_2G_Security = 'id=EncryptType'
ST_Label_2G_Mode = 'id=WifiMode'
ST_Label_2G_Channel = 'id=Channel'
ST_Label_2G_Mac = 'id=wifiMac'
#5G无线状态
ST_Label_5G_Status = 'id=Wlan5Switch'
ST_Label_5G_SSID = 'id=Wlan5Ssid'
ST_Label_5G_Security = 'id=EncryptType5G'
ST_Label_5G_Mode = 'id=WifiMode5G'
ST_Label_5G_Channel = 'id=Channel5G'
ST_Label_5G_Mac = 'id=wifi5Mac'
#-----------------------------------------------------------------------
#                      上网设置
#-----------------------------------------------------------------------
#上网设置页面Title
OG_Network_Title = u'上网设置'
#自动检测按钮
OG_Network_AutoDetect = 'id=Detect'
#上网方式
OG_Option_Method_Select = '//span[@id="WanType"]/i'
OG_Option_Method_DHCP = '//ul[@id="sel-opts-ulWanType"]/li'
OG_Option_Method_PPPoE = '//ul[@id="sel-opts-ulWanType"]/li[2]'
OG_Option_Method_Static = '//ul[@id="sel-opts-ulWanType"]/li[3]'
#特殊拨号
OG_EditBox_PPPoE_SpecialMode_Select = '//*[@id="PppoeDiaType"]/span'
OG_EditBox_PPPoE_NormalMode = '//*[@id="sel-opts-ulPppoeDiaType"]/li[1]'
OG_EditBox_PPPoE_SpecialMode1 = '//*[@id="sel-opts-ulPppoeDiaType"]/li[2]'
OG_EditBox_PPPoE_SpecialMode2 = '//*[@id="sel-opts-ulPppoeDiaType"]/li[3]'
OG_EditBox_PPPoE_SpecialMode3 = '//*[@id="sel-opts-ulPppoeDiaType"]/li[4]'
OG_EditBox_PPPoE_SpecialMode4 = '//*[@id="sel-opts-ulPppoeDiaType"]/li[5]'
#PPPoE
OG_EditBox_PPPoE_UserName = 'id=PppoeUser'
OG_EditBox_PPPoE_PassWord = 'id=PppoePwd'
OG_EditBox_PPPoE_ServreName = 'id=PppoeServ'
#Static
OG_EditBox_Static_IP = 'id=WanIpaddr'
OG_EditBox_Static_Mask = 'id=WanMask'
OG_EditBox_Static_GateWay = 'id=WanGw'
OG_EditBox_Static_PrimDns = 'id=PrimDns'
OG_EditBox_Static_SecondDns = 'id=SecDns'
#高级设置
OG_Network_WAN_Advance = 'id=SeniorSet'
#高级设置-Mtu设置
OG_Network_WAN_Advance_Mtu = 'id=Mtu'
OG_Network_WAN_Advance_PPPoEMtu = 'id=PppoeMtu'#PPPOE下使用的MTU id
#高级设置-Mac地址克隆
OG_Network_WAN_MacCloneSelect = 'id=CloneSwitch'#'//span[@id="MacClone"]/i'
OG_Network_WAN_MacClone_No = '//ul[@id="sel-opts-ulMacClone"]/li'
OG_Network_WAN_MacClone_Local = '//ul[@id="CloneParam"]/li/span'#'//ul[@id="sel-opts-ulMacClone"]/li[2]'
OG_Network_WAN_MacClone_Manual = '//ul[@id="sel-opts-ulMacClone"]/li[3]'
OG_Network_WAN_MacClone_InputManual = 'id=MacCloAddr'
#高级设置-DNS设置(PPPoE和DHCP)
OG_Network_WAN_DnsSelect = 'id=Switch'
#OG_Network_WAN_PrimDns = 'id=AdvPrimDns'
#OG_Network_WAN_SecondDns = 'id=AdvSecDns'
OG_Network_WAN_PrimDns = 'id=SeniorPrimDns'
OG_Network_WAN_SecondDns = 'id=SeniorSecDns'
#保存
OG_Network_WAN_Save = 'id=Save'

#-----------------------------------------------------------------------
#                      访客网络
#-----------------------------------------------------------------------

#进入访客网络
AP_GuestSetPage = '//*[@id="AppList"]/ul[1]/a[3]/li/div[1]'
#访客网络开关
WLS_Guest_Switch = '//span[@id="Switch"]'
WLS_Guest_Switch_Enable = '//span[@id="Switch"][@data-value="1"]'
WLS_Guest_Switch_Disable = '//span[@id="Switch"][@data-value="0"]'
#访客网络
WLS_Guest_Ssid = 'id=VisitorSsid'
WLS_Guest_Password = 'id=VisitorPwd'
WLS_Guest_Save = 'id=Save'
WLS_Guest_Save_Ok='//div[@id="Pop"]/div/div/input[2]'
WLS_Guest_Save_Close='//div[@id="Pop"]/div/div/input[1]'
#访客无线密码明码或加密显示按钮
WLS_Guest_PswDisplay = '//div[@id="Param"]/ul[2]/li/i'
WLS_Guest_PswDisplay_Enable = '//div[@id="Param"]/ul[2]/li/i[@data-value="1"]'
WLS_Guest_PswDisplay_Disable = '//div[@id="Param"]/ul[2]/li/i[@data-value="0"]'
#防呆出现提示信息
WLS_Guest_Message = '//*[@id="Content"]/div[3]/div[2]/p'


#-----------------------------------------------------------------------
#                      家长控制
#-----------------------------------------------------------------------
#家长控制页面Title
PC_ParentControl_Title = '//div[@id="Content"]/div[2]/a/span'
#家长控制开关
PC_ParentControl_SwitchButton = 'id=SwitchParent'
PC_ParentControl_Switch_Enable = '//div[@id="Content"]/div[3]/ul/p/span[@data-value="1"]'
PC_ParentControl_Switch_Disable = '//div[@id="Content"]/div[3]/ul/p/span[@data-value="0"]'
#设备名称
PC_ParentControl_Device_Name = '//*[@id="RuleName"]'
PC_ParentControl_Device_Name_List = '//*[@id="ParentTable"]/tbody/tr[2]/td[1]/div/ul/li'
PC_ParentControl_Device_Rule_Name = '//*[@id="ParentTable"]/tbody/tr/td[1]/div/ul/li'
#设备MAC
PC_ParentControl_Device_MAC = '//*[@id="RuleMac"]'
#规则周期
PC_ParentControl_Period = '//*[@id="RuleCycle"]'
PC_ParentControl_Period_EveryDay = '//li[1][contains(text(),"每天")]'
PC_ParentControl_Period_WorkDay = '//li[2][contains(text(),"工作日")]'
PC_ParentControl_Period_WeekendDay = '//li[3][contains(text(),"周末")]'
PC_ParentControl_Period_FreeDay = '//li[4][contains(text(),"自定义")]'
PC_ParentControl_Period_FreeDay_List = '//*[@id="ParentTable"]/tbody/tr/td[3]/div/div[2]/ul/li'
PC_ParentControl_Period_FreeDay_Monday = '//li[1][contains(text(),"周一")]'
PC_ParentControl_Period_FreeDay_Tuesday = '//li[2][contains(text(),"周二")]'
PC_ParentControl_Period_FreeDay_Wednesday = '//li[3][contains(text(),"周三")]'
PC_ParentControl_Period_FreeDay_Thursday = '//li[4][contains(text(),"周四")]'
PC_ParentControl_Period_FreeDay_Friday = '//li[5][contains(text(),"周五")]'
PC_ParentControl_Period_FreeDay_Sturday = '//li[6][contains(text(),"周六")]'
PC_ParentControl_Period_FreeDay_Sunday = '//li[7][contains(text(),"周日")]'
#规则起始时间
PC_ParentControl_StartHour = '//*[@id="StartHour"]/span'
PC_ParentControl_StartHour_List = '//*[@id="sel-opts-ulStartHour"]/li'
PC_ParentControl_StartMinute = '//*[@id="StartMinute"]/span'
PC_ParentControl_StartMinute_List = '//*[@id="sel-opts-ulStartMinute"]/li'
#规则终止时间
PC_ParentControl_EndHour = '//*[@id="EndHour"]/span'
PC_ParentControl_EndHour_List = '//*[@id="sel-opts-ulEndHour"]/li'
PC_ParentControl_EndMinute = '//*[@id="EndMinute"]/span'
PC_ParentControl_EndMinute_List = '//*[@id="sel-opts-ulEndMinute"]/li'
#保存或编辑
PC_ParentControl_SaveOrEdit = '//*[@id="SaveAdd"]'
#取消或删除
PC_ParentControl_CancelOrDelete = '//*[@id="Cancel"]'
#添加
PC_ParentControl_Add = '//*[@id="ParentCtrlTable"]/ul/i'
PC_ParentControl_Add_Enable = '//*[@id="Add"][@ value="0"]/span'
PC_ParentControl_Add_Disable = '//*[@id="Add"][@ value="1"]/span'
#-----------------------------------------------------------------------
#                      一键体检
#-----------------------------------------------------------------------
#一键体检页面Title
DN_Diagnose_Title = '//div[@id="Content"]/div[2]/a/span'
#一键体检初始状态
DN_Diagnose_CheckResult_InitialStatus = '//div[@id="Content"]/div[3]/div[1]/div/p[1]'
DN_Diagnose_WanState_InitialStatus = '//ul[@id="WanState"]/li[1]/span[2]'
DN_Diagnose_NetState_InitialStatus = '//ul[@id="NetState"]/li[1]/span[2]'
DN_Diagnose_WifiState_InitialStatus = '//li[@id="WifiState"]/span[2]'
DN_Diagnose_WifiPwdState_InitialStatus = '//li[@id="WifiPwdState"]/span[2]'
DN_Diagnose_RouterPwdState_InitialStatus = '//li[@id="RouterPwdState"]/span[2]'
DN_Diagnose_UpgradeState_InitialStatus = '//li[@id="UpgradeState"]/span[2]'
#一键体检结果
DN_Diagnose_CheckResult = '//div[@id="Content"]/div[3]/div[1]/div/p[2]'
#Wan口状态
DN_Diagnose_WanState_Right = '//ul[@id="WanState"]/li[1]/i[1]'
DN_Diagnose_WanState_Wrong = '//ul[@id="WanState"]/li[1]/i[2]'
DN_Diagnose_WanState_Alert = '//ul[@id="WanState"]/li[2]/p'
#上网状态
DN_Diagnose_NetState_Right = '//ul[@id="NetState"]/li[1]/i[1]'
DN_Diagnose_NetState_Wrong = '//ul[@id="NetState"]/li[1]/i[2]'
DN_Diagnose_NetState_Alert = 'id=WanErrDetail'
DN_Diagnose_NetState_Modify = '//ul[@id="NetState"]/li[2]/a'
#WiFi状态
DN_Diagnose_WiFiState_Right = '//li[@id="WifiState"]/i[1]'
DN_Diagnose_WiFiState_Wrong = '//li[@id="WifiState"]/i[2]'
DN_Diagnose_WiFiState_24G_Switch = 'id=SwitchWifi2G'
DN_Diagnose_WiFiState_24G_EnableAlert = '//*[@id="Wifi2G"]/span[1]'
DN_Diagnose_WiFiState_24G_Disable = '//*[@id="SwitchWifi2G"][@data-value="0"]'
DN_Diagnose_WiFiState_24G_DisableAlert = '//*[@id="Wifi2G"]/span[2]'
DN_Diagnose_WiFiState_5G_Switch = 'id=SwitchWifi5G'
DN_Diagnose_WiFiState_5G_EnableAlert = '//*[@id="Wifi5G"]/span[1]'
DN_Diagnose_WiFiState_5G_Disable = '//*[@id="SwitchWifi5G"][@data-value="0"]'
DN_Diagnose_WiFiState_5G_DisableAlert = '//*[@id="Wifi5G"]/span[2]'
DN_Diagnose_WiFiState_Signal_Switch = 'id=SwitchWifiSignal'
DN_Diagnose_WiFiState_Signal_EnableAlert =  '//*[@id="WifiSignal"]/span[1]'
DN_Diagnose_WiFiState_Signal_Disable = '//*[@id="SwitchWifiSignal"][@ data-value="0"]'
DN_Diagnose_WiFiState_Signal_DisableAlert =  '//*[@id="WifiSignal"]/span[2]'
#WiFi密码
DN_Diagnose_WiFiPswState_Right = '//li[@id="WifiPwdState"]/i[1]'
DN_Diagnose_WiFiPswState_Wrong = '//li[@id="WifiPwdState"]/i[2]'
DN_Diagnose_WiFiPswState_24GAlert = '//li[@id="WifiPwd2G"]/span'
DN_Diagnose_WiFiPswState_24GModify = '//li[@id="WifiPwd2G"]/a'
DN_Diagnose_WiFiPswState_5GAlert = '//li[@id="WifiPwd5G"]/span'
DN_Diagnose_WiFiPswState_5GModify = '//li[@id="WifiPwd5G"]/a'
#管理员密码
DN_Diagnose_RouterPsw_Right = '//li[@id="RouterPwdState"]/i[1]'
DN_Diagnose_RouterPsw_Wrong = '//li[@id="RouterPwdState"]/i[2]'
DN_Diagnose_RouterPsw_Alert = '//li[@id="RouterPwd"]/span'
DN_Diagnose_RouterPsw_Modify = '//li[@id="RouterPwd"]/a'
#固件版本
DN_Diagnose_Upgrade_Right = '//li[@id="UpgradeState"]/i[1]'
DN_Diagnose_Upgrade_Wrong = '//li[@id="UpgradeState"]/i[2]'
DN_Diagnose_Upgrade_Alert = '//li[@id="UpgradeDetail"]/span'
DN_Diagnose_Upgrade_Modify = '//li[@id="UpgradeDetail"]/a'
#开始体检/重新体检按钮
DN_Diagnose_StatrtCheck = 'id=Start'
#-----------------------------------------------------------------------
#                      健康节能
#-----------------------------------------------------------------------
#健康节能页面Title
ST_SignalSet_Title = '//div[@id="Content"]/div[2]/a/span'
#健康节能开关
ST_SignalSet_SwitchBotton = 'id=SignalSwitch'
ST_SignalSet_Switch_EnableStatus = '//div[@id="Content"]/div[3]/ul/p/span[@data-value="1"]'#健康节能模式
ST_SignalSet_Switch_DisableStatus = '//div[@id="Content"]/div[3]/ul/p/span[@data-value="0"]'#一件穿墙模式
#健康节能页面提示信息
ST_SignalSet_NoticeMassage = K2P_MTK_Spec.S_SignalSet_NoticeMassage
#-----------------------------------------------------------------------
#                       无线扩展
#-----------------------------------------------------------------------
#无线扩展页面Title
WE_Wisp_Title = '//div[@id="Content"]/div[2]/a/span'
#无线扩展开关
WE_Wisp_Switch = 'id=Switch'
WE_Wisp_Disable = '//span[@id="Switch"][@data-value="0"]'
WE_Wisp_Enable = '//span[@id="Switch"][@data-value="1"]'
#连接弹出框‘确认’按钮
WE_Wisp_Confirm =u'//input[@value="确定"]'
#连接模式
WE_Wisp_Mode_Auto = '//span[@id="WispModal"]/span[1][@data-idx="0"]'
WE_Wisp_Mode_Manual = '//span[@id="WispModal"]/span[2][@data-idx="1"]'
#--------------------------自动扫描获取模式----------------------------
#自动扫描获取开关状态
WE_Wisp_Mode_Auto_Disable= '//span[@id="WispModal"]/span[1][@data-idx="0"]/i[1]'
WE_Wisp_Mode_Auto_Enable ='//span[@id="WispModal"]/span[1][@data-idx="0"]/i[2]'
#开始扫描按钮
WE_Wisp_Mode_Auto_StartScan = 'id=StartScanbtn'
#重新扫描按钮
WE_Wisp_Mode_Auto_ReStartScan = 'id=reScanbtn'
#密码
WE_Wisp_Mode_Auto_PassWord = 'id=SsidPwdAuto'
#开始扩展
WE_Wisp_Mode_Auto_Save = 'id=SaveWisp'

#---------------------------扫描结果列表-----------------------------
#2.4G无线SSID列表参数
#SSID
WE_Wisp_Mode_Auto_24GSSID_List = ['//table[@id="ApTab2G"]/tbody/tr','/td[1]']
#MAC
WE_Wisp_Mode_Auto_24GMAC_List = ['//table[@id="ApTab2G"]/tbody/tr','/td[2]']
#连接
WE_Wisp_Mode_Auto_24GConnect_List = ['//table[@id="ApTab2G"]/tbody/tr','/td[4]']
#5G无线SSID列表参数
#5G无线表名
WE_Wisp_Mode_Auto_5G_Title = '//table[@id="ApTab5G"]/tbody/tr[1]/th[1]'
#SSID
WE_Wisp_Mode_Auto_5GSSID_List = ['//table[@id="ApTab5G"]/tbody/tr','/td[1]']
#MAC
WE_Wisp_Mode_Auto_5GMAC_List = ['//table[@id="ApTab5G"]/tbody/tr','/td[2]']
#连接
WE_Wisp_Mode_Auto_5GConnect_List = ['//table[@id="ApTab5G"]/tbody/tr','/td[4]']
#--------------------------手动输入模式-----------------------------
#手动输入开关状态
WE_Wisp_Mode_Manual_Disable = '//span[@id="WispModal"]/span[2][@data-idx="1"]/i[1]'
WE_Wisp_Mode_Manual_Enable = '//span[@id="WispModal"]/span[2][@data-idx="1"]/i[2]'
#网络名称
WE_Wisp_Mode_Manual_SSIDName = 'id=SsidName'
#安全模式
WE_Wisp_Mode_Manual_SafeMode = '//span[@id="SafeMode"]/span'
WE_Wisp_Mode_Manual_SafeMode_Open = '//ul[@id="sel-opts-ulSafeMode"]/li[1]'
WE_Wisp_Mode_Manual_SafeMode_WPAPSK = '//ul[@id="sel-opts-ulSafeMode"]/li[2]'
WE_Wisp_Mode_Manual_SafeMode_WPA2PSK = '//ul[@id="sel-opts-ulSafeMode"]/li[3]'
#加密类型
WE_Wisp_Mode_Manual_SafeType = '//span[@id="SafeType"]/span'
WE_Wisp_Mode_Manual_SafeType_TKIP = '//ul[@id="sel-opts-ulSafeType"]/li[1]'
WE_Wisp_Mode_Manual_SafeType_AES = '//ul[@id="sel-opts-ulSafeType"]/li[2]'
#网络密码
WE_Wisp_Mode_Manual_PassWord = 'id=WispPwd'
#开始扩展按钮
WE_Wisp_Mode_Manual_StartExtend = 'id=ExtendSave'
#-------------------------扩展完成信息显示----------------
WE_Wisp_SSID = 'id=ExtendSsid'
WE_Wisp_NetType = 'id=WanProto'
WE_Wisp_WanIP = 'id=WanIpaddr'
WE_Wisp_WanGateWay = 'id=WanGateway'
WE_Wisp_ReConfig = 'id=ConfigureSave'
WE_Wisp_Alert = '//div[@id="ExtendFail"]/div[1]/p'
#-----------------------------------------------------------------------
#                       屏幕显示
#-----------------------------------------------------------------------
#屏幕显示页面Title
SS_ScreenSet_Title = '//div[@id="Content"]/div[2]/a/span'
#息屏时间输入框
SS_ScreenSet_Time_Input = '//span[@id="Time"]/span'
SS_ScreenSet_Time_OneMinute = '//ul[@id="sel-opts-ulTime"]/li[1]'
SS_ScreenSet_Time_FiveMinute = '//ul[@id="sel-opts-ulTime"]/li[2]'
SS_ScreenSet_Time_TenMinute = '//ul[@id="sel-opts-ulTime"]/li[3]'
SS_ScreenSet_Time_ThirtyMinute = '//ul[@id="sel-opts-ulTime"]/li[4]'
SS_ScreenSet_Time_Never = '//ul[@id="sel-opts-ulTime"]/li[5]'
#保存
SS_ScreenSet_Save = 'id=Save'
#-----------------------------------------------------------------------
#                       存储管理
#-----------------------------------------------------------------------
#打开存储管理
US_UsbStorageSet = '//a[@href="#/pc/usbStorageApp"]'
#存储共享开关
US_UsbStorage_Switch = '//*[@id="SambaSwitch"]'
US_UsbStorage_Switch_Enable = '//*[@id="SambaSwitch"][@data-value="1"]'
US_UsbStorage_Switch_Disable = '//*[@id="SambaSwitch"][@data-value="0"]'
#存储加密开关
US_UsbStorage_Encrypt = '//*[@id="EncryptSwitch"]'
US_UsbStorage_Encrypt_Enable = '//*[@id="EncryptSwitch"][@data-value="1"]'
US_UsbStorage_Encrypt_Disable = '//*[@id="EncryptSwitch"][@data-value="0"]'
#存储加密用户名
US_UsbStorage_UserName = '//*[@id="UserName"]'
#存储加密密码
US_UsbStorage_PassWord = '//*[@id="Pwd"]'
#存储加密明码或加密显示按钮
US_UsbStorage_PswDisplay = '//*[@id="EncryptParam"]/ul[2]/li/i'
US_UsbStorage_PswDisplay_Enable = '//*[@id="EncryptParam"]/ul[2]/li/i[@data-value="1"]'
US_UsbStorage_PswDisplay_Disable = '//*[@id="EncryptParam"]/ul[2]/li/i[@data-value="0"]'

#媒体服务器
US_UsbStorage_Media = '//*[@id="MediaSwitch"]'
US_UsbStorage_Media_Enable = '//*[@id="MediaSwitch"][@data-value="1"]'
US_UsbStorage_Media_Disable = '//*[@id="MediaSwitch"][@data-value="0"]'
#保存
US_UsbStorage_Save = 'id=Save'
#防呆出现提示信息
US_UsbStorage_Message = '//*[@id="Content"]/div[3]/div[2]/p'

#-----------------------------------------------------------------------
#                       离线下载
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
#                       自动升级
#-----------------------------------------------------------------------
#进入自动升级
AU_AutoUpdateSet = u'//p[contains(text(),"自动升级")]'
#在线升级
AU_AutoUpdate_UpdateOnline = u'//label[contains(text(),"在线升级")]'
#自定义升级时间
AU_AutoUpdate_UpdateCustom = u'//label[contains(text(),"自定义升级时间")]'
#小时
AU_AutoUpdate_Hour = '//*[@id="Hour"]'
#分钟
AU_AutoUpdate_Minute = '//*[@id="Minute"]'
#保存
AU_AutoUpdate_Save = '//*[@id="Save"]'
#检测版本
AU_AutoUpdate_UpgradeNow = '//*[@id="Check"]'
#当前版本
AU_AutoUpdate_NowSW = '//*[@id="CurSwVer"]'
#最新版本
AU_AutoUpdate_NewSW = '//*[@id="NewSwVer"]'
#防呆出现提示信息
AU_AutoUpdate_Message = '//*[@id="TimingUpgrade"]/div[1]/p'
#自动升级
AU_AutoUpdate_Update = '//*[@id="Upgrade"]'
#自动升级固件下载提示
AU_AutoUpdate_Download = '//*[@id="Pop"]/div/div/div/i'
#路由器升级
AU_AutoUpdate_Update_Img = '//*[@id="Pop"]/div/div/p[1]/label'
#路由器升级警告
AU_AutoUpdate_Update_Warning = '//*[@id="Pop"]/div/p[2]'



#-----------------------------------------------------------------------
#                       安全设置
#-----------------------------------------------------------------------
#进入安全设置（按字搜索）
SS_SecuritySettingSet =u'//p[contains(text(),"安全设置")]'
#防火墙
SS_SecuritySetting_FirewallSwitch = '//*[@id="FirewallSwitch"]'
SS_SecuritySetting_FirewallSwitch_Enable = '//*[@id="FirewallSwitch"][@data-value="1"]'
SS_SecuritySetting_FirewallSwitch_Disable = '//*[@id="FirewallSwitch"][@data-value="0"]'
#DOS攻击过滤
SS_SecuritySetting_DosSwitch = '//*[@id="DosSwitch"]'
SS_SecuritySetting_DosSwitch_Enable = '//*[@id="DosSwitch"][@data-value="1"]'
SS_SecuritySetting_DosSwitch_Disable = '//*[@id="DosSwitch"][@data-value="0"]'
#ICMP攻击过滤
SS_SecuritySetting_IcmpSwitch = '//*[@id="IcmpSwitch"]'
SS_SecuritySetting_IcmpSwitch_Enable = '//*[@id="IcmpSwitch"][@data-value="1"]'
SS_SecuritySetting_IcmpSwitch_Disable = '//*[@id="IcmpSwitch"][@data-value="0"]'
SS_SecuritySetting_IcmpFlood = '//*[@id="IcmpFlood"]'
#UDP攻击过滤
SS_SecuritySetting_UdpSwitch = '//*[@id="UdpSwitch"]'
SS_SecuritySetting_UdpSwitch_Enable = '//*[@id="UdpSwitch"][@data-value="1"]'
SS_SecuritySetting_UdpSwitch_Disable = '//*[@id="UdpSwitch"][@data-value="0"]'
SS_SecuritySetting_UdpFlood = '//*[@id="UdpFlood"]'
#TCP攻击过滤
SS_SecuritySetting_TcpSwitch = '//*[@id="TcpSwitch"]'
SS_SecuritySetting_TcpSwitch_Enable = '//*[@id="TcpSwitch"][@data-value="1"]'
SS_SecuritySetting_TcpSwitch_Disable = '//*[@id="TcpSwitch"][@data-value="0"]'
SS_SecuritySetting_TcpFlood = '//*[@id="TcpFlood"]'
#PING过滤
SS_SecuritySetting_PingSwitch = '//*[@id="PingSwitch"]'
SS_SecuritySetting_PingSwitch_Enable = '//*[@id="PingSwitch"][@data-value="1"]'
SS_SecuritySetting_PingSwitch_Disable = '//*[@id="PingSwitch"][@data-value="0"]'
#保存
SS_SecuritySetting_Save = '//*[@id="Save"]'
#防呆出现提示信息
SS_SecuritySetting_Message = '//*[@id="DosAttack"]/div/p'
#-----------------------------------------------------------------------
#                       手动升级
#-----------------------------------------------------------------------

#当前版本
SC_Manual_UpgradeCurrentVer='//*[@id="CurSwVer"]'
#升级文件
SC_Manual_Upgrade_Scan='//*[@id="UpgradeFile"]'
#升级文件上传
SC_Manual_Upgrade_ScanFile='//*[@id="ScanFile"]'
#升级文件浏览按键
SC_Manual_Upgrade_ScanFileButton='//*[@id="ScanFile"]'
#上传升级
SC_Manual_Upgrade_Button='//*[@id="MnulUpgrade"]'
#官方下载链接
SC_Manual_Upgrade_URL = u'//span[contains(text(),"点击此处")]'
#没有选择版本文件，直接点上传升级后，弹出的对话框，确定按钮的id
SC_Manual_Upgrade_Message=u'//input[@value="确定"]'


#-----------------------------------------------------------------------
#                       打印服务器
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
#                       远程管理
#-----------------------------------------------------------------------
#进入远程管理
RM_RemoteManageSet = u'//p[contains(text(),"远程管理")]'
#远程管理开关
RM_RemoteManage_Switch ='//*[@id="RemoteSwitch"]'
RM_RemoteManage_Switch_Enable  = '//*[@id="RemoteSwitch"][@data-value="1"]'
RM_RemoteManage_Switch_Disable = '//*[@id="RemoteSwitch"][@data-value="0"]'
#远程管理端口
RM_RemoteManage_Switch_Port = '//*[@id="RemotePort"]'
#远程管理允许IP
RM_RemoteManage_Switch_Ip = '//*[@id="RemoteIp"]'
#保存
RM_RemoteManage_Save = 'id=Save'
#远程管理提示信息
RM_RemoteManage_Message = '//*[@id="Param"]/div/p'

#-----------------------------------------------------------------------
#                       购物比价
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
#                       LAN设置
#-----------------------------------------------------------------------
FS_LanSet_IpAddress = 'id=LanIp'
FS_LanSet_Mask = 'id=LanMask'
FS_LanSet_Save = 'id=Save'
FS_LanSet_SaveConfirm = '//input[2]'
FS_LanSet_SaveCancel = '//input[1]'
#-----------------------------------------------------------------------
#                       DHCP服务
#-----------------------------------------------------------------------
#返回上一级按钮
ST_DHCPReturn='//div[@id="Content"]/div/a/i'
ST_DHCPService='//div[@id="Content"]/div/a/span' #css=span.head-title
#ST_DHCPEnable='//span[@id="Switch"]/i' #css=i.switch-circle.icon_select_off id=Switch
ST_DHCPSwitch='id=Switch'
ST_DHCPStartIP='id=DhcpStart'
ST_DHCPEndIP='id=DhcpEnd'
ST_DHCPSave='id=Save'
ST_DHCPNet='id=DhcpNet'
ST_DHCPDevName='id=DevName'
ST_DHCPIpAddr='id=IpAddr'
ST_DHCPMacAddr='id=MacAddr'
ST_DHCPBind='id=Bind'
ST_DHCPEdit=['']
ST_DHCPDelete=['']
for i in range (2,12):
    ST_DHCPEdit.append('//table[@id="DhcpBind"]/tbody/tr[%s]/td[4]/span[1][contains(text(),"编辑")]'%i)
    ST_DHCPDelete.append('//table[@id="DhcpBind"]/tbody/tr[%s]/td[4]/span[2][contains(text(),"删除")]'%i)
    
ST_DHCPCancel='id=Cancel'
#-----------------------------------------------------------------------
#                       动态DNS
#-----------------------------------------------------------------------
DDNS_Switch_Off='//*[@id="Switch"][@data-value="0"]'
DDNS_Switch_Provider='//*[@id="Provider"]/i'
DDNS_User='id=UserName'
DDNS_Pwd='id=Pwd'
DDNS_Hostname='id=HostName'
DDNS_Save='id=Save'


#-----------------------------------------------------------------------
#                       端口转发
#-----------------------------------------------------------------------
PF_Switch_On='//*[@id="SwitchFwd"][@data-value="1"]'
PF_Switch_Off='//*[@id="SwitchFwd"][@data-value="0"]'
PF_RuleName='id=RuleName'
PF_ServerIp='id=ServerIp'
PF_ExternalPort='id=ExternalPort'
PF_InternalPort='id=InternalPort'
PF_protocol='//*[@id="PortAgreement"]/i'
PF_Save='id=SaveAdd'
PF_Cancel='id=Cancel'
PF_AddRule='//*[@id="FwdTab"]/ul'
PF_RuleEdit=['']
PF_RuleDelete=['']
for i in range (2,12):
    PF_RuleEdit.append('//*[@id="PortfwdTab"]/tbody/tr[%s]/td[6]/span[1][contains(text(),"编辑")]'%i)
    PF_RuleDelete.append('//*[@id="PortfwdTab"]/tbody/tr[%s]/td[6]/span[2][contains(text(),"删除")]'%i)
PF_RuleSaveEdit='id=SaveEdit'

#-----------------------------------------------------------------------
#                       DMZ主机
#-----------------------------------------------------------------------
DMZ_Switch_Off='//*[@id="RemoteSwitch"][@data-value="0"]'
DMZ_Switch_On='//*[@id="RemoteSwitch"][@data-value="1"]'
DMZ_IP='id=RemoteIp'
DMZ_Save='id=Save'
#-----------------------------------------------------------------------
#                       UPNP
#-----------------------------------------------------------------------
UPNP_Switch_On='//*[@id="UpnpSwitch"][@data-value="1"]'
UPNP_Switch_Off='//*[@id="UpnpSwitch"][@data-value="0"]'

#-----------------------------------------------------------------------
#                       QoS
#-----------------------------------------------------------------------
#进入QoS
QS_QosSet = '//*[@href="#/pc/QoSApp"]'
#QoS开关
QS_Qos_Switch = '//*[@id="QosSwitch"]'
QS_Qos_Switch_Enable = '//*[@id="QosSwitch"][@data-value="1"]'
QS_Qos_Switch_Disable = '//*[@id="QosSwitch"][@data-value="0"]'
#QoS上行带宽
QS_Qos_Up = '//*[@id="QosObw"]'
#QoS下行带宽
QS_Qos_Down = '//*[@id="QosIbw"]'

#智能模式 
QS_Qos_Mode_Smart = '//*[@data-idx="0"]'
#优先级模式 
QS_Qos_Mode_Priority = '//*[@data-idx="1"]'

#优先级模式 规则名称
QS_Qos_List_RuleName = '//*[@id="RuleName"]'
#优先级模式 协议类型
QS_Qos_Protocol = '//*[@id="QosProtocol"]'
#优先级模式 协议类型 UDP
QS_Qos_Protocol_UDP = '//*[@id="sel-opts-ulQosProtocol"]/li[1]'
#优先级模式 协议类型 TCP
QS_Qos_Protocol_TCPUDP = '//*[@id="sel-opts-ulQosProtocol"]/li[2]'
#优先级模式 协议类型 TCP&UDP
QS_Qos_Protocol_TCP = '//*[@id="sel-opts-ulQosProtocol"]/li[3]'
#优先级模式 端口类型
QS_Qos_Porttype = '//*[@id="QosPorttype"]'
#优先级模式 端口类型 目的端口
QS_Qos_Porttype_Destination  = '//*[@id="sel-opts-ulQosPorttype"]/li[1]'
#优先级模式 端口类型 源端口
QS_Qos_Porttype_Original  = '//*[@id="sel-opts-ulQosPorttype"]/li[2]'
#优先级模式 端口类型 源或目的端口
QS_Qos_Porttype_DestinationOrOriginal = '//*[@id="sel-opts-ulQosPorttype"]/li[3]'
#优先级模式 端口号
QS_Qos_List_Port = '//*[@id="QosPort"]'
#优先级模式 优先级
QS_Qos_Priority = '//*[@id="QosPriority"]'
#优先级模式 优先级 高
QS_Qos_Priority_High  = '//*[@id="sel-opts-ulQosPriority"]/li[1]'
#优先级模式 优先级 中
QS_Qos_Priority_Medium = '//*[@id="sel-opts-ulQosPriority"]/li[2]'
#优先级模式 优先级 低
QS_Qos_Priority_Low = '//*[@id="sel-opts-ulQosPriority"]/li[3]'
#优先级模式 保存
QS_Qos_List_Save = '//*[@id="SaveAdd"]'
#优先级模式 取消
QS_Qos_List_Cancel = '//*[@id="Cancel"]'
#优先级模式 编辑
QS_Qos_List_Edit = '//tr[@value="'
QS_Qos_List_Edit1 = '"]/*/span[1]'
#优先级模式 删除
QS_Qos_List_Delete = '//tr[@value="'
QS_Qos_List_Delete1 = '"]/*/span[2]'
#优先级模式 添加规则
QS_Qos_List_Add = '//*[@id="QosTab"]/ul'
#保存
QS_Qos_Save = 'id=Save'
#防呆出现提示信息
QS_Qos_Message = '//*[@style="display: block;"]/div/p'




#-----------------------------------------------------------------------
#                       VPN服务器
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#                       VPN客户端
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
#                       PhiCloud个人云
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#                       PhiCDN
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#                       自动升级
#-----------------------------------------------------------------------
#进入自动升级
AU_AutoUpdateSet = u'//p[contains(text(),"自动升级")]'
#在线升级
AU_AutoUpdate_UpdateOnline = u'//label[contains(text(),"在线升级")]'
#自定义升级时间
AU_AutoUpdate_UpdateCustom = u'//label[contains(text(),"自定义升级时间")]'
#小时
AU_AutoUpdate_Hour = '//*[@id="Hour"]'
#分钟
AU_AutoUpdate_Minute = '//*[@id="Minute"]'
#保存
AU_AutoUpdate_Save = '//*[@id="Save"]'
#检测版本
AU_AutoUpdate_UpgradeNow = '//*[@id="Check"]'
#当前版本
AU_AutoUpdate_NowSW = '//*[@id="CurSwVer"]'
#最新版本
AU_AutoUpdate_NewSW = '//*[@id="NewSwVer"]'
#防呆出现提示信息
AU_AutoUpdate_Message = '//*[@id="TimingUpgrade"]/div[1]/p'
#自动升级
AU_AutoUpdate_Update = '//*[@id="Upgrade"]'

#-----------------------------------------------------------------------
#                       备份恢复
#-----------------------------------------------------------------------
#打开备份恢复
BR_BackupRestore = '//*[contains(text(),"备份恢复")]'
#当前版本
BR_BackupRestore_NowSW = '//*[@id="CurSwVer"]'

#备份配置按键
BR_BackupRestore_Backup = 'id=BackupCfg'
#恢复配置文件浏览_页面检查
BR_BackupRestore_FileBrowse = '//*[@id="CfgFile"]'
#恢复配置文件浏览_配置
BR_BackupRestore_File = '//*[@id="ScanFile"]'
#恢复配置按键
BR_BackupRestore_Recover = 'id=RecoverCfg'
#恢复出厂设置按键
BR_BackupRestore_Restore = '//*[@id="Reset"]'
#恢复出厂设置按键，再次确认页面，点击确认
BR_BackupRestore_Restore_Again = '//input[@value="确定"]'
#防呆出现提示信息
BR_BackupRestore_Message = '//*[@id="Pop"]/div/div/input'

