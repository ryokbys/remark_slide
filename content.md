
class: middle
      
# .center[Slide using [**remark.js**](https://remarkjs.com/)]

<br>
<br>
<br>

### Ryo KOBAYASHI

<br>

Department of Physical Science and Engineering, Nagoya Institute of Technology

[Github page for this slide](https://github.com/ryokbys/remark_slide)

---

# Items and ordered items

```
- list1
- list2
- list3

1. numbered list
2. second item
```

- list1
- list2
- list3

1. ordered items
2. second

---

# Math formulas

Math formula is available using *MathJax.js*.

```
$$
E = mc^2
$$
where \\(E, m, c\\) are energy, mass and speed of light.
```

$$
E = mc^2
$$
where \\(E, m, c\\) are energy, mass and speed of light.

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

# Movie

.center[
<iframe width="700" height="350" src="https://www.youtube.com/embed/BQ4yd2W50No" frameborder="0" allowfullscreen></iframe>
]

Right click on the movie at *youtube.com* and copy its URL and paste it as,
```
.center[
<iframe width="700" height="400" src="https://www.youtube.com/embed/BQ4yd2W50No"
frameborder="0" allowfullscreen></iframe>
]
```

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


But the *code block* on the rigth column seems not working with this trick.
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

# References

- [Introduction of the remark.js](https://remarkjs.com/)
      
