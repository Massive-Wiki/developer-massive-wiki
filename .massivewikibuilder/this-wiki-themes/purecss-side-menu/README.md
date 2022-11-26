# Pure.css Side Menu Theme

This is an alpha / in-development theme.

It currently lives in the `this-wiki-themes/purecss-side-menu` directory of the Massive Wiki Developer Wiki.

It uses [Pure.css](https://purecss.io/).

It was initially created by [Peter Kaminski](mailto:kaminski@istori.com), by lightly adapting the [Pure "side menu"](https://github.com/pure-css/pure/tree/master/site/static/layouts/side-menu) layout.

Comments, contributions, or forks are welcome.

## Wishes and Issues

BUG: The bounding box for links in the sidebar is too tall, which means it's easy to for a click to go to the wrong link for links that are stacked right on top of one another.

Needs a "home page" template (which would need support in MWB).

Sidebar is very narrow for typical Sidebar.md content; perhaps it should be wider.

Should there be a topbar on every page template for branding?

Needs examples of doing color theming / branding. Pure says, "We believe that it's much easier to add new CSS rules than to overwrite existing rules. By adding a few lines of CSS, you can customize Pure's appearance to work with your web project." It then links to [Extend - build on top of Pure](https://purecss.io/extend/).

There should be better integration with Pure.css (some of which may require additional features in MWB):

- Use the Pure.css menu/navigation classes in the sidebar.
- Responsive images - "Add the `.pure-img` class name to an `<img>` element to make it scale with the viewport."
- See if we can be clever and use Grids, Forms, Buttons, Tables.

## Resources

- [Pure.css home page](https://purecss.io/)
- [Pure.CSS Tutorial - TutorialsPoint](https://www.tutorialspoint.com/purecss/index.htm)
- [Purelog: for Writers](https://purelog.netlify.app/) by [Brennan Brown](https://brennanbrown.ca/) - a Jekyll theme built with Pure, might be a good example for some Pure things.