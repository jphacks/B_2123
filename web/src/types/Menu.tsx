export type Menu = {
  id: string;
  menuName: string;
};

export const getMenuById = (menus: Menu[], menuId: string) =>
  menus.filter((_) => _.id == menuId)[0];
