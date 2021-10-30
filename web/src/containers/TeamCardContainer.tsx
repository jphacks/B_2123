import React, { useEffect, useState } from "react";
import { useHistory } from "react-router";
import { TeamCard } from "../components/TeamCard";
import { getGroupUsers } from "../lib/fetch";

export const TeamCardContainer = ({ groupId }: { groupId: string }) => {
  const [groupNumber, setGroupNumber] = useState<number>();

  useEffect(() => {
    (async () => {
      const num = (await getGroupUsers(groupId)).length;
      setGroupNumber(num);
    })();
  }, [groupId]);
  const history = useHistory();

  return (
    <div>
      <h2 style={{ margin: 0, marginBottom: 35 }}>My-Team</h2>
      <TeamCard
        teamName="グループへ"
        ranking={String(groupNumber) || "0"}
        onClick={() => history.push(`/group/${groupId}`)}
      />
    </div>
  );
};
