import store from "../store";

export default function guest({ next, router }) {
  if (store.getters.isAuthenticated && store.getters.isRole == "HR") {
    return router.push({ name: "Home" });
  } else if (store.getters.isAuthenticated && store.getters.isRole == "Manager") {
    return router.push({ name: "Home" });
  } else if (store.getters.isAuthenticated && store.getters.isRole == "Staff") {
    return router.push({ name: "Home" });
}

  return next();
}