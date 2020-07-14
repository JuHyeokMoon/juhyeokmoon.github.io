module.exports = (Sequelize, sequelize) => {
  const sing_up = sequelize.define("sing_up", {
    student_id: {
      type: Sequelize.STRING(45),
      primaryKey: true,
      allowNull: false,
    },
    subject_id: {
      type: Sequelize.INTEGER(11),
      primaryKey: true,
      allowNull: true,
    },
    grade_point: {
      type: Sequelize.INTEGER(11),
      allowNull: true,
    },
  });

  return sing_up;
};
