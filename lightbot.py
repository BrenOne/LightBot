import vk_api
import datetime
import time
import random as r
import RPi.GPIO ad GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT, initial=1)

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.exceptions import ApiError
C_VK = 198427451
C_TOKEN_ME = "8694df0df2f331c0bfddbf73425f40000000000000000b6004658d13c74844f56dffc73c9e65422c157c3"
vk_me = vk_api.VkApi(token=C_TOKEN_ME)
longpoll = VkBotLongPoll(vk_me, C_VK)
upload = vk_api.VkUpload(vk_me)
""""довы"""
rob1 = 396886945
rob2 = 35184757
nikita = 237472667
nikita1 = 590952346
""""довы"""
dostup_All = [rob2, rob1, nikita, nikita1]
"""клава..............................................................."""
keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Включить свет💡', color=VkKeyboardColor.POSITIVE)
"""клава..............................................................."""
"""свет"""
keyboard1 = VkKeyboard(one_time=False)
keyboard1.add_button('Выключить свет', color=VkKeyboardColor.NEGATIVE)
"""свет"""

def send_msg(peer_id, textsend):
    vk_me.method('messages.send',
                 {'user_id': peer_id,
                  'random_id': r.randint(0, 2**64),
                  'message': textsend})

def klava_msg(peer_id, textklava):
    vk_me.method('messages.send',
                 {'user_id': peer_id,
                  'random_id': r.randint(0, 2**64),
                  'message': textklava,
                  "keyboard": keyboard.get_keyboard()})
def klavastop_msg(peer_id, textklava):
    vk_me.method('messages.send',
                 {'user_id': peer_id,
                  'random_id': r.randint(0, 2**64),
                  'message': textklava,
                  "keyboard": keyboard1.get_keyboard()})
while True:
    try:
        try:
            for event in longpoll.listen():
                from_id = event.obj.peer_id
                if from_id in dostup_All:
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        cm = event.obj.text.lower()
                        peer_id = event.obj.peer_id
                        user_id = peer_id - 2000000000
                        if cm == 'клава' or cm == "Начать" or cm == "начать" or cm == "Клава":
                            klava_msg(peer_id, "Клавиатура успешно открыта")
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        cm = event.obj.text.lower()
                        peer_id = event.obj.peer_id
                        user_id = peer_id - 2000000000
                        if cm == 'Включить свет💡' or cm == "вкл" or cm == "Включить" or cm == "включить свет💡":
                            GPIO.output(24, 1)
                            klavastop_msg(peer_id, "Свет вкл💡")

                    if event.type == VkBotEventType.MESSAGE_NEW:
                        cm = event.obj.text.lower()
                        peer_id = event.obj.peer_id
                        user_id = peer_id - 2000000000
                        if cm == 'выключить свет' or cm == "Выключить свет":
                            GPIO.output(24, 0)
                            klava_msg(peer_id, "Свет выкл")
        except ApiError as ex:
            print('VK_EROR: ' + str(ex))
    except Exception as ex:
            print('PYTHON_EROR: ' + str(ex))

