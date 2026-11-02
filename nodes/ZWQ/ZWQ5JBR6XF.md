---
tag: ZWQ5JBR6XF
kind: problem
name: Brachistochrone problem
msc: [49K05, 49-03, 70H03]
uses: [JRQZ803Q5Y, F7EKTEESQ5, PS0VV149ET]
about: [PQ25NHV0KS]
sources:
  - url: https://en.wikipedia.org/wiki/Brachistochrone_curve
history:
  posed_by: "Johann Bernoulli"
  first_stated: "1696"
---

## Problem

Let $A$ and $B$ be two points in a vertical plane, with $B$ lower than $A$ and not on the vertical line through $A$.
A particle starts at rest at $A$ and slides without friction along a curve from $A$ to $B$ under constant gravity $g$.
Which curve makes the time of travel from $A$ to $B$ as small as possible?

In coordinates, put $A = (0, 0)$, measure $y$ downwards, and let $B = (x_1, y_1)$ with $x_1, y_1 > 0$.
Energy conservation gives the speed $\sqrt{2 g y}$.
So for a graph $y(x)$ the time is the [[integral functional|JRQZ803Q5Y]]
$$T(y) = \int_0^{x_1} \sqrt{\frac{1 + y'(x)^2}{2 g \, y(x)}} \, dx,$$
to be minimised among curves with $y(0) = 0$ and $y(x_1) = y_1$.

## Remarks

The answer is an arc of a cycloid, the curve traced by a point on a circle that rolls along a horizontal line.
Its parametric form is $x = r(\theta - \sin \theta)$, $y = r(1 - \cos \theta)$, with the radius $r$ fixed by the condition that the curve passes through $B$.
The integrand does not depend on $x$, so the [[Beltrami identity|F7EKTEESQ5]] applies and gives $y (1 + y'^2) = 2r$ for a constant $r$; the cycloid solves this equation.
The fastest curve is not the straight segment; when $x_1 / y_1 > \pi / 2$, the cycloid even dips below the height of $B$ before it rises to $B$.
Johann Bernoulli posed the problem as a public challenge in Acta Eruditorum; solutions by Johann Bernoulli, Jacob Bernoulli, Leibniz and Newton appeared in 1697.
The problem is often taken as the start of the calculus of variations.

## Explanations

### L1 human

A ball rolls from a high point to a lower point off to the side, and one wants the track that gets it there fastest.
The straight track is the shortest but not the fastest.
A track that first drops steeply lets the ball pick up speed early, and the best balance between length and speed is a cycloid.
