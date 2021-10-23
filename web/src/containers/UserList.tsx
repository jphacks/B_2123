import React from "react";
import { UserList } from "../components/UserList";
import { Title } from "../components/Title";
import "./css/ranking.scss";
import { Box } from "@mui/material";

export const Users = () => {
  return (
    <div className="ranking">
      <Box sx={{ marginBottom: 1 }}>
        <Title>ユーザー一覧</Title>
      </Box>
      <UserList />
    </div>
  );
};
