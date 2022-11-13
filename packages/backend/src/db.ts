import { DataSource } from "typeorm";
import { Answer } from "./models/Answer";
import { Nft } from "./models/Nft";
import { Project } from "./models/Projects";
import { Question } from "./models/Question";
import { Quiz } from "./models/Quiz";
import { User } from "./models/User";


export const AppDataSource = new DataSource({
    type:"sqlite",
    database: "./sql_app.db",
    //synchronize: true, //si modifico las tablas del modelo en la base de datos se refleja
    logging: true,
    entities: [Project,Quiz,Question, Answer, User,Nft],
    //subscribers: [],
    //migrations: [],
})