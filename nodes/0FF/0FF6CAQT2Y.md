---
tag: 0FF6CAQT2Y
kind: definition
name: Ellipse
msc: [51N20]
defines: 0VKCCEXBJ1
uses: [0XW7V9ZZ05, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Ellipse
    locator: Definition as locus of points
  - url: https://en.wikipedia.org/wiki/Ellipse
    locator: Standard equation
  - url: https://en.wikipedia.org/wiki/Ellipse
    locator: Area
---

## Definition

Let $F_1$ and $F_2$ be points of the [[Euclidean plane|0XW7V9ZZ05]] $\mathbb{R}^2$, and let $d$ be the [[Euclidean distance|0NPPGHQNXQ]]. Let $a$ be a real number with $2a > d(F_1, F_2)$.
The ellipse with the foci $F_1$, $F_2$ and the semi-major axis $a$ is the set
$$\{\, P \in \mathbb{R}^2 \;:\; d(P, F_1) + d(P, F_2) = 2a \,\}.$$

## Remarks

Let $c = \frac{1}{2} d(F_1, F_2)$ and $b = \sqrt{a^2 - c^2}$. For $F_1 = (-c, 0)$ and $F_2 = (c, 0)$, the ellipse is the set of the points with $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$.
If $F_1 = F_2$, the ellipse is the [[circle|060W5CBZP6]] with the centre $F_1$ and the radius $a$.
The [[eccentricity|0HVX863SAJ]] of the ellipse is $e = c / a$, with $0 \leq e < 1$. The ellipse bounds a region of area $\pi a b$.

## Explanations

### L1 human

Fix two pins in a board and tie a loose string to both. Pull the string tight with a pencil and move it round: the pencil draws an ellipse. The length of the string is the constant sum $2a$ of the distances to the two pins.
