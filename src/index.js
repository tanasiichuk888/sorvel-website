// Sorvel site worker: sends www.sorvel.agency to sorvel.agency (301), serves the static site for everything else.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname === "www.sorvel.agency") {
      url.hostname = "sorvel.agency";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
