import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class TestMyModule(unittest.TestCase):
    def test_f2e1(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    def test_f2e2(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    def test_f2e3(self):
        self.assertEqual(frenchToEnglish('Néant'),'None')  
    

class TestMyModule1(unittest.TestCase):
    def test_e2f1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    def test_e2f2(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    def test_e2f3(self):
        self.assertEqual(englishToFrench('None'),'Néant')  
    
unittest.main()          
        
                               