
# Culture Time

**Enhance your knowledge every day!**  
Culture Time is a web application designed to improve your English language skills and broaden your cultural knowledge. 
It provides daily questions, fun facts, and insights into British culture, making learning both fun and engaging.

---

## Features

- **Daily Question:** A new question every day with explanations and sources to dive deeper into the topic.
- **Explore Records:** Browse through past questions and categories to revisit topics of interest.
- **Categories and Search:** Organize content into topics with a search feature for easy navigation.
- **User Interaction:** Users can register, sign in, and participate in daily questions.
- **Admin Functionality:** Administrators can add new questions, manage categories, and enrich the database.

---

## Project Structure

```
.
├── cultureTime.py         # Main Flask application file
├── functions.py           # Backend functions for database interaction
├── data/                  # Database and related files
├── flask_session/         # Flask session data
├── static/                # Static files (CSS, JS, images)
├── templates/             # HTML templates for web pages
└── README.md              # Project documentation
```

---

## Prerequisites

Make sure you have Python 3.6+ and Flask installed. Create and activate a virtual environment for the project:

```bash
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment (Linux/Mac)
source env/bin/activate

# Activate the virtual environment (Windows)
env\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

---

## Running the Application

1. Ensure the database is properly set up:
   - If necessary, initialize the database by running:
     ```python
     from functions import initdb, init_data
     initdb()
     init_data()
     ```

2. Start the Flask server:
   ```bash
   export FLASK_APP=cultureTime.py  # For Linux/Mac
   set FLASK_APP=cultureTime.py     # For Windows
   flask run
   ```

3. Access the application at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## How to Use

### User Features:
- Visit the homepage to view the **Daily Question**.
- Participate in quizzes and explore detailed explanations.
- Browse past questions in the **Records** section, filtered by categories.

### Admin Features:
- Add new questions and categories to the database.
- Manage the database to ensure content quality.

---

## Example

### Daily Question Page
Here’s an example of how a daily question appears on the website:

- **Question:** What is the capital of England?  
- **Options:** London | Manchester  
- **Explanation:** London is the capital and largest city of England and the United Kingdom.

---

## Contributing

Feel free to contribute to this project by creating pull requests or reporting issues. For major changes, please discuss them with the project maintainers beforehand.

---

## Authors

- **Thomas Jeanjacquot** - Frontend and Flask setup.
- **Amandine Lapique-Favre** - Database design and content management.

---

