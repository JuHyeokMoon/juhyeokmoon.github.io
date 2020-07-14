const Sequelize = require("sequelize");
const model = require("../model");

// const sequelize = new Sequelize("world", "userTest", "wjdtltjf123!", {
//   host: "localhost",
//   dialect: "mysql",
//   define: {
//     freezeTableName: true,
//     timestamps: false,
//   },
// });
const sequelize = new Sequelize("mydb", "root", "sidsid2", {
  host: "localhost",
  dialect: "mysql",
  port: "3306",
  define: {
    freezeTableName: true,
    timestamps: false,
  },
  timezone: "+09:00",
});

sequelize
  .authenticate()
  .then(() => {
    console.log("Connection has been established successfully.");
  })
  .catch((err) => {
    console.error("Unable to connect to the database:", err);
  });

const models = model(Sequelize, sequelize);

module.exports = {
  Sequelize,
  sequelize,
  models,
};
