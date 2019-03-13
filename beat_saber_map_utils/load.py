import json
import subprocess


class Info:

    DefaultFilename = "info.json"

    def __init__(self, filename=DefaultFilename):
        self.filename = filename

        with open(filename) as info_file:
            self.raw = json.load(info_file)

    def __getitem__(self, key):
        return self.raw[key]

    def __setitem__(self, key, value):
        self.raw[key] = value

    @property
    def difficulty_levels_by_name(self):
        """Difficulty levels keyed by difficulty name."""
        levels = dict()
        for level in self.raw["difficultyLevels"]:
            name = level["difficulty"]
            del level["difficulty"]
            levels[name] = level

        return levels

    @property
    def revision_description(self):
        """
        A description including the song name and authorship fields and the
        output of `git describe` if available.
        """
        return self._describe()

    def _describe(self, song_suffix=None):
        if song_suffix is None:
            song_suffix = ""

        try:
            describe_bytes = subprocess.check_output(["git", "describe"])
            tag = describe_bytes.decode("utf8").rstrip() + " "

            # If both tag and suffix are specified, separate them by a space.
            if song_suffix and song_suffix[-1] != " ":
                song_suffix += " "
        except subprocess.CalledProcessError:
            tag = " "

        return "{info[songName]} - {info[songSubName]} {suffix}{tag}by {info[authorName]}".format(
            info=self, tag=tag, suffix=song_suffix)

    def get_difficulty_description(self, difficulty):
        """
        :return: A description song including the name and authorship fields,
        the difficulty, and the output of `git describe` if available.
        """
        return self._describe(difficulty)

    @property
    def song_title(self):
        """Song name and sub-name."""
        return "{info[songName]} - {info[songSubName]}".format(info=self)
