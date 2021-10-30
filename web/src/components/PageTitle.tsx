import React from "react";
import "./css/page-title.scss";

export const PageTitle = ({
  titleRed,
  title,
}: {
  titleRed: string;
  title: string;
}) => {
  return (
    <h2 className="page-title">
      <span className="page-title__red">{titleRed}</span>
      <span className="page-title__title">{title}</span>
    </h2>
  );
};
