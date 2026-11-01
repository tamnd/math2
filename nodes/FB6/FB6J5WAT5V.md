---
tag: FB6J5WAT5V
kind: statement
role: theorem
name: Cubic formula
msc: ["12E12", 12D10]
uses: [00EHX6FWC0, J7YS0DA3HQ]
about: [J7YS0DA3HQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cubic_equation
    locator: Cardano's formula
---

## Statement

Let $a, b, c, d \in \C$ with $a \ne 0$.
Put
$$p = \frac{3ac - b^2}{3a^2}, \qquad q = \frac{2b^3 - 9abc + 27a^2 d}{27a^3}.$$
Then $x$ is a [[root|00EHX6FWC0]] of $ax^3 + bx^2 + cx + d$ if and only if $t = x + \frac{b}{3a}$ is a root of $t^3 + pt + q$.
If $p = q = 0$, the only root of $t^3 + pt + q$ is $t = 0$.
Otherwise, let $\delta$ be a square root of $\frac{q^2}{4} + \frac{p^3}{27}$, chosen so that $w = -\frac{q}{2} + \delta \ne 0$.
Let $u$ be a cube root of $w$ and let $\omega = e^{2\pi i/3}$.
Then the three roots of $t^3 + pt + q$, counted with multiplicity, are
$$t_k = \omega^k u - \frac{p}{3\omega^k u}, \qquad k = 0, 1, 2.$$

## Remarks

A choice of $\delta$ with $w \ne 0$ exists: if both choices gave $w = 0$, then $\delta = 0$ and $q = 0$, hence $p = 0$.
For the proof, put $v = -p/(3u)$, so that $uv = -p/3$ and $(u + v)^3 = u^3 + v^3 - p(u + v)$.
The numbers $u^3 = w$ and $v^3 = -p^3/(27w)$ are the two roots of $z^2 + qz - p^3/27$, so $u^3 + v^3 = -q$ and $u + v$ is a root.
The same holds for $\omega^k u$ in place of $u$, and expanding $\prod_k (t - t_k)$ gives $t^3 + pt + q$.
Example: for $t^3 - 6t - 9$, the number $\frac{q^2}{4} + \frac{p^3}{27} = \frac{81}{4} - 8 = \frac{49}{4}$; with $\delta = \frac{7}{2}$, $w = 8$, $u = 2$ and $t_0 = 2 + 1 = 3$.
When the cubic has real coefficients and three distinct real roots, $\delta$ is not real, and the formula passes through nonreal numbers.
By the [[casus irreducibilis|MJ864PBRRJ]], this detour cannot be avoided when the cubic is irreducible over $\Q$.

## Explanations

### L1 human

The cubic formula gives the roots of any equation of degree $3$ using arithmetic, square roots and cube roots.
First a shift of $x$ removes the $x^2$ term.
Then the root is split as a sum $u + v$ of two cube roots, and $u^3$ and $v^3$ solve a quadratic equation.

### L2 human

The formula shows that every cubic is [[solvable by radicals|J7YS0DA3HQ]], as [[Galois' theorem|VHCWCFA3MX]] predicts, since the Galois group lies in $S_3$, which is solvable.
The quantity under the square root is $-\frac{1}{108}$ times the discriminant of $t^3 + pt + q$, which is $-4p^3 - 27q^2$.
The same method of shifting and resolving into a lower-degree equation leads to the [[quartic formula|4CDFMKKZ01]].
