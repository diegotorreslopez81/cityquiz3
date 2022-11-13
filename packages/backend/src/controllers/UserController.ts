import { Request, Response } from "express";
import { Nft } from "../models/Nft";
import { Quiz } from "../models/Quiz";
import { User } from "../models/User";



export const registerUser=async (req:Request, res:Response)=>{
    try {
        const {username,address} = req.body;
        console.log(req.body)
        let user= await User.findOne({where:{address}});
        if(user==null){
            user=new User();
            user.username= username;
            user.address= address;
            user.nfts=[];
            await user.save();
        }
        return res.json(user);
    } catch (error ) {
        if(error instanceof Error){
            return res.status(500).json({message: error.message});
        }   
    }
}


export const loginUser=async (req:Request, res:Response)=>{
    const {address} = req.body;
    const user= await User.findOne({where:{address},relations:['nfts']});
    if(user){
        return res.json(user);
    }
    return res.status(404).json({message: "user no encontrado"});    
}


export const registerToken=async (req:Request, res:Response)=>{
    const {address,token, project_id} = req.body;
    let user= await User.findOne({where:{address},relations:['nfts']});
    
    if(user==null){
        return res.status(404).json({message: "user no encontrado"});
    }
    let nft = user.nfts.find(item=>item.token==token); 
    if(nft!=undefined){
        return res.json(user);    
    }
    
    nft= new Nft();
    nft.project=project_id;
    nft.token=token;
    nft.user=user;
    await nft.save();
    
    user= await User.findOne({where:{address},relations:['nfts']});



    return res.json(user);
}