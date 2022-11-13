import {BaseEntity, Column, Entity, JoinColumn, ManyToOne, OneToMany, OneToOne, PrimaryGeneratedColumn} from 'typeorm';
import { Answer } from './Answer';
import { Quiz } from './Quiz';


@Entity("questions")
export class Question extends BaseEntity{

    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    name: string;    

    @ManyToOne(() => Quiz, (quiz) => quiz.questions)
    @JoinColumn({ name: 'quiz_id' })
    quiz: Quiz;


    /* 
    @OneToMany(() => Answer, (answer) => answer.question) // note: we will create author property in the Photo class below
    answers: Answer[] */

}