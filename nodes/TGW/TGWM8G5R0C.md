---
tag: TGWM8G5R0C
kind: problem
name: Newton's minimal resistance problem
msc: [49Q10, 49K05, 49-03]
uses: [JRQZ803Q5Y, 07Q7CNM5WF, NE09EDK19V]
about: [PQ25NHV0KS]
sources:
  - url: https://en.wikipedia.org/wiki/Newton%27s_minimal_resistance_problem
same_as:
  wikidata: Q39087306
  wikipedia: Newton's minimal resistance problem
history:
  posed_by: "Isaac Newton"
  first_stated: "1687"
---

## Problem

A solid body moves with constant speed along its axis through a rarefied medium.
The particles of the medium do not interact with each other and bounce off the body elastically.
Among convex bodies of revolution with base radius $R > 0$ and height $h > 0$, which shape has the least resistance?

In Newton's model, the body is $\set{(x, z) \in \R^2 \times \R : \abs{x} \le R, \ 0 \le z \le u(\abs{x})}$.
Its profile $u \colon [0, R] \to [0, h]$ is [[concave|07Q7CNM5WF]] and nonincreasing.
The resistance is proportional to the [[integral functional|JRQZ803Q5Y]]
$$F(u) = \int_0^R \frac{r}{1 + u'(r)^2} \, dr.$$
The problem is to minimise $F$ over such profiles.

## Remarks

Newton stated the answer in the Principia.
The optimal profile is not pointed: it has a flat disc of positive radius at the front, followed by a curved part that meets the disc at a nonzero angle.
The convexity condition matters.
Without it, profiles with steep zigzags make $F(u)$ as small as one likes.
But then particles would hit the body more than once, and the model no longer describes the resistance.
Later work showed that convex bodies without rotational symmetry can have smaller resistance than Newton's body of the same radius and height.

## Explanations

### L1 human

Newton asked how to shape the nose of a body so that it pushes through a thin gas as easily as possible.
His answer is surprising: the best nose is blunt, with a flat front, and not a sharp point.
It was one of the first problems in which a shape was found by minimising an integral.
