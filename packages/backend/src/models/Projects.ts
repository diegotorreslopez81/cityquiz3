import {BaseEntity, Column, Entity, OneToMany, PrimaryGeneratedColumn} from 'typeorm';
import { Quiz } from './Quiz';

@Entity("projects")
export class Project extends BaseEntity {

    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    name: string;

    @Column()
    logo: string;

    @Column()
    description: string;

    @Column({default:50})
    aproval_percent: number;

    @OneToMany(() => Quiz, (quiz) => quiz.project) // note: we will create author property in the Photo class below
    quizes: Quiz[]

}