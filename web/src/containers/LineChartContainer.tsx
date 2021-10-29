import React, { useEffect, useState } from "react";
import { Grid } from "@mui/material";
import { UserMenuCard } from "../components/UserMenuCard";
import { UserMenu } from "../types/user";
import { getMenus } from "../lib/fetch";
import { getMenuById, Menu } from "../types/Menu";

export const LineChartContainer = ({
  userMenus,
}: {
  userMenus: UserMenu[];
}) => {
  const [menus, setMenus] = useState<Menu[]>();
  useEffect(() => {
    (async () => {
      const menus = await getMenus();
      console.log(menus);
      setMenus(menus);
    })();
  }, []);
  if (!menus) return null;
  return (
    <>
      <Grid container spacing={4} style={{ marginBottom: 40 }}>
        {userMenus.map((_) => {
          const menu = getMenuById(menus, _.menuId);
          return (
            <Grid xs={6} item>
              <UserMenuCard title={menu.menuName} num={_.numberOfTimes} />
            </Grid>
          );
        })}
      </Grid>
    </>
  );
};
