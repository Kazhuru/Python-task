import unittest
from SherlockExcersise import sherlockValidString

class TestStringMethods(unittest.TestCase):

    def test_FirstString(self):
        self.assertEqual('NO', sherlockValidString('bbcccccdddddaaaaa'))

    def test_SecondString(self):
        self.assertEqual('NO', sherlockValidString('aaaabbcc'))

    def test_ThirdString(self):
        self.assertEqual('NO', sherlockValidString('aaaaabc'))

    def test_Fourthtring(self):
        self.assertEqual('NO', sherlockValidString('aabbccddeefghi'))
    
    def test_FifthString(self):
        self.assertEqual('NO', sherlockValidString('aaaabbbbddddee'))

    def test_SixthString(self):
        self.assertEqual('YES', sherlockValidString('abcdefghhgfedecba'))
    
    def test_SeventhString(self):
        self.assertEqual('YES', sherlockValidString('dcceefeecfffc'))
    
    def test_EighthString(self):
        self.assertEqual('YES', sherlockValidString('eeaaccaaeeaccbbbccbbe'))

    def test_NinthString(self):
        self.assertEqual('YES', sherlockValidString('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'))

if __name__ == '__main__':
    unittest.main()
