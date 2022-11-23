const express = require("express");

const app = express();

const urlencodedParser = express.urlencoded({extended: false});

const MongoClient = require("mongodb").MongoClient;

const url = "mongodb://localhost:27017/";

const mongoClient = new MongoClient(url);

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
                    a = a + "<br>" + "номер: " + results[i]._id + ", " + "название: " + results[i].title + ", " + "автор: " + results[i].autor + ", " + "дата публикации: " + results[i].date_of_public
                          + "<form action=\"/state" + i +"\" method=\"post\"> " + "<p>" + "  <input type=\"submit\" value=\"Подробная информация\" />" + "</p>" + "</form>"
                          + "<form action=\"/delete" + i +"\" method=\"post\"> " + "<p>" + "  <input type=\"submit\" value=\"Удалить\" />" + "</p>" + "</form>"
                          + "</br>";
                    app.post("/state" + i, urlencodedParser, function (request, response) {
                        mongoClient.connect(function(err, client){

                            const db = client.db("articledb");
                            const collection = db.collection("articles");

                            if(err) return console.log(err);

                            collection.aggregate([{$project: {_id: 1, title: 1, autor: 1, date_of_public: 1, text:1, tags:1, comments:1}}])
                                .toArray(function(err, results){
                                    let c = "";
                                    for (let j = 0; j < results[i].comments.length; j++){
                                        c = c + "[Имя пользователя: " + results[i].comments[j].name + ", " + "Текст комментария: " + results[i].comments[j].text_comment + ", " + "Оценка: " + results[i].comments[j].raiting + "], ";
                                    }
                                    let b = "<p>" + "номер: " + results[i]._id + ", " + "название: " + results[i].title + ", " + "автор: " + results[i].autor + ", " + "дата публикации: " + results[i].date_of_public + ", " + "Текст статьи: " + results[i].text + ", " + "Теги: " + results[i].tags + ", " + "Комментраии пользователей: " + c + "</p>"
                                    response.send(b);
                                    client.close();
                                });
                        });
                    });

                    app.post("/delete" + i, urlencodedParser, function (request, response) {
                        mongoClient.connect(function(err, client) {

                            const db = client.db("articledb");
                            const collection = db.collection("articles");

                            if (err) return console.log(err);

                            collection.deleteOne({_id: results[i]._id});

                            collection.aggregate([{$project: {_id: 1, title: 1, autor: 1, date_of_public: 1}}])
                                .toArray(function (err, results) {
                                    let c = "";
                                    for(let i = 0; i < results.length; i++) {
                                        c = c + "<br>" + "номер: " + results[i]._id + ", " + "название: " + results[i].title + ", " + "автор: " + results[i].autor + ", " + "дата публикации: " + results[i].date_of_public
                                            + "<form action=\"/state" + i + "\" method=\"post\"> " + "<p>" + "  <input type=\"submit\" value=\"Подробная информация\" />" + "</p>" + "</form>"
                                            + "<form action=\"/delete" + i + "\" method=\"post\"> " + "<p>" + "  <input type=\"submit\" value=\"Удалить\" />" + "</p>" + "</form>"
                                            + "</br>";
                                    }
                                    response.send(c);
                                    client.close();
                                });
                        });
                    });
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

app.post("/artickes9", urlencodedParser, function (request, response) {
    mongoClient.connect(function(err, client){

        const db = client.db("articledb");
        const collection = db.collection("articles");

        if(err) return console.log(err);

        collection.aggregate([{$project: {_id: 1, title: 1, autor: 1, date_of_public: 1, comments: 1}}])
            .toArray(function (err, results) {
            let a = [];
            let d = [];
            let t = [];
            for(let i = 0; i < results.length; i++){
                let sum = 0;
                for(let j = 0; j < results[i].comments.length; j++){
                    sum = sum + results[i].comments[j].raiting;
                }
                d.push(sum/results[i].comments.length);
                a.push("<p>" + "номер: " + results[i]._id + ", " + "название: " + results[i].title + ", " + "автор: " + results[i].autor + ", " + "дата публикации: " + results[i].date_of_public + ", " + "Рейтинг: " + sum/results[i].comments.length + ", " + "Количество комментариев: " + results[i].comments.length + "</p>");
                t.push(results[i].comments.length);
            }
            for (let i = 0; i < a.length; i++){
                for (let j = 0; j < a.length; j++){
                    if (d[i] > d[j]){
                        let c = a[i];
                        a[i] = a[j];
                        a[j] = c;
                        c = d[i];
                        d[i] = d[j];
                        d[j] = c;
                        c = t[i];
                        t[i] = t[j];
                        t[j] = c;
                    }
                }
            }
                for (let i = 0; i < a.length; i++){
                    for (let j = 0; j < a.length; j++){
                        if(d[i] === d[j]){
                            if (t[i] > t[j]) {
                                let c = a[i];
                                a[i] = a[j];
                                a[j] = c;
                                c = d[i];
                                d[i] = d[j];
                                d[j] = c;
                                c = t[i];
                                t[i] = t[j];
                                t[j] = c;
                            }
                        }
                    }
                }
            let k = "";
            for(let i = 0; i < results.length; i++){
                k = k + a[i];
            }
            response.send(k);
            client.close();
        });
    });
});

app.post("/artickes10", urlencodedParser, function (request, response) {
    mongoClient.connect(function(err, client){

        const db = client.db("articledb");
        const collection = db.collection("articles");

        let b = request.body.dat1;
        let c = request.body.dat2;

        if(err) return console.log(err);

        collection.find({date_of_public: {$gte: new Date("\"" + b + "\""), $lte: new Date("\"" + c + "\"")}}).toArray(function(err, results){
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

app.post("/p_insert", urlencodedParser, function (request, response) {
        response.sendFile(__dirname + "/index4.html");
});

app.post("/insert", urlencodedParser, function (request, response) {
    mongoClient.connect(function(err, client){

        const db = client.db("articledb");
        const collection = db.collection("articles");

        let title_ = request.body.title;
        let autor_ = request.body.autor;
        let date_ = request.body.date;
        let text_ = request.body.text_;
        let tags_ = request.body.tags;

        if(err) return console.log(err);

        let user = {
            title: title_,
            autor: autor_,
            date_of_public: new Date("\"" + date_ + "\""),
            text: text_,
            tags: tags_.split(" "),
            comments: [],
        };

        collection.insertOne(user, function( result){
            client.close();
        });
    });
    response.sendFile(__dirname + "/index5.html");
});

app.listen(3000);