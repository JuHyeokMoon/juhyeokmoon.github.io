const boardModel = require("./boards");
const studentModel = require("./student");
const sing_upModel = require("./sing_up");
const subjectModel = require("./subject");

module.exports = (Sequelize, sequelize) => {    //내 DB에 데이터 입력
  const boards = boardModel(Sequelize, sequelize);
  const student = studentModel(Sequelize, sequelize);
  const sing_up = sing_upModel(Sequelize, sequelize);
  const subject = subjectModel(Sequelize, sequelize);

  sing_up.belongsTo(student, { foreignKey: "student_id" });
  sing_up.belongsTo(subject, { foreignKey: "subject_id" });

  return {
    boards,
    student,
    sing_up,
    subject,
  };
};
