import { Router } from "express";
import { createAnswerQuiz } from "../controllers/AnswerController";
import { createProject, getProjectById, getProjects, resolveQuizProject } from "../controllers/ProjectController";
import { createQuestion } from "../controllers/QuestionController";
import { createQuiz, getQuiz } from "../controllers/QuizController";
import { loginUser, registerToken, registerUser } from "../controllers/UserController";

const router = Router();

router.get('/',  getProjects);
router.get('/projects',  getProjects);
//router.get('/project/:id',  getProjectById);
router.post('/projects',  createProject);
router.get('/projects/:id',  getProjectById);
router.post('/projects/resolve', resolveQuizProject);
router.post('/user/register/token', registerToken);



router.post('/quizes',  createQuiz);
router.get('/quiz/:id',  getQuiz);


router.post('/questions',  createQuestion);
router.post('/answer',  createAnswerQuiz);

router.post('/register',registerUser);
router.post('/login',loginUser);



export default router;