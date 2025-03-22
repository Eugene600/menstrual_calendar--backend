from django.db import models
from users.models import CustomUser
from cycles.models import Cycles

# Create your models here.
class SexualIntercourseLog(models.Model):
    PROTECTION_CHOICES = [
        ("protected", "Protected"),
        ("unprotected", "Unprotected"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycles, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    protection_used = models.CharField(max_length=20,choices=PROTECTION_CHOICES, default=False, null=True, blank=True)

class MoodLog(models.Model):
    MOOD_CHOICES = [
        ("happy", "Happy"), ("energized", "Energized"), ("confident", "Confident"),
        ("optimistic", "Optimistic"), ("relaxed", "Relaxed"), ("focused", "Focused"), ("sociable", "Sociable"),
        ("irritable", "Irritable"), ("anxious", "Anxious"), ("sad", "Sad"), ("depressed", "Depressed"),
        ("fatigued", "Fatigued"), ("stressed", "Stressed"), ("restless", "Restless"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycles, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES, null=True, blank=True)

class BloodFlowLog(models.Model):
    BLOOD_FLOW_CHOICES = [
        ("none", "None"), ("light", "Light"), ("spotting", "Spotting"),
        ("medium", "Medium"), ("heavy", "Heavy"), ("very_heavy", "Very Heavy"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycles, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    flow_level = models.CharField(max_length=20, choices=BLOOD_FLOW_CHOICES, null=True, blank=True)

class MedicationLog(models.Model):
    MEDICATION_CHOICES = [
        ("birth_control", "Birth Control Pills"),
        ("depo_shot", "Depo-Provera Shot"),
        ("hormone_therapy", "Hormone Therapy"),
        ("fertility_drugs", "Fertility Drugs"),
        ("pain_relief", "Pain Relief (e.g., Ibuprofen)"),
        ("pcos_medication", "PCOS Medication"),
        ("thyroid_medication", "Thyroid Medication"),
        ("antidepressants", "Antidepressants"),
        ("antibiotics", "Antibiotics"),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycles, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    medication = models.CharField(max_length=100, choices=MEDICATION_CHOICES, null=True, blank=True)

class SymptomLog(models.Model):
    SYMPTOM_CHOICES = [
        ("cramps", "Cramps"), ("low_energy", "Low Energy"), ("mood_swings", "Mood Swings"),
        ("increased_energy", "Increased Energy"), ("clearer_skin", "Clearer Skin"),
        ("clear_cervical_mucus", "Clear Cervical Mucus"),
        ("egg_white_cervical_mucus", "Egg White Cervical Mucus"),
        ("increased_libido", "Increased Libido"), ("bbt_rise", "Basal Body Temperature Rise"),
        ("cravings", "Cravings"), ("bloating", "Bloating"), ("acne", "Acne"),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycles, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    symptom = models.CharField(max_length=100, choices=SYMPTOM_CHOICES, null=True, blank=True)