"""
Dictionaries of Weasyl staff.

This module must be initialized with a call to `staff._init_staff()`,
passing in a dict of staff members. Normally, this dict is generated by
weasyl/read_staff_yaml.py, which reads YAML from macro.MACRO_SYS_STAFF_CONFIG_PATH.
A properly configured staff YAML file contains staff levels, and their user ID
number. A properly configured configuration file might look as folows:

    directors:
        - 1014   # Fiz
        - 2061   # Ikani

    technical_staff:
        - 5756   # Weykent

    admins:  # Directors and technical_staff also have admin privs.
        - 23613  # Hendikins
        - 3      # Kihari

    mods:  # Admins also have mod privs.
        - 40212  # pinardilla

    developers:
        - 38623  # 8BitFur
        - 34165  # Charmander
        - 15224  # Foximile
        - 2475   # Kailys
        - 8627   # Kauko

We recommend storing staff members in lexicographic order by name
within each group.
"""

DIRECTORS = set()
""" Directors have the same powers as admins. """


TECHNICAL = set()
""" Technical staff can moderate all content and manage all users. """


ADMINS = set()
""" Site administrators can update site news and moderate user content. """


MODS = set()
""" Site moderators can hide submissions, manage non-admin users, etc. """


DEVELOPERS = set()
""" Purely cosmetic group for users who contribute to site development. """


def _init_staff(staff_config_dict):
    """
    Loads staff from a dictionary object.

    Parameters:
        staff_config_dict: Dictionary object containing staff levels and user ids.
    """

    DIRECTORS.update(staff_config_dict['directors'])
    TECHNICAL.update(DIRECTORS, staff_config_dict['technical_staff'])
    ADMINS.update(DIRECTORS, TECHNICAL, staff_config_dict['admins'])
    MODS.update(ADMINS, staff_config_dict['mods'])
    DEVELOPERS.update(staff_config_dict['developers'])
