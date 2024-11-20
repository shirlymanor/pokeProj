# Pockemon SDK
SDK For Pockemon API

<div align="center">
<img src="https://res.cloudinary.com/rh-demo/image/upload/w_400/og-default-image_wiaczn.jpg" width="400" height="400">
</div>

## Installation

To install the Pockemon SDK, run the following command:

```bash
npm install pokeclient
``` 
## Usage
Here's a basic example of how to use the Pockemon SDK:

```js
const { Pockemon } = require('pokeclient');

    const pockemon = new Pockemon();
    pockemon.getPockemon('pikachu').then(data => console.log(data));
    ```
Bonus points for python :)
    
    ```python
    from pokeclient import Pockemon

    pockemon = Pockemon()
    pockemon.get_pockemon('pikachu')
    ```

## Test

    To run the tests, run the following command:
    ```bash
    npm run test
    ```

    To run the tests, run the following command:
    ```bash
    python -m unittest
    ``` 

    ## Design Decisions and Tools
    - [requests](https://pypi.org/project/requests/) / [axios](https://www.npmjs.com/package/axios) - I choose axios because it's a popular library for making HTTP requests in JavaScript. I also chose requests because it's a popular library for making HTTP requests and response back in Python.
    - [streamlit](https://streamlit.io/) - I used streamlit because it's my favorite library for building web applications in Python.

    - [docstrings](https://www.python.org/dev/peps/pep-0257/)
    
    ## Run the app
    ```bash
    streamlit run src/pokemon_app.py 
    ```
    
    ## Run the app
    ```bash
    python3 -m streamlit run src/pokemon_app.py 
    ```
    
   