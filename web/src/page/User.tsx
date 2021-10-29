import "../App.css";
import "./css/user.scss";
import { PageTitle } from "../components/PageTitle";
import { LineChartContainer } from "../containers/LineChartContainer";
import { TeamCardContainer } from "../containers/TeamCardContainer";
import { Grid, Container } from "@mui/material";
import { useEffect, useState } from "react";
import { getUser } from "../lib/fetch";
import { User as UserType } from "../types/user";
import { Footer } from "../containers/Footer";
import { useParams } from "react-router";

export const User = () => {
  const [user, setUser] = useState<UserType>();
  const { id } = useParams<{ id: string }>();
  console.log(id);
  useEffect(() => {
    (async () => {
      const user = await getUser(id);
      setUser(user);
    })();
  }, []);

  return (
    <div className="wrapper">
      <Container maxWidth="xl">
        <div className="user-page">
          <PageTitle titleRed="ユーザー" title="詳細" />
          <h2 style={{ fontSize: 18, fontWeight: "normal", marginBottom: 40 }}>
            ユーザー名: {user && user.slackName}
          </h2>
          <Grid container spacing={8}>
            <Grid item xs={8}>
              {user && <LineChartContainer userMenus={user.menus} />}
            </Grid>
            <Grid item xs={4}>
              {user && <TeamCardContainer groupId={user.groupId} />}
            </Grid>
          </Grid>
        </div>
      </Container>
      <Footer />
    </div>
  );
};
