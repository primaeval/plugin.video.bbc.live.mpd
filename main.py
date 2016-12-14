from xbmcswift2 import Plugin, ListItem
from xbmcswift2 import actions
import xbmc,xbmcaddon,xbmcvfs,xbmcgui


plugin = Plugin()

def log(v):
    xbmc.log(repr(v))


@plugin.route('/')
def index():
    channel_list = [
            ('bbc_one_hd',                       'BBC One'),
            ('bbc_two_hd',                       'BBC Two'),
            ('bbc_four_hd',                      'BBC Four'),
            ('cbbc_hd',                          'CBBC'),
            ('cbeebies_hd',                      'CBeebies'),
            ('bbc_news24',                       'BBC News Channel'),
            ('bbc_parliament',                   'BBC Parliament'),
            ('bbc_alba',                         'Alba'),
            ('s4cpbs',                           'S4C'),
            ('bbc_one_london',                   'BBC One London'),
            ('bbc_one_scotland_hd',              'BBC One Scotland'),
            ('bbc_one_northern_ireland_hd',      'BBC One Northern Ireland'),
            ('bbc_one_wales_hd',                 'BBC One Wales'),
            ('bbc_two_scotland',                 'BBC Two Scotland'),
            ('bbc_two_northern_ireland_digital', 'BBC Two Northern Ireland'),
            ('bbc_two_wales_digital',            'BBC Two Wales'),
            ('bbc_two_england',                  'BBC Two England',),
            ('bbc_one_cambridge',                'BBC One Cambridge',),
            ('bbc_one_channel_islands',          'BBC One Channel Islands',),
            ('bbc_one_east',                     'BBC One East',),
            ('bbc_one_east_midlands',            'BBC One East Midlands',),
            ('bbc_one_east_yorkshire',           'BBC One East Yorkshire',),
            ('bbc_one_north_east',               'BBC One North East',),
            ('bbc_one_north_west',               'BBC One North West',),
            ('bbc_one_oxford',                   'BBC One Oxford',),
            ('bbc_one_south',                    'BBC One South',),
            ('bbc_one_south_east',               'BBC One South East',),
            ('bbc_one_west',                     'BBC One West',),
            ('bbc_one_west_midlands',            'BBC One West Midlands',),
            ('bbc_one_yorks',                    'BBC One Yorks',),
    ]
    items = []
    for id,name in channel_list:
        icon = 'special://home/addons/plugin.video.bbc.live.mpd/resources/media/%s.png' % id
        path = 'http://a.files.bbci.co.uk/media/live/manifesto/audio_video/simulcast/dash/uk/dash_pc/ak/%s.mpd' % id
        item = ListItem(label=name,icon=icon,path=path)
        item.set_property('inputstreamaddon', 'inputstream.adaptive')
        item.set_property('inputstream.adaptive.manifest_type', 'mpd')
        item.set_is_playable(True)
        items.append(item)
    return items


if __name__ == '__main__':
    plugin.run()
