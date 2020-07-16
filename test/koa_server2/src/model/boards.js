module.exports = (Sequelize, sequelize) => {
  const boards = sequelize.define("boards", { //""데이터 모델 이름 = mysql에서 테이블 이름과 같음
    id: {
      type: Sequelize.INTEGER(11).UNSIGNED,   // UNSIGNED는 음수 데이터 x
      primaryKey: true,
      autoIncrement: true,
      allowNull: false,
    },
    name: {
      type: Sequelize.STRING(100),    // EOL에서 끝난다고 봄
      allowNull: false,
    },
    content: {
      type: Sequelize.TEXT,           //문서에 가까움 다음줄에 문자가 없을때 끝난다고 봄
      allowNull: false,
    },
    created_at: {
      type: Sequelize.DATE,           //DATE 타입은 시계열 분석에 많이 사용하게 됨
      defaultValue: Sequelize.fn("now"),  //now라는 function을 사용해서 기본값을 설정 now() 년-월-일 시:분:초
      allowNull: false,
    },
  });   //이와같이 데이터 모델을 만듦

  boards.sync();    //sync() 테이블이 없을때 테이블을 만들어 줌
  return boards;    
};
