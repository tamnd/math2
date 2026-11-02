---
tag: KHN8H3SNSM
kind: statement
role: proposition
name: Abel transform as the projection of a radial function
msc: [44A15, 44A12]
uses: [QMW1MWQH6J, DWJF7ABPR1, VJNZJ352PC, 2P9YWDGKC4]
about: [QMW1MWQH6J]
sources:
  - url: https://en.wikipedia.org/wiki/Abel_transform
---

## Statement

Let $f \colon [0, \infty) \to \C$ be continuous with $\int_0^\infty \abs{f(r)}\, dr < \infty$.
Let $g(x, y) = f\big(\sqrt{x^2 + y^2}\big)$ be the radial function on $\R^2$ with profile $f$.
Then for every $y \in \R$ the integral $\int_\R g(x, y)\, dx$ converges absolutely, and
$$\int_\R g(x, y)\, dx = F(\abs{y}),$$
where $F$ is the [[Abel transform|QMW1MWQH6J]] of $f$.

## Remarks

Since $g(x, y)$ is even in $x$, the line integral is $2 \int_0^\infty f\big(\sqrt{x^2 + y^2}\big)\, dx$.
For $y \ne 0$, the substitution $r = \sqrt{x^2 + y^2}$, with $dx = \frac{r\, dr}{\sqrt{r^2 - y^2}}$, maps $x \in (0, \infty)$ onto $r \in (\abs{y}, \infty)$ and gives the formula; for $y = 0$ it is immediate.
The absolute convergence follows the same way: $\frac{r}{\sqrt{r^2 - y^2}}$ is integrable near $r = \abs{y}$ and tends to $1$ as $r \to \infty$, while $f$ is bounded near $\abs{y}$ and integrable.
By rotation invariance, the integral of $g$ along any line at distance $\abs{y}$ from the origin is also $F(\abs{y})$; this is the [[Radon transform|VJNZJ352PC]] of $g$.

Example: for $f(r) = e^{-r^2}$ the line integral is $\int_\R e^{-x^2 - y^2}\, dx = \sqrt{\pi}\, e^{-y^2}$, which is the Abel transform of $f$ at $\abs{y}$.

## Explanations

### L1 human

A round object seen from the side looks the same from every direction.
The Abel transform gives what one sees: the total along each line of sight as a function of the distance of the line from the centre.
This statement is the computation behind that picture.

### L2 human

The statement identifies the Abel transform with the two-dimensional Radon transform restricted to radial functions.
Together with the projection-slice theorem, it shows that the Fourier transform of the Abel transform of $f$ is the [[Hankel transform|2P9YWDGKC4]] of order $0$ of $f$, up to constants.
This chain is used in tomography of axially symmetric objects, where only one projection is needed.
