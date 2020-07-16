module.exports = (Sequelize, sequelize) => {
  const sing_up = sequelize.define("sing_up", {
    id: {
      type: Sequelize.INTEGER(11),
      primaryKey: true,
      autoIncrement: true,
      allowNull: false,
    },
    student_id: {
      type: Sequelize.INTEGER(10),
      primaryKey: true,
      allowNull: false,
    },
    subject_id: {
      type: Sequelize.INTEGER(10),
      primaryKey: true,
      allowNull: false,
    },
    grade_point: {
      type: Sequelize.INTEGER(11),
      allowNull: true,
    },
  });
  sing_up.sync();
  return sing_up;
};
