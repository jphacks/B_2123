import { Box } from "@mui/material";
import React from "react";
import { useParams } from "react-router";
import { RankingList } from "../components/RankingList";
import { Title } from "../components/Title";
import "./css/ranking.scss";

export const Ranking = () => {
  const { id } = useParams<{ id: string }>();
  return (
    <div className="ranking">
      <Box sx={{ marginBottom: 1 }}>
        <Title>ランキング</Title>
      </Box>
      <RankingList groupId={id}></RankingList>
    </div>
  );
};
