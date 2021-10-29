export type Menu = {
  id: string;
  menuName: string;
};

export const getMenuById = (menus: Menu[], menuId: string) =>
  menus.filter((_) => String(_.id) === String(menuId))[0];
