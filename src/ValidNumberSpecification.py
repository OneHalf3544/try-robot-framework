from ValidNumberSolution import Solution

class ValidNumberSpecification(object):
    solution = Solution()

    def is_a_valid_number(self, stringRepresentationOfNumber :str):
        assert self.__isValidNumber(stringRepresentationOfNumber), "{} isn't a valid number".format(stringRepresentationOfNumber)

    def is_not_a_valid_number(self, stringRepresentationOfNumber :str):
        assert not self.__isValidNumber(stringRepresentationOfNumber), "{} is a valid number".format(stringRepresentationOfNumber)

    def __isValidNumber(self, string: str) -> bool:
        return self.solution.isNumber(string)