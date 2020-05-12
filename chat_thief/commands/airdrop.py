import random
from pathlib import Path
import traceback

from chat_thief.models.command import Command
from chat_thief.irc import send_twitch_msg
from chat_thief.soundeffects_library import SoundeffectsLibrary
from chat_thief.config.stream_lords import STREAM_LORDS, STREAM_GODS
from chat_thief.welcome_committee import WelcomeCommittee
from chat_thief.chat_logs import ChatLogs

INVALID_USERS = ["nightbot", ".tim.twitch.tv"] + STREAM_GODS
CONNECTING_MSG = '{"message": "Connecting to #beginbot as beginbotbot"}'


def random_soundeffect():
    return random.sample(SoundeffectsLibrary.soundeffects_only(), 1)[0]


def drop_effect(user, soundeffect):
    if user not in INVALID_USERS:
        print(f"\n\n\tDROPPING FOR: {user}\n")
        Command(soundeffect).allow_user(user)
        return f"@{user} now has access to Sound Effect: !{soundeffect}"


def dropreward():
    with Path(__file__).parent.parent.joinpath("logs/chat.log") as log:
        chat_lines = [
            line
            for line in log.read_text().split("\n")
            if line
            and line.split(":")[0] not in INVALID_USERS
            and line != CONNECTING_MSG
        ]
    user = chat_lines[-1].split(":")[0]
    soundeffect = random_soundeffect()
    return drop_effect(user, soundeffect)


def drop_random_soundeffect_to_user(user):
    soundeffect = random_soundeffect()
    return drop_effect(user, soundeffect)


class Airdrop:
    def drop_random_soundeffect_to_random_user(self):
        user = self.random_user()
        soundeffect = random_soundeffect()
        return drop_effect(user, soundeffect)

    def random_user(self, blacklisted_users=[]):
        # try:
        looking_for_user = True
        while looking_for_user:
            users = ChatLogs().recent_stream_peasants()
            user = random.sample(users, 1)[0]
            if user not in INVALID_USERS + blacklisted_users:
                looking_for_user = False
        return user
        # except:
        #     traceback.print_exc()
        #     breakpoint()

    def __init__(self, target_user=None, target_command=None, amount=None):
        self._target_user = target_user
        self._target_command = target_command
        self._amount = amount

    def drop(self):
        return self.drop_random_soundeffect_to_random_user()

        # if self._target_user is None and self._target_command is None and
        # self._amount is None

    # if len(args) == 0:
    #     print(f"Dropping Sound Effect since we got no args")
    #     return drop_random_soundeffect_to_random_user()
    # else:
    #     if _is_int_between(args[0]):
    #         for i in range(0, int(args[0])):
    #             print(f"Dropping {i} Sound Effect")
    #             send_twitch_msg(drop_random_soundeffect_to_random_user())
    #     elif args[0] in WelcomeCommittee().present_users():
    #         user = args[0]
    #         print(f"Dropping a Sound Effect for: @{user}")
    #         return drop_random_soundeffect_to_user(user)
    #     elif args[0] in SoundeffectsLibrary.fetch_soundeffect_names():
    #         user = random_user()
    #         soundeffect = args[0]
    #         print(f"Dropping the Sound Effect: {soundeffect}")
    #         return drop_effect(user, soundeffect)