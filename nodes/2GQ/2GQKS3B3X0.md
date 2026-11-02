---
tag: 2GQKS3B3X0
kind: statement
role: theorem
name: Phragmén–Lindelöf principle for subharmonic functions
msc: [31A05, 30C80]
uses: [Z1MHMGFNFW, 9XJ5FBQD7M, 0T3RZQXDYD, 0DEB0JMN0W, FYR6V2NH6C]
about: [Z1MHMGFNFW]
sources:
  - url: https://en.wikipedia.org/wiki/Phragm%C3%A9n%E2%80%93Lindel%C3%B6f_principle
---

## Statement

Let $S = \set{z \in \C : \abs{\operatorname{Im} z} < \pi/2}$ be the horizontal strip of width $\pi$, and let $u$ be [[subharmonic|Z1MHMGFNFW]] on $S$.
Assume that $\limsup_{z \to \zeta,\, z \in S} u(z) \le 0$ for every point $\zeta$ of the boundary of $S$.
Assume also that there are constants $A > 0$ and $\alpha < 1$ with $u(z) \le A \exp(\alpha \abs{\operatorname{Re} z})$ for all $z \in S$.
Then $u \le 0$ on $S$.

## Remarks

Proof idea: pick $\beta$ with $\max(\alpha, 0) < \beta < 1$ and put $w(z) = \operatorname{Re} \cosh(\beta z) = \cosh(\beta x) \cos(\beta y)$ for $z = x + iy$.
The function $w$ is [[harmonic|0DEB0JMN0W]], and on $\overline{S}$ it satisfies $w \ge \cos(\beta\pi/2) \cosh(\beta x) > 0$.
For $\varepsilon > 0$, the subharmonic function $u - \varepsilon w$ tends to $-\infty$ as $\abs{\operatorname{Re} z} \to \infty$, because $\beta > \alpha$.
The [[maximum principle for subharmonic functions|9XJ5FBQD7M]] on long rectangles gives $u \le \varepsilon w$, and letting $\varepsilon \to 0$ gives $u \le 0$.

The bound on $\alpha$ is sharp.
The function $u(z) = \operatorname{Re} e^{z} = e^{x}\cos y$ is harmonic on $S$, vanishes on the boundary lines $y = \pm\pi/2$, and satisfies $u \le e^{\abs{\operatorname{Re} z}}$, which is the case $\alpha = 1$.
But $u > 0$ on $S$.
For holomorphic $f$, applying the theorem to $\log\abs{f}$ gives the [[Phragmén–Lindelöf principle|FYR6V2NH6C]] for strips, and conformal maps carry it to sectors.

## Explanations

### L1 human

On a bounded region, a subharmonic function that is at most $0$ at the edge is at most $0$ inside.
On an unbounded strip this can fail, because the function may grow without limit along the strip.
The principle says it still holds as long as the function does not grow too fast: slower than $\exp(\abs{\operatorname{Re} z})$, by a definite margin.

### L2 human

This is the maximum principle for unbounded domains, with a growth condition replacing boundedness of the domain.
The threshold growth is the growth of the positive harmonic function $\operatorname{Re} e^{z}$, which vanishes on the boundary.
The proof compares $u$ with the harmonic function $\operatorname{Re}\cosh(\beta z)$, which grows more slowly than $\operatorname{Re} e^{z}$ but faster than $u$.
The subharmonic form is more flexible than the holomorphic one, since it applies to $\log\abs{f}$, $\abs{f}^p$ and to maxima of such functions.
