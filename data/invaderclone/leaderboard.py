"""Implements a leaderboard"""

import pickle
from os.path import join

LEADERBOARD_VERSION_NAME = "beebo"

class Leaderboard:
    """a leaderboard"""

    def __init__(self):
        """initialize a leaderbaord"""
        self._version_name = LEADERBOARD_VERSION_NAME
        self._scores = []

    def add_score(self, score):
        """add a score to the leaderboard"""

        if (
            self._scores is None
            or len(self._scores) == 10
            ):
            self._scores.pop()
        self._scores.append(score)
        self.sort()

    @property
    def version_name(self):
        return self._version_name

    @property
    def scores(self):
        """get the socres"""

        return self._scores

    def sort(self):
        """sort the scores"""

        self._scores.sort(key=lambda e: e[0])
        self._scores.reverse()

    @property
    def lowest(self):
        """get the lowest score"""

        if not self._scores:
            return 0

        lowest = len(self._scores) - 1
        return self._scores[lowest]

    def save(self, path):
        """save the scores to a file"""

        save_filename = join(path, "scores.pkle")
        with open(save_filename, "wb") as handle:
            pickle.dump(self, handle, pickle.HIGHEST_PROTOCOL)


def create_leaderboard_from_pickle(apickle):
    """create a leaderboard from a file"""

    with open(apickle, "rb") as handle:
        leader = pickle.load(handle)
        leader.sort()

    return leader
