from itertools import chain, cycle

from chat_thief.models.user import User
from chat_thief.models.vote import Vote
from chat_thief.permissions_fetcher import PermissionsFetcher
from chat_thief.audio_command import AudioCommand


# 2 Paths for Coup:
#   - Peace
#       - Voted For Peace:
#           - Get a cut of the revolutionaries, sounds and points
#       - Voted for Revolution:
#           -  You lose it all
#   - Revolution
#       - Voted For Peace:
#           -  You lose it all
#       - Voted for Revolution:
#           - You will get a small selections of founds

class Revolution:
    def __init__(self, tide):
        self.tide = tide

    def turn_the_tides(self):
        user = User("beginbot")
        vote = Vote("beginbot")

        revolutionaries = vote.revolutionaries()
        peace_keepers = vote.peace_keepers()

        revolutionary_sounds = list(chain.from_iterable([
            User(user).commands() for user in
            revolutionaries
        ]))

        peace_keeper_sounds = list(chain.from_iterable([
           User(user).commands() for user in
           peace_keepers
        ]))

        print(f"Revolutionaries: {revolutionaries}")
        print(f"Sounds: {revolutionary_sounds}\n")
        print(f"Peace Keepers: {peace_keepers}")
        print(f"Sounds: {peace_keeper_sounds}\n")

        if self.tide == "peace":
            self._transfer_power(cycle(peace_keepers), revolutionaries,
                    revolutionary_sounds)

        if self.tide == "revolution":
            self._transfer_power(cycle(revolutionaries), peace_keepers, peace_keeper_sounds)

    def _transfer_power(self, power_users, weaklings, bounty):
        for user in weaklings:
            print(f"Removing All Commands for {user}")
            User(user).remove_all_commands()

        for sfx in bounty:
            user = next(power_users)
            print(f"Giving {user} SFX: {sfx}")
            audio_command = AudioCommand(sfx)
            audio_command.allow_user(user)

    # It should cost to coup
    def _revolution(self):
        results = []
        result = self.user.purge()
        results.append(result)
        permissions_manager = PermissionsFetcher("beginbot")
        result = permissions_manager.purge()
        results.append(result)
        return results