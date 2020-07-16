const Router = require("koa-router");
const db = require("../db");
const sequelize = require("sequelize");
const Op = sequelize.Op;
const urlencode = require("urlencode");
//npm install urlencode

module.exports = () => {
  const router = new Router();
  const models = db.models;
// ***************************************************
  router.get("/testQuery1", async (ctx) => {    // testQuery1이 주소에 붙을 텍스트 자리
    const results = await db.sequelize.query(
      "SELECT * FROM student WHERE name = ?",   //? 자리에 김기현을 대입하는 문법임 ?개수 만큼 김기현 자리의 개수도 맞게
      {
        replacements: ["김기현"],
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };                     //get 이 ctx 값을 가지고 요청해 결과를 가져옴
  });
// ***************************************************   중요
  router.get("/testQuery2", async (ctx) => {
    const results = await db.sequelize.query(
      "SELECT * FROM student WHERE name = :userid",
      {
        replacements: { userid: "김기현" },
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuery3", async (ctx) => {
    const results = await db.sequelize.query(
      "SELECT * FROM student WHERE name = :userid and department = :department",
      {
        replacements: { userid: "김기현", department: "산업경영공학과" },
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuery4", async (ctx) => {
    const { name, department } = ctx.request.query;
    const results = await db.sequelize.query(
      "SELECT * FROM student WHERE name = :userid and department = :department",
      {
        replacements: { userid: name, department: department },
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuery5", async (ctx) => {
    const { name } = ctx.request.query;
    const results = await db.sequelize.query(
      "SELECT * FROM student WHERE name = :userid",
      {
        replacements: { userid: name },
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuery6", async (ctx) => {
    const { name, department } = ctx.request.query;
    const results = await db.sequelize.query(
      "SELECT * FROM student WHERE name = :userid and department = :department",
      {
        replacements: { userid: name, department: department },
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuery7", async (ctx) => {
    const results = await db.sequelize.query(
      "SELECT * FROM student, sign_up, subject where student_id = student.id and subject_id=subject.id",
      {
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuery8", async (ctx) => {
    const results = await db.sequelize.query(
      "SELECT  stu.id, stu.name, stu.department, sj.subject_name, su.grade_point FROM student as stu, sign_up as su , subject as sj where su.student_id = stu.id and su.subject_id=sj.id",
      {
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuery9", async (ctx) => {
    const results = await db.sequelize.query("SELECT now() as date;", {
      type: sequelize.QueryTypes.SELECT,
    });
    ctx.body = { results };
  });

  router.get("/testQuery10", async (ctx) => {
    const { setTime } = ctx.request.query;
    const results = await db.sequelize.query(
      "SELECT date_format(DATE_ADD(NOW(), INTERVAL :setTime HOUR), '%H') as date;",
      {
        replacements: { setTime: setTime },
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuery11", async (ctx) => {
    const results = await db.sequelize.query(
      "SELECT DATEDIFF(now(),created_at) AS DiffDate from boards;",
      {
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuery12", async (ctx) => {
    const results = await db.sequelize.query(
      "SELECT TIMESTAMPDIFF(minute,created_at,now()) AS DiffTIME from boards;",
      {
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuery13", async (ctx) => {
    const results = await db.sequelize.query(
      "SELECT TIMESTAMPDIFF(second,created_at,now()) AS DiffTIME from boards;",
      {
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuery14", async (ctx) => {
    const { name } = ctx.request.query;
    const results = await db.sequelize.query(
      "SELECT * FROM student WHERE grade < :userid ",
      {
        replacements: { userid: name },
        type: sequelize.QueryTypes.SELECT,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQueryup1", async (ctx) => {
    const { id, num } = ctx.request.query;
    const results = await db.sequelize.query(
      "update student set grade=:chagenum WHERE id = :studentid ",
      {
        replacements: { studentid: id, chagenum: num },
        type: sequelize.QueryTypes.UPDATE,
      }
    );
    ctx.body = { results };
  });

  router.get("/testQuerydel", async (ctx) => {
    const { id } = ctx.request.query;
    const results = await db.sequelize.query(
      "delete from boards where id=:id",
      {
        replacements: { id: id },
        type: sequelize.QueryTypes.DELETE,
      }
    );
    ctx.body = { results };
  });
  // models.student.association = function (models) {
  //   models.student.belongTo(models.sing_up, {
  //     target: "id",
  //     foreign: "student_id",
  //   });
  // };
  // models.subject.association = function (models) {
  //   models.subject.belongTo(models.sing_up, {
  //     target: "id",
  //     foreign: "subject_id",
  //   });
  // };

  router.post("/postTest", async (ctx) => {
    ctx.body = { title: "postTest 페이지 입니다." };
  });

  router.get("/", async (ctx) => {
    ctx.body = "7777 서버 페이지 입니다.";
  });

  router.get("/post", (ctx) => {
    const { id } = ctx.request.query;
    if (id) {
      ctx.body = "포스트 #" + id;
    } else {
      ctx.body = "포스트 아이디가 없습니다.";
    }
  });

  router.get("/studentsearch", async (ctx) => {
    const { name } = ctx.request.query;
    const name2 = urlencode.decode(name);
    console.log(name2);
    const results = await models.student.findAll({
      where: {
        name: name2,
      },
    });

    ctx.body = {
      results,
    };
  });

  router.get("/studentsearch2", async (ctx) => {
    const results = await models.sing_up.findAll({
      include: [models.student],
    });

    ctx.body = {
      results,
    };
  });

  router.get("/studentlist", async (ctx) => {
    const results = await models.student.findAll();

    ctx.body = {
      results,
    };
  });

  router.get("/studentsubject", async (ctx) => {
    const results = await models.subject.findAll();

    ctx.body = {
      results,
    };
  });

  router.post("/studentadd", async (ctx) => {
    const { id, name, department, grade } = ctx.request.body;

    try {
      const result = await models.student.create({
        id,
        name,
        department,
        grade,
      });
      ctx.body = { result };
    } catch (e) {
      ctx.throw(e, 500);
    }
  });

  //select name, content from boards
  router.get("/list1", async (ctx) => {
    const results = await models.boards
      .findAll({ attributes : ['name','content']});
      // .map(({ id, name, content, created_at }) => {
      //   return { id, name, content, created_at };
      // });

    ctx.body = {results};
  });

  //select name, content as ct from boards
  router.get("/list2", async (ctx) => {
    const results = await models.boards
      .findAll({ attributes : ['name',['content','ct']]});
    ctx.body = {results};
  });

  //select count(name) as ct from boards
  router.get("/list3", async (ctx) => {
    const results = await models.boards
      .findAll({ attributes : [sequelize.fn('COUNT', sequelize.col['name'])]});
    ctx.body = {results};
  });

  //select name, content(name) as ct from boards
  router.get("/list4", async (ctx) => {
    const results = await models.boards
      .findAll({
        where : {name : "김기현"}
      });
    ctx.body = {results};
  });  

  router.post("/add", async (ctx) => {
    const { name, content } = ctx.request.body;

    console.log(name);
    console.log(content);

    await models.boards
      .create({
        name,
        content,
      })
      .catch((e) => {
        console.log(e);
      });

    ctx.status = 204;
  });

  router.post("/addList", async (ctx) => {
    await models.boards
      .bulkCreate([
        {
          name: "blue",
          content: "hello",
        },
        {
          name: "red",
          content: "world",
        },
      ])
      .catch((e) => {
        console.log(e);
      });
    ctx.status = 204;
  });

  router.put("/update", async (ctx) => {
    await models.boards
      .update(
        {
          content: "hi, world",
        },
        {
          where: {
            name: "blue",
          },
        }
      )
      .catch((e) => {
        console.log(e);
      });
    ctx.status = 204;
  });

  return router;
};
