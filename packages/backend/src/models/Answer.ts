import {BaseEntity, Column, Entity, JoinColumn, ManyToOne, OneToOne, PrimaryGeneratedColumn} from 'typeorm';
import { Question } from './Question';

@Entity("answers")
export class Answer extends BaseEntity {

    @PrimaryGeneratedColumn()
    id: number;

/*     @Column({nullable:true})
    question_id: number; */

    @OneToOne(() => Question)
    @JoinColumn({name: "question_id"})
    question: Question;

    /* @ManyToOne(() => Question, (question) => question.answers)
    @JoinColumn({ name: 'question_id' })
    question: Question; */

}