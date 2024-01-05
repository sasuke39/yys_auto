# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime, time

from tasks.Component.SwitchSoul.switch_soul_config import SwitchSoulConfig
from tasks.Component.SwitchSoul.switch_soul_config_by_choice import SwitchSoulConfigByChoice
from tasks.Component.config_scheduler import Scheduler
from tasks.Component.config_base import ConfigBase, TimeDelta
from tasks.Component.GeneralBattle.config_general_battle import GeneralBattleConfig
from tasks.Utils.config_enum import ShikigamiClass

class UtilizeScheduler(Scheduler):
    priority = Field(default=2, description='priority_help')

class DemonEncounter(ConfigBase):
    scheduler: UtilizeScheduler = Field(default_factory=UtilizeScheduler)
    # switch_soul: SwitchSoulConfig = Field(default_factory=SwitchSoulConfig)
    switch_soul_by_ch: SwitchSoulConfigByChoice = Field(default_factory=SwitchSoulConfigByChoice)
    # general_battle_config: GeneralBattleConfig = Field(default_factory=GeneralBattleConfig)


