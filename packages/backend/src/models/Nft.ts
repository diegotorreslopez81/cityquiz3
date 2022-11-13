import {BaseEntity, Column, Entity, JoinColumn, ManyToOne, OneToOne, PrimaryGeneratedColumn} from 'typeorm';
import { Project } from './Projects';
import { User } from './User';

@Entity("nfts")
export class Nft extends BaseEntity{

    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    token: string;

    @ManyToOne(() => User, (user) => user.nfts)
    @JoinColumn({ name: 'user_id' })
    user: User;

    

    @OneToOne(() => Project)
    @JoinColumn({name: "project_id"})
    project: Project;


    

    
}