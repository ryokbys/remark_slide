
class: middle
      
# .center[Slide using [**remark.js**](https://remarkjs.com/)]

<br>
<br>
<br>

### Ryo KOBAYASHI

<br>

[Github page for this slide](https://github.com/ryokbys/remark_slide)

---

# Items and ordered items

```
- list1
- list2
- list3

1. numbered list
2. second item
3. third one
```

- list1
- list2
- list3

1. ordered items
2. second
3. third one

---

# Math formulas

Math formula is available using *MathJax.js*.

```
$$
E = mc^2
$$
where $E, m, c$ are energy, mass and speed of light.
```

$$
E = mc^2
$$
where $E, m, c$ are energy, mass and speed of light.

In case of inline math, default identifier would be like `\\(x\\)`, but you can change them to `$` by putting the following lines in `index.html`
```
        tex2jax: {
          inlineMath: [["\x24","\x24"]]
        },
```

---

# Images

```
.center[![:scale 30%](./yoda.png)]
```
.center[![:scale 30%](./yoda.png)]

This scaling works with the following code just before `var slideshow = remark.create();`.
```
remark.macros.scale = function (percentage) {
  var url = this;
  return '<img src="' + url + '" style="width: ' + percentage + '" />';
};
```

---

# Images *contd.*

```
![:scale 25%](./yoda.png) Text alongside the non-aligned image.
```
![:scale 25%](./yoda.png) Text alongside the non-aligned image.

<br>
```
.right[Text alongside the right aligned image. ![:scale 25%](./yoda.png)]
```
.right[Text alongside the right aligned image. ![:scale 25%](./yoda.png)]

---

# Video from youtube

.center[
<iframe width="500" height="300" src="https://www.youtube.com/embed/BQ4yd2W50No" frameborder="0" allowfullscreen></iframe>
]

Right click on the movie at *youtube.com* and copy its URL and paste it as,
```
.center[
<iframe width="700" height="400" src="https://www.youtube.com/..."
frameborder="0" allowfullscreen></iframe>
]
```

---

# Local video

To load a local video file, `iframe` could work but `video` tag would be appropriate,
because you can control `autoplay` or something.
```
<video width="700" height="400" controls>
    <source src="auto-refresh_remark-slide.m4v" type="video/mp4">
</video>
```

.center[
<video width="500" height="300" controls>
    <source src="auto-refresh_remark-slide.m4v" type="video/mp4">
</video>
]

---

# Two-column slide

```
.column:first-of-type {float:left}
.column:last-of-type {float:right}
.split-50 .column:first-of-type {width: 50%}
.split-50 .column:last-of-type {width: 50%}

...

class: split-50

# Two-column slide

.column[
left
]

.column[
right
]
```
There should be two `.column[...]` blocks in the slide.

---

class: split-50

# Two-column slide

.column[
The example below can achieve two-column slide like this.


But the *code block* on the rigth column seems not working with this trick (see below).
]

.column[
.right[![:scale 40%](yoda.png)]

```
class: split-50

# Two-column slide

.column[
left
]
.column[
right
]
```
]

---

# Fonts for local use

Download font files (`*.ttf`) from the internet like [Google fonts](https://fonts.google.com/) and put them into `fonts/` directory.
```
$ ls fonts
DroidSerif-Regular.ttf		YanoneKaffeesatz-Regular.ttf
UbuntuMono-Regular.ttf
```
Then put the following lines in the CSS
```
      @font-face{
        font-family: 'Droid Serif';
        src: url('fonts/DroidSerif-Regular.ttf');
      }
      @font-face{
        font-family: 'Yanone Kaffeesatz';
        src: url('fonts/YanoneKaffeesatz-Regular.ttf');
      }
      @font-face{
        font-family: 'Ubuntu Mono';
        src: url('fonts/UbuntuMono-Regular.ttf');
      }
```

---

# MathJax for local use

Make a link `mathjax` that points to the directory where the `mathjax` is installed.
And put the following code in the `index.html` file.
```
<script src="mathjax/MathJax.js?config=TeX-AMS_HTML&delayStartupUntil=configured" type="text/javascript"></script>
```

---

# Auto-refresh of the slide

Using the script `auto-refresh.py` included in this directory, you can check the slide at the same time you save the `content.md`.

`auto-refresh.py` requires `watch.rb` script by [@calo](https://github.com/carlo/haml-sass-file-watcher).

```bash
$ cp watch.rb ~/bin
$ cd /path/to/remark_slide/
$ python auto-refresh.py
```
You should run `auto-refresh.py` at the same directory where `index.html` and `content.md` exist.

---

name: refresh

# Auto-refresh test

`auto-refresh.py` lets **Safari** reload the slide URL when it detects update in the current working directory.

.center[
<!-- <iframe frameborder="0" width="700" height="350" src="./auto-refresh_remark-slide.m4v"></iframe> -->
<video width="700" height="400" controls>
    <source src="auto-refresh_remark-slide.m4v" type="video/mp4">
</video>
]

---

# References

- [Introduction of the remark.js](https://remarkjs.com/)
      
- [watch.rb script used in autoload.sh](https://github.com/carlo/haml-sass-file-watcher)
