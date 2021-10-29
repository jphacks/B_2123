import { List, ListItem, Paper, ListItemText, Divider } from "@mui/material";
import React, { useEffect, useState } from "react";
import "./css/ranking.scss";
import { getGroupUsers } from "../lib/fetch";
import { User } from "../types/user";
import { useHistory, useParams } from "react-router";

export const UserList = () => {
  const [groupUsers, setGroupUsers] = useState<User[]>();
  const { id } = useParams<{ id: string }>();
  useEffect(() => {
    (async () => {
      const users = await getGroupUsers(id);
      setGroupUsers(users);
    })();
  }, []);

  const history = useHistory();

  const moveUserPage = (id: string) => history.push(`/user/${id}`);

  return (
    <Paper
      style={{
        width: "100%",
      }}
    >
      <List>
        {groupUsers?.map((_) => (
          <>
            <ListItem
              onClick={() => moveUserPage(_.userId)}
              style={{ cursor: "pointer" }}
            >
              <ListItemText primary={_.slackName} />
            </ListItem>
            <Divider />
          </>
        ))}
      </List>
    </Paper>
  );
};
