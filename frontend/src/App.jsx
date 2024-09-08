import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App(){
    const [data, setData] = useState({"isValid": false, "validator": false});

    useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await axios.get("http://localhost:5000/api/data");
            setData(response.data);
            console.log(response.data);
          } catch (error) {
            console.error('There was an error fetching the data!', error);
          }
        };
    
        fetchData();
      }, []);

      const validStyle = {
        color: data.isValid ? 'green' : 'red',
        fontSize: '24px',
        textAlign: 'center',
        display: data.validator ? 'block' : 'none'
      };

    return (
        <div id="container">
            <form action="/check" method="POST">
                <h2 id="checker" style={validStyle}>{data.isValid ? "This card is valid" : "This card is not valid"}</h2>
                <label >Check if a card number is valid</label>
                <br />
                <input type="text" name="ccnumber"/>
                <br />
                <button type="submit">Check</button>
                </form>
        </div>
    )
}

export default App;