# Project setup
1. Download and install [Docker](https://www.docker.com/products/docker-desktop/)
2. Open **Terminal** in project directory
3. Run command ```docker-compose up```
4. Run command `python manage.py migrate` in web container terminal
5. Done!

---

Project contains auto generated Swagger doc, but it contains error in `POST /products/users/` endpoint ( it is available for unauthenticated users ). 

---

Custom command for populating DB is `python manage.py populate_db`

---