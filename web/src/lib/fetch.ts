import { Menu } from "../types/Menu";
import { Rank } from "../types/rank";
import { User } from "../types/user";

export const getUser = async (userId: string) => {
  const user = (await (
    await fetch(`https://test-use-domain.net/api/users?userId=${userId}`)
  ).json()) as User;

  return user;
};

export const getMenus = async () => {
  const menu = (await (
    await fetch(`https://test-use-domain.net/api/menus`)
  ).json()) as Menu[];

  return menu;
};

export const getGroupUsers = async (groupId: string) => {
  const user = (
    await (
      await fetch(`https://test-use-domain.net/api/users/${groupId}`)
    ).json()
  ).users as User[];

  return user;
};

export const getRank = async (groupId: string) => {
  const rank = (await (
    await fetch(`https://test-use-domain.net/api/records/${groupId}`)
  ).json()) as Rank[];

  return rank;
};
