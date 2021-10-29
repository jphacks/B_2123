import React, { useEffect, useState } from "react";
import { UserList } from "../components/UserList";
import { Title } from "../components/Title";
import "./css/ranking.scss";
import { Box } from "@mui/material";
import { getGroupUsers } from "../lib/fetch";
import { User } from "../types/user";

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
