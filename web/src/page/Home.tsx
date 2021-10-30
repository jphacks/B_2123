import React from "react";
import { Grid, Box, Container } from "@mui/material";
import "../App.css";
import { Footer } from "../containers/Footer";
import { Header } from "../containers/Header";
import { Ranking } from "../containers/Ranking";
import { Users } from "../containers/UserList";

export const Home = () => {
  return (
    <div className="wrapper">
      <Header />
      <Container>
        <h2 style={{ textAlign: "center" }}>グループ名</h2>
        <Box sx={{ width: "100%" }}>
          <Grid container spacing={8}>
            <Grid xs={6} item>
              <Users />
            </Grid>
            <Grid item xs={6}>
              <Ranking />
            </Grid>
          </Grid>
        </Box>
      </Container>
      <Footer />
    </div>
  );
};
