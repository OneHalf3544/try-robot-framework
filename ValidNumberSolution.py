import re

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip(" ")
        if len(s) == 0:
            return False

        split = s.split("e")
        if len(split) > 2:
            # several 'e'
            return False

        if len(split) == 2 and not self.isIntegerNumber(split[1]):
            # Wrong exponent degree
            return False

        mantissa = split[0]
        return self.isDecimalNumber(mantissa)

    def isDecimalNumber(self, numberString: str) -> bool:
        return len(numberString) > 0 and re.fullmatch(r"[-+]?(\d+|((\d+\.|\.\d+)\d*))", numberString) != None

    def isIntegerNumber(self, numberString: str) -> bool:
        return len(numberString) > 0 and re.fullmatch(r"[-+]?\d+", numberString) != None


class SoftAsserter:
    solution = Solution()
    errors = []

    def assert_is_number(self, string):
        if not self.solution.isNumber(string):
            self.errors.append("'{}' expected to be a number".format(string))

    def assert_is_not_a_number(self, string):
        if self.solution.isNumber(string):
            self.errors.append("'{}' expected to be not a number".format(string))

    def assert_no_errors_found(self):
        assert not self.errors, "found errors: \n" + "\n".join(self.errors)


if __name__ == '__main__':
    sa = SoftAsserter()
    sa.assert_is_number(" 23  ")
    sa.assert_is_number("12.")
    sa.assert_is_number(".3")
    sa.assert_is_number("0.23")
    sa.assert_is_number("12323")
    sa.assert_is_number("123.23")
    sa.assert_is_number("+123.23")
    sa.assert_is_number("+123.2e3")
    sa.assert_is_number("-123.2e+3")

    sa.assert_is_not_a_number("  ")
    sa.assert_is_not_a_number(".")
    sa.assert_is_not_a_number("e9")
    sa.assert_is_not_a_number("-e58 ")
    sa.assert_is_not_a_number("12e2.5")
    sa.assert_is_not_a_number("12e2e5")
    sa.assert_is_not_a_number("abc")
    sa.assert_is_not_a_number("1.23.23")
    sa.assert_is_not_a_number("--123.23")
    sa.assert_is_not_a_number("+-123.23")

    sa.assert_no_errors_found()