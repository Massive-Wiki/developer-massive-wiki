# Installing a Google Font in Basso

_Last updated 2024-04-10 by Peter Kaminski_

[[Basso]] is the current standard theme used for Massive Wikis. You can customize this theme to change how your wiki website looks when built. Here, we will demonstrate how to use a font from Google Fonts, instead of the standard font.

To use a font from Google Fonts, follow these steps:

1. Find a font.
2. Find the embed / import code (CSS).
3. Edit the `custom.css` file and insert the CSS.
4. Check in your changes.

Assumptions:

- Your wiki website is using the Basso them
- You can edit the `custom.css` file.
- You want to use just one font. To use different fonts for different elements of the page, the process is similar, but you'll need to identify the elements you want to change with CSS selectors. That process is typical when using CSS, but is not covered by this page.

Notes:

This uses a CSS `@import` statement so all the changes can be made in `custom.css`. If you know HTML and CSS, it's probably better to use `<link>` or `<link rel="preload">` in `_header.html` for faster loading and rendering, while still defining the font family in `custom.css`. It's a small optimization, though; `@import` should work fine.

Fonts loaded from other web sources can be used as well; Google Fonts is used to demonstrate the concepts required.

## Find a font

Go to <https://fonts.google.com/> and find a font. Navigate to the font's page. For "Roboto", the font page is <https://fonts.google.com/specimen/Roboto>.

Click the "Get font" button at the top right. The page should refresh and say "1 font family selected".

## Find the embed / import code (CSS)

On the font page, click the "<> Get embed code" button at the top right.

Make sure the "Web" tab is chosen, then select the "@import" radio button.

Click the "Copy code" link.

Paste into a text editor. You should have something like this:

```html
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap')
</style>
```

## Edit the `custom.css` file and insert the CSS

Find the `custom.css` file in your Basso instance. It should be here inside your wiki website:

`.massivewikibuilder/this-wiki-themes/basso/static/mwb-static/css/custom.css`

Edit `custom.css` with a text editor.

From the embed code you found above, copy the line between `<style>` and `</style>`. It should be similar to this:

```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap')
```

Paste it into `custom.css`.

Below that, paste these lines:

```css
* { font-family: 'Roboto', Arial, sans-serif; font-size: 16px; line-height: 1.5; word-wrap: break-word; }

.markdown-body { font-family: 'Roboto', Arial, sans-serif; font-size: 16px; line-height: 1.5; word-wrap: break-word; }

```

Replace `'Roboto'` with the name of your Google Font.

Save `custom.css`.

## Check in your changes

You have now installed the font. Using your normal tools, commit and push your changed file. You can use a commit message like "Installed new Google Font".

When your wiki website rebuilds, you should see the new font being used.

