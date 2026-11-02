---
tag: W1C0W5MCX0
kind: statement
role: theorem
name: Briançon–Skoda theorem
msc: [13B22, 32S05, 14F18]
uses: [EVPZ7ZG1HB, 096Z9MP2ME, G0V86SJBQW]
about: [G0V86SJBQW]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplier_ideal
---

## Statement

Let $\mathcal{O}_n = \C\{z_1, \dots, z_n\}$ be the [[ring of convergent power series|EVPZ7ZG1HB]] in $n$ variables.
Let $I$ be an [[ideal|096Z9MP2ME]] of $\mathcal{O}_n$.
Its *integral closure* $\overline{I}$ is the set of $h \in \mathcal{O}_n$ that satisfy an equation
$$h^m + a_1 h^{m-1} + \cdots + a_m = 0 \quad \text{with } a_j \in I^j \text{ for } j = 1, \dots, m,$$
for some $m \ge 1$; it is an ideal containing $I$.
Then, for every ideal $I$ of $\mathcal{O}_n$ and every integer $k \ge 1$,
$$\overline{I^{\,n + k - 1}} \subseteq I^k.$$
In particular $\overline{I^n} \subseteq I$.

## Remarks

Joël Briançon and Henri Skoda proved the theorem in 1974, using Skoda's $L^2$ estimates for the division problem.
A modern proof uses [[multiplier ideals|BKM0TQSCD9]]: one has $\overline{I^{\,l}} \subseteq \mathcal{J}(I^{\,l})$ for all $l$, and Skoda's theorem gives $\mathcal{J}(I^{\,l}) \subseteq I \cdot \mathcal{J}(I^{\,l-1})$ for $l \ge n$, so induction gives the inclusion.
Lipman and Teissier, and Lipman and Sathaye, extended the result to regular local rings.

A corollary answers a question of Mather.
If $f \in \mathcal{O}_n$ and $f(0) = 0$, then $f$ lies in the integral closure of its Jacobian ideal $J(f) = (\partial f / \partial z_1, \dots, \partial f / \partial z_n)$, and hence $f^n \in J(f)$.

The exponent cannot be lowered to $1$ in general.
For $n = 2$ and $I = (x^2, y^2)$, the element $xy$ satisfies $(xy)^2 - x^2 y^2 = 0$ with $x^2 y^2 \in I^2$, so $xy \in \overline{I}$, but $xy \notin I$.
The theorem gives instead $\overline{I^2} \subseteq I$.

## Explanations

### L1 human

The integral closure of an ideal adds the elements that are "as small as" elements of the ideal.
This means that they satisfy a polynomial equation with coefficients from powers of the ideal.
This can be strictly bigger than the ideal.
The theorem says that taking enough powers makes up for the difference, and the number of powers needed depends only on the number of variables.

### L2 human

In analytic terms, $h \in \overline{I}$ when $\abs{h} \le C (\abs{g_1} + \cdots + \abs{g_r})$ near $0$, where $g_1, \dots, g_r$ generate $I$.
The theorem turns such a size bound into an algebraic membership in a power of $I$.
This is how it is used in the study of the Jacobian ideal and of the [[Milnor number|1ZE51P7GRQ]].
It is a model for many effective results in commutative algebra and for applications of $L^2$ methods in algebraic geometry.
