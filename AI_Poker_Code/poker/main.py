from honest_player import HonestPlayer
from fish_player import FishPlayer
from console_player import ConsolePlayer
from emulator_player import EmulatorPlayer

h = HonestPlayer()
f = FishPlayer()

from pypokerengine.api.game import setup_config, start_poker

# config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
# config.register_player(name="p1", algorithm=FishPlayer())
# config.register_player(name="p2", algorithm=FishPlayer())
# config.register_player(name="p3", algorithm=FishPlayer())
# game_result = start_poker(config, verbose=1)



# from pypokerengine.api.game import setup_config, start_poker
# config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
# config.register_player(name="fish_player", algorithm=FishPlayer())
# config.register_player(name="honest_player", algorithm=HonestPlayer())
# game_result = start_poker(config, verbose=1)
# for player_info in game_result["players"]:
#     print (player_info)


# config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
# config.register_player(name="fish_player", algorithm=FishPlayer())
# config.register_player(name="human_player", algorithm=ConsolePlayer())
# game_result = start_poker(config, verbose=0)  # verbose=0 because game progress is visualized by ConsolePlayer


from pypokerengine.api.game import setup_config, start_poker
config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
config.register_player(name="Honest_player", algorithm=FishPlayer())
config.register_player(name="emulator_player", algorithm=EmulatorPlayer())
game_result = start_poker(config, verbose=1)