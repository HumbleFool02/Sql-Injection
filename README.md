
# SQL Injection CTF Challenge

Welcome to a beginner-friendly **Capture The Flag (CTF)** challenge designed to teach you the basics of **SQL Injection** and **role-based access control** vulnerabilities using a real-world inspired scenario.

---

## Challenge Description

This challenge is a Flask-based web application with:

- A **vulnerable login page** prone to SQL Injection
- A **hidden route** hinted via HTML source code
- **Role-based flag access** — normal users get blocked, admin users get the flag

Your goal is to:
1. Bypass login using SQL Injection
2. Discover and access the `/profile` route
3. Escalate privileges to retrieve the flag

---

## How to Run the Challenge

### Option 1: Run Locally (Using Python)

> Requires: Python 3.x

1. Clone this repository:

```bash
git clone git@github.com:HumbleFool02/Sql-Injection.git
cd Sql-Injection
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Initialize the database:

```bash
python init_db.py
```

4. Run the app:

```bash
python app.py
```

5. Visit the challenge at:

```
http://localhost:5000
```

---

### Option 2: Run via Docker (Recommended)

> Docker Desktop must be installed on your system.

You can **pull and run the pre-built Docker image** from Docker Hub:

```bash
docker pull humblefool07/ctf_sql
docker run -p 5000:5000 humblefool07/ctf_sql
```

Then visit:

```
http://localhost:5000
```

---

## Objective: How to Solve

1. Use SQL Injection on the login page:
   ```
   ' OR '1' --
   ```

2. View the page source for a hidden hint:
   ```html
   <!-- Secure /profile route, it might expose sensitive flags -->
   ```

3. Visit `/profile` route:
   - If logged in as **user** → rejection
   - If logged in as **admin** → flag is revealed

---

## 🏁 Flag Format

```
flag{CTF_is_awesome}
```

---

## Created By

**Piyush (humblefool07)**  
Feel free to try out the challenge

---


