#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import seaborn as sns
import itertools as it
import tkinter as tk
import webbrowser as wb
import customtkinter as ctk
from PIL import ImageTk, Image

from sklearn.cluster import KMeans

sns.set_context('talk')

import os

# Image Files (pre-loaded)
mushroom_mkc_path = r"images/179px-MK8_Mario_Kart_Stadium_Course_Icon.png"
mushroom_wp_path = r"images/179px-MK8_Water_Park_Course_Icon.png"
mushroom_ssc_path = r"images/179px-MK8_Sweet_Sweet_Canyon_Course_Icon.png"
mushroom_tr_path = r"images/179px-MK8_Thwomp_Ruins_Course_Icon.png"
flower_mc_path = r"images/179px-MK8_Mario_Circuit_Course_Icon.png"
flower_th_path = r"images/179px-MK8_Toad_Harbor_Course_Icon.png"
flower_tm_path = r"images/179px-MK8_Twisted_Mansion_Course_Icon.png"
flower_sgf_path = r"images/179px-MK8_Shy_Guy_Falls_Course_Icon.png"
star_sa_path = r"images/179px-MK8_Sunshine_Airport_Course_Icon.png"
star_ds_path = r"images/179px-MK8_Dolphin_Shoals_Course_Icon.png"
star_electro_path = r"images/179px-MK8_Electrodrome_Course_Icon.png"
star_mw_path = r"images/179px-MK8_Mount_Wario_Course_Icon.png"
speical_cc_path = r"images/179px-MK8_Cloudtop_Cruise_Course_Icon.png"
speical_bdd_path = r"images/179px-MK8_Bone-Dry_Dunes_Course_Icon.png"
speical_bc_path = r"images/179px-MK8_Bowser's_Castle_Course_Icon.png"
speical_rr_path = r"images/179px-MK8_Rainbow_Road_Course_Icon.png"
shell_mmm_path = r"images/179px-MK8_Wii_Moo_Moo_Meadows_Course_Icon.png"
shell_GBA_mc_path = r"images/179px-MK8_GBA_Mario_Circuit_Course_Icon.png"
shell_ccb_path = r"images/179px-MK8_DS_Cheep_Cheep_Beach_Course_Icon.png"
shell_tt_path = r"images/179px-MK8_N64_Toad's_Turnpike_Course_Icon.png"
banana_ddd_path = r"images/179px-MK8_GCN_Dry_Dry_Desert_Course_Icon.png"
banana_dp3_path = r"images/179px-MK8_SNES_Donut_Plains_3_Course_Icon.png"
banana_rr_path = r"images/179px-MK8_N64_Royal_Raceway_Course_Icon.png"
banana_dkj_path = r"images/179px-MK8_3DS_DK_Jungle_Course_Icon.png"
leaf_ws_path = r"images/179px-MK8_DS_Wario_Stadium_Course_Icon.png"
leaf_sl_path = r"images/179px-MK8_GCN_Sherbet_Land_Course_Icon.png"
leaf_mp_path = r"images/179px-MK8_3DS_Music_Park_Course_Icon.png"
leaf_yv_path = r"images/179px-MK8_N64_Yoshi_Valley_Course_Icon.png"
lightning_ttc_path = r"images/179px-MK8_DS_Tick-Tock_Clock_Course_Icon.png"
lightning_pps_path = r"images/179px-MK8_3DS_Piranha_Plant_Slide_Course_Icon.png"
lightning_gv_path = r"images/179px-MK8_Wii_Grumble_Volcano_Course_Icon.png"
lightning_n64_rr_path = r"images/179px-MK8_N64_Rainbow_Road_Course_Icon.png"
egg_yc_path = r"images/179px-MK8_GCN_Yoshi_Circuit_Course_Icon.png"
egg_ea_path = r"images/179px-MK8_Excitebike_Arena_Course_Icon.png"
egg_dd_path = r"images/179px-MK8_Dragon_Driftway_Course_Icon.png"
egg_mc_path = r"images/179px-MK8_Mute_City_Course_Icon.png"
triforce_wgm_path = r"images/179px-MK8_Wii_Wario's_Gold_Mine_Course_Icon.png"
triforce_snes_rr_path = r"images/179px-MK8_SNES_Rainbow_Road_Course_Icon.png"
triforce_iio_path = r"images/179px-MK8_Ice_Ice_Outpost_Course_Icon.png"
triforce_hc_path = r"images/179px-MK8_Hyrule_Circuit_Course_Icon.png"
crossing_bp_path = r"images/179px-MK8_GCN_Baby_Park_Course_Icon.png"
crossing_cl_path = r"images/179px-MK8_GBA_Cheese_Land_Course_Icon.png"
crossing_ww_path = r"images/179px-MK8_Wild_Woods_Course_Icon.png"
crossing_ac_path = r"images/179px-MK8_Animal_Crossing_Course_Icon.png"
bell_neb_path = r"images/179px-MK8_3DS_Neo_Bowser_City_Course_Icon.png"
bell_gba_rr_path = r"images/179px-MK8_GBA_Ribbon_Road_Course_Icon.png"
bell_sbs_path = r"images/179px-MK8_Super_Bell_Subway_Course_Icon.png"
bell_bb_path = r"images/179px-MK8_Big_Blue_Course_Icon.png"

# Track Maps
mushroom_mkc_map = r"images/120px-MK8_Mario_Kart_Stadium_Map.png"
mushroom_wp_map = r"images/120px-MK8_Water_Park_Map.png"
mushroom_ssc_map = r"images/120px-MK8_Sweet_Sweet_Canyon_Map.png"
mushroom_tr_map = r"images/120px-MK8_Thwomp_Ruins_Map.png"
flower_mc_map = r"images/120px-MK8_Mario_Circuit_Map.png"
flower_th_map = r"images/120px-MK8_Toad_Harbor_Map.png"
flower_tm_map = r"images/120px-MK8_Twisted_Mansion_Map.png"
flower_sgf_map = r"images/120px-MK8_Shy_Guy_Falls_Map.png"
star_sa_map = r"images/120px-MK8_Sunshine_Airport_Map.png"
star_ds_map = r"images/120px-MK8_Dolphin_Shoals_Map.png"
star_electro_map = r"images/120px-MK8_Electrodrome_Map.png"
star_mw_map = r"images/120px-MK8_Mount_Wario_Map.png"
speical_cc_map = r"images/120px-MK8_Cloudtop_Cruise_Map.png"
speical_bdd_map = r"images/120px-MK8_Bone-Dry_Dunes_Map.png"
speical_bc_map = r"images/120px-MK8_Bowser's_Castle_Map.png"
speical_rr_map = r"images/120px-MK8_Rainbow_Road_Map.png"
shell_mmm_map = r"images/120px-MK8_Wii_Moo_Moo_Meadows_Map.png"
shell_GBA_mc_map = r"images/120px-MK8_GBA_Mario_Circuit_Map.png"
shell_ccb_map = r"images/120px-MK8_DS_Cheep_Cheep_Beach_Map.png"
shell_tt_map = r"images/120px-MK8_N64_Toad's_Turnpike_Map.png"
banana_ddd_map = r"images/120px-MK8_GCN_Dry_Dry_Desert_Map.png"
banana_dp3_map = r"images/120px-MK8_SNES_Donut_Plains_3_Map.png"
banana_rr_map = r"images/120px-MK8_N64_Royal_Raceway_Map.png"
banana_dkj_map = r"images/120px-MK8_3DS_DK_Jungle_Map.png"
leaf_ws_map = r"images/120px-MK8_DS_Wario_Stadium_Map.png"
leaf_sl_map = r"images/120px-MK8_GCN_Sherbet_Land_Map.png"
leaf_mp_map = r"images/120px-MK8_3DS_Music_Park_Map.png"
leaf_yv_map = r"images/120px-MK8_N64_Yoshi_Valley_Map.png"
lightning_ttc_map = r"images/120px-MK8_DS_Tick-Tock_Clock_Map.png"
lightning_pps_map = r"images/120px-MK8_3DS_Piranha_Plant_Slide_Map.png"
lightning_gv_map = r"images/120px-MK8_Wii_Grumble_Volcano_Map.png"
lightning_n64_rr_map = r"images/120px-MK8_N64_Rainbow_Road_Map.png"
egg_yc_map = r"images/120px-MK8_GCN_Yoshi_Circuit_Map.png"
egg_ea_map = r"images/120px-MK8_Excitebike_Arena_Map.png"
egg_dd_map = r"images/120px-MK8_Dragon_Driftway_Map.png"
egg_mc_map = r"images/120px-MK8_Mute_City_Map.png"
triforce_wgm_map = r"images/120px-MK8_Wii_Wario's_Gold_Mine_Map.png"
triforce_snes_rr_map = r"images/120px-MK8_SNES_Rainbow_Road_Map.png"
triforce_iio_map = r"images/120px-MK8_Ice_Ice_Outpost_Map.png"
triforce_hc_map = r"images/120px-MK8_Hyrule_Circuit_Map.png"
crossing_bp_map = r"images/120px-MK8_GCN_Baby_Park_Map.png"
crossing_cl_map = r"images/120px-MK8_GBA_Cheese_Land_Map.png"
crossing_ww_map = r"images/120px-MK8_Wild_Woods_Map.png"
crossing_ac_map = r"images/120px-MK8_Animal_Crossing_Map.png"
bell_neb_map = r"images/120px-MK8_3DS_Neo_Bowser_City_Map.png"
bell_gba_rr_map = r"images/120px-MK8_GBA_Ribbon_Road_Map.png"
bell_sbs_map = r"images/120px-MK8_Super_Bell_Subway_Map.png"
bell_bb_map = r"images/120px-MK8_Big_Blue_Map.png"

# Chars Images
shyguy = r"images/MK8_ShyGuy_Icon.png"
bowser = r"images/MK8_Bowser_Icon.png"
link = r"images/MK8_Link_Icon.png"
yoshi = r"images/MK8_Yoshi_Icon.png"
babyDaisy = r"images/MK8_BabyDaisy_Icon.png"
babyRosalina = r"images/MK8_BabyRosalina_Icon.png"
blueShyguy = r"images/MK8_Blue_Shy_Guy_Icon.png"
babyPeach = r"images/MK8_BabyPeach_Icon.png"
wario = r"images/MK8_Wario_Icon.png"
ludwig = r"images/MK8_Ludwig_Icon.png"
toad = r"images/MK8_Toad_Icon.png"
luigi = r"images/MK8_Luigi_Icon.png"
catPeach = r"images/MK8_Cat_Peach_Icon.png"
furryMario = r"images/MK8_Tanooki_Mario_Icon.png"
lightblueYoshi = r"images/MK8_Light-Blue_Yoshi_Icon.png"
dKong = r"images/MK8_DKong_Icon.png"
dryBowser = r"images/MK8_Dry_Bowser_Icon.png"
girl = r"images/MK8_Isabelle_Icon.png"
pinkShyguy = r"images/MK8_Pink_Shy_Guy_Icon.png"
greenShyguy = r"images/MK8_Green_Shy_Guy_Icon.png"
goldPeach = r"images/MK8_PGPeach_Icon.png"
rosalina = r"images/MK8_Rosalina_Icon.png"
orangeShyguy = r"images/MK8_Orange_Shy_Guy_Icon.png"
blackShyguy = r"images/MK8_Black_Shy_Guy_Icon.png"
lakitu = r"images/MK8_Lakitu_Icon.png"
orangeYoshi = r"images/MK8_Orange_Yoshi_Icon.png"
whiteYoshi = r"images/MK8_White_Yoshi_Icon.png"
metalMario = r"images/MK8_MMario_Icon.png"
redYoshi = r"images/MK8_Red_Yoshi_Icon.png"
pinkYoshi = r"images/MK8_Pink_Yoshi_Icon.png"
peach = r"images/MK8_Peach_Icon.png"
lemmy = r"images/MK8_Lemmy_Icon.png"
wendy = r"images/MK8_Wendy_Icon.png"
mario = r"images/MK8_Mario_Icon.png"
yellowShyguy = r"images/MK8_Yellow_Shy_Guy_Icon.png"
whiteShyguy = r"images/MK8_White_Shy_Guy_Icon.png"
babyMario = r"images/MK8_BabyMario_Icon.png"
blackYoshi = r"images/MK8_Black_Yoshi_Icon.png"
roy = r"images/MK8_Roy_Icon.png"
babyLuigi = r"images/MK8_BabyLuigi_Icon.png"
lightblueShyguy = r"images/MK8_Light-Blue_Shy_Guy_Icon.png"
yellowYoshi = r"images/MK8_Yellow_Yoshi_Icon.png"
morton = r"images/MK8_Morton_Icon.png"
girlToad = r"images/MK8_Toadette_Icon.png"
daisy = r"images/MK8_Daisy_Icon.png"
blueYoshi = r"images/MK8_Blue_Yoshi_Icon.png"
sexyman = r"images/MK8_Waluigi_Icon.png"
iggy = r"images/MK8_Iggy_Icon.png"
koopatroopa = r"images/MK8_Koopa_Icon.png"
larry = r"images/MK8_Larry_Icon.png"
mii = r"images/Mii_MK8.png"
goldMario = r"images/120px-MK8DX_Gold_Mario_Icon.png"
boyVillager = r"images/deluxe/MK8DX_Male_Villager.png"
girlVillager = r"images/deluxe/MK8DX_Female_Villager.png"
furryPeach = r"images/deluxe/MK8DX_Cat_Peach_Icon.png"

cptfal_mii = r"images/MarioKart8FoxSuit-0.png"
toad_mii = r"images/MK8_Toad_Suit.png"
crossing_mii = r"images/MK8_Animal_Crossing_Suit.png"

# Body files
standard_kart = r"images/120px-StandardKartBodyMK8.png"
pipe_frame = r"images/120px-PipeFrameBodyMK8.png"
mach_8 = r"images/120px-Mach8BodyMK8.png"
steel_driver = r"images/120px-Steel_Driver.png"
cat_cruiser = r"images/120px-CatCruiserBodyMK8.png"
circuit_special = r"images/120px-CircuitSpecialBodyMK8.png"
tri_speeder = r"images/120px-TrispeederBodyMK8.png"
badwagon = r"images/120px-BadwagonBodyMK8.png"
prancer = r"images/120px-PrancerBodyMK8.png"
biddybuggy = r"images/120px-BiddybuggyBodyMK8.png"
landshit = r"images/120px-LandshipBodyMK8.png"
sneaker = r"images/120px-SneakerBodyMK8.png"
sports_coupe = r"images/120px-SportsCoupeMK8.png"
gold_standart = r"images/120px-Gold_Standard.png"
gla = r"images/120px-GLA-MK8.png"
silver_arrow = r"images/120px-W25SilverArrow-MK8.png"
roadster = r"images/120px-300SLRoadster_MK8.png"
blue_falcon = r"images/120px-MK8BlueFalcon.png"
dasher = r"images/120px-ZeldaMK8Bdasher.png"
tanooki_kart = r"images/120px-MK8_Tanooki_Buggy_Sprite.png"
streetle = r"images/120px-MK8Streetle.png"
p_wing = r"images/120px-MK8PWing.png"
standard_bike = r"images/120px-StandardBikeBodyMK8.png"
comet = r"images/120px-CometBodyMK8.png"
sport_bike = r"images/120px-SportBikeBodyMK8.png"
duke = r"images/120px-TheDukeBodyMK8.png"
flame_rider = r"images/120px-FlameRiderBodyMK8.png"
varmit = r"images/120px-VarmintBodyMK8.png"
mr_scooty = r"images/120px-MrScootyBodyMK8.png"
jet_bike = r"images/120px-JetBikeBodyMK8.png"
yoshi_bike = r"images/120px-YoshiBikeBodyMK8.png"
master_cycle = r"images/120px-MK8MasterCycle.png"
city_tripper = r"images/120px-MK8_Light-Green_City_Tripper.png"
standard_atv = r"images/120px-StandardATVBodyMK8.png"
wild_wiggler = r"images/120px-WildWigglerBodyMK8.png"
teddy_buggy = r"images/120px-TeddyBuggyBodyMK8.png"
bone_ratter = r"images/120px-MK8BoneRattler.png"
koopa_clown = r"images/deluxe/120px-MK8DX_Koopa_Clown.png"
master_cycle_zero = r"images/deluxe/120px-MK8D_Master_Cycle_Zero.png"
splat_buddy = r"images/deluxe/120px-MK8DX_Splat_Buggy.png"
inkstriker = r"images/deluxe/120px-MK8DX_Inkstriker.png"

# Tire files
standard_tires = r"images/120px-StandardTiresMK8.png"
monster_tires = r"images/120px-MonsterTiresMK8.png"
roller_tires = r"images/120px-RollerTiresMK8.png"
slim_tires = r"images/120px-SlimTiresMK8.png"
slick_tires = r"images/120px-SlickTiresMK8.png"
metal_tires = r"images/120px-MetalTiresMK8.png"
button_tires = r"images/120px-ButtonTiresMK8.png"
off_road_tires = r"images/120px-Off-Road.png"
sponge_tires = r"images/120px-SpongeTiresMK8.png"
wood_tires = r"images/120px-WoodTiresMK8.png"
cushion_tires = r"images/120px-CushionTiresMK8.png"
blue_standard_tires = r"images/120px-Blue_Standard.png"
hot_monster_tires = r"images/120px-HotMonsterTiresMK8.png"
azure_roller_tires = r"images/120px-AzureRollerTiresMK8.png"
crimson_slim_tires = r"images/120px-CrimsonSlimTiresMK8.png"
cyber_slick_tires = r"images/120px-CyberSlickTiresMK8.png"
retro_off_road_tires = r"images/120px-Retro_Off-Road.png"
gold_tires = r"images/120px-Gold_Tires_MK8.png"
gla_tires = r"images/120px-GLATires-MK8.png"
triforce_tires = r"images/120px-MK8-TriforceTires.png"
leaf_tires = r"images/120px-Leaf_Tires_MK8.png"
ancient_tires = r"images/deluxe/120px-MK8D_Ancient_Tires.png"

# Glider files
super_glider = r"images/120px-SuperGliderMK8.png"
cloud_glider = r"images/120px-Cloud_Glider.png"
wario_wing = r"images/120px-WarioWingMK8.png"
waddle_wing = r"images/120px-WaddleWingMK8.png"
peach_parasol = r"images/120px-PeachParasolGliderMK8.png"
parachute = r"images/120px-ParachuteGliderMK8.png"
parafoil = r"images/120px-ParafoilGliderMK8.png"
flower_glider = r"images/120px-FlowerGliderMK8.png"
bowser_kite = r"images/120px-BowserKiteMK8.png"
plane_glider = r"images/120px-PlaneGliderMK8.png"
mktv_parafoil = r"images/120px-MKTVParafoilGliderMK8.png"
gold_glider = r"images/120px-GoldGliderMK8.png"
hylian_kite = r"images/120px-MK8-HylianKite.png"
paper_glider = r"images/120px-PaperGliderIcon-MK8.png"
paraglider = r"images/deluxe/120px-MK8D_Paraglider.png"

# Image Files Dict.
img_files = {
    'Mario Kart Stadium': mushroom_mkc_path,
    'Water Park': mushroom_wp_path,
    'Sweet Sweet Canyon': mushroom_ssc_path,
    'Thwomp Ruins': mushroom_tr_path,
    'Mario Circuit': flower_mc_path,
    'Toad Harbor': flower_th_path,
    'Twisted Mansion': flower_tm_path,
    'Shy Guy Falls': flower_sgf_path,
    'Sunshine Airport': star_sa_path,
    'Dolphin Shoals': star_ds_path,
    'Electrodrome': star_electro_path,
    'Mount Wario': star_mw_path,
    'Cloudtop Cruise': speical_cc_path,
    'Bone-Dry Dunes': speical_bdd_path,
    'Bowser\'s Castle': speical_bc_path,
    'Rainbow Road': speical_rr_path,
    'Wii Moo Moo Meadows': shell_mmm_path,
    'GBA Mario Circuit': shell_GBA_mc_path,
    'DS Cheep Cheep Beach': shell_ccb_path,
    'N64 Toad\'s Turnpike':shell_tt_path,
    'GCN Dry Dry Desert': banana_ddd_path,
    'SNES Donut Plains 3': banana_dp3_path,
    'N64 Royal Raceway': banana_rr_path,
    '3DS DK Jungle': banana_dkj_path,
    'DS Wario Stadium': leaf_ws_path,
    'GCN Sherbet Land': leaf_sl_path,
    '3DS Music Park': leaf_mp_path,
    'N64 Yoshi Valley': leaf_yv_path,
    'DS Tick-Tock Clock': lightning_ttc_path,
    '3DS Piranha Plant Slide': lightning_pps_path,
    'Wii Grumble Volcano': lightning_gv_path,
    'N64 Rainbow Road': lightning_n64_rr_path,
    'GCN Yoshi Circuit': egg_yc_path,
    'Excitebike Arena': egg_ea_path,
    'Dragon Driftway': egg_dd_path,
    'Mute City': egg_mc_path,
    'Wii Wario\'s Gold Mine': triforce_wgm_path,
    'SNES Rainbow Road': triforce_snes_rr_path,
    'Ice Ice Outpost': triforce_iio_path,
    'Hyrule Circuit': triforce_hc_path,
    'GCN Baby Park': crossing_bp_path,
    'GBA Cheese Land': crossing_cl_path,
    'Wild Woods': crossing_ww_path,
    'Animal Crossing': crossing_ac_path,
    '3DS Neo Bowser City': bell_neb_path,
    'GBA Ribbon Road': bell_gba_rr_path,
    'Super Bell Subway': bell_sbs_path,
    'Big Blue': bell_bb_path
}

# Track Map image files
track_maps = {
    'Mario Kart Stadium': mushroom_mkc_map,
    'Water Park': mushroom_wp_map,
    'Sweet Sweet Canyon': mushroom_ssc_map,
    'Thwomp Ruins': mushroom_tr_map,
    'Mario Circuit': flower_mc_map,
    'Toad Harbor': flower_th_map,
    'Twisted Mansion': flower_tm_map,
    'Shy Guy Falls': flower_sgf_map,
    'Sunshine Airport': star_sa_map,
    'Dolphin Shoals': star_ds_map,
    'Electrodrome': star_electro_map,
    'Mount Wario': star_mw_map,
    'Cloudtop Cruise': speical_cc_map,
    'Bone-Dry Dunes': speical_bdd_map,
    'Bowser\'s Castle': speical_bc_map,
    'Rainbow Road': speical_rr_map,
    'Wii Moo Moo Meadows': shell_mmm_map,
    'GBA Mario Circuit': shell_GBA_mc_map,
    'DS Cheep Cheep Beach': shell_ccb_map,
    'N64 Toad\'s Turnpike':shell_tt_map,
    'GCN Dry Dry Desert': banana_ddd_map,
    'SNES Donut Plains 3': banana_dp3_map,
    'N64 Royal Raceway': banana_rr_map,
    '3DS DK Jungle': banana_dkj_map,
    'DS Wario Stadium': leaf_ws_map,
    'GCN Sherbet Land': leaf_sl_map,
    '3DS Music Park': leaf_mp_map,
    'N64 Yoshi Valley': leaf_yv_map,
    'DS Tick-Tock Clock': lightning_ttc_map,
    '3DS Piranha Plant Slide': lightning_pps_map,
    'Wii Grumble Volcano': lightning_gv_map,
    'N64 Rainbow Road': lightning_n64_rr_map,
    'GCN Yoshi Circuit': egg_yc_map,
    'Excitebike Arena': egg_ea_map,
    'Dragon Driftway': egg_dd_map,
    'Mute City': egg_mc_map,
    'Wii Wario\'s Gold Mine': triforce_wgm_map,
    'SNES Rainbow Road': triforce_snes_rr_map,
    'Ice Ice Outpost': triforce_iio_map,
    'Hyrule Circuit': triforce_hc_map,
    'GCN Baby Park': crossing_bp_map,
    'GBA Cheese Land': crossing_cl_map,
    'Wild Woods': crossing_ww_map,
    'Animal Crossing': crossing_ac_map,
    '3DS Neo Bowser City': bell_neb_map,
    'GBA Ribbon Road': bell_gba_rr_map,
    'Super Bell Subway': bell_sbs_map,
    'Big Blue': bell_bb_map
}

chars_dict = {
    'Baby Mario': babyMario,
    'Baby Luigi': babyLuigi,
    'Baby Peach': babyPeach,
    'Baby Daisy': babyDaisy,
    'Baby Rosalina': babyRosalina,
    'Lemmy': lemmy,
    'Light Mii': mii,
    'Toad': toad,
    'Shy Guy': shyguy,
    'Koopa Troopa': koopatroopa,
    'Lakitu': lakitu,
    'Wendy': wendy,
    'Larry': larry,
    'Toadette': girlToad,
    'Peach': peach,
    'Daisy': daisy,
    'Yoshi': yoshi,
    'Mario': mario,
    'Luigi': luigi,
    'Iggy': iggy,
    'Ludwig': ludwig,
    'Medium Mii': mii,
    'Donkey Kong': dKong,
    'Waluigi': sexyman,
    'Rosalina': rosalina,
    'Roy': roy,
    'Metal Mario': metalMario,
    'Pink Gold Peach': goldPeach,
    'Wario': wario,
    'Bowser': bowser,
    'Morton': morton,
    'Heavy Mii': mii,
    'Tanooki Mario': furryMario,
    'Male Villager': boyVillager,
    'Cat Peach': furryPeach,
    'Female Villager': girlVillager,
    'Isabelle': girl,
    'Dry Bowser': dryBowser,
    'Link': link,
    'Heavy Mii Toad': toad_mii,
    'Heavy Mii Cpt Falcon': cptfal_mii,
    'Heavy Mii Crossing': crossing_mii
}

body_dict = {
    'Standard Kart': standard_kart,
    'Prancer': prancer,
    'Cat Cruiser': cat_cruiser,
    'Sneeker': sneaker,
    'Gold Standard': gold_standart,
    'Mach 8': mach_8,
    'Circuit Special': circuit_special,
    'Sports Coupe': sports_coupe,
    'Badwagon': badwagon,
    'TriSpeeder': tri_speeder,
    'Steel Driver': steel_driver,
    'Biddybuggy': biddybuggy,
    'Landship': landshit,
    'Pipe Frame': pipe_frame,
    'The Duke': duke,
    'Mr. Scooty': mr_scooty,
    'Standard Bike': standard_bike,
    'Flame Ride': flame_rider,
    'Varmit': varmit,
    'Sport Bike': sport_bike,
    'Jet Bike': jet_bike,
    'Comet': comet,
    'Yoshi Bike': yoshi_bike,
    'Teddy Buggy': teddy_buggy,
    'Wild Wiggler': wild_wiggler,
    'Standard ATV': standard_atv,
    'GLA': gla,
    'W 25 Silver Arrow': silver_arrow,
    '300 SL Roadster': roadster,
    'Blue Falcon': blue_falcon,
    'Tanooki Kart': tanooki_kart,
    'B Dasher': dasher,
    'Streetle': streetle,
    'P-Wing': p_wing,
    'Master Cycle': master_cycle,
    'City Tripper': city_tripper,
    'Bone Rattler': bone_ratter,
    'Splat Buggy': splat_buddy
}

tire_dict = {
    'Standard': standard_tires,
    'Blue Standard': blue_standard_tires,
    'Offroad': off_road_tires,
    'Retro Offroad': retro_off_road_tires,
    'Monster': monster_tires,
    'Hot Monster': hot_monster_tires,
    'Slick': slick_tires,
    'Cyber Slick': cyber_slick_tires,
    'Roller': roller_tires,
    'Azure Roller': azure_roller_tires,
    'Button': button_tires,
    'Slim': slim_tires,
    'Crimson Slim': crimson_slim_tires,
    'Metal': metal_tires,
    'Gold': gold_tires,
    'Wood': wood_tires,
    'Sponge': sponge_tires,
    'Cushion': cushion_tires,
    'GLA Tires': gla_tires,
    'Triforce Tires': triforce_tires,
    'Leaf Tires': leaf_tires,
    'Ancient Tires': ancient_tires
}

glider_dict = {
    'Super Glider': super_glider,
    'Waddle Wing': waddle_wing,
    'Plane Glider': plane_glider,
    'Wario Wing': wario_wing,
    'Gold Glider': gold_glider,
    'Flower Glider': flower_glider,
    'Peach Parasol': peach_parasol,
    'Parachute': parachute,
    'Parafoil': parafoil,
    'MKTV Parafoil': mktv_parafoil,
    'Bowser Kite': bowser_kite,
    'Cloud Glider': cloud_glider,
    'Hylian Kite': hylian_kite,
    'Paper Glider': paper_glider,
    'Paraglider': paraglider
}

# originally from https://github.com/woodnathan/MarioKart8-Stats, added DLC and fixed a few typos
bodies = pd.read_csv('src-data/BODIES.csv')
chars = pd.read_csv('src-data/CHARACTERS.csv')
gliders = pd.read_csv('src-data/GLIDERS.csv')
tires = pd.read_csv('src-data/TIRES.csv')
#tracks = pd.read_csv('MK8DX-World-Record-Data.csv')
tracks = pd.read_csv('src-data/WR_data.csv')
"""
# use only stock (non-DLC) characters / karts / tires
chars = chars.loc[chars['DLC']==0]
bodies = bodies.loc[bodies['DLC']==0]
tires = tires.loc[tires['DLC']==0]
gliders = gliders.loc[gliders['DLC']==0]
"""
stat_cols = bodies.columns[2:-1]
main_cols = ['Weight','Speed','Acceleration','Handling','Traction']
track_cols = ['Track', 'Character', 'Vehicle', 'Tires', 'Glider', 'Tilt']

# lots of characters/karts/tires are exactly the same. here we just want one from each stat type
chars_unique = chars.drop_duplicates(subset=stat_cols).set_index('Character')[stat_cols].sort_values('Weight')
bodies_unique = bodies.drop_duplicates(subset=stat_cols).set_index('Body')[stat_cols].sort_values('Acceleration')
tires_unique = tires.drop_duplicates(subset=stat_cols).set_index('Tire')[stat_cols].sort_values('Speed')

n_uniq_chars = len(chars_unique)
n_uniq_bodies = len(bodies_unique)
n_uniq_tires = len(tires_unique)
print(n_uniq_chars)

# add a column indicating which category each character/kart/tire is in
chars['char_class'] = KMeans(n_uniq_chars, n_init=10, random_state=0).fit_predict(chars[stat_cols])
bodies['body_class'] = KMeans(n_uniq_bodies, n_init=10).fit_predict(bodies[stat_cols])
tires['tire_class'] = KMeans(n_uniq_tires, n_init=10).fit_predict(tires[stat_cols])

# change the character class labels so that they correspond to weight order
# for Non-DLC Stats:
#char_class_dict = dict(zip([3, 0, 5, 4, 2, 6, 1], [0, 1, 2, 3, 4, 5, 6]))
# for DLC Stats:
#char_class_dict = dict(zip([0, 3, 2, 7, 8, 4, 1, 6, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8]))

#TESTING
char_class_dict = dict(zip([14, 11, 1, 10, 7, 8, 12, 5, 2, 13, 4, 0, 6, 15, 9, 3], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
chars['char_class'] = chars['char_class'].apply(lambda c: char_class_dict[c])

# only two types of gliders, one of which is pretty clearly just better
glider_best = gliders.loc[gliders['Glider']=='Flower']

# plot a heatmap of the stats for each component class
def hmap_char_class():
    fig, ax = plt.subplots(1,1, figsize=(8,5))

    sns.heatmap(chars_unique[main_cols], annot=True, ax=ax, linewidth=1, fmt='.3g')
    
    fig.tight_layout()

    plt.show()

# plot a heatmap of the stats for each component class
def hmap_part_class():
    fig, axes = plt.subplots(2,1, figsize=(8,10))

    tables = [bodies_unique, tires_unique]

    for ax, table in zip(axes, tables):
        sns.heatmap(table[main_cols], annot=True, ax=ax, linewidth=1, fmt='.3g')
            
    fig.tight_layout()

    plt.show()

def check(char_name, body_type, tire_type):
    # find the stats for each element of the configuration
    character = chars.loc[chars['Character']==char_name]
    kart = bodies.loc[bodies['Body']==body_type]
    wheels = tires.loc[tires['Tire']==tire_type]

    # the total stats for the configuration are just the sum of the components
    stats = pd.concat([character[stat_cols], kart[stat_cols], wheels[stat_cols], glider_best[stat_cols]]).sum()
                                
    # index the row by the configuration (character, kart, tire)
    index = pd.MultiIndex.from_tuples([(char_name, body_type, tire_type)], names=['Character', 'Body', 'Tire'])
                                            
    df = pd.DataFrame(stats).transpose()
    df.index = index
    return df

# returns True if the row is at the pareto frontier for variables xlabel and ylabel
def is_pareto_front(row, xlabel, ylabel):
        
    x = row[xlabel]
    y = row[ylabel]
                
    # look for points with the same y value but larger x value
    is_max_x = config_base.loc[config_base[ylabel]==y].max()[xlabel] <= x
    # look for points with the same x value but larger y value
    is_max_y = config_base.loc[config_base[xlabel]==x].max()[ylabel] <= y
    # look for points that are larger in both x and y
    is_double = len(config_base.loc[(config_base[xlabel]>x) & (config_base[ylabel]>y)])==0
                                            
    return is_max_x and is_max_y and is_double

# generate list of tuples for every possible configuration
config_all = it.product(chars_unique.index, bodies_unique.index, tires_unique.index)

# generate a dataframe with stats for each unique configuration
frames = []
#config_base = pd.DataFrame()
for (c,b,t) in config_all:
    this_config = check(c,b,t)
    frames.append(this_config)
    #config_base = config_base.append(this_config)
config_base = pd.concat(frames)

# array of True/False indicating whether the corresponding row is on the pareto frontier
is_pareto = config_base.apply(lambda row: is_pareto_front(row, 'Speed', 'Acceleration'), axis=1)

# just the configurations that are on the pareto frontier
config_pareto = config_base.loc[is_pareto].sort_values('Speed')

def pareto_frontier():
    # plot all the configurations
    fig, ax = plt.subplots(1,1, figsize=(8,5))
    sns.regplot(x='Speed', y='Acceleration', data=config_base, fit_reg=False, ax=ax)
            
    # plot the pareto frontier
    plt.plot(config_pareto['Speed'], config_pareto['Acceleration'], '--', label='Pareto frontier', alpha=0.5)

    plt.xlim([0.75,6]);
    plt.legend(loc='best');

    plt.show()

def interactive_graph():
    wb.open_new_tab('bokeh_plot.html')

def combos():
    # number of possible combinations
    print('Possible combinations    : ',len(list(it.product(chars.index, bodies.index, tires.index, gliders.index))))

    # number of combinations with different statistics
    print('Unique stat combinations : ',len(config_base.drop_duplicates(subset=stat_cols)))

    # number of optimal combinations (considering only speed and acceleration)
    print('Optimal combinations     : ',len(config_pareto))

    print(config_base.loc[is_pareto][['Speed','Acceleration']].sort_values('Speed'))

    fig, ax = plt.subplots(1,1, figsize=(8,7))
    sns.heatmap(config_pareto[main_cols].sort_values('Speed'), annot=True, ax=ax, linewidth=1, fmt='.3g');

def categories():
    # print out the various components, grouped by category
    tables = [chars, bodies, tires]
    keys = ['char_class', 'body_class', 'tire_class']
    columns = ['Character', 'Body', 'Tire']

    for table, key, col in zip(tables, keys, columns):
        print(col + ' Classes')
        print('*****************')
        for class_ in table[key].unique():
            class_list = table.loc[table[key]==class_][col].values
            print(', '.join(class_list))
                                            
        print()


def hide_buttons():
    button7.grid_forget()
    button8.grid_forget()
    button9.grid_forget()
    button10.grid_forget()
    button11.grid_forget()
    button12.grid_forget()
    button13.grid_forget()
    button14.grid_forget()
    button15.grid_forget()
    button16.grid_forget()
    button17.grid_forget()
    button18.grid_forget()

def show_buttons():
    button7.grid(row=1, column=0, ipady=10, pady=10, padx=5)
    button8.grid(row=1, column=1, ipady=10, pady=10, padx=5)
    button9.grid(row=1, column=2, ipady=10, pady=10, padx=5)
    button10.grid(row=1, column=3, ipady=10, pady=10, padx=5)
    button11.grid(row=1, column=4, ipady=10, pady=10, padx=5)
    button12.grid(row=1, column=5, ipady=10, pady=10, padx=5)
    button13.grid(row=2, column=0, ipady=10, pady=10, padx=5)
    button14.grid(row=2, column=1, ipady=10, pady=10, padx=5)
    button15.grid(row=2, column=2, ipady=10, pady=10, padx=5)
    button16.grid(row=2, column=3, ipady=10, pady=10, padx=5)
    button17.grid(row=2, column=4, ipady=10, pady=10, padx=5)
    button18.grid(row=2, column=5, ipady=10, pady=10, padx=5)

images = []
def display_tracks(key):
    button_array = []
    #track_list = tracks[tracks.Cup == key]
    track_list = tracks.loc[tracks['Cup'] == key]
    track_list = track_list["Track"].drop_duplicates()
    for x in track_list:
        track_img = ImageTk.PhotoImage(file=img_files[x])
        images.append(track_img)
        my_button = tk.Button(root, image=track_img, borderwidth=0, command=lambda x=x: track_details(x))
        button_array.append(my_button)

    for i, button in enumerate(button_array):
        button.grid(row=3, column=i)

def track_details(key):
    # Track detail window
    detail = tk.Toplevel()
    detail.title(key)
    detail.geometry("720x720")

    map_text_label = tk.Label(detail, text="Track Map")
    map_text_label.grid(row=0, column=0)
    char_text_label = tk.Label(detail, text="Character")
    char_text_label.grid(row=0, column=1)
    body_text_label = tk.Label(detail, text="Body")
    body_text_label.grid(row=0, column=2)
    tires_text_label = tk.Label(detail, text="Tires")
    tires_text_label.grid(row=0, column=3)
    glider_text_label = tk.Label(detail, text="Glider")
    glider_text_label.grid(row=0, column=4)

    # locate the details for the track
    if (var.get() == 0):
        track_list = tracks.loc[tracks['Speed'] == "150cc"]
    elif (var.get() == 1):
        track_list = tracks.loc[tracks['Speed'] == "200cc"]


    #track_list = tracks.loc[tracks['Track'] == key]
    track_list = track_list.loc[track_list['Track'] == key]
    character = track_list['Character'].iloc[0]
    body = track_list['Vehicle'].iloc[0]
    tire = track_list['Tires'].iloc[0]
    glider = track_list['Glider'].iloc[0]


    # display track map
    map_img = ImageTk.PhotoImage(file=track_maps[key])
    char_img = ImageTk.PhotoImage(file=chars_dict[character])
    body_img = ImageTk.PhotoImage(file=body_dict[body])
    tire_img = ImageTk.PhotoImage(file=tire_dict[tire])
    glider_img = ImageTk.PhotoImage(file=glider_dict[glider])


    map_label = tk.Label(detail, image=map_img, borderwidth=0)
    char_label = tk.Label(detail, image=char_img, borderwidth=0)
    body_label = tk.Label(detail, image=body_img, borderwidth=0)
    tire_label = tk.Label(detail, image=tire_img, borderwidth=0)
    glider_lbl = tk.Label(detail, image=glider_img, borderwidth=0)


    map_label.grid(row=1, column=0, ipadx=10)
    char_label.grid(row=1, column=1, ipadx=10)
    body_label.grid(row=1, column=2, ipadx=10)
    tire_label.grid(row=1, column=3, ipadx=10)
    glider_lbl.grid(row=1, column=4, ipadx=10)


    detail.mainloop()


# Main window
root = tk.Tk()
root.title("Pareto Efficiency Stats")
root.geometry("1366x768")
root.protocol("WM_DELETE_WINDOW", root.quit)

button1 = ctk.CTkButton(master=root, text="Character Classes (by weight)", width=190, height=40, command=hmap_char_class)
button1.grid(row=0, column=0, ipady=10, pady=10, padx=5)

button2 = ctk.CTkButton(master=root, text="Body/Tire Stats", width=190, height=40, command=hmap_part_class)
button2.grid(row=0, column=1, ipady=10, pady=10, padx=5)

button3 = ctk.CTkButton(master=root, text="Pareto Frontier", width=190, height=40, command=pareto_frontier)
button3.grid(row=0, column=2, ipady=10, pady=10, padx=5)

button4 = ctk.CTkButton(master=root, text="Interactive Graph", width=190, height=40, command=interactive_graph)
button4.grid(row=0, column=3, ipady=10, pady=10, padx=5)

button5 = ctk.CTkButton(master=root, text="Combos", width=190, height=40, command=combos)
button5.grid(row=0, column=4, ipady=10, pady=10, padx=5)

button6 = ctk.CTkButton(master=root, text="All Classes", width=190, height=40, command=categories)
#button6.pack(pady=5)
button6.grid(row=0, column=5, ipady=10, pady=10, padx=5)

# All cup buttons
mushroom_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_MushroomCup.png"))
button7 = tk.Button(root, image=mushroom_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Mushroom"))
button7.grid(row=1, column=0, ipady=10, pady=10, padx=5)

flower_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_FlowerCup.png"))
button8 = tk.Button(root, image=flower_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Flower"))
button8.grid(row=1, column=1, ipady=10, pady=10, padx=5)

star_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Star_Cup_Emblem.png"))
button9 = tk.Button(root, image=star_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Star"))
button9.grid(row=1, column=2, ipady=10, pady=10, padx=5)

special_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Special_Cup_Emblem.png"))
button10 = tk.Button(root, image=special_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Speical"))
button10.grid(row=1, column=3, ipady=10, pady=10, padx=5)

egg_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Egg_Cup_Emblem.png").resize((128,128), Image.Resampling.BICUBIC))
button11 = tk.Button(root, image=egg_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Egg"))
button11.grid(row=1, column=4, ipady=10, pady=10, padx=5)

crossing_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Crossing_Cup_Emblem.png").resize((128,128), Image.Resampling.BICUBIC))
button12 = tk.Button(root, image=crossing_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Crossing"))
button12.grid(row=1, column=5, ipady=10, pady=10, padx=5)

shell_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Shell_Cup_Emblem.png"))
button13 = tk.Button(root, image=shell_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Shell"))
button13.grid(row=2, column=0, ipady=10, pady=10, padx=5)

banana_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Banana_Cup_Emblem.png"))
button14 = tk.Button(root, image=banana_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Banana"))
button14.grid(row=2, column=1, ipady=10, pady=10, padx=5)

leaf_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Leaf_Cup_Emblem.png"))
button15 = tk.Button(root, image=leaf_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Leaf"))
button15.grid(row=2, column=2, ipady=10, pady=10, padx=5)

lightning_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Lightning_Cup_Emblem.png"))
button16 = tk.Button(root, image=lightning_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Lightning"))
button16.grid(row=2, column=3, ipady=10, pady=10, padx=5)

triforce_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Triforce_Cup_Emblem.png").resize((128,128), Image.Resampling.BICUBIC))
button17 = tk.Button(root, image=triforce_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Triforce"))
button17.grid(row=2, column=4, ipady=10, pady=10, padx=5)

bell_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Bell_Cup_Emblem.png").resize((128,128), Image.Resampling.BICUBIC))
button18 = tk.Button(root, image=bell_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Bell"))
button18.grid(row=2, column=5, ipady=10, pady=10, padx=5)

# Checkbox button
var = tk.IntVar()
cb_150cc = tk.Radiobutton(root, text="150cc", variable=var, value=0)
cb_200cc = tk.Radiobutton(root, text="200cc", variable=var, value=1)

cb_150cc.grid(row=0, column=6)
cb_200cc.grid(row=0, column=7)

root.mainloop()
