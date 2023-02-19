# Mountain Madness Hackathon 2023 - Rubey on Tails

This web app generates funny pet names for all kinds of animals, using the OpenAI API through Natural Language Processing. It makes additional GET requests to another API (node-server), which makes GET requests to another API (french-translator-server) which takes in the AI generated pet name and translates it to a newly invented language, known as French++.

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

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! 

Now we need to setup our backend servers for the app to work:

7. Run Node Server
https://github.com/dannyl1u/node-server

8. Run French translater Server
https://github.com/dannyl1u/french-translator-server

Generate your pet name!
