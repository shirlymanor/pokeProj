# Pockemon SDK
SDK For Pockemon API

<div align="center">
<img src="https://github.com/Pockemon/Pockemon-SDK/blob/main/Pockemon.png" width="200" height="200">
</div>

## Installation

```bash
npm install pokeclient
``` 
## Usage
```js
const { Pockemon } = require('pokeclient');

    const pockemon = new Pockemon();
    pockemon.getPockemon('pikachu').then(data => console.log(data));
    ```
    
    
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

    ## Library Dependencies
    - [requests](https://pypi.org/project/requests/)
    - [axios
    ](https://www.npmjs.com/package/axios)
    - [docstrings](https://www.python.org/dev/peps/pep-0257/)
    
    ## Run the app
    ```bash
    streamlit run pokemon_app.py 
    ```
    
   