import unittest
from FirstExercise import getSpecificNumbers

class TestStringMethods(unittest.TestCase):

    def test_givenAnArrayThatContainsStringNumbers_thenExceptACorrectResultArray(self):
        X = 9
        testArray = ['9', '3456', '80' '27', '940', '17', '45', '232349', '1', '12']
        result = getSpecificNumbers(testArray, X)
        self.assertEqual(result, ['9', '3456', '940', '45'])


    def test_givenAnArrayThatContainsStringWithoutNumbers_thenExceptEmptyArray(self):
        X = 2
        testArray = ['hello', 'world']
        result = getSpecificNumbers(testArray, X)
        self.assertEqual(result, [])
    
    def test_givenAnArrayThatContainsXAtThStartOrEnd_thenExceptOnlyWithXAtTheStart(self):
        X = 5
        testArray = ['hello'+str(X), 'world', str(X)+'im', 'a', str(X)+'test']
        result = getSpecificNumbers(testArray, X)
        self.assertEqual(result, [str(X)+'im', str(X)+'test'])

    def test_givenAnArrayThatContainsStringNumbersAndEmptyStrings_thenExceptACorrectResultArray(self):
        X = 2
        testArray = ['9', '3456', '80' '27', '940', '17', '45', '232349', '1', '12', '   ', '']
        result = getSpecificNumbers(testArray, X)
        self.assertEqual(result, ['3456', '940', '232349', '12'])

    def test_givenAnArrayThatContainsStringNumbersAndXIsMinorToZero_thenExceptEmptyArray(self):
        X1 = 0
        X2 = -9
        testArray = ['9', '3456', '80' '27', '940', '17', '45', '232349', '1', '12']
        firstResult = getSpecificNumbers(testArray, X1)
        secondResult = getSpecificNumbers(testArray, X2)
        self.assertEqual(firstResult, [])
        self.assertEqual(secondResult, [])

    def test_givenAnArrayThatContainsStringNumbersAndXContainsMoreThanOneDigits_thenExceptEmptyArray(self):
        X = 17
        testArray = ['9', '3456', '80' '27', '940', '17', '45', '232349', '1', '12']
        result = getSpecificNumbers(testArray, X)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
