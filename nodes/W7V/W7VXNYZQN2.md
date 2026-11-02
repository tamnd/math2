---
tag: W7VXNYZQN2
kind: statement
role: theorem
name: Sturm comparison theorem
msc: [34C10, 34B24]
uses: [0QQRP17Z7S]
about: [ZH2S50NSZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Sturm–Picone_comparison_theorem
---

## Statement

Let $a < b$ and let $q_1, q_2 \colon [a, b] \to \R$ be continuous with $q_2(x) \ge q_1(x)$ for all $x \in [a, b]$.
Let $y$ be a solution of $y'' + q_1(x) y = 0$ that is not identically zero and satisfies $y(a) = y(b) = 0$.
Let $z$ be a solution of $z'' + q_2(x) z = 0$.
Then $z$ has a zero in the open interval $(a, b)$, unless $q_1 = q_2$ on $[a, b]$ and $z$ is a constant multiple of $y$.

## Remarks

The proof uses the function $W = y' z - y z'$, whose derivative is $(q_2 - q_1) y z$.
If $z$ had no zero in $(a, b)$, one may take $y > 0$ and $z > 0$ on $(a, b)$.
Integrating $W'$ over $[a, b]$ gives $y'(b) z(b) - y'(a) z(a) \ge 0$, while the signs $y'(a) > 0$, $y'(b) < 0$ and $z \ge 0$ force the left side to be $\le 0$.
Analysing the case of equality gives $q_1 = q_2$ and $z(a) = z(b) = 0$, so $z$ is a multiple of $y$.
Example: $y = \sin x$ solves $y'' + y = 0$ with zeros $0$ and $\pi$; every solution of $z'' + 4 z = 0$, such as $\cos 2x$, has a zero in $(0, \pi)$.
The inequality $q_2 \ge q_1$ is needed: with $q_2 = 0$, the solution $z = 1$ of $z'' = 0$ has no zero at all.
Mauro Picone extended the theorem to equations $(p_i y')' + q_i y = 0$ with $p_1 \ge p_2 > 0$ and $q_2 \ge q_1$; this is the Sturm–Picone comparison theorem.

## Explanations

### L1 human

A larger coefficient $q$ in $y'' + q y = 0$ pulls the solution back to the axis harder, so it oscillates faster.
The theorem makes this precise: between two zeros of a solution of the slower equation, every solution of the faster equation has a zero.

### L2 human

The theorem lets one bound the zeros of solutions by comparison with equations with constant coefficients.
If $m^2 \le q(x) \le M^2$ with $m, M > 0$, then the distance between consecutive zeros of a nonzero solution of $y'' + q y = 0$ lies between $\pi / M$ and $\pi / m$.
It is the main tool of [[oscillation theory|ZH2S50NSZ6]] and it underlies the count of zeros of eigenfunctions in Sturm–Liouville theory.
For equations of the form $y'' + q y = 0$, the case $q_1 = q_2$ gives the [[Sturm separation theorem|YEBPTXZ1FS]].
