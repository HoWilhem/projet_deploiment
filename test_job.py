# test_job.py
from job import moyenne

def test_moyenne_correcte():
    assert moyenne([1, 2, 3, 4, 5]) == 3

def test_moyenne_liste_vide():
    assert moyenne([]) == 0
