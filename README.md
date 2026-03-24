# RecipeBook – Test-Driven Development (TDD)

Select Language: [English](#-english) | [Deutsch](#-deutsch)

---

## 🇬🇧 English

This project is a recipe management backend built using **Test-Driven Development (TDD)** principles. It utilizes Django and Django REST Framework (DRF) with a focus on automated integration testing.

### 🚀 Features
- **Recipe CRUD:** Create and list recipes via REST API.
- **TDD Approach:** All endpoints are covered by integration tests (Happy & Unhappy Paths).
- **Security:** Access is protected via `TokenAuthentication` and `IsAuthenticated` permissions.
- **Clean Architecture:** API logic is isolated within a dedicated `api/` sub-package.

### 🛠 Tech Stack
- **Framework:** Django 5.x / Django REST Framework
- **Testing:** Pytest, Pytest-Django
- **Coverage:** Pytest-Cov
- **Environment:** Python-Dotenv for `.env` management

### 📋 Setup & Installation

1.  **Clone and Navigate**:
```bash
    git clone <your-repository-url>
    cd <project-folder>
```

2.  **Environment Setup**:
```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
```

3.  **Install Dependencies**:
```bash
    pip install -r requirements.txt
```

4. **Environment Variables**:
Create your local environment file by copying the template:
```bash
   cp .env.template .env
```
Open the new .env file and add your SECRET_KEY.
(Note: You can generate a secure key using in your terminal.)
```bash
     python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())" 
```

5. **Run Migrations & Tests:**
```bash
    python manage.py migrate
    pytest --cov=.
```

---

## 🇩🇪 Deutsch

Dieses Projekt ist ein Rezeptbuch-Backend, das nach den Prinzipien der testgetriebenen Entwicklung (TDD) erstellt wurde. Es nutzt Django und das Django REST Framework (DRF) mit einem klaren Fokus auf automatisierte Integrationstests.

### 🚀 Features
- **Rezept-CRUD**: Erstellen und Auflisten von Rezepten über eine REST-API.
- **TDD-Ansatz:** Alle Endpunkte sind durch Integrationstests abgesichert (Happy & Unhappy Paths).
- **Sicherheit:** Zugriffsschutz durch TokenAuthentication und IsAuthenticated-Berechtigungen.
- **Clean Architecture:** Die API-Logik ist in einem eigenen api/-Unterordner isoliert.

### 🛠 Tech Stack
- **Framework:** Django 5.x / Django REST Framework
- **Testing:** Pytest, Pytest-Django
- **Abdeckung:** Pytest-Cov
- **Umgebung:** Python-Dotenv für das .env-Management

### 📋 Setup & Installation

1. **Klonen und Navigieren:**
```bash
    git clone <deine-repository-url>
    cd <projekt-ordner>
```

2. **Umgebung einrichten:**
```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
```

3. **Abhängigkeiten installieren:**
```bash
    pip install -r requirements.txt
```

4. **Umgebungsvariablen:**
Erstelle deine lokale Umgebungsdatei, indem du die Vorlage kopierst:
```bash
   cp .env.template .env
```
Öffne die neue .env-Datei und füge deinen SECRET_KEY hinzu.
(Hinweis: Du kannst einen sicheren Schlüssel direkt über dein Terminal generieren.)
```bash
     python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())" 
```

5. **Migrationen & Tests ausführen:**
```bash
    python manage.py migrate
    pytest --cov=.
```
