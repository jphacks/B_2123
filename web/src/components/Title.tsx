import React from "react";
import "./css/title.scss";

export const Title = ({ children }: { children: React.ReactChildren }) => {
  return <h2 className="title">{children}</h2>;
};
