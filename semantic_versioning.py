#!/usr/bin/env python3


def convert_string_to_version_component_numbers(s):
    """
    Waypoint 1: Convert a Semantic Versioning Component Number String to Tuple
    Convert a string representation of a semantic versioning 3-component
    number (at least 1), and that returns a tuple composed of 3 integers
    (major, minor, patch).
    @param:
    s: string representation of a semantic versioning 3-component number.
    """
    nums = tuple(s.split('.'))
    if nums[0] == "" or len(nums) > 3:
        return (1, 0, 0)
    while len(nums) < 3:
        nums += (0,)
    return tuple((int(num) for num in nums))


def compare_versions(this, other):
    """
    Waypoint 2: Compare Versions
    Return: 1 if this is above other;
            0 if this equals other;
            -1 if this is below other.
    @param:
    this, other: tuples composed of 3 integers (major, minor, patch).
    """
    if this > other:
        return 1
    elif this == other:
        return 0
    else:
        return -1


class Version:
    def __init__(self, arg1, arg2=0, arg3=0):
        """
        Waypoint 3: Write a Class Version
        Return object Version with 3 attributes (major, minor, patch)
        """
        self.version = (arg1, arg2, arg3)
        if type(arg1) == str:
            self.version = convert_string_to_version_component_numbers(arg1)
        elif type(arg1) == tuple:
            arg_str = '.'.join(str(num) for num in arg1)
            self.version = convert_string_to_version_component_numbers(arg_str)
        self.major, self.minor, self.patch = self.version

    def __repr__(self):
        """
        Waypoint 4: Compute "Official" String Representations
        Return the “official” string representation of a Version object.
        """
        return "Version" + '(' + ', '.join([str(self.major), str(self.minor),\
        str(self.patch)]) + ')'

    def __str__(self):
        """
        Waypoint 5: Compute "Informal" String Representation
        Return the "informal" or nicely printable string representation
        of a Version object.
        """
        return ".".join([str(self.major), str(self.minor), str(self.patch)])

    def __lt__(self, other):
        """
        Waypoint 6: Compare Version Instances
        """
        flag = compare_versions(self.version, other.version)
        return True if flag == -1 else False

    def __le__(self, other):
        """
        Waypoint 6: Compare Version Instances
        """
        flag = compare_versions(self.version, other.version)
        return True if flag == -1 or flag == 0 else False

    def __eq__(self, other):
        """
        Waypoint 6: Compare Version Instances
        """
        flag = compare_versions(self.version, other.version)
        return True if flag == 0 else False

    def __ne__(self, other):
        """
        Waypoint 6: Compare Version Instances
        """
        flag = compare_versions(self.version, other.version)
        return True if flag != 0 else False

    def __gt__(self, other):
        """
        Waypoint 6: Compare Version Instances
        """
        flag = compare_versions(self.version, other.version)
        return True if flag == 1 else False

    def __ge__(self, other):
        """
        Waypoint 6: Compare Version Instances
        """
        flag = compare_versions(self.version, other.version)
        return True if flag == 1 or flag == 0 else False


def main():
    version = Version("2")
    print(version.major, version.minor, version.patch)
    version = Version(1, 2)
    print(version.major, version.minor, version.patch)
    version = Version((1, 2, 8))
    print(version.major, version.minor, version.patch)
    print(repr(version))
    print(version)
    print(Version("1.2.8") > Version("2.4.5"))
    print(Version("2.4.5") > Version("1.2.8"))
    print(Version("1.2.8") < Version("2.4.5"))
    print(Version("2.4.5") < Version("1.2.8"))
    print(Version("2.4.5") == Version("1.2.8"))
    print(Version("2.4.5") == Version("2.4.5"))
    print(Version("2.4.5") != Version("2.4.5"))
    print(Version("2.4.5") != Version("1.2.8"))
    print(Version("2.4.5") >= Version("2.4.5"))
    print(Version("2.4.5") >= Version("1.2.8"))
    print(Version("2.4.5") <= Version("2.4.5"))
    print(Version("2.4.5") <= Version("1.2.8"))


if __name__ == '__main__':
    main()
