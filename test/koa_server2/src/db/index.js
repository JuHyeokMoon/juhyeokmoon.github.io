const Sequelize = require("sequelize");
const model = require("../model");    //model 파일만 경로로 명시해도 index.js를 찾아감

// const sequelize = new Sequelize("world", "userTest", "wjdtltjf123!", {
//   host: "localhost",
//   dialect: "mysql",
//   define: {
//     freezeTableName: true,
//     timestamps: false,
//   },
// });
const sequelize = new Sequelize("mydb2", "root", "sidsid2", {  //sequelize가 객체를 담는 그릇 new Sequelize가 생성자, + 파라미터들 DB이름, user ID, PW, 정보
  host: "localhost",  //host, dialect, port 3개정도는 적어서 본인에 해당하는 파라미터를 넣음
  dialect: "mysql",
  port: "3306",       //port는 보안 이슈가 항상 있음 
  define: {
    freezeTableName: true,
    timestamps: false,
  },
  timezone: "+09:00",
});

sequelize         //log를 찍어보기 위해 작성한 코드, 없어도 됨
  .authenticate() // 인증, sequelize 변수가 접속이 잘 됬는지 확인 하는 
  .then(() => {   // .앞에 있는 함수가 제대로 작동 했으면 로그 찍어줌
    console.log("Connection has been established successfully.");
  })
  .catch((err) => { // then과 같이 사용 제대로 작동 안해서 로그 찍음
    console.error("Unable to connect to the database:", err);
  });

const models = model(Sequelize, sequelize);   //위의 const model에 가서 const Sequelize와 내가 구체화 시킨 sequelize를 가지고 변수화

module.exports = {    // 함수의 return 기능 아래 3가지 정보를 가진
  Sequelize,          // exports 해줘야만 다른 파일에서 받을 수 있음
  sequelize,
  models,
};
