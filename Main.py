# PLYDOIR 3 - AI Cold Chain System for Rural Cameroon
# Author: Arthur - 19/20 in Computer Science
# Purpose: Protect vaccines by predicting ice shortage

import random
from datetime import datetime

print("=== PLYDOIR 3 - AI Cold Chain System ===")
print("Project for Open Doors - Informatics and Data Science")
print(f"Date: {datetime.now().strftime('%d/%m/%2025')}\n")

temperatures = [random.randint(28, 42) for _ in range(7)]
ice_stock = 15

print(f"Températures 7 derniers jours: {temperatures} °C")
print(f"Stock actuel de glace: {ice_stock} kg")

moyenne_temp = sum(temperatures) / len(temperatures)
print(f"\nTempérature moyenne: {moyenne_temp:.1f}°C")

consommation_predite = moyenne_temp * 0.8
jours_restants = ice_stock / consommation_predite if consommation_predite > 0 else 0

print(f"Consommation IA prédite: {consommation_predite:.1f} kg/jour")
print(f"Jours avant rupture: {jours_restants:.1f} jours")

print("\n--- DIAGNOSTIC IA ---")
if jours_restants < 2:
    print("🚨 ALERTE ROUGE: Rupture imminente !")
    print("Risque: Vaccins et médicaments vont périr.")
    print("Action: Envoyer SMS au chef du village pour ravitailler 50kg.")
    status = "CRITICAL"
elif jours_restants < 5:
    print("⚠️ ALERTE ORANGE: Stock faible.")
    print("Action: Prévoir ravitaillement.")
    status = "WARNING"
else:
    print("✅ OK: Stock sécurisé pour les vaccins.")
    status = "OK"

print(f"\n--- Rapport Data Science ---")
print(f"Total data points analysés: {len(temperatures)}")
print(f"Status du Cold Chain: {status}")
print(f"Impact: Protection de ~200 vaccins infantiles")
print("\n19/20 en Info - Arthur - Cameroun")
