const koa = require("koa");
const cors = require("@koa/cors");
const koaBody = require("koa-body");
const logger = require("koa-logger");
const router = require("./router");   //const 는 import와 비슷한 기능

const run = async () => { //async는 await와 비동기식 연결
  const app = new koa();
  const _router = router(router);

  app.use(cors());
  app.use(logger());
  app.use(koaBody());
  app.use(_router.routes());

  const port = 7777;    //port 번호는 마음대로 지정 할 수는 있지만 충돌 조심
  const server = await app.listen(port);  //서버 오픈 하는 부분
  console.log(`server run ${port}`); //문자열 밖에서 선언된 변수를 사용할땐 ${}

  return server;
};

run();

// node js 파일 시작
// 1. npm install ''
// 2. const 찾아가 보기
// 3. 