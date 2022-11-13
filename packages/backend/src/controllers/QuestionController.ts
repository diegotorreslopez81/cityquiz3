import { Request, Response } from "express";
import { Question } from "../models/Question";



export const createQuestion=async (req:Request, res:Response)=>{
    try {
        const {quiz_id,name} = req.body;
        const question1= new Question();
        question1.name= name;
        question1.quiz= quiz_id;
        await question1.save();
        return res.json(question1);
    } catch (error ) {
        if(error instanceof Error){
            return res.status(500).json({message: error.message});
        }
    }
}
