# Interface web de Youtube-dl pour YunoHost

[![Niveau d'intégration](https://dash.yunohost.org/integration/REPLACEBYYOURAPP.svg)](https://dash.yunohost.org/appci/app/REPLACEBYYOURAPP)  
[![Installer REPLACEBYYOURAPP avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.png)](https://install-app.yunohost.org/?app=REPLACEBYYOURAPP)

*[Read this readme in english.](./README.md)* 

> *Ce package vous permet d'installer youtube-dl-webui rapidement et simplement sur un serveur Yunohost.  
Si vous n'avez pas YunoHost, regardez [ici](https://yunohost.org/#/install) pour savoir comment l'installer et en profiter.*

## Vue d'ensemble
Ce package vous permet d'installer [une interface web de youtube-dl](https://github.com/d0u9/youtube-dl-webui) développée par [d0u9](https://github.com/d0u9) sur Yunohost. Il peut utiliser les dossiers yunohost.multimedia pour facilement accéder et partager les vidéos téléchargées.

**Version incluse:** 0.2.2

## Captures d'écran

![Lien vers une capture d'écran pour cette application](https://github.com/roukydesbois/youtube-dl-webui/raw/master/screen_shot/1.gif)

## Configuration

Quelques paramètres de l'application peuvent être modifiés depuis l'interface - je vous recommande de ne pas le faire étant donné que je n'ai pas testé ces cas d'usages. Mais bon, c'est un logiciel libre, donc vous faites ce que vous voulez :)

## Documentation

Il n'y a pas de documentation pour l'interface en elle-même. Cependant, à l'ajout d'une vidéo, vous pouvez choisir le format à passer à Youtube-dl. La documentation de ces formats peut être trouvée [ici](https://github.com/ytdl-org/youtube-dl#format-selection) (en anglais). Vous pouvez utiliser bestvideo+bestaudio/best (c'est la valeur par défaut de Youtube-dl).

## Caractéristiques spécifiques YunoHost

#### Support multi-utilisateurs

* L'application ne fonctionne pas différemment pour les différents utilisateurs, ils utilisent tous la même.

#### Architectures supportées

* x86-64b - [![Build Status](https://ci-apps.yunohost.org/ci/logs/REPLACEBYYOURAPP%20%28Apps%29.svg)](https://ci-apps.yunohost.org/ci/apps/REPLACEBYYOURAPP/)
* ARMv8-A - [![Build Status](https://ci-apps-arm.yunohost.org/ci/logs/REPLACEBYYOURAPP%20%28Apps%29.svg)](https://ci-apps-arm.yunohost.org/ci/apps/REPLACEBYYOURAPP/)
* Jessie x86-64b - [![Build Status](https://ci-stretch.nohost.me/ci/logs/REPLACEBYYOURAPP%20%28Apps%29.svg)](https://ci-stretch.nohost.me/ci/apps/REPLACEBYYOURAPP/)

## Limitations

* Pour l'instant les vidéos ne peuvent être supprimées que via l'interface, ou avec des droits root.

## Informations additionnelles

Une tâche cron met à jour youtube-dl chaque nuit.

### A faire

* Mieux gérer les utilisateurs multiples - soit en installant une application par utilisateur, soit en gérant des dossiers de téléchargement différents.

**Plus d'informations sur la page de documentation:**  
https://yunohost.org/packaging_apps

## Liens

 * Signaler un bug: https://github.com/YunoHost-Apps/REPLACEBYYOURAPP_ynh/issues
 * Dépôt de l'application principale: https://github.com/d0u9/youtube-dl-webui
 * Site web YunoHost: https://yunohost.org/

---

Informations pour les développeurs
----------------

**Seulement si vous voulez utiliser une branche de test pour le codage, au lieu de fusionner directement dans la banche principale.**
Merci de faire vos pull request sur la [branche testing](https://github.com/YunoHost-Apps/REPLACEBYYOURAPP_ynh/tree/testing).

Pour essayer la branche testing, procédez comme suit.
```
sudo yunohost app install https://github.com/YunoHost-Apps/REPLACEBYYOURAPP_ynh/tree/testing --debug
ou
sudo yunohost app upgrade REPLACEBYYOURAPP -u https://github.com/YunoHost-Apps/REPLACEBYYOURAPP_ynh/tree/testing --debug
```
