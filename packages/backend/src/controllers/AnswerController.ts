import { Request, Response } from "express";
import { Quiz } from "../models/Quiz";



export const createAnswerQuiz=async (req:Request, res:Response)=>{
    try {
        const {question_id,quiz_id} = req.body;
        const quiz= await Quiz.findOneOrFail({where:{id:quiz_id},relations:['answer','questions']});
        const answer = quiz.questions.find(item=>item.id==question_id);
        if(answer){
            quiz.answer= answer;
            quiz.save();
        }else{
            return res.status(404).json({message: 'item no encontrado'});
        }
        
        return res.json(quiz.answer);
    } catch (error ) {
        if(error instanceof Error){
            return res.status(500).json({message: error.message});
        }   
    }
}
