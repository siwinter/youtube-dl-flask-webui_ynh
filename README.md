# Youtube-dl web interface for YunoHost

[![Integration level](https://dash.yunohost.org/integration/REPLACEBYYOURAPP.svg)](https://dash.yunohost.org/appci/app/REPLACEBYYOURAPP)  
[![Install REPLACEBYYOURAPP with YunoHost](https://install-app.yunohost.org/install-with-yunohost.png)](https://install-app.yunohost.org/?app=REPLACEBYYOURAPP)

*[Lire ce readme en français.](./README_fr.md)*

> *This package allow you to install youtube-dl-webui quickly and simply on a YunoHost server.  
If you don't have YunoHost, please see [here](https://yunohost.org/#/install) to know how to install and enjoy it.*

## Overview
This package provides a way to install a [web UI for youtube-dl](https://github.com/d0u9/youtube-dl-webui) developed by [d0u9](https://github.com/d0u9) on Yunohost. It can make the most of the yunohost.multimedia folders so that you can easily access and share the downloaded videos.

**Shipped version:** 0.2.2

## Screenshots

Screenshots from the original repo:

![Link to an screenshot for this app](https://github.com/roukydesbois/youtube-dl-webui/raw/master/screen_shot/1.gif)

## Configuration

Some parameters can be changed in the application - I recommend not to change them as I have not tested how it behaves. But hey, this is free software, you're free to try!

## Documentation

There is no documentation for the interface. Still, when you download a video, you can choose the format option for Youtube-dl. The documentation on these can be found [here](https://github.com/ytdl-org/youtube-dl#format-selection). You can use bestvideo+bestaudio/best (it's the default of youtube-dl).

## YunoHost specific features

#### Multi-users support

* No smart multi-user support - all users can use the same application.

#### Supported architectures

* x86-64b - [![Build Status](https://ci-apps.yunohost.org/ci/logs/REPLACEBYYOURAPP%20%28Apps%29.svg)](https://ci-apps.yunohost.org/ci/apps/REPLACEBYYOURAPP/)
* ARMv8-A - [![Build Status](https://ci-apps-arm.yunohost.org/ci/logs/REPLACEBYYOURAPP%20%28Apps%29.svg)](https://ci-apps-arm.yunohost.org/ci/apps/REPLACEBYYOURAPP/)

## Limitations

* Any known limitations.

## Additional information

### To do

* Handle multiple users - either by installing one app per user or handling different download paths

**More information on the documentation page:**  
https://yunohost.org/packaging_apps

## Links

 * Report a bug: https://github.com/YunoHost-Apps/REPLACEBYYOURAPP_ynh/issues
 * Upstream app repository: https://github.com/d0u9/youtube-dl-webui
 * YunoHost website: https://yunohost.org/

---

Developers info
----------------

**Only if you want to use a testing branch for coding, instead of merging directly into master.**
Please do your pull request to the [testing branch](https://github.com/YunoHost-Apps/REPLACEBYYOURAPP_ynh/tree/testing).

To try the testing branch, please proceed like that.
```
sudo yunohost app install https://github.com/YunoHost-Apps/REPLACEBYYOURAPP_ynh/tree/testing --debug
or
sudo yunohost app upgrade REPLACEBYYOURAPP -u https://github.com/YunoHost-Apps/REPLACEBYYOURAPP_ynh/tree/testing --debug
```
