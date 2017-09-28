# -*- coding: utf-8 -*-
#------------------------------------------------------------
# 
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# 
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.ismoke'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UC_24jKIAWs4f3nk21CGgVRg"
YOUTUBE_CHANNEL_ID_2 = "PL3tf-8jUewlnWQ1cD5xaYjlmY8640BYVB"
YOUTUBE_CHANNEL_ID_3 = "PL3tf-8jUewll7lWLg23G7bhDq6lYEBKLH"
YOUTUBE_CHANNEL_ID_4 = "PL3tf-8jUewlmIFw7oZxpa_QVFWOelkyzf"
YOUTUBE_CHANNEL_ID_5 = "PL3tf-8jUewlkLQe9_NppdO7QI9VvgZ7cI"
YOUTUBE_CHANNEL_ID_6 = "PL3tf-8jUewlmQFmrm_KTZ4JzgkDpvujMl"
YOUTUBE_CHANNEL_ID_7 = "PL3tf-8jUewlmPaBJ1x8DRasYN8q7Q6B97"
YOUTUBE_CHANNEL_ID_8 = ""
YOUTUBE_CHANNEL_ID_9 = ""
YOUTUBE_CHANNEL_ID_10 = ""
YOUTUBE_CHANNEL_ID_11 = ""
YOUTUBE_CHANNEL_ID_12 = ""
YOUTUBE_CHANNEL_ID_13 = ""
YOUTUBE_CHANNEL_ID_14 = ""
YOUTUBE_CHANNEL_ID_15 = ""


# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="All ISMOKE Videos",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/playlists/",
        thumbnail="http://www.ismokemag.co.uk/wp-content/uploads/2017/02/logo-retina.png",
        fanart="https://github.com/lefty420/media/raw/master/background.jpg",
        
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Strain Reviews",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://github.com/lefty420/media/blob/master/1.jpg?raw=true",
        fanart="https://github.com/lefty420/media/raw/master/background.jpg",
        
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wake and Bake With Tyler Green",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://github.com/lefty420/media/blob/master/4.jpg?raw=true",
        fanart="https://github.com/lefty420/media/raw/master/background.jpg",
        folder=True )
  
    plugintools.add_item( 
        #action="", 
        title="Cannabis News",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
       thumbnail="https://github.com/lefty420/media/blob/master/5.jpg?raw=true",
        fanart="https://github.com/lefty420/media/raw/master/background.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Cannabis Events",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://github.com/lefty420/media/blob/master/2.jpg?raw=true",
        fanart="https://github.com/lefty420/media/raw/master/background.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Ismoke Bud Facts",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://github.com/lefty420/media/blob/master/6.jpg?raw=true",
        fanart="https://github.com/lefty420/media/raw/master/background.jpg",
        folder=True )   
run()
