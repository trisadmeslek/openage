# Copyright 2021-2021 the openage authors. See copying.md for legal info.
#
# pylint: disable=too-few-public-methods

"""
Organize export data (nyan objects, media, scripts, etc.)
into modpacks.
"""
from ....entity_object.conversion.modpack import Modpack
from ..aoc.modpack_subprocessor import AoCModpackSubprocessor


class HDModpackSubprocessor:
    """
    Creates the modpacks containing the nyan files and media from the HD conversion.
    """

    @classmethod
    def get_modpacks(cls, gamedata):
        """
        Return all modpacks that can be created from the gamedata.
        """
        hd_base = cls._get_aoe2_base(gamedata)

        return [hd_base]

    @classmethod
    def _get_aoe2_base(cls, gamedata):
        """
        Create the aoe2_base modpack.
        """
        modpack = Modpack("hd_base")

        mod_def = modpack.get_info()

        mod_def.set_info("hd_base", "5.8", repo="openage")

        mod_def.add_include("data/*")

        AoCModpackSubprocessor.organize_nyan_objects(modpack, gamedata)
        AoCModpackSubprocessor.organize_media_objects(modpack, gamedata)

        return modpack
