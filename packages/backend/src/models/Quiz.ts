import {BaseEntity, Column, Entity, JoinColumn, ManyToOne, OneToMany, OneToOne, PrimaryGeneratedColumn} from 'typeorm';
import { Answer } from './Answer';
import { Project } from './Projects';
import { Question } from './Question';

@Entity("quizes")
export class Quiz extends BaseEntity{

    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    name: string;    

    @ManyToOne(() => Project, (project) => project.quizes)
    @JoinColumn({ name: 'project_id' })
    project: Project;


    @OneToMany(() => Question, (question) => question.quiz) 
    questions: Question[];



    @OneToOne(() => Question)
    @JoinColumn({name: "answer_id"})
    answer: Question;


    
}