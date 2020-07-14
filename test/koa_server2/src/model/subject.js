module.exports = (Sequelize, sequelize) => {
  const subject = sequelize.define("subject", {
    id: {
      type: Sequelize.STRING(45),
      primaryKey: true,
      allowNull: false,
    },
    subject_name: {
      type: Sequelize.STRING(45),
      allowNull: true,
    },
    credits: {
      type: Sequelize.INTEGER(11),
      allowNull: true,
    },
  });

  return subject;
};
