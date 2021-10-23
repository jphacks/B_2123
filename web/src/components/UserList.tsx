import {
  List,
  ListItem,
  Paper,
  ListItemText,
  ListItemIcon,
  Divider,
} from "@mui/material";
import React from "react";

export const UserList = () => {
  return (
    <Paper
      style={{
        width: "100%",
      }}
    >
      <List>
        <ListItem>
          <ListItemText primary="Inbox" />
        </ListItem>
        <Divider />
        <ListItem>
          <ListItemText primary="Inbox" />
        </ListItem>
        <Divider />
        <ListItem>
          <ListItemText primary="Inbox" />
        </ListItem>
        <Divider />
        <ListItem>
          <ListItemText primary="Inbox" />
        </ListItem>
      </List>
    </Paper>
  );
};
