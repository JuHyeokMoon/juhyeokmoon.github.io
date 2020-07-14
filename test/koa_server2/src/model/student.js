module.exports = (Sequelize, sequelize) => {
  const student = sequelize.define("student", {
    id: {
      type: Sequelize.STRING(45),
      primaryKey: true,
      allowNull: false,
    },
    name: {
      type: Sequelize.STRING(45),
      allowNull: true,
    },
    department: {
      type: Sequelize.STRING(45),
      allowNull: true,
    },
    grade: {
      type: Sequelize.INTEGER(11),
      allowNull: true,
    },
  });

  return student;
};
