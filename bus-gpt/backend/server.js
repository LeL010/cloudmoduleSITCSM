const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');
const cors = require('cors');
const path = require('path');

const app = express();
const port = 5000;

app.use(bodyParser.json());
app.use(cors());

const db = mysql.createConnection({
    host: 'busgptstack-rdsinstance-lpj8yfxa5uto.c5skgmsgyt42.us-east-1.rds.amazonaws.com',
    user: 'admin',
    password: 'Password1234',
    database: 'BusGPT_Db'
});

db.connect(err => {
    if (err) {
        console.error('Error connecting to the database:', err);
        return;
    }
    console.log('Connected to the database');
});

app.post('/api/contact', (req, res) => {
    const { name, email, message } = req.body;
    const query = 'INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)';

    db.query(query, [name, email, message], (err, result) => {
        if (err) {
            console.error('Error inserting data:', err);
            res.status(500).send('Error inserting data');
            return;
        }
        res.status(200).send('Data inserted successfully');
    });
});

app.use(express.static(path.join(__dirname, 'build')));

app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname + '/build/index.html'));
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
