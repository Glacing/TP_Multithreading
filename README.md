# Rapport de Performance des Tâches

Ce document présente les résultats des tâches exécutées en C++ et Python, ainsi que les temps moyens pour chaque ensemble de tâches traitant de matrices de taille 1000.

## Résultats Moyens

| Algorithme                | Tâches                          | Temps Moyen (en secondes) |
|---------------------------|----------------------------------|---------------------------|
| **C++ - colPivHouseholderQr** | Task 1 à Task 4                 | **0.1869**                |
| **C++ - ldlt**               | Task 1 à Task 4                 | **0.0444**                |
| **C++ - llt**                | Task 2 à Task 5                 | **0.0059**                |
| **Python - Minion-1**        | Task 1 à Task 4                 | **0.0261**                |

## Détails des Tâches

### C++ - colPivHouseholderQr

Les tâches suivantes ont été exécutées avec l'algorithme `colPivHouseholderQr` :

- **Task 1** réalisée en **0.1892 secondes**
- **Task 2** réalisée en **0.1789 secondes**
- **Task 3** réalisée en **0.1881 secondes**
- **Task 4** réalisée en **0.1893 secondes**

### C++ - ldlt

Les tâches suivantes ont été exécutées avec l'algorithme `ldlt` :

- **Task 1** réalisée en **0.0459 secondes**
- **Task 2** réalisée en **0.0420 secondes**
- **Task 3** réalisée en **0.0429 secondes**
- **Task 4** réalisée en **0.0449 secondes**

### C++ - llt

Les tâches suivantes ont été exécutées avec l'algorithme `llt` :

- **Task 2** réalisée en **0.0026 secondes**
- **Task 3** réalisée en **0.0031 secondes**
- **Task 4** réalisée en **0.0044 secondes**
- **Task 5** réalisée en **0.0126 secondes**

### Python - Minion-1

Les tâches suivantes ont été exécutées avec le module Python **Minion-1** :

- **Task 1** réalisée en **0.0415 secondes**
- **Task 2** réalisée en **0.0220 secondes**
- **Task 3** réalisée en **0.0198 secondes**
- **Task 4** réalisée en **0.0212 secondes**

---

## Conclusion

Les résultats montrent une différence significative dans les temps d'exécution entre les algorithmes C++ et Python. L'algorithme LLT en C++ offrent de bien meilleures performances que ceux en python, mais contrairement à ce qui avait pu être attendu le python peut parfois être plus rapide que le c++, notamment grâce à l'utilisation du module numpy.
