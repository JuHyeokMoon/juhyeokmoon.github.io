module.exports = (Sequelize, sequelize) => {
  const subject = sequelize.define("subject", {
    id: {
      type: Sequelize.INTEGER(10),
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
    created_at: {
      type: Sequelize.DATE,           
      defaultValue: Sequelize.fn("now"),  
      allowNull: false,
    },
  });
  subject.sync();
  return subject;
};
