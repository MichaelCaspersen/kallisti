import sys
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_book(name, zone, type, quality, worn, features, composition, restricted, weight, value, size, weapon_speed, weapon_speednum, weapon_missiletype, punchdamage_dice1, punchdamage_dice2, special_name, special_power, special_frequency, special_frequencynum, special_dice1, special_dice2, ac_max, ac_current, hoursremaining, color, capacity, weapon_dice1, weapon_dice2, weapon_damage, weapon_attacktype, spell_chargesmax, spell_chargesleft, missile_str_required, missile_dice1, missile_dice2, missile_type, missile_boomeranging, spell_level, spell_spells, spell_1_name, spell_1_level, spell_2_name, spell_2_level, spell_3_name, spell_3_level, castlevel, affects_1_name, affects_1_rank, affects_2_name, affects_2_rank, affects_3_name, affects_3_rank, affects_4_name, affects_4_rank, affects_5_name, affects_5_rank, affects_6_name, affects_6_rank, affects_7_name, affects_7_rank, minlevel_fighter, minlevel_rogue, minlevel_priest, minlevel_monastic, minlevel_mage, minlevel_barbarian, minlevel_assassin, minlevel_templar, minlevel_monk, minlevel_wizard, minlevel_paladin, minlevel_demoniac, minlevel_druid, minlevel_samurai, minlevel_necromancer, minlevel_dreadlord, minlevel_bard, minlevel_prophet, minlevel_ranger, minlevel_valkyrie, weapon_skilltype, weapon_wield_str, weapon_wield_dex, weapon_wield_rank, weapon_hold_str, weapon_hold_dex, weapon_hold_rank, armor_type, armor_wear_str, armor_wear_rank, ammo_type, ammo_current, ammo_max, ammo_dice1, ammo_dice2):
    query = "INSERT INTO `items`(name, zone, type, quality, worn, features, composition, restricted, weight, value, size, weapon_speed, weapon_speednum, weapon_missiletype, punchdamage_dice1, punchdamage_dice2, special_name, special_power, special_frequency, special_frequencynum, special_dice1, special_dice2, ac_max, ac_current, hoursremaining, color, capacity, weapon_dice1, weapon_dice2, weapon_damage, weapon_attacktype, spell_chargesmax, spell_chargesleft, missile_str_required, missile_dice1, missile_dice2, missile_type, missile_boomeranging, spell_level, spell_spells, spell_1_name, spell_1_level, spell_2_name, spell_2_level, spell_3_name, spell_3_level, castlevel, affects_1_name, affects_1_rank, affects_2_name, affects_2_rank, affects_3_name, affects_3_rank, affects_4_name, affects_4_rank, affects_5_name, affects_5_rank, affects_6_name, affects_6_rank, affects_7_name, affects_7_rank, minlevel_fighter, minlevel_rogue, minlevel_priest, minlevel_monastic, minlevel_mage, minlevel_barbarian, minlevel_assassin, minlevel_templar, minlevel_monk, minlevel_wizard, minlevel_paladin, minlevel_demoniac, minlevel_druid, minlevel_samurai, minlevel_necromancer, minlevel_dreadlord, minlevel_bard, minlevel_prophet, minlevel_ranger, minlevel_valkyrie, weapon_skilltype, weapon_wield_str, weapon_wield_dex, weapon_wield_rank, weapon_hold_str, weapon_hold_dex, weapon_hold_rank, armor_type, armor_wear_str, armor_wear_rank, ammo_type, ammo_current, ammo_max, ammo_dice1, ammo_dice2) " \
	"VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    args = (name, zone, type, quality, worn, features, composition, restricted, weight, value, size, weapon_speed, weapon_speednum, weapon_missiletype, punchdamage_dice1, punchdamage_dice2, special_name, special_power, special_frequency, special_frequencynum, special_dice1, special_dice2, ac_max, ac_current, hoursremaining, color, capacity, weapon_dice1, weapon_dice2, weapon_damage, weapon_attacktype, spell_chargesmax, spell_chargesleft, missile_str_required, missile_dice1, missile_dice2, missile_type, missile_boomeranging, spell_level, spell_spells, spell_1_name, spell_1_level, spell_2_name, spell_2_level, spell_3_name, spell_3_level, castlevel, affects_1_name, affects_1_rank, affects_2_name, affects_2_rank, affects_3_name, affects_3_rank, affects_4_name, affects_4_rank, affects_5_name, affects_5_rank, affects_6_name, affects_6_rank, affects_7_name, affects_7_rank, minlevel_fighter, minlevel_rogue, minlevel_priest, minlevel_monastic, minlevel_mage, minlevel_barbarian, minlevel_assassin, minlevel_templar, minlevel_monk, minlevel_wizard, minlevel_paladin, minlevel_demoniac, minlevel_druid, minlevel_samurai, minlevel_necromancer, minlevel_dreadlord, minlevel_bard, minlevel_prophet, minlevel_ranger, minlevel_valkyrie, weapon_skilltype, weapon_wield_str, weapon_wield_dex, weapon_wield_rank, weapon_hold_str, weapon_hold_dex, weapon_hold_rank, armor_type, armor_wear_str, armor_wear_rank, ammo_type, ammo_current, ammo_max, ammo_dice1, ammo_dice2)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def main():
   name=sys.argv[1]
   zone=sys.argv[2]
   type=sys.argv[3]
   quality=sys.argv[4]
   worn=sys.argv[5]
   features=sys.argv[6]
   composition=sys.argv[7]
   restricted=sys.argv[8]
   weight=sys.argv[9]
   value=sys.argv[10]
   size=sys.argv[11]
   weapon_speed=sys.argv[12]
   weapon_speednum=sys.argv[13]
   weapon_missiletype=sys.argv[14]
   punchdamage_dice1=sys.argv[15]
   punchdamage_dice2=sys.argv[16]
   special_name=sys.argv[17]
   special_power=sys.argv[18]
   special_frequency=sys.argv[19]
   special_frequencynum=sys.argv[20]
   special_dice1=sys.argv[21]
   special_dice2=sys.argv[22]
   ac_max=sys.argv[23]
   ac_current=sys.argv[24]
   hoursremaining=sys.argv[25]
   color=sys.argv[26]
   capacity=sys.argv[27]
   weapon_dice1=sys.argv[28]
   weapon_dice2=sys.argv[29]
   weapon_damage=sys.argv[30]
   weapon_attacktype=sys.argv[31]
   spell_chargesmax=sys.argv[32]
   spell_chargesleft=sys.argv[33]
   missile_str_required=sys.argv[34]
   missile_dice1=sys.argv[35]
   missile_dice2=sys.argv[36]
   missile_type=sys.argv[37]
   missile_boomeranging=sys.argv[38]
   spell_level=sys.argv[39]
   spell_spells=sys.argv[40]
   spell_1_name=sys.argv[41]
   spell_1_level=sys.argv[42]
   spell_2_name=sys.argv[43]
   spell_2_level=sys.argv[44]
   spell_3_name=sys.argv[45]
   spell_3_level=sys.argv[46]
   castlevel=sys.argv[47]
   affects_1_name=sys.argv[48]
   affects_1_rank=sys.argv[49]
   affects_2_name=sys.argv[50]
   affects_2_rank=sys.argv[51]
   affects_3_name=sys.argv[52]
   affects_3_rank=sys.argv[53]
   affects_4_name=sys.argv[54]
   affects_4_rank=sys.argv[55]
   affects_5_name=sys.argv[56]
   affects_5_rank=sys.argv[57]
   affects_6_name=sys.argv[58]
   affects_6_rank=sys.argv[59]
   affects_7_name=sys.argv[60]
   affects_7_rank=sys.argv[61]
   minlevel_fighter=sys.argv[62]
   minlevel_rogue=sys.argv[63]
   minlevel_priest=sys.argv[64]
   minlevel_monastic=sys.argv[65]
   minlevel_mage=sys.argv[66]
   minlevel_barbarian=sys.argv[67]
   minlevel_assassin=sys.argv[68]
   minlevel_templar=sys.argv[69]
   minlevel_monk=sys.argv[70]
   minlevel_wizard=sys.argv[71]
   minlevel_paladin=sys.argv[72]
   minlevel_demoniac=sys.argv[73]
   minlevel_druid=sys.argv[74]
   minlevel_samurai=sys.argv[75]
   minlevel_necromancer=sys.argv[76]
   minlevel_dreadlord=sys.argv[77]
   minlevel_bard=sys.argv[78]
   minlevel_prophet=sys.argv[79]
   minlevel_ranger=sys.argv[80]
   minlevel_valkyrie=sys.argv[81]
   weapon_skilltype=sys.argv[82]
   weapon_wield_str=sys.argv[83]
   weapon_wield_dex=sys.argv[84]
   weapon_wield_rank=sys.argv[85]
   weapon_hold_str=sys.argv[86]
   weapon_hold_dex=sys.argv[87]
   weapon_hold_rank=sys.argv[88]
   armor_type=sys.argv[89]
   armor_wear_str=sys.argv[90]
   armor_wear_rank=sys.argv[91]

   ammo_type=sys.argv[92]
   ammo_current=sys.argv[93]
   ammo_max=sys.argv[94]
   ammo_dice1=sys.argv[95]
   ammo_dice2=sys.argv[96]

   insert_book(name, zone, type, quality, worn, features, composition, restricted, weight, value, size, weapon_speed, weapon_speednum, weapon_missiletype, punchdamage_dice1, punchdamage_dice2, special_name, special_power, special_frequency, special_frequencynum, special_dice1, special_dice2, ac_max, ac_current, hoursremaining, color, capacity, weapon_dice1, weapon_dice2, weapon_damage, weapon_attacktype, spell_chargesmax, spell_chargesleft, missile_str_required, missile_dice1, missile_dice2, missile_type, missile_boomeranging, spell_level, spell_spells, spell_1_name, spell_1_level, spell_2_name, spell_2_level, spell_3_name, spell_3_level, castlevel, affects_1_name, affects_1_rank, affects_2_name, affects_2_rank, affects_3_name, affects_3_rank, affects_4_name, affects_4_rank, affects_5_name, affects_5_rank, affects_6_name, affects_6_rank, affects_7_name, affects_7_rank, minlevel_fighter, minlevel_rogue, minlevel_priest, minlevel_monastic, minlevel_mage, minlevel_barbarian, minlevel_assassin, minlevel_templar, minlevel_monk, minlevel_wizard, minlevel_paladin, minlevel_demoniac, minlevel_druid, minlevel_samurai, minlevel_necromancer, minlevel_dreadlord, minlevel_bard, minlevel_prophet, minlevel_ranger, minlevel_valkyrie, weapon_skilltype, weapon_wield_str, weapon_wield_dex, weapon_wield_rank, weapon_hold_str, weapon_hold_dex, weapon_hold_rank, armor_type, armor_wear_str, armor_wear_rank, ammo_type, ammo_current, ammo_max, ammo_dice1, ammo_dice2)

if __name__ == '__main__':
    main()
