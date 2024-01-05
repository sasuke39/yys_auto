from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class BuyAssets: 


	# Click Rule Assets
	# description 
	C_BUY_ONE = RuleClick(roi_front=(551,506,174,36), roi_back=(551,506,174,36), name="buy_one")
	# description 
	C_BUY_MORE = RuleClick(roi_front=(551,540,174,40), roi_back=(551,540,174,40), name="buy_more")
	# 取消购买 
	C_BUY_CANCEL = RuleClick(roi_front=(121,2,100,22), roi_back=(121,2,100,22), name="buy_cancel")


	# Image Rule Assets
	# 拉满 
	I_BUY_PLUS = RuleImage(roi_front=(759,422,50,58), roi_back=(746,397,98,156), threshold=0.8, method="Template matching", file="./tasks/Component/Buy/buy/buy_buy_plus.png")
	# 加一个 
	I_BUY_ADD = RuleImage(roi_front=(671,428,51,54), roi_back=(645,412,111,141), threshold=0.8, method="Template matching", file="./tasks/Component/Buy/buy/buy_buy_add.png")
	# 减 
	I_BUY_SUB = RuleImage(roi_front=(467,429,50,48), roi_back=(452,412,85,147), threshold=0.8, method="Template matching", file="./tasks/Component/Buy/buy/buy_buy_sub.png")
	# 出现用魂玉购买 
	I_BUY_RMB = RuleImage(roi_front=(610,532,35,32), roi_back=(548,483,178,119), threshold=0.8, method="Template matching", file="./tasks/Component/Buy/buy/buy_buy_rmb.png")


	# Ocr Rule Assets
	# Ocr-description 
	O_BUY_NUMBER = RuleOcr(roi=(578,416,52,46), area=(578,416,52,46), mode="Digit", method="Default", keyword="", name="buy_number")


