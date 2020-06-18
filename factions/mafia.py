from game import Game
from .base import Faction

# all factions that oppose the mafia, including town and competing evil
OPPOSING_FACTIONS = ['town', 'neutral.serialkiller']


class Mafia(Faction):
    name = 'Mafia'
    id = 'mafia'
    win_con = 'Kill all townies and competing evil factions.'

    def has_won(self, game: Game):
        alive_maf = len(game.filter_players(faction='mafia'))
        alive_opposing = len(
            [*filter(lambda pl: pl.faction.id in OPPOSING_FACTIONS and pl.alive, game.players)])
        return alive_maf > 0 and alive_maf >= alive_opposing
