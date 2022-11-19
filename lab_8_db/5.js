const express = require("express");

const app = express();

const urlencodedParser = express.urlencoded({extended: false});

const MongoClient = require("mongodb").MongoClient;

const url = "mongodb://localhost:27017/";
const mongoClient = new MongoClient(url, { useUnifiedTopology: true });

app.get("/", function (request, response) {
    response.sendFile(__dirname + "/index5.html");
});

app.post("/artickes", urlencodedParser, function (request, response) {
    mongoClient.connect(function(err, client){

        const db = client.db("articledb");
        const collection = db.collection("articles");

        if(err) return console.log(err);

        collection.aggregate([{$project: {_id: 1, title: 1, autor: 1, date_of_public: 1}}])
            .toArray(function(err, results){
                let a = "";
                for(let i = 0; i < results.length; i++){
                    a = a + "<p>" + "номер: " + results[i]._id + ", " + "название: " + results[i].title + ", " + "автор: " + results[i].autor + ", " + "дата публикации: " + results[i].date_of_public + "</p>"
                }
                response.send(a);
                client.close();
            });
    });
});

app.post("/artickes4", urlencodedParser, function (request, response) {
    mongoClient.connect(function(err, client){

        const db = client.db("articledb");
        const collection = db.collection("articles");
        let b = request.body.text;

        let reg = ".*" + b + ".*";

        if(err) return console.log(err);

        collection.find({
            title: {
                $regex: reg,
                $options: 'i'
            }
        })
            .toArray(function(err, results){
                console.log(results)
                let a = "";
                for(let i = 0; i < results.length; i++){
                    a = a + "<p>" + "номер: " + results[i]._id + ", " + "название: " + results[i].title + ", " + "автор: " + results[i].autor + ", " + "дата публикации: " + results[i].date_of_public + "</p>"
                }
                response.send(a);
                client.close();
            });
    });
});

app.post("/artickes5", urlencodedParser, function (request, response) {
    mongoClient.connect(function(err, client){

        const db = client.db("articledb");
        const collection = db.collection("articles");

        let b = request.body.aut;
        console.log(b);

        if(err) return console.log(err);

        collection.find({autor: b}).toArray(function(err, results){
                console.log(results)
                let a = "";
                for(let i = 0; i < results.length; i++){
                    a = a + "<p>" + "номер: " + results[i]._id + ", " + "название: " + results[i].title + ", " + "автор: " + results[i].autor + ", " + "дата публикации: " + results[i].date_of_public + "</p>"
                }
                response.send(a);
                client.close();
            });
    });
});

app.listen(3000);