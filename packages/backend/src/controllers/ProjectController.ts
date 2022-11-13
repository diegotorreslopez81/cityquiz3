import { Request, Response } from "express";
import { Project } from "../models/Projects";
import { User } from "../models/User";




export interface ReponseQuiz{
    quiz_id: number;
    answer_id: number;
}
export interface CheckProjectInput{
    address: string;
    project_id: number;
    responses: ReponseQuiz[];
}


export const createProject=async (req:Request, res:Response)=>{
    try {
        const {name, description, logo} = req.body;
        const project= new Project();
        project.name= name;
        project.description=description;
        project.logo= logo;
        await project.save();
        return res.json(project);
    } catch (error ) {
        if(error instanceof Error){
            return res.status(500).json({message: error.message});
        }   
    }
}

export const getProjectById= async (req:Request, res: Response)=>{
    const project = await Project.findOne({where:{id: parseInt(req.params.id)},relations:['quizes','quizes.questions']});
    return res.json(project);
}


export const getProjects= async (req:Request, res: Response)=>{
    const projects = await Project.find({relations:['quizes','quizes.questions','quizes.answer']});
    return res.json(projects);
}

export const resolveQuizProject=async(req: Request, res:Response)=>{
    const data:CheckProjectInput = req.body;
    
    const user = await User.findOne({where:{address: data.address}});
    if(user==null){
        return res.status(404).json({message: 'usuario no encontrado'});
    }

    const project= await Project.findOne({where:{id:data.project_id},relations:['quizes','quizes.answer']});
    if(project==null){
        return res.status(404).json({message: 'Quiz no encontrado no encontrado'});
    }
    const resolved =[];
    for (let index = 0; index < project.quizes.length; index++) {
        const quiz = project.quizes[index];
        const resp=data.responses.find(item=>item.quiz_id==quiz.id && quiz.answer!=null && quiz.answer.id==item.answer_id);
        if(resp!=null){
            resolved.push(resp);
        }
        
    }

    const preguntas= project.quizes.length;

    const aproved_limit = project.aproval_percent;
    const respuestas_aprovadas = resolved.length;
    const calc_percent = (respuestas_aprovadas* 100)/ preguntas;
    const aproved= calc_percent>aproved_limit;
    const message=`El resultado de su examen fue ${respuestas_aprovadas}/${preguntas} ${aproved==false ? 'intente otra vez' : ' exitos, reclame su nft'}`;
    return res.json({
        /* limite_aprovado:aproved_limit,
        preguntas,
        respuestas_aprovadas,
        resultado_porcentual: calc_percent, */
        //resolved,
        aproved,
        message
    });
    /* 
    address: string;
    project_id: string;
    responses: ReponseQuiz[]; */
}

const checkQuestion=(responses:any[], question_id:number)=>{
    const index = responses.findIndex(item=>item.questionId)
}