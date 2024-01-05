# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime, time


# 逢魔针对不同妖怪切换不同预设御魂
class SwitchSoulConfigByChoice(BaseModel):
    enable: bool = Field(default=False, description= '逢魔御魂预设组，初始值会默认阵容战斗"1,2"表示第一个预设组\n，第二个队伍预设组支持[1-7], 预设队伍支持[1-4]')
    NAMAZU: str = Field(default='-1,-1', description='地震鲇')
    SHINKIRO: str = Field(default='-1,-1', description='蜃气楼')
    ODOKURO: str = Field(default='-1,-1', description='荒骷髅')
    OBOROGURUMA: str = Field(default='-1,-1', description='胧车')
    TSUCHIGUMO: str = Field(default='-1,-1', description='土蜘蛛')
    SONGSTRESS: str = Field(default='-1,-1', description='歌姬')