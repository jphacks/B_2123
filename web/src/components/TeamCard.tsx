import { Card } from "@mui/material";
import React from "react";
import "./css/team-card.scss";

export const TeamCard = ({
  teamName,
  ranking,
  onClick,
}: {
  teamName: string;
  ranking: string;
  onClick: () => void;
}) => {
  return (
    <Card
      className="team-card"
      style={{
        borderRadius: 20,
        boxShadow: "0px 2px 50px rgba(0, 0, 0, 0.1)",
        cursor: "pointer",
      }}
      onClick={onClick}
    >
      <h4 className="team-card__name">{teamName}</h4>
      <span className="team-card__rank">チーム人数:{ranking}人</span>
    </Card>
  );
};
