

# Projet de Classification d'Images pour la Détection de Pneumonie

Ce projet vous permet de déployer un modèle de classification d'images pour la détection de la pneumonie à l'aide de Flask et de tester le modèle avec des images.

## Compilation du Code

Pour exécuter l'application Flask, suivez ces étapes :

1. Assurez-vous d'avoir installé les bibliothèques nécessaires. Si elles ne sont pas déjà installées, vous pouvez les installer en utilisant `pip` :

   ```bash
   pip install flask tensorflow pillow
   ```

2. Compilez le code en exécutant `app.py` :

   ```bash
   python app.py
   ```

3. L'application Flask sera en cours d'exécution et écoutera sur l'adresse `http://127.0.0.1:5000`. Vous pouvez maintenant tester le modèle en utilisant la commande `curl`.

## Test de l'API avec Curl

Pour tester le modèle avec une image, vous pouvez utiliser la commande `curl`. Voici comment faire :

```bash
curl -X POST -F "file=@/chemin/vers/votre/image.jpg" http://127.0.0.1:5000/predict
```

Assurez-vous de remplacer `/chemin/vers/votre/image.jpg` par le chemin absolu de l'image que vous souhaitez utiliser pour le test. Le modèle renverra une réponse JSON indiquant la prédiction.