const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');

const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Database setup
const db = new sqlite3.Database('users.db', (err) => {
    if (err) {
        console.error('Error connecting to the database:', err);
    } else {
        console.log('Connected to the SQLite database');
        // Create users table
        db.run(`
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                age INTEGER,
                role TEXT DEFAULT 'user'
            )
        `);
    }
});

// GET all users
app.get('/api/users', (req, res) => {
    db.all('SELECT * FROM users', [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json(rows);
    });
});

// GET user by ID
app.get('/api/users/:id', (req, res) => {
    db.get('SELECT * FROM users WHERE id = ?', [req.params.id], (err, row) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        if (!row) {
            res.status(404).json({ error: 'User not found' });
            return;
        }
        res.json(row);
    });
});

// CREATE new user
app.post('/api/users', (req, res) => {
    const { username, email, age, role } = req.body;
    if (!username || !email) {
        res.status(400).json({ error: 'Username and email are required' });
        return;
    }

    db.run(
        'INSERT INTO users (username, email, age, role) VALUES (?, ?, ?, ?)',
        [username, email, age, role || 'user'],
        function (err) {
            if (err) {
                res.status(500).json({ error: err.message });
                return;
            }
            res.status(201).json({
                id: this.lastID,
                username,
                email,
                age,
                role: role || 'user'
            });
        }
    );
});

// UPDATE user
app.put('/api/users/:id', (req, res) => {
    const { username, email, age, role } = req.body;
    db.run(
        'UPDATE users SET username = ?, email = ?, age = ?, role = ? WHERE id = ?',
        [username, email, age, role, req.params.id],
        function (err) {
            if (err) {
                res.status(500).json({ error: err.message });
                return;
            }
            if (this.changes === 0) {
                res.status(404).json({ error: 'User not found' });
                return;
            }
            res.json({ id: req.params.id, username, email, age, role });
        }
    );
});

// DELETE user
app.delete('/api/users/:id', (req, res) => {
    db.run('DELETE FROM users WHERE id = ?', [req.params.id], function (err) {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        if (this.changes === 0) {
            res.status(404).json({ error: 'User not found' });
            return;
        }
        res.json({ message: 'User deleted successfully' });
    });
});

// Add health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'healthy' });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
}); 