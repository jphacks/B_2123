import {
  List,
  ListItem,
  Paper,
  ListItemText,
  ListItemIcon,
  Divider,
} from "@mui/material";
import React, { useEffect, useState } from "react";
import { useHistory } from "react-router";
import { getRank } from "../lib/fetch";
import { Rank } from "../types/rank";
import "./css/ranking.scss";

export const RankingList = ({ groupId }: { groupId: string }) => {
  const [rank, setRank] = useState<Rank[]>();

  useEffect(() => {
    (async () => {
      const rank = await getRank(groupId);
      setRank(rank);
    })();
  }, [groupId]);

  const history = useHistory();

  return (
    <Paper
      style={{
        width: "100%",
      }}
    >
      <List>
        {rank?.map((_, i) => (
          <>
            <ListItem
              style={{ paddingTop: 10, paddingBottom: 10, cursor: "pointer" }}
              onClick={() => history.push(`/user/${_.userId}`)}
            >
              {i === 0 && (
                <ListItemIcon>
                  <div className="rank">1</div>
                </ListItemIcon>
              )}
              {i === 1 && (
                <ListItemIcon>
                  <div className="rank rank__2">2</div>
                </ListItemIcon>
              )}
              {i === 2 && (
                <ListItemIcon>
                  <div className="rank rank__3">3</div>
                </ListItemIcon>
              )}
              <ListItemText primary={_.slackName} />
            </ListItem>
            <Divider />
          </>
        ))}
      </List>
    </Paper>
  );
};
