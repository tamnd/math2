---
tag: A67QNADARQ
kind: proof
name: Proof of the Jordan-von Neumann theorem
msc: ["46C15", "39B52"]
topics: [1D4JTZ9VS3]
audience: ug2
proves: 46WGVM5VS6
methods: [TFQ1845T84, 0NTF6DMVAP, 0ASJVEFA9J, J2J35J3055, GQHHNV79PA, DX2H7AD66G]
uses: [00A0RPAQ8A, 0VGSYBWHV2, 026HPGYGS4, 05FKHRT0B4, 0FJZMBX0ZZ, 0STX0WRDNG, 055Z15H69G, 05M5SWSZZD, KF719SZD5T]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: Jordan–von Neumann theorems
  - url: https://en.wikipedia.org/wiki/Parallelogram_law
    locator: Normed vector spaces satisfying the parallelogram law
---

## Proof

We define the candidate inner product by the polarization formula, and we show that the parallelogram law makes it additive, then homogeneous over $\mathbb{Q}$, then over $\mathbb{R}$ by continuity; the complex case and the uniqueness follow.
The direction from 1 to 2 is the [[parallelogram law|026HPGYGS4]], which holds in every inner product space.
For the direction from 2 to 1, let $(V, \norm{\cdot})$ be a [[normed vector space|00A0RPAQ8A]] whose norm satisfies the parallelogram law.

*Part A: the real case.*
Let $\mathbb{K} = \mathbb{R}$, and for $x, y \in V$ define
$$r(x, y) = \frac14\left(\norm{x + y}^2 - \norm{x - y}^2\right).$$

1. Symmetry: $\norm{y - x} = \norm{(-1)(x - y)} = \norm{x - y}$ by homogeneity of the norm, so $r(y, x) = r(x, y)$.
2. The diagonal: by homogeneity, $r(x, x) = \frac14(\norm{2x}^2 - \norm{0}^2) = \frac14 \cdot 4\norm{x}^2 = \norm{x}^2$.
3. Signs: by homogeneity, $r(-x, y) = \frac14(\norm{y - x}^2 - \norm{-(x + y)}^2) = -r(x, y)$.
   With $x = 0$ this gives $r(0, y) = -r(0, y)$, so $r(0, y) = 0$.
4. Apply the parallelogram law to the pairs $(u + y, v)$ and $(u - y, v)$:
$$\norm{u + v + y}^2 + \norm{u - v + y}^2 = 2\norm{u + y}^2 + 2\norm{v}^2,$$
$$\norm{u + v - y}^2 + \norm{u - v - y}^2 = 2\norm{u - y}^2 + 2\norm{v}^2.$$
5. Subtract the second line from the first and divide by $4$.
   The terms $2\norm{v}^2$ cancel, and for all $u, v, y \in V$ we get
$$r(u + v, y) + r(u - v, y) = 2r(u, y).$$
6. Doubling: put $v = u$ in step 5 and use $r(0, y) = 0$ from step 3, to get $r(2u, y) = 2r(u, y)$.
7. Additivity: for $x, x' \in V$, put $u = \frac12(x + x')$ and $v = \frac12(x - x')$, so that $u + v = x$ and $u - v = x'$.
   Steps 5 and 6 give $r(x, y) + r(x', y) = 2r(u, y) = r(2u, y) = r(x + x', y)$.
8. Integer multiples: for $n \geq 0$, induction with step 7 gives $r(nx, y) = n\,r(x, y)$, starting from $r(0, y) = 0$ and using $r((n + 1)x, y) = r(nx, y) + r(x, y)$.
   For $n < 0$, step 3 gives $r(nx, y) = -r(\abs{n}x, y) = n\,r(x, y)$.
9. Rational multiples: let $q = m/n$ with integers $m, n$ and $n \geq 1$.
   By step 8, $n\,r(qx, y) = r(nqx, y) = r(mx, y) = m\,r(x, y)$, so $r(qx, y) = q\,r(x, y)$.
10. Continuity: fix $x, y$ and put $g(t) = r(tx, y)$ for real $t$.
    The reverse [[triangle inequality for norms|0FJZMBX0ZZ]] gives
$$\big|\norm{tx \pm y} - \norm{sx \pm y}\big| \leq \norm{(t - s)x} = \abs{t - s}\,\norm{x}.$$
    So $t \mapsto \norm{tx + y}$ and $t \mapsto \norm{tx - y}$ are continuous, hence so are their squares and $g$.
11. Real multiples: let $t \in \mathbb{R}$.
    By the [[density of the rationals|0STX0WRDNG]], for each $k \geq 1$ there is a rational $q_k$ with $t < q_k < t + \frac1k$, so $q_k \to t$ in the sense of the [[limit of a sequence|05M5SWSZZD]].
12. By step 9, $g(q_k) = q_k\,r(x, y) \to t\,r(x, y)$.
    By step 10 and [[sequential continuity|055Z15H69G]], $g(q_k) \to g(t)$.
    A sequence has only one limit, so $r(tx, y) = t\,r(x, y)$.
13. By steps 7 and 12, $r$ is linear in the first slot, and by step 1 it is symmetric.
    By step 2, $r(x, x) = \norm{x}^2 > 0$ for $x \neq 0$, since a norm vanishes only at $0$.
    So $r$ is an [[inner product|0VGSYBWHV2]] on the real space $V$, and it induces $\norm{\cdot}$.

*Part B: the complex case.*
Let $\mathbb{K} = \mathbb{C}$.
Every complex vector space is also a real vector space, and the norm still satisfies the law, so Part A gives a real inner product $r$ on $V$ with $r(x, x) = \norm{x}^2$.
Define
$$\ip{x}{y} = r(x, y) + i\,r(x, iy).$$

14. Multiplication by $i$ keeps the norm, since $\norm{iz} = \abs{i}\,\norm{z} = \norm{z}$.
    With $z = x \pm y$ this gives $\norm{ix \pm iy} = \norm{x \pm y}$, so $r(ix, iy) = r(x, y)$.
15. Step 14 for the pair $(ix, y)$ and step 3 give
$$r(ix, y) = r(i \cdot ix, iy) = r(-x, iy) = -r(x, iy).$$
16. With $y = x$, step 15 gives $r(ix, x) = -r(x, ix)$.
    Symmetry gives $r(ix, x) = r(x, ix)$, so $r(x, ix) = 0$.
17. Real linearity: $r$ is real-linear in its first slot by Part A, so $\ip{\cdot}{y}$ is additive and $\ip{tx}{y} = t\ip{x}{y}$ for real $t$.
18. The factor $i$: by steps 15 and 14,
$$\ip{ix}{y} = r(ix, y) + i\,r(ix, iy) = -r(x, iy) + i\,r(x, y) = i\big(r(x, y) + i\,r(x, iy)\big) = i\ip{x}{y}.$$
19. Complex linearity: for $a = s + ti$ with $s, t$ real, steps 17 and 18 give $\ip{ax}{y} = s\ip{x}{y} + t\ip{ix}{y} = (s + ti)\ip{x}{y}$.
20. Conjugate symmetry: by the symmetry of $r$ and step 15,
$$\ip{y}{x} = r(y, x) + i\,r(y, ix) = r(x, y) + i\,r(ix, y) = r(x, y) - i\,r(x, iy) = \overline{\ip{x}{y}}.$$
21. The diagonal: by step 16, $\ip{x}{x} = r(x, x) + i \cdot 0 = \norm{x}^2$, which is positive for $x \neq 0$.
    So $\ip{\cdot}{\cdot}$ is a complex inner product, and it induces $\norm{\cdot}$.
22. The formula: expand
$$r(x, y) + i\,r(x, iy) = \frac14\left(\norm{x + y}^2 - \norm{x - y}^2\right) + \frac{i}{4}\left(\norm{x + iy}^2 - \norm{x - iy}^2\right).$$
    Since $i^2 = -1$ and $i^3 = -i$, this is $\frac14\sum_{k=0}^{3} i^k\norm{x + i^k y}^2$.

*Part C: uniqueness.*

23. Let $\ip{\cdot}{\cdot}'$ be any inner product on $V$ with $\ip{x}{x}' = \norm{x}^2$.
    The [[polarization identity|05FKHRT0B4]] expresses its values by the formula of Part A over $\mathbb{R}$, and by the formula of step 22 over $\mathbb{C}$.
24. These formulas involve only the norm.
    So $\ip{\cdot}{\cdot}'$ equals the inner product that we built, and the inner product is unique.

## Idea

Any inner product that induces the norm must be given by the polarization formula, so we take that formula as the definition and check the axioms.
Symmetry and the diagonal are immediate from homogeneity of the norm.
The real work is linearity, and the parallelogram law, applied twice and subtracted, gives additivity in the first slot.
Additivity gives homogeneity for rational scalars, and the continuity of the norm with the density of $\mathbb{Q}$ in $\mathbb{R}$ gives it for all real scalars.
Over $\mathbb{C}$, the isometry $x \mapsto ix$ turns the real inner product into the real part of a complex one.

## Variants

Steps 11 and 12 can avoid sequences.
An additive function from $\mathbb{R}$ to $\mathbb{R}$ that is continuous at one point is linear, as the page on [[additive functions|KF719SZD5T]] explains, and $g$ is additive by step 7.
The page on the [[quadratic functional equation|7MZGZFQ347]] runs the same argument for a general function $f$ with $f(x + y) + f(x - y) = 2f(x) + 2f(y)$.
