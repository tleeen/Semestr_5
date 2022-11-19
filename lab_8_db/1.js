const MongoClient = require("mongodb").MongoClient;

const url = "mongodb://localhost:27017/";
const mongoClient = new MongoClient(url, { useUnifiedTopology: true });

mongoClient.connect(function(err, client){

    const db = client.db("articledb");
    const collection = db.collection("articles");
    let user = {
        title: "Машина",
        autor: "Воробьёв",
        date_of_public: new Date("07.07.2019"),
        text: "0",
        tags: ["скорость", "гонки"],
        comments: [{
            name:"User0.1",
            text_comment: "text0.1",
            raiting: 5,
        },
            {
                name:"User0.2",
                text_comment: "text0.2",
                raiting: 8,
            }],
    };
    collection.insertOne(user, function( result){
        client.close();
    });
});