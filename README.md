# Slide template using Remark.js

[Here](http://ryokbys.web.nitech.ac.jp/contents/slides/remark_slide/index.html) you can see the slide template.

## Offline first

To avoid using online scripts such as `remark-latest.min.js` and `MathJax.js`,

- `remark-latest.min.js` were downloaded from somewhere (official website?) and should be contained in this directory.
- The link to the directory that contains `MathJax` shoul be created in this directory. If you installed `mathjax` using `npm`, the `mathjax` directory would be at `~/.nodebrew/node/vX.X.X/lib/node_modules/`.

### Make it online

Replace the following lines
```
<script src="remark-latest.min.js"></script>
<script src="mathjax/MathJax.js?config=TeX-AMS_HTML&delayStartupUntil=configured" type="text/javascript"></script>
```
with
```
<script src="http://gnab.github.io/remark/downloads/remark-latest.min.js" type="text/javascript"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML&delayStartupUntil=configured" type="text/javascript"></script>
```
Then this slide will load `remark-latest.min.js` and `MathJax.js` online.


## Open with a browser

Since the main content is separated from `index.html` and loaded from it, the HTML file should be loaded via HTTP server. You can launch a simple HTTP server with Python2 as
```
$ python -m SimpleHTTPServer
```
and the file can be loaded at `localhost:8000` with a browser.



