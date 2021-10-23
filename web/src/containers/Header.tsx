import React from "react";
import "./css/header.scss";

export const Header = () => {
  return (
    <div className="header">
      <div className="header__title_wrapper">
        <div className="header__subtitle">slackで管理ができる</div>
        <h1 className="header__title">筋トレサイト</h1>
      </div>
    </div>
  );
};
