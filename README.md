# Reverse Edge detection
Ce projet est une implémentation d'un programme qui inverse la détection de contour sur des visages humains.

## Prérequis
Pour exécuter les scripts et le notebook de ce projet vous avez besoin de python, NumPy, Scikit-Learn, OpenCV et joblib.

## Clone du projet
```bash
git clone https://github.com/Baragouine/ReverseEdgeDetection.git
```

## Préparer les données à l'entrainement
```bash
python3 prepare_dataset.py
```

## Entrainer le modèle
Executer le notebook `fit_model.ipynb` dans google colab ou jupyter notebook.
L'entrainement prend plusieurs heures.


## Inverser la détection de contour sur des visages humain
```bash
python3 invert_edge_detection_for_face.py IMG_CONTOUR
```

avec IMG_CONTOUR l'image binaire contenant les contours dont on doit trouver l'image.
Les contours doivent être noirs et le fond blanc.

IMG_CONTOUR doit être de taille 66x81 sinon le résultat n'est pas garanti.

Ce programme ne marche que sur des contours de visage humain.

Le modèle n'a pas été entrainer sur les images de numéro pair vous pouvez donc les utiliser pour les tests (ex: input-000002.jpg).

