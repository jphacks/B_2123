import { Box } from "@mui/material";
import React from "react";
import { RankingList } from "../components/RankingList";
import { Title } from "../components/Title";
import "./css/ranking.scss";

export const Ranking = () => {
  return (
    <div className="ranking">
      <Box sx={{ marginBottom: 1 }}>
        <Title>ランキング</Title>
      </Box>
      <RankingList></RankingList>
    </div>
  );
};
