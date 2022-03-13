# TODO: This is post-v4.
# TODO: Reorganise these models based on which big obj uses little obj
# TODO: Potentially rename some model references to enums, if applicable
# TODO: Reorganise mixins to its own thing, currently placed here because circular import sucks.
# also, it should be serialiser* but idk, fl0w'd say something if I left it like that. /shrug
import datetime
from logging import Logger
from math import floor
from typing import Union

from interactions.base import get_logger

log: Logger = get_logger("mixin")


class DictSerializerMixin(object):
    """
    The purpose of this mixin is to be subclassed.

    .. note::
        On subclass, it:
            -- From kwargs (received from the Discord API response), add it to the `_json` attribute
            such that it can be reused by other libraries/extensions
            -- Aids in attributing the kwargs to actual model attributes, i.e. `User.id`
            -- Dynamically sets attributes not given to kwargs but slotted to None, signifying that it doesn't exist.

    .. warning::
        This does NOT convert them to its own data types, i.e. timestamps, or User within Member. This is left by
        the object that's using the mixin.
    """

    __slots__ = "_json"

    def __init__(self, **kwargs):
        self._json = kwargs
        # for key in kwargs:
        #    setattr(self, key, kwargs[key])

        for key in kwargs:
            if key in self.__slots__ if hasattr(self, "__slots__") else True:
                # else case if the mixin is used outside of this library and/or SDK.
                setattr(self, key, kwargs[key])
            else:
                log.warning(
                    f"Attribute {key} is missing from the {self.__class__.__name__} data model, skipping."
                )
                # work on message printout? Effective, but I think it should be a little bit more friendly
                # towards end users

        # if self.__slots__ is not None:  # safeguard, runtime check
        if hasattr(self, "__slots__"):
            for _attr in self.__slots__:
                if not hasattr(self, _attr):
                    setattr(self, _attr, None)


class Overwrite(DictSerializerMixin):
    """
    This is used for the PermissionOverride object.

    :ivar int id: Role or User ID
    :ivar int type: Type that corresponds ot the ID; 0 for role and 1 for member.
    :ivar str allow: Permission bit set.
    :ivar str deny: Permission bit set.
    """

    __slots__ = ("_json", "id", "type", "allow", "deny")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ClientStatus(DictSerializerMixin):
    """
    An object that symbolizes the status per client device per session.

    :ivar Optional[str] desktop?: User's status set for an active desktop application session
    :ivar Optional[str] mobile?: User's status set for an active mobile application session
    :ivar Optional[str] web?: User's status set for an active web application session
    """

    __slots__ = ("_json", "desktop", "mobile", "web")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Snowflake(object):
    """
    The Snowflake object.

    This snowflake object will have features closely related to the
    API schema. In turn, compared to regular d.py's treated snowflakes,
    these will be treated as strings.


    (Basically, snowflakes will be treated as if they were from d.py 0.16.12)

    .. note::
        You can still provide integers to them, to ensure ease of use of transition and/or
        if discord API for some odd reason will switch to integer.
    """

    __slots__ = "_snowflake"

    # Slotting properties are pointless, they are not in-memory
    # and are instead computed in-model.

    def __init__(self, snowflake: Union[int, str, "Snowflake"]) -> None:
        self._snowflake = str(snowflake)

    def __str__(self):
        # This is overridden for model comparison between IDs.
        return self._snowflake

    def __int__(self):
        # Easier to use for HTTP calling instead of int(str(obj)).
        return int(self._snowflake)

    @property
    def increment(self) -> int:
        """
        This is the 'Increment' portion of the snowflake.
        This is incremented for every ID generated on that process.

        :return: An integer denoting the increment.
        """
        return int(self._snowflake) & 0xFFF

    @property
    def worker_id(self) -> int:
        """
        This is the Internal Worker ID of the snowflake.
        :return: An integer denoting the internal worker ID.
        """
        return (int(self._snowflake) & 0x3E0000) >> 17

    @property
    def process_id(self) -> int:
        """
        This is the Internal Process ID of the snowflake.
        :return: An integer denoting the internal process ID.
        """
        return (int(self._snowflake) & 0x1F000) >> 12

    @property
    def epoch(self) -> float:
        """
        This is the Timestamp field of the snowflake.

        :return: A float containing the seconds since Discord Epoch.
        """
        return floor(((int(self._snowflake) >> 22) + 1420070400000) / 1000)

    @property
    def timestamp(self) -> datetime.datetime:
        """
        The Datetime object variation of the Timestamp field of the snowflake.

        :return: The converted Datetime object from the Epoch. This respects UTC.
        """
        return datetime.datetime.utcfromtimestamp(self.epoch)

    # ---- Extra stuff that might be helpful.

    def __hash__(self):
        return hash(self._snowflake)

    def __eq__(self, other):
        if isinstance(other, Snowflake):
            return str(self) == str(other)
        elif isinstance(other, int):
            return int(self) == other
        elif isinstance(other, str):
            return str(self) == other

        return NotImplemented

    # Do we need not equals, equals, gt/lt/ge/le?
    # If so, list them under. By Discord API this may not be needed
    # but end users might.


class Color(object):
    """
    An object representing Discord branding colors.

    .. note::
        This object only intends to cover the branding colors
        and no others. The main reason behind this is due to
        the current accepted standard of using hex codes or other
        custom-defined colors.
    """

    @property
    def blurple(self) -> hex:
        """Returns a hexadecimal value of the blurple color."""
        return 0x5865F2

    @property
    def green(self) -> hex:
        """Returns a hexadecimal value of the green color."""
        return 0x57F287

    @property
    def yellow(self) -> hex:
        """Returns a hexadecimal value of the yellow color."""
        return 0xFEE75C

    @property
    def fuchsia(self) -> hex:
        """Returns a hexadecimal value of the fuchsia color."""
        return 0xEB459E

    @property
    def red(self) -> hex:
        """Returns a hexadecimal value of the red color."""
        return 0xED4245

    # I can't imagine any bot developers actually using these.
    # If they don't know white is ff and black is 00, something's seriously
    # wrong.

    @property
    def white(self) -> hex:
        """Returns a hexadecimal value of the white color."""
        return 0xFFFFFF

    @property
    def black(self) -> hex:
        """Returns a hexadecimal value of the black color."""
        return 0x000000


class MISSING:
    """A pseudosentinel based from an empty object. This does violate PEP, but, I don't care."""

    ...
