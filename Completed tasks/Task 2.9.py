Default_string = """SKU: 32515151jDJASD1924
SKU: 12389719287498124
SKU: JKDFLK893479831749
SKU: fdakf998u3498U(jD(
SKU: aSDJALKSJD189432719"""


list = Default_string.split("SKU: ")[1:]    #start from the first position ignores the empty ''
final_list = []


for x in list:
    id = x.split("\n")                  #cringe ass split
    clean_id = id[0]
    final_list.append(clean_id)

print(final_list)




HTML = """<li class="toclevel-1 tocsection-13"><a href="#Pets"><span class="tocnumber">3</span> <span class="toctext">Pets</span></a></li>
<li class="toclevel-1 tocsection-14"><a href="#Shop_Upgrades"><span class="tocnumber">4</span> <span class="toctext">Shop Upgrades</span></a>
<ul>
<li class="toclevel-2 tocsection-15"><a href="#Ship_Upgrades"><span class="tocnumber">4.1</span> <span class="toctext">Ship Upgrades</span></a></li>
<li class="toclevel-2 tocsection-16"><a href="#Other_Shop_Purchases"><span class="tocnumber">4.2</span> <span class="toctext">Other Shop Purchases</span></a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-17"><a href="#All_Points_of_Interest"><span class="tocnumber">5</span> <span class="toctext">All Points of Interest</span></a></li>
<li class="toclevel-1 tocsection-18"><a href="#Skill_Boosts"><span class="tocnumber">6</span> <span class="toctext">Skill Boosts</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Skill_Overview">Skill Overview</span></h2>
<p>The World Map of Melvor consists of a grid of 944 hexagonal map tiles (called Hexes). The map layout is the same for all players and all players start on <span style="display:inline-block">(15, 16)</span>. The primary action for Cartography is Surveying map tiles in order to discover them.
</p><p>Once a Hex has been fully discovered, the player may travel there. Some Hexes contain Points of Interest which will be revealed upon traveling to the tile. Visiting a Point of Interest will always provide a blurb of text explaining a bit about the location, and some Points of Interest will reward the player with resources upon the first visit.
</p><p>The base interval for a Survey action is 5 seconds. It can be reduced through <a href="/w/Cartography/Boosts#Interval_Boosts" title="Cartography/Boosts">various boosts</a>.
</p>
<h3><span class="mw-headline" id="Map_Mastery">Map Mastery</span></h3>
<p>When first discovering the map, each hex will have a level between 1 and 5 that will determine how many times it must be surveyed in order to be discovered. Initially only point-of-interest tiles will let you survey to level 5. Once the map has been fully discovered, the maximum level for all hexes will increase to 5. Leveling a hex to 5 is referred to as "Mastering" it, and Mastering all 944 hexes is referred to as "Map Mastery".
</p><p>Fully discovering the map takes 192,168 survey actions and will provide sufficient experience to get to <span style="display:inline-block"><span><a href="/w/Cartography" title="Cartography"><img alt="Cartography" src="/images/thumb/0/05/Cartography_%28skill%29.png/20px-Cartography_%28skill%29.png" decoding="async" width="20" height="20" srcset="/images/thumb/0/05/Cartography_%28skill%29.png/30px-Cartography_%28skill%29.png 1.5x, /images/thumb/0/05/Cartography_%28skill%29.png/40px-Cartography_%28skill%29.png 2x"></a></span> Level 100</span>. Fully mastering the map takes 815,616 survey actions, for a total of 47 days, 4 hours, 48 minutes at the base time interval of 5 seconds, and will provide more than enough experience to reach <span style="display:inline-block"><span><a href="/w/Cartography" title="Cartography"><img alt="Cartography" src="/images/thumb/0/05/Cartography_%28skill%29.png/20px-Cartography_%28skill%29.png" decoding="async" width="20" height="20" srcset="/images/thumb/0/05/Cartography_%28skill%29.png/30px-Cartography_%28skill%29.png 1.5x, /images/thumb/0/05/Cartography_%28skill%29.png/40px-Cartography_%28skill%29.png 2x"></a></span> Level 120</span>.
</p>
<div class="content-table-wrapper"><div class="content-table-scrollbar inactive" style="width: 852.102px;"><div class="content-table-spoof" style="width: 286.886px;"></div></div><div class="content-table-left"></div><div class="content-table-right"></div><div class="content-table"><table class="wikitable">
<td>240
</td></tr>
<tr>
<td>5</td>
<td>864</td>
<td>360
</td></tr></tbody></table></div></div>
<h3><span class="mw-headline" id="Mastery_Unlocks">Mastery Unlocks</span></h3>
<p>Once enough tiles have been mastered, the following bonuses will be unlocked:
</p>
<div class="content-table-wrapper"><div class="content-table-scrollbar inactive" style="width: 852.102px;"><div class="content-table-spoof" style="width: 568.5px;"></div></div><div class="content-table-left"></div><div class="content-table-right"></div><div class="content-table"><table class="wikitable stickyHeaders"><tbody><tr class="headerRow-0"><th>Hexes Mastered</th><th>Passive Bonuses</th><th>Rewards</th></tr><tr><td>100</td><td><span class="text-positive">+5% Skill XP for all Skills</span></td><td><span class="img-text">5 <a href="/w/Bank_Slot_Token" title="Bank Slot Token"><img alt="" src="/images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/25px-Bank_Slot_Token_%28item%29.png" decoding="async" width="25" height="25" srcset="/images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/38px-Bank_Slot_Token_%28item%29.png 1.5x, /images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/50px-Bank_Slot_Token_%28item%29.png 2x"></a> <a href="/w/Bank_Slot_Token" title="Bank Slot Token">Bank Slot Token</a></span></td></tr><tr><td>200</td><td><span class="text-positive">+5% Mastery XP in all Skills</span></td><td><span class="img-text">10 <a href="/w/Bank_Slot_Token" title="Bank Slot Token"><img alt="" src="/images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/25px-Bank_Slot_Token_%28item%29.png" decoding="async" width="25" height="25" srcset="/images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/38px-Bank_Slot_Token_%28item%29.png 1.5x, /images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/50px-Bank_Slot_Token_%28item%29.png 2x"></a> <a href="/w/Bank_Slot_Token" title="Bank Slot Token">Bank Slot Token</a></span></td></tr><tr><td>300</td><td class="table-na">None</td><td><span class="img-text">25 <a href="/w/Bank_Slot_Token" title="Bank Slot Token"><img alt="" src="/images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/25px-Bank_Slot_Token_%28item%29.png" decoding="async" width="25" height="25" srcset="/images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/38px-Bank_Slot_Token_%28item%29.png 1.5x, /images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/50px-Bank_Slot_Token_%28item%29.png 2x"></a> <a href="/w/Bank_Slot_Token" title="Bank Slot Token">Bank Slot Token</a></span></td></tr><tr><td>500</td><td><span class="text-positive">+10% Global GP (except Item Sales)</span></td><td><span class="img-text">15 <a href="/w/Bank_Slot_Token" title="Bank Slot Token"><img alt="" src="/images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/25px-Bank_Slot_Token_%28item%29.png" decoding="async" width="25" height="25" srcset="/images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/38px-Bank_Slot_Token_%28item%29.png 1.5x, /images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/50px-Bank_Slot_Token_%28item%29.png 2x"></a> <a href="/w/Bank_Slot_Token" title="Bank Slot Token">Bank Slot Token</a></span></td></tr><tr><td>750</td><td class="table-na">None</td><td><span class="img-text">45 <a href="/w/Bank_Slot_Token" title="Bank Slot Token"><img alt="" src="/images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/25px-Bank_Slot_Token_%28item%29.png" decoding="async" width="25" height="25" srcset="/images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/38px-Bank_Slot_Token_%28item%29.png 1.5x, /images/thumb/2/2d/Bank_Slot_Token_%28item%29.png/50px-Bank_Slot_Token_%28item%29.png 2x"></a> <a href="/w/Bank_Slot_Token" title="Bank Slot Token">Bank Slot Token</a></span></td></tr><tr><td>944</td><td><span class="text-positive">-3% Interval for all non-Combat Skills</span><br><span class="text-positive">-3% Attack Interval</span></td><td><span class="img-text"><a href="/w/Atlas_of_Discovery_Expansion" title="Atlas of Discovery Expansion"><img alt="AoD.png" src="/images/thumb/c/c0/AoD.png/25px-AoD.png" decoding="async" width="25" height="24" srcset="/images/thumb/c/c0/AoD.png/38px-AoD.png 1.5x, /images/thumb/c/c0/AoD.png/50px-AoD.png 2x"></a></span> <span class="img-text"><a href="/w/Carthulu" title="Carthulu"><img alt="" src="/images/thumb/9/9e/Carthulu_%28pet%29.png/25px-Carthulu_%28pet%29.png" decoding="async" width="25" height="25" srcset="/images/thumb/9/9e/Carthulu_%28pet%29.png/38px-Carthulu_%28pet%29.png 1.5x, /images/thumb/9/9e/Carthulu_%28pet%29.png/50px-Carthulu_%28pet%29.png 2x"></a> <a href="/w/Carthulu" title="Carthulu">Carthulu</a></span></td></tr></tbody></table></div></div>
<h3><span class="mw-headline" id="Undiscovered_Hexes">Undiscovered Hexes</span></h3>
<p>These icons will appear on undiscovered Hexes if there is something to discover underneath.
</p>
<div class="content-table-wrapper"><div class="content-table-scrollbar inactive" style="width: 852.102px;"><div class="content-table-spoof" style="width: 1199.38px;"></div></div><div class="content-table-left"></div><div class="content-table-right"></div><div class="content-table"><table class="wikitable">

<tbody><tr>
<th>Icon</th>
<th>Description
</th></tr>
<tr>
<td><div class="center"><div class="floatnone"><a href="/w/File:Undisc_dig_site.png" class="image"><img alt="! icon" src="/images/thumb/e/e3/Undisc_dig_site.png/7px-Undisc_dig_site.png" decoding="async" width="7" height="38" srcset="/images/thumb/e/e3/Undisc_dig_site.png/11px-Undisc_dig_site.png 1.5x, /images/thumb/e/e3/Undisc_dig_site.png/14px-Undisc_dig_site.png 2x"></a></div></div></td>
<td>Denotes the location of an undiscovered <span class="img-text"><a href="/w/Archaeology" title="Archaeology"><img alt="" src="/images/thumb/a/a7/Archaeology_%28skill%29.png/23px-Archaeology_%28skill%29.png" decoding="async" width="23" height="23" srcset="/images/thumb/a/a7/Archaeology_%28skill%29.png/35px-Archaeology_%28skill%29.png 1.5x, /images/thumb/a/a7/Archaeology_%28skill%29.png/46px-Archaeology_%28skill%29.png 2x"></a> <a href="/w/Archaeology" title="Archaeology">Archaeology</a></span> Dig Site. Locations for these dig sites can be learned with unique items in <span class="img-text"><a href="/w/Archaeology" title="Archaeology"><img alt="" src="/images/thumb/a/a7/Archaeology_%28skill%29.png/23px-Archaeology_%28skill%29.png" decoding="async" width="23" height="23" srcset="/images/thumb/a/a7/Archaeology_%28skill%29.png/35px-Archaeology_%28skill%29.png 1.5x, /images/thumb/a/a7/Archaeology_%28skill%29.png/46px-Archaeology_%28skill%29.png 2x"></a> <a href="/w/Archaeology" title="Archaeology">Archaeology</a></span>.
</td></tr>
<tr>
<td><div class="center"><div class="floatnone"><a href="/w/File:Undisc_POI.png" class="image"><img alt="? icon" src="/images/thumb/e/ee/Undisc_POI.png/20px-Undisc_POI.png" decoding="async" width="20" height="32" srcset="/images/thumb/e/ee/Undisc_POI.png/30px-Undisc_POI.png 1.5x, /images/thumb/e/ee/Undisc_POI.png/40px-Undisc_POI.png 2x"></a></div></div></td>
<td>Denotes an undiscovered Point of Interest (POI). Discovering a POI will reveal more of the lore, and may earn you a reward.
</td></tr>
<tr>
<td><div class="center"><div class="floatnone"><a href="/w/File:Hidden_poi.png" class="image"><img alt="A cat" src="/images/thumb/e/eb/Hidden_poi.png/32px-Hidden_poi.png" decoding="async" width="32" height="32" srcset="/images/thumb/e/eb/Hidden_poi.png/48px-Hidden_poi.png 1.5x, /images/thumb/e/eb/Hidden_poi.png/64px-Hidden_poi.png 2x"></a></div></div></td>
<td>If "Toggle Cat" is enabled in Settings, then this icon will denote a hidden <span class="img-text"><a href="/w/Archaeology" title="Archaeology"><img alt="" src="/images/thumb/a/a7/Archaeology_%28skill%29.png/23px-Archaeology_%28skill%29.png" decoding="async" width="23" height="23" srcset="/images/thumb/a/a7/Archaeology_%28skill%29.png/35px-Archaeology_%28skill%29.png 1.5x, /images/thumb/a/a7/Archaeology_%28skill%29.png/46px-Archaeology_%28skill%29.png 2x"></a> <a href="/w/Archaeology" title="Archaeology">Archaeology</a></span> Dig Site. It will display only when you locate a required Dig Site item in <span class="img-text"><a href="/w/Archaeology" title="Archaeology"><img alt="" src="/images/thumb/a/a7/Archaeology_%28skill%29.png/23px-Archaeology_%28skill%29.png" decoding="async" width="23" height="23" srcset="/images/thumb/a/a7/Archaeology_%28skill%29.png/35px-Archaeology_%28skill%29.png 1.5x, /images/thumb/a/a7/Archaeology_%28skill%29.png/46px-Archaeology_%28skill%29.png 2x"></a> <a href="/w/Archaeology" title="Archaeology">Archaeology</a></span> (One example being the <span class="img-text"><a href="/w/Torn_Chart" title="Torn Chart"><img alt="" src="/images/thumb/1/1e/Torn_Chart_%28item%29.png/23px-Torn_Chart_%28item%29.png" decoding="async" width="23" height="23" srcset="/images/thumb/1/1e/Torn_Chart_%28item%29.png/35px-Torn_Chart_%28item%29.png 1.5x, /images/thumb/1/1e/Torn_Chart_%28item%29.png/46px-Torn_Chart_%28item%29.png 2x"></a> <a href="/w/Torn_Chart" title="Torn Chart">Torn Chart</a></span>).
</td></tr></tbody></table></div></div>
<h3><span class="mw-headline" id="Points_of_Interest">Points of Interest</span></h3>
<p>These are the types of Points of Interest (POIs) that can be discovered underneath a Hex.
</p>
<div class="content-table-wrapper"><div class="content-table-scrollbar inactive" style="width: 852.102px;"><div class="content-table-spoof" style="width: 1199.38px;"></div></div><div class="content-table-left"></div><div class="content-table-right"></div><div class="content-table"><table class="wikitable">

<tbody><tr>
<th>Icon</th>
<th>Description
</th></tr>
<tr>
<td><div class="center"><div class="floatnone"><a href="/w/File:Dig_site.png" class="image"><img alt="Dig Site" src="/images/thumb/e/e8/Dig_site.png/25px-Dig_site.png" decoding="async" width="25" height="25" srcset="/images/thumb/e/e8/Dig_site.png/38px-Dig_site.png 1.5x, /images/thumb/e/e8/Dig_site.png/50px-Dig_site.png 2x"></a></div></div></td>
<td>An <span class="img-text"><a href="/w/Archaeology" title="Archaeology"><img alt="" src="/images/thumb/a/a7/Archaeology_%28skill%29.png/23px-Archaeology_%28skill%29.png" decoding="async" width="23" height="23" srcset="/images/thumb/a/a7/Archaeology_%28skill%29.png/35px-Archaeology_%28skill%29.png 1.5x, /images/thumb/a/a7/Archaeology_%28skill%29.png/46px-Archaeology_%28skill%29.png 2x"></a> <a href="/w/Archaeology" title="Archaeology">Archaeology</a></span> Dig Site. Use <span class="img-text"><a href="/w/Cartography" title="Cartography"><img alt="" src="/images/thumb/0/05/Cartography_%28skill%29.png/23px-Cartography_%28skill%29.png" decoding="async" width="23" height="23" srcset="/images/thumb/0/05/Cartography_%28skill%29.png/35px-Cartography_%28skill%29.png 1.5x, /images/thumb/0/05/Cartography_%28skill%29.png/46px-Cartography_%28skill%29.png 2x"></a> <a class="mw-selflink selflink">Cartography</a></span> to create, upgrade or refine maps for dig sites. Use <span class="img-text"><a href="/w/Archaeology" title="Archaeology"><img alt="" src="/images/thumb/a/a7/Archaeology_%28skill%29.png/23px-Archaeology_%28skill%29.png" decoding="async" width="23" height="23" srcset="/images/thumb/a/a7/Archaeology_%28skill%29.png/35px-Archaeology_%28skill%29.png 1.5x, /images/thumb/a/a7/Archaeology_%28skill%29.png/46px-Archaeology_%28skill%29.png 2x"></a> <a href="/w/Archaeology" title="Archaeology">Archaeology</a></span> to excavate dig sites you have discovered.
</td></tr>
<tr>
<td><div class="center"><div class="floatnone"><a href="/w/File:Point_of_interest.png" class="image"><img alt="Standard Point of Interest" src="/images/thumb/f/fb/Point_of_interest.png/25px-Point_of_interest.png" decoding="async" width="25" height="25" srcset="/images/thumb/f/fb/Point_of_interest.png/38px-Point_of_interest.png 1.5x, /images/thumb/f/fb/Point_of_interest.png/50px-Point_of_interest.png 2x"></a></div></div></td>
</td></tr>
<tr class="">
<td><span class="img-text"><img alt="Watchtower" src="/images/thumb/4/46/Watchtower_%28poi%29.png/50px-Watchtower_%28poi%29.png" decoding="async" width="50" height="40" srcset="/images/thumb/4/46/Watchtower_%28poi%29.png/75px-Watchtower_%28poi%29.png 1.5x, /images/thumb/4/46/Watchtower_%28poi%29.png/100px-Watchtower_%28poi%29.png 2x"></span></td>
<td id="Watchtower"><a href="/w/Watchtower" title="Watchtower">Watchtower</a></td>
<td>Dig&nbsp;Site</td>
<td>10</td>
<td>2
</td>
<td><span class="img-text"><a href="/w/Cartography" title="Cartography"><img alt="Cartography" src="/images/thumb/0/05/Cartography_%28skill%29.png/25px-Cartography_%28skill%29.png" decoding="async" width="25" height="25" srcset="/images/thumb/0/05/Cartography_%28skill%29.png/38px-Cartography_%28skill%29.png 1.5x, /images/thumb/0/05/Cartography_%28skill%29.png/50px-Cartography_%28skill%29.png 2x"></a> Level 90</span><br>Find <span class="img-text"><a href="/w/Island_Chart" title="Island Chart"><img alt="" src="/images/thumb/c/c4/Island_Chart_%28item%29.png/25px-Island_Chart_%28item%29.png" decoding="async" width="25" height="25" srcset="/images/thumb/c/c4/Island_Chart_%28item%29.png/38px-Island_Chart_%28item%29.png 1.5x, /images/thumb/c/c4/Island_Chart_%28item%29.png/50px-Island_Chart_%28item%29.png 2x"></a> <a href="/w/Island_Chart" title="Island Chart">Island Chart</a></span>"""


Watchtower_list = HTML.split('<td><span class="img-text"><img alt="')[1].split('" src="/images/thumb/4/46/')[0]
print(Watchtower_list)
