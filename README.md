# meditation
A simple meditation guide and recommender chatbot (practive engine chat) based on Culadasa's The Mind Illuminated.

Using mongoose/mlab for the practice engine chat.
This chat example showcases how to use `socket.io` with a static `express` server. 

Once that's done --
Try creating a Flask version in Python to deliver recommender content using NLP.

Debugging: 

DEALING WITH CORS:
Launch using Firefox (NOT CHROME) and make sure js scripts include [ crossorigin="anonymous" ]
as in <script src="https://stackoverflow.com/foo.js" crossorigin="anonymous">
    
Make sure socket.io, express, body-parser and mongoose are all installed on this same directory!

Read error messages (deprecation) and add "http://" in the socket.io scipt references EG 

<script src="http://localhost:3000/socket.io/socket.io.js"></script>

and 

function getMessages(){
        $.get('http://localhost:3000/messages' <<
    
## Running the server (instructions for c9... On own mac, just cd to directory then run Step 2.)

1) Open `server.js` and start the app by clicking on the "Run" button in the top menu.

2) Alternatively you can launch the app from the Terminal:

    $ node server.js
    or
    $ nodemon server.js 

Once the server is running, open the project in the shape of 'https://projectname-username.c9users.io/' (or localhost:3000 for mac). As you enter your name, watch the Users list (on the left) update. Once you press Enter or Send, the message is shared with all connected clients.


https://ide.c9.io/eagarcia/todolist