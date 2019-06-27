import minqlx

NON_SYMMETRICAL_MAPS = set([
    "grimdungeons",
])

class swap_bases_ad(minqlx.Plugin):

    def __init__(self):
        self.mapname = None
        self.are_bases_swapped = False
        self.non_symmetrical_map = False

        self.add_hook("new_game", self.handle_new_game)
        self.add_hook("round_end", self.handle_round_end)

    def handle_new_game(self):
        if self.mapname != self.game.map:
            self.are_bases_swapped = False
            self.mapname = self.game.map
            self.non_symmetrical_map = self.mapname in NON_SYMMETRICAL_MAPS
            return

        if self.are_bases_swapped:
            self.swap()

    def handle_round_end(self, data):
        if not self.non_symmetrical_map:
            return

        self.swap()

    def swap(self):
        minqlx.swap_team_bases()
        self.are_bases_swapped = not self.are_bases_swapped
