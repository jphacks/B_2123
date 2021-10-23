import {
  List,
  ListItem,
  Paper,
  ListItemText,
  ListItemIcon,
  Divider,
} from "@mui/material";
import React from "react";
import "./css/ranking.scss";

export const RankingList = () => {
  return (
    <Paper
      style={{
        width: "100%",
      }}
    >
      <List>
        <ListItem style={{ paddingTop: 10, paddingBottom: 10 }}>
          <ListItemIcon>
            <div className="rank">1</div>
          </ListItemIcon>
          <ListItemText primary="Inbox" />
        </ListItem>
        <Divider />
        <ListItem style={{ paddingTop: 10, paddingBottom: 10 }}>
          <ListItemIcon>
            <div className="rank rank__2">2</div>
          </ListItemIcon>
          <ListItemText primary="Inbox" />
        </ListItem>
        <Divider />
        <ListItem style={{ paddingTop: 10, paddingBottom: 10 }}>
          <ListItemIcon>
            <div className="rank rank__3">3</div>
          </ListItemIcon>
          <ListItemText primary="Inbox" />
        </ListItem>
        <Divider />
        <ListItem style={{ paddingTop: 10, paddingBottom: 10 }}>
          <ListItemIcon></ListItemIcon>
          <ListItemText primary="Inbox" />
        </ListItem>
      </List>
    </Paper>
  );
};
