export type User = {
  userId: string;
  slackName: string;
  groupId: string;
  created_at: null;
  updated_at: null;
  menus: UserMenu[];
};

export type UserMenu = {
  id: string;
  userId: string;
  menuId: string;
  numberOfTimes: string;
  created_at: null;
  updated_at: null;
};
