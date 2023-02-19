# Mountain Madness Hackathon 2023 - Rubey on Tails

This web app generates funny pet names for all kinds of animals, making POST requests to the OpenAI API that generates a pet name using Natural Language Processing. It makes additional GET requests to another API (node-server), which makes GET requests to another API (french-translator-server) which takes in the AI generated pet name and translates it to a newly invented language, known as French++. 

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository


3. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

4. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

5. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

6. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

7. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)

## Now we need to setup our backend servers for the app to work:

8. Node Server
https://github.com/dannyl1u/node-server

1. Clone the repo. 

   ```bash
   $ git clone https://github.com/dannyl1u/node-api.git
   ```

2. Navigate into the project directory

   ```bash
   $ cd node-api
   ```

3. run npm install

   ```bash
   $ npm install
   ```

4. Run the server

   ```bash
   $ node .
   ```

Server should now be up at [http://localhost:8080](http://localhost:8080)

9. French translater Server
https://github.com/dannyl1u/french-translator-server
1. Ensure python is installed.

   ```bash
   $ python --version
   ```
2. Install flask

   ```bash
   $ pip install Flask
   # we might need to replace pip with pip3
   # this also requires that pip is installed
   $ pip --version
   ```

3. Run the server

   ```bash
   $ python api.py
   ```
   
4. Run the server

   ```bash
   $ python api.py
   ```
   
Server should now be up at [http://localhost:8000](http://localhost:8000)

10. All done. Generate your pet name!
