
# Sim-Dis (Simple Discord-like Web App in Django)

A simple web application built using Django that mimics some basic features of Discord.

## Features
- User authentication (Login, Signup)
- Real-time chat functionality
- Channels and messaging
- User profiles
- Dark theme similar to Discord

## Installation

Follow these steps to set up the project on your local machine:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/sim-dis.git
    cd sim-dis
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Create an account or log in to start using the chat.

## Contributing

Feel free to submit a pull request. All contributions are welcome.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Submit a pull request.

## License

This is free and unencumbered software released into the public domain.
