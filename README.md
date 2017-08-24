# Slide template using Remark.js

## Go offline

To avoid using online script like `remark-latest.min.js` and `MathJax.js`,

- `remark-latest.min.js` were downloaded from somewhere and should be contained in this directory.
- `MathJax.js` is loaded from `~/.nodebrew/node/v8.4.0/lib/node_modules/mathjax/` which was installed using `npm`.

## Separate `contents.md` or directly into `index.html`

Originally, the Markdown contents are to be written directly into `<textarea id='source'>...</textarea>` in the `index.html` file with,
```
<script>
  var slideshow = remark.create();
</script>
```

If you want to write the contents separately from `index.html`, you can do it by replacing the above code with
```
<script>
  var q = window.location.search.substring(1);
  var slideshow = remark.create({sourceUrl: q ? q : "contents.md"});
</script>
```
But in this case, the slide should be opened via a HTTP server, which is achieved by
```
$ python -m SimpleHTTPServer
```
and then opening `localhost:8000` with a web browser.
Notice that in this case, MathJax seems not working with local `MathJax.js` script. Thus currently this option is not the default choice.


