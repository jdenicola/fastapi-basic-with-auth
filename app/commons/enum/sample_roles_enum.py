from enum import Enum


class SampleRoleEnum(Enum):
    ADMIN = 'Admin'
    READONLY = 'ReadOnly'

    # It is recommended to add static methods to obtain Enum from name and value.
