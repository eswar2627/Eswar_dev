# Eswar_dev – Django Portfolio Website

A production-ready **personal portfolio website** built with **Django** to showcase projects, skills, and contact information. The project follows modern deployment best practices, including **secure environment variable management**, **Cloudinary-based media storage**, and **Railway-ready configuration**.

---

## ✨ Features

* Dynamic project showcase with multiple screenshots per project
* Admin-managed content (projects, images, skills, contact messages)
* Responsive UI suitable for desktop and mobile
* Secure handling of secrets using environment variables
* Cloud-based media storage (no local media dependency)
* Deployment-ready for Railway (or similar platforms)

---

## 🛠 Tech Stack

**Backend**

* Python
* Django (4.2+ compatible)

**Frontend**

* HTML5
* CSS3
* JavaScript

**Media & Storage**

* Cloudinary (via `django-cloudinary-storage`)

**Deployment**

* Railway
* Gunicorn
* WhiteNoise (static files)

---

## 📁 Project Structure

```
Eswar_dev/
│
├── Eswar_dev/          # Django project settings
├── core/               # Main application (projects, images, views)
├── staticfiles/        # Collected static files (production)
├── manage.py
├── requirements.txt
├── Procfile
└── .gitignore
```

---

## 🔐 Security & Best Practices

* **No secrets committed to GitHub**
* Environment variables used for:

  * `SECRET_KEY`
  * `DEBUG`
  * `ALLOWED_HOSTS`
  * Cloudinary credentials
* Database files and virtual environments excluded via `.gitignore`
* Media files served securely from Cloudinary

---

## ⚙️ Environment Variables

Create a `.env` file locally (do **not** commit it):

```env
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

---

## ▶️ Run Locally

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

---

## 🚀 Deployment (Railway)

1. Push code to GitHub (no `.env`, no database)
2. Create a new Railway project → **Deploy from GitHub**
3. Add environment variables in Railway dashboard
4. Railway will automatically:

   * Install dependencies
   * Collect static files
   * Start Gunicorn

Media files are served directly from **Cloudinary**.

---

## 📸 Media Handling

* Uses Django 4.2+ `STORAGES` setting
* All uploaded images are stored on Cloudinary
* No reliance on local `/media` in production

---

## 📄 License

This project is for **personal and portfolio use**.

---

<img width="1920" height="955" alt="INTERFACE" src="https://github.com/user-attachments/assets/02e55b89-037a-4375-80e2-4671d7e71ce2" />
<img width="1920" height="804" alt="WHAT I DO" src="https://github.com/user-attachments/assets/03861268-3e62-4f4e-a7f9-75a18e84ca9a" />
<img width="1920" height="652" alt="SKILLS" src="https://github.com/user-attachments/assets/b6bc5374-70a2-4d0e-9fdc-c943748d76b2" />
<img width="1920" height="951" alt="MY PROJECTS" src="https://github.com/user-attachments/assets/83ca452c-e73d-4210-99f0-be6d5acef002" />
<img width="1920" height="950" alt="PRIME STORE" src="https://github.com/user-attachments/assets/53e3341c-a988-44fe-851a-085b40c8b142" />
<img width="1920" height="944" alt="PRIME STORE SS" src="https://github.com/user-attachments/assets/66b3eb5d-a7e7-488d-958c-cc37e3a46f30" />
<img width="1920" height="918" alt="FOODPLAZA" src="https://github.com/user-attachments/assets/3e67f38f-6d22-41a0-9d8e-aaa5efe12d17" />
<img width="1920" height="927" alt="FOODPLAZA SS" src="https://github.com/user-attachments/assets/d532cc65-5088-4162-88cc-d9575411aee9" />
<img width="1881" height="943" alt="CONTACT ME" src="https://github.com/user-attachments/assets/60984c4c-8f1b-4566-bf8a-2348a7dc678d" />



## 👤 Author

**Eswar Maguluri**
Django / Python Developer

GitHub: [https://github.com/eswar2627](https://github.com/eswar2627)

---

If you are a recruiter or developer reviewing this repository:

This project demonstrates **production-correct Django practices**, secure deployments, and real-world media handling.



