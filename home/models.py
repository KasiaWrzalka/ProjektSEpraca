from django.db import models

# Create your models here.

class Tests(models.Model): #Testy np. MBTI
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Questions(models.Model): #Pytania do testów
    title = models.CharField(max_length=500)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE) #test_id

    def __str__(self):
        return self.title

class Factors(models.Model): #Czynniki
    title = models.CharField(max_length=100)
    letter = models.CharField(max_length=1)
    description = models.CharField(max_length=500)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE) #test_id

    def __str__(self):
        return self.title

class Answers(models.Model): #odpowiedzi do pytań
    value = models.CharField(max_length=100)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE) #question_id

    def __str__(self):
        return self.value

class AnswersFactors(models.Model):
    impact = models.IntegerField()
    factor = models.ForeignKey(Factors, on_delete=models.CASCADE) # factor_id
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)  # question_id

    def __int__(self):
        return self.impact

class Results(models.Model): #wyniki testu
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)  # test_id

    def __str__(self):
        return self.title

class Conditions(models.Model):
    sign = models.CharField(max_length=1)
    value = models.IntegerField()
    factor = models.ForeignKey(Factors, on_delete=models.CASCADE)  # factor_id
    result = models.ForeignKey(Results, on_delete=models.CASCADE)  # result_id

class Jobs(models.Model):
    name = models.CharField(max_length=100)
    result_title = models.CharField(max_length=100)
    # ("Niezależność": "autonomia", "Atmosfera i kontaty społeczne": "atmosfera",
    #  "Kierowanie innymi": "kierowanie", "Dobre warunki finansowe": "finanse",
    #  "Jasne cele i zadania": "zadania", "Urozmaicenie": "urozmaicenie",
    #  "Produktywność i wyzwania": "wyzwania", "Uznanie, pochwały": "uznanie",
    #  "Rozwój osobisty": "rozwoj", "Niski poziom stresu": "stres")
    autonomia = models.IntegerField()
    atmosfera = models.IntegerField()
    kierowanie = models.IntegerField()
    finanse = models.IntegerField()
    zadania = models.IntegerField()
    urozmaicenie = models.IntegerField()
    wyzwania = models.IntegerField()
    uznanie = models.IntegerField()
    rozwoj = models.IntegerField()
    stres = models.IntegerField()

class ResultsJobs(models.Model):
    result = models.ForeignKey(Results, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)