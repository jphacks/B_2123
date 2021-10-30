import React from "react";
import { Card } from "@mui/material";
import "./css/user-menu-card.scss";

export const UserMenuCard = ({
  title,
  num,
}: {
  title: string;
  num: string;
}) => {
  return (
    <Card
      className="user-menu-card"
      style={{ boxShadow: "0px 2px 50px rgba(0, 0, 0, 0.1)" }}
    >
      <h3 className="user-menu-card__title">{title}</h3>
      <span className="user-menu-card__num">{num}回</span>
    </Card>
  );
};
