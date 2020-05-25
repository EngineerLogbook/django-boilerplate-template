+++
title = "Hey There !"
date = "2020-05-24"
author = "Vividh Mariya"
description = "This repository can be used a boilerplate for most django projects out there. It does most of the tedious and repetitive setup process for you, leaving you free to code !"
+++

### Features

- In built User app, with login / register / password reset views
- Custom `settings.py` files for debug and production environments.
- Custom manage.py command to rename your project automatically
- Includes the debug toolbar for reviewing request metadata, sql queries etc.

---

### Deployment

Also, you don't need to worry about unittesting or deployment, everything is built-in !
We all know how hard is to start something on the web, especially these days. You need to prepare a bunch of stuff, configure them and when that’s done — create the content.
\
\
\
Just run this in a terminal

```bash
sudo docker compose up --build
```

Docker will automatically switch to using the PostgreSQL Database, relying on gunicorn and nginx for serving your website to the web. Just go to http://*yourip* to see the site in action !

Assuming you're using github to manage your code, this also has an inbuilt workflow file, for unit testing and deployment.

So there you have it, we have the essentials covered, all you have to do is start typing !
