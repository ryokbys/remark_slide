# Slide template using Remark.js

## Offline first

To avoid using online scripts such as `remark-latest.min.js` and `MathJax.js`,

- `remark-latest.min.js` were downloaded from somewhere (official website?) and should be contained in this directory.
- `MathJax.js` is loaded from `~/.nodebrew/node/v8.4.0/lib/node_modules/mathjax/` which was installed using `npm`. **The path should be modified to match your system.**

### Making it online

Replace the following lines
```
<script src="remark-latest.min.js"></script>
<script src="file:///Users/kobayashi/.nodebrew/node/v8.4.0/lib/node_modules/mathjax/MathJax.js?config=TeX-AMS_HTML&delayStartupUntil=configured" type="text/javascript"></script>
```
with
```
<script src="http://gnab.github.io/remark/downloads/remark-latest.min.js" type="text/javascript"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML&delayStartupUntil=configured" type="text/javascript"></script>
```
Then this slide will load `remark-latest.min.js` and `MathJax.js` online.


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


