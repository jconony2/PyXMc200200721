# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:17:13 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random

#我邊走,不同的花一直出現
while True : 
    x,y,z = mc.player.getTilePos()
    color = random.randrange(0,10)
    mc.setBlock(x,y,z-1,38,color)
    time.sleep(0.2)





















