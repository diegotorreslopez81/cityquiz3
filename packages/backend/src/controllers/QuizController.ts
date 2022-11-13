import { Request, Response } from "express";
import { Quiz } from "../models/Quiz";



export const createQuiz=async (req:Request, res:Response)=>{
    try {
        const {project_id,name} = req.body;
        const quiz= new Quiz();
        quiz.name= name;
        quiz.project= project_id;
        await quiz.save();
        return res.json(quiz);
    } catch (error ) {
        if(error instanceof Error){
            return res.status(500).json({message: error.message});
        }   
    }
}


export const getQuiz=async (req:Request, res:Response)=>{
    const quiz= await Quiz.findOneOrFail({where:{id: parseInt(req.params.id)},relations:['answer','questions']});
    res.json(quiz);
}