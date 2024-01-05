from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class RestartAssets: 


	# Image Rule Assets
	# 点击勾玉 
	I_HARVEST_JADE = RuleImage(roi_front=(732,489,34,33), roi_back=(177,451,963,100), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_jade.png")
	# 签到小图标 
	I_HARVEST_SIGN = RuleImage(roi_front=(295,496,32,43), roi_back=(70,481,889,71), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign.png")
	# description 
	I_HARVEST_SIGN_2 = RuleImage(roi_front=(592,135,100,252), roi_back=(592,135,100,252), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_2.png")
	# 999签到福袋 
	I_HARVEST_SIGN_999 = RuleImage(roi_front=(345,494,23,29), roi_back=(51,459,888,92), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_999.png")
	# 邮件小图标 
	I_HARVEST_MAIL = RuleImage(roi_front=(337,505,37,25), roi_back=(38,476,880,78), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail.png")
	# 全部收取 
	I_HARVEST_MAIL_ALL = RuleImage(roi_front=(80,622,75,64), roi_back=(80,622,75,64), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_all.png")
	# 有些邮件需要点击一次 
	I_HARVEST_MAIL_OPEN = RuleImage(roi_front=(163,367,45,48), roi_back=(139,86,100,487), threshold=0.9, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_open.png")
	# 确认收取邮件 
	I_HARVEST_MAIL_CONFIRM = RuleImage(roi_front=(687,543,168,64), roi_back=(687,543,168,64), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_confirm.png")
	# description 
	I_HARVEST_SOUL = RuleImage(roi_front=(241,497,38,36), roi_back=(68,480,930,72), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_soul.png")
	# description 
	I_HARVEST_MAIL_TITLE = RuleImage(roi_front=(520,48,245,41), roi_back=(520,48,245,41), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_title.png")
	# description 
	I_HARVEST_AP = RuleImage(roi_front=(721,486,31,38), roi_back=(206,462,999,81), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_ap.png")
	# 打开聊天频道会自动关闭 
	I_HARVEST_CHAT_CLOSE = RuleImage(roi_front=(639,309,35,100), roi_back=(639,309,35,100), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_chat_close.png")
	# 签到 
	I_HARVEST_SIGN_3 = RuleImage(roi_front=(291,495,33,36), roi_back=(100,473,1014,70), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_3.png")
	# description 
	I_HARVEST_SIGN_4 = RuleImage(roi_front=(587,151,100,228), roi_back=(547,123,185,281), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_4.png")


	# Image Rule Assets
	# 庭院卷轴打开 
	I_LOGIN_SCROOLL_OPEN = RuleImage(roi_front=(1208,609,33,83), roi_back=(1208,609,33,83), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_scrooll_open.png")
	# 庭院卷轴关闭 
	I_LOGIN_SCROOLL_CLOSE = RuleImage(roi_front=(1184,628,35,45), roi_back=(1184,628,35,45), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_scrooll_close.png")
	# description 
	I_LOGIN_RED_CLOSE = RuleImage(roi_front=(1158,62,39,37), roi_back=(912,42,309,281), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_red_close.png")
	# description 
	I_LOGIN_YELLOW_CLOSE = RuleImage(roi_front=(29,17,46,44), roi_back=(0,0,94,86), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_yellow_close.png")
	# 用于判断是否出现登录选区的 
	I_LOGIN_8 = RuleImage(roi_front=(178,572,53,60), roi_back=(1,547,241,105), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_8.png")
	# 登录时候不观看CG视频 
	I_WATCH_VIDEO_CANCEL = RuleImage(roi_front=(466,396,130,61), roi_back=(466,396,130,61), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_watch_video_cancel.png")
	# 指定角色进入游戏,默认第一个 
	I_LOGIN_SPECIFIC_SERVE = RuleImage(roi_front=(24,33,52,47), roi_back=(24,33,52,47), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_specific_serve.png")
	# 下载插画 
	I_LOGIN_LOAD_DOWN = RuleImage(roi_front=(711,450,153,58), roi_back=(711,450,153,58), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_load_down.png")


	# Ocr Rule Assets
	# 正在连接服务器 
	O_LOGIN_NETWORK = RuleOcr(roi=(534,649,189,39), area=(210,492,100,100), mode="Single", method="Default", keyword="正在连接服务器", name="login_network")
	# Ocr-description 
	O_LOGIN_ENTER_GAME = RuleOcr(roi=(550,567,176,56), area=(558,574,154,49), mode="Single", method="Default", keyword="进入游戏", name="login_enter_game")
	# 点击屏幕跳过 
	O_LOGIN_SKIP_1 = RuleOcr(roi=(1046,35,130,37), area=(1046,35,130,37), mode="Single", method="Default", keyword="点击屏幕跳过", name="login_skip_1")
	# 登录指定角色，默认第一个 
	O_LOGIN_SPECIFIC_SERVE = RuleOcr(roi=(524,600,242,53), area=(516,75,662,585), mode="Single", method="Default", keyword="游戏", name="login_specific_serve")

