# -*- coding: utf-8 -*-
import requests
import json
from python.package.hvapi import HVAPI
from package.databasesq3 import *
from bs4 import BeautifulSoup as bs

config = json.load(open('python/config.json'))
api = HVAPI(config['api_server'])
db = DATABASE(config['database'])
AUCTION_ID = 'ISK005'
config = json.load(open('python/config.json'))

HVLOGINURL = f"http://alt.hentaiverse.org/isekai/login?ipb_member_id={config['ipb_member_id']}&ipb_pass_hash={config['ipb_pass_hash']}"
session = requests.Session()
session.get(HVLOGINURL)

auction_mail = [{'seller': 'unikwind', 'title': '[wts] equips for auction', 'content': 'Thank you. :)', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Peerless Shocking Willow Staff of Destruction': 'https://hentaiverse.org/isekai/equip/596425/5a16b3bb39', 'Legendary Ruby Power Boots of Protection': 'https://hentaiverse.org/isekai/equip/477363/88394bb74f'}}}, {'seller': 'chjj30', 'title': 'Auction', 'content': '========== Attachment ==========\n\n25 x Crystallized Phazon\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['25x Crystallized Phazon']}}, {'seller': 'chjj30', 'title': 'Auction', 'content': '========== Attachment ==========\n\n20 x Repurposed Actuator\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['20x Repurposed Actuator']}}, {'seller': 'chjj30', 'title': 'Auction', 'content': '========== Attachment ==========\n\n25 x Defense Matrix Modulator\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['25x Defense Matrix Modulator']}}, {'seller': 'chjj30', 'title': 'Auction', 'content': '========== Attachment ==========\n\n50 x High-Grade Cloth\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['50x High-Grade Cloth']}}, {'seller': 'chjj30', 'title': '100 x Scroll of the Avatar', 'content': '========== Attachment ==========\n\n100 x Scroll of the Avatar\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['100x Scroll of the Avatar']}}, {'seller': 'chjj30', 'title': 'Auction', 'content': '========== Attachment ==========\n\n200 x Scroll of Protection\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['200x Scroll of Protection']}}, {'seller': 'Jake643', 'title': 'Auction', 'content': "Hi,\n\nI'd like to send this equip for the next auction.\n\nThank you!", 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Magnificent Phase Shoes of Niflheim': 'https://hentaiverse.org/isekai/equip/314089/ff0da269b2'}}}, {'seller': 'Jake643', 'title': 'Auction', 'content': "Hi,\n\nI'd like to send this equip for the next auction.\n\nThank you!", 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Arctic Willow Staff of Destruction': 'https://hentaiverse.org/isekai/equip/247881/78eda54a88'}}}, {'seller': 'Jake643', 'title': 'Auction', 'content': "Hi,\n\nI'd like to send this equip for the next auction.\n\nThank you!", 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Magnificent Phase Robe of Niflheim': 'https://hentaiverse.org/isekai/equip/272957/adb3fe266c'}}}, {'seller': 'Jake643', 'title': 'Auction', 'content': "Hi,\n\nI'd like to send this equip for the next auction.\n\nThank you!", 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Magnificent Amber Force Shield of Protection': 'https://hentaiverse.org/isekai/equip/533257/a49e8c84c6'}}}, {'seller': 'Jake643', 'title': 'Auction', 'content': "Hi,\n\nI'd like to send this equip for the next auction.\n\nThank you!", 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Onyx Phase Pants of Niflheim': 'https://hentaiverse.org/isekai/equip/580613/cd0aa132d9'}}}, {'seller': 'Jake643', 'title': 'Auction', 'content': "Hi,\n\nI'd like to send this equip for the next auction.\n\nThank you!", 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Magnificent Phase Pants of Heimdall': 'https://hentaiverse.org/isekai/equip/593158/a94638ded2'}}}, {'seller': 'Jake643', 'title': 'Auction', 'content': "Hi,\n\nI'd like to send this equip for the next auction.\n\nThank you!", 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Magnificent Charged Phase Gloves of Niflheim': 'https://hentaiverse.org/isekai/equip/595318/e6f77c1570'}}}, {'seller': 'Pretty anon', 'title': 'For auction-Legendary Cobalt Force Shield of Protection', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Cobalt Force Shield of Protection': 'https://hentaiverse.org/isekai/equip/595395/3bb3bdfdb4'}}}, {'seller': 'chjj30', 'title': 'Auction', 'content': '========== Attachment ==========\n\n80 x High-Grade Wood\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['80x High-Grade Wood']}}, {'seller': 'chjj30', 'title': 'Auction', 'content': '========== Attachment ==========\n\n100 x High-Grade Leather\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['100x High-Grade Leather']}}, {'seller': 'Chizuru Ichinose', 'title': 'e', 'content': "or just return if you don't want it, thanks.\n\n========== Attachment ==========\n\n[537062] Legendary Savage Power Armor of Protection\n\n================================", 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Savage Power Armor of Protection': 'https://hentaiverse.org/isekai/equip/537062/858d697b63'}}}, {'seller': 'sharmy', 'title': 'For Auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['20x Defense Matrix Modulator']}}, {'seller': 'sharmy', 'title': 'For Auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['20x Repurposed Actuator']}}, {'seller': 'sharmy', 'title': 'For Auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Jade Power Gauntlets of Protection': 'https://hentaiverse.org/isekai/equip/581929/10c0de0d55'}}}, {'seller': 'sharmy', 'title': 'For Auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Zircon Phase Cap of Fenrir': 'https://hentaiverse.org/isekai/equip/585385/f68287b5e9'}}}, {'seller': 'sharmy', 'title': 'For Auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Onyx Phase Cap of Fenrir': 'https://hentaiverse.org/isekai/equip/588152/46a363f203'}}}, {'seller': 'Pretty anon', 'title': 'For auction-Legendary Onyx Shade Boots of the Fleet', 'content': 'Thanks!', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Onyx Shade Boots of the Fleet': 'https://hentaiverse.org/isekai/equip/586289/7b7aeeddca'}}}, {'seller': 'Jake643', 'title': 'Auction', 'content': "Hi,\n\nI'd like to send this equip for the next auction.\n\nThank you!", 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Magnificent Onyx Power Leggings of Protection': 'https://hentaiverse.org/isekai/equip/588143/a7aac8e399'}}}, {'seller': 'chjj30', 'title': 'Auction', 'content': '========== Attachment ==========\n\n500 x Mid-Grade Metals\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['500x Mid-Grade Metals']}}, {'seller': '稗田阿一', 'title': 'auction', 'content': '========== Attachment ==========\n\n[516253] Legendary Onyx Phase Shoes of Niflheim\n[504816] Magnificent Radiant Phase Shoes of Mjolnir\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Onyx Phase Shoes of Niflheim': 'https://hentaiverse.org/isekai/equip/516253/ed1a5bcc38', 'Magnificent Radiant Phase Shoes of Mjolnir': 'https://hentaiverse.org/isekai/equip/504816/da82317d39'}}}, {'seller': 'Pretty anon', 'title': 'For auction-Legendary Ruby Power Leggings of Protection', 'content': 'Resending this one too for the same reason as the other one, thanks!', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Ruby Power Leggings of Protection': 'https://hentaiverse.org/isekai/equip/519667/cd1d8d4e79'}}}, {'seller': 'Pretty anon', 'title': 'For auction-Legendary Mithril Buckler of Warding', 'content': "Resending because I saw the test thread and they aren't there and it's been a few weeks since I sent it so just in case. Thanks!", 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Mithril Buckler of Warding': 'https://hentaiverse.org/isekai/equip/525559/3e92dba327'}}}, {'seller': 'Jake643', 'title': 'Auction', 'content': 'Hi,\n\nI would like this equipment to be auctioned in the next auction.\n\nThank you.', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Fiery Club of Slaughter': 'https://hentaiverse.org/isekai/equip/574492/578c80da2c'}}}, {'seller': 'Firew', 'title': 'For the next Auction', 'content': 'Thank you!\n\n========== Attachment ==========\n\n[520895] Legendary Cobalt Force Shield of Dampening\n[296049] Legendary Onyx Phase Cap of Heimdall\n[555006] Legendary Frugal Phase Pants of Fenrir\n[499957] Legendary Jade Power Helmet of Protection\n[367917] Legendary Cobalt Power Armor of Protection\n[506192] Peerless Jade Power Leggings of Protection\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Cobalt Force Shield of Dampening': 'https://hentaiverse.org/isekai/equip/520895/b0bc6c43a8', 'Legendary Onyx Phase Cap of Heimdall': 'https://hentaiverse.org/isekai/equip/296049/ad7f552d70', 'Legendary Frugal Phase Pants of Fenrir': 'https://hentaiverse.org/isekai/equip/555006/5172e11ab3', 'Legendary Jade Power Helmet of Protection': 'https://hentaiverse.org/isekai/equip/499957/2db91bece5', 'Legendary Cobalt Power Armor of Protection': 'https://hentaiverse.org/isekai/equip/367917/41a2e64ca8', 'Peerless Jade Power Leggings of Protection': 'https://hentaiverse.org/isekai/equip/506192/ce8fce6fdc'}}}, {'seller': '稗田阿一', 'title': 'for auction', 'content': '========== Attachment ==========\n\n[568766] Legendary Ruby Shade Breastplate of the Fleet\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Ruby Shade Breastplate of the Fleet': 'https://hentaiverse.org/isekai/equip/568766/15a55c3aae'}}}, {'seller': '稗田阿一', 'title': 'auction', 'content': '========== Attachment ==========\n\n[498287] Legendary Ruby Shade Helmet of the Fleet\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Ruby Shade Helmet of the Fleet': 'https://hentaiverse.org/isekai/equip/498287/cdad4c0de2'}}}, {'seller': 'silverporcupine', 'title': 'Auction', 'content': '========== Attachment ==========\n\n[572302] Legendary Jade Phase Gloves of Fenrir\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Jade Phase Gloves of Fenrir': 'https://hentaiverse.org/isekai/equip/572302/0dd2feb87e'}}}, {'seller': 'Pretty anon', 'title': 'For auction-Legendary Mithril Plate Cuirass of Warding', 'content': 'thx', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Mithril Plate Cuirass of Warding': 'https://hentaiverse.org/isekai/equip/554349/dbe5d1cee1'}}}, {'seller': 'chikeshi', 'title': 'for isk auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Jade Power Helmet of Protection': 'https://hentaiverse.org/isekai/equip/549968/1093a2ecf9'}}}, {'seller': 'chikeshi', 'title': 'for isk auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Magnificent Charged Phase Pants of Heimdall': 'https://hentaiverse.org/isekai/equip/545177/778d8bc7ee'}}}, {'seller': 'chikeshi', 'title': 'for isk auction', 'content': '你好，請問能幫我拍賣這些東西嗎?\n另外想詢問isk拍賣大約多久會舉辦一次?\n謝謝', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Fiery Club of Slaughter': 'https://hentaiverse.org/isekai/equip/545084/0b6c561f8f'}}}, {'seller': 'silverporcupine', 'title': 'Auction', 'content': '========== Attachment ==========\n\n[536820] Legendary Cobalt Cotton Shoes of the Demon-fiend\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Cobalt Cotton Shoes of the Demon-fiend': 'https://hentaiverse.org/isekai/equip/536820/4fd6426772'}}}, {'seller': 'lololo16', 'title': 'Auction', 'content': 'thanks', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Magnificent Frugal Phase Shoes of Heimdall': 'https://hentaiverse.org/isekai/equip/474560/024c093cda'}}}, {'seller': 'lololo16', 'title': 'Auction', 'content': 'thanks', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Magnificent Radiant Phase Gloves of Fenrir': 'https://hentaiverse.org/isekai/equip/335179/d78087b14f'}}}, {'seller': 'chjj30', 'title': 'Auction', 'content': '========== Attachment ==========\n\n[532056] Legendary Radiant Phase Robe of Heimdall\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Radiant Phase Robe of Heimdall': 'https://hentaiverse.org/isekai/equip/532056/cfcd42ebe8'}}}, {'seller': 'silverporcupine', 'title': 'Auction', 'content': '========== Attachment ==========\n\n[478395] Legendary Ethereal Katana of Balance\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Ethereal Katana of Balance': 'https://hentaiverse.org/isekai/equip/478395/a74296624f'}}}, {'seller': 'silverporcupine', 'title': 'Auction', 'content': '========== Attachment ==========\n\n[507444] Legendary Ruby Shade Boots of the Fleet\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Ruby Shade Boots of the Fleet': 'https://hentaiverse.org/isekai/equip/507444/324e22837d'}}}, {'seller': 'silverporcupine', 'title': 'Auction', 'content': '========== Attachment ==========\n\n[526072] Legendary Cobalt Force Shield of Protection\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Cobalt Force Shield of Protection': 'https://hentaiverse.org/isekai/equip/526072/772c091ed7'}}}, {'seller': 'Pretty anon', 'title': 'For auction-Legendary Jade Power Helmet of Warding', 'content': 'Thanks!', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Jade Power Helmet of Warding': 'https://hentaiverse.org/isekai/equip/530523/1cb34b6d28'}}}, {'seller': 'chjj30', 'title': 'Auction', 'content': '========== Attachment ==========\n\n[526870] Legendary Charged Phase Shoes of Freyr\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Legendary Charged Phase Shoes of Freyr': 'https://hentaiverse.org/isekai/equip/526870/1640d66942'}}}, {'seller': 'chjj30', 'title': 'Auction', 'content': '========== Attachment ==========\n\n[523171] Magnificent Tempestuous Willow Staff of Destruction\n\n================================', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'equips': {'Magnificent Tempestuous Willow Staff of Destruction': 'https://hentaiverse.org/isekai/equip/523171/b1b0ca8f22'}}}, {'seller': 'Null2Null', 'title': 'auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['168x Mid-Grade Cloth']}}, {'seller': 'Null2Null', 'title': 'auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['35x High-Grade Wood']}}, {'seller': 'Null2Null', 'title': 'auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['28x High-Grade Metals']}}, {'seller': 'Null2Null', 'title': 'auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['5x Crystallized Phazon']}}, {'seller': 'Null2Null', 'title': 'auction', 'content': 'n/t', 'mmtoken': 'ob07dfu9ngc', 'cod': 0, 'attachments': {'items': ['67x High-Grade Cloth']}}]

def accept(mid, mm_token):
    url = f'http://alt.hentaiverse.org/?s=Bazaar&ss=mm&filter=inbox&mid={mid}'
    post_data = {
        'action': 'attach_remove',
        'action_value': 0,
        'mmtoken': mm_token}
    resp = session.post(url, data=post_data)
    resp = bs(resp.text, 'html.parser')
    assert resp.find(id='mailform')
    if not resp.find('img', onclick='mooglemail.remove_attachment(0)'):
        return True
    else:
        return False

def attach_items(self, mm_token, item_id, quantity):
    new_mail_url = 'http://alt.hentaiverse.org/isekai/?s=Bazaar&ss=mm&filter=new'
    resp = self.session.post(new_mail_url, data={
        'action': 'attach_add',
        'action_value': 0,
        'select_item': item_id,
        'select_count': quantity,
        'mmtoken': mm_token,
        'select_pane': 'item'})
    resp = bs(resp.text, 'html.parser')
    assert resp.find('img', onclick='mooglemail.remove_attachment(0)')
    return True

def set_cod(mm_token, cod_amount):
    if cod_amount > 0:
        cod_amount = max(cod_amount, 10)  # minimum CoD is 10c, you wont need this
    new_mail_url = 'http://alt.hentaiverse.org/?s=Bazaar&ss=mm&filter=new'
    resp = session.post(new_mail_url, data={
        'action': 'attach_cod',
        'action_value': cod_amount,
        'mmtoken': mm_token})
    resp = bs(resp.text, 'html.parser')
    find_string = 'Requested Payment on Delivery: ' \
                  + f"{cod_amount:,}" \
                  + ' credits'
    assert resp.find('div', string=find_string)
    return True

def new(mm_receiver,mm_subject,mm_body):
    new_mail_url = 'http://alt.hentaiverse.org/?s=Bazaar&ss=mm&filter=new'
    resp = session.get(new_mail_url)
    resp = bs(resp.text, 'html.parser')
    assert resp.find(id='mailform')
    mm_token = resp.find('input', {'name': 'mmtoken'}).get('value')
    mm_receiver = '' # the user's name you want to send to
    mm_subject = '' # mail subject
    mm_body = '' # mail body
    resp = session.post(new_mail_url, data = {
        'message_to_name': mm_receiver,
        'message_subject': mm_subject,
        'message_body': mm_body,
        'action': 'send',
        'mmtoken': mm_token})
    resp = bs(resp.text, 'html.parser')
    if resp.find('div', string='Invalid or missing recipient, kupo!'): # name changes cause this mostly
        raise ValueError('Invalid or missing recipient.') # you should handle this
    assert resp.find('div', string='Your message has been sent.')

for mail in auction_mail:

    if 'attachments' in mail:
        mid = mail['mid']
        mm_token = mail['mmtoken']
        if 'items' in mail['attachments']:
            for item in mail['attachments']['items']:
                seller, winner, price = db.search_mat(AUCTION_ID, item)
                if price == None:
                    # reject(mail['mid'], mail['mmtoken'])
                    print(f"已退回{mail['seller']}的{item}")
                elif seller == mail['seller']:
                    if accept(mid, mm_token):



        if 'equips' in mail['attachments']:
            for equip in mail['attachments']['equips']:
                equip_link = mail['attachments']['equips'][equip]
                seller, winner, price = db.search_equip(AUCTION_ID, equip_link)
                if price == None:
                    # reject(mail['mid'], mail['mmtoken'])
                    print(f"已退回{mail['seller']}的{equip, equip_link}")
                elif seller == mail['seller']:


