import {BaseEntity, Column, Entity, JoinColumn, ManyToOne, OneToMany, OneToOne, PrimaryColumn, PrimaryGeneratedColumn} from 'typeorm';
import { Answer } from './Answer';
import { Nft } from './Nft';
import { Project } from './Projects';
import { Question } from './Question';

@Entity("users")
export class User extends BaseEntity{

    @PrimaryGeneratedColumn()
    id: number;

    @Column({unique:true})
    address: string;

    @Column({unique:true})
    username: string;

    
    @OneToMany(() => Nft, (nft) => nft.user) 
    nfts: Nft[]


    
}