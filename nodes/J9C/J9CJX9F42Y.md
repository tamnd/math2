---
tag: J9CJX9F42Y
kind: statement
role: theorem
name: Prékopa–Leindler inequality
msc: [26D15, 52A40]
uses: [DWJF7ABPR1, YYNCJSR0PJ]
about: [DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Prékopa–Leindler_inequality
same_as:
  wikidata: Q7253815
  wikipedia: Prékopa–Leindler inequality
---

## Statement

Let $n \ge 1$ and $0 < t < 1$.
Let $f, g, h \colon \R^n \to [0, \infty)$ be Lebesgue [[measurable functions|YYNCJSR0PJ]] such that
$$h((1-t) x + t y) \ge f(x)^{1-t} g(y)^{t} \quad \text{for all } x, y \in \R^n.$$
Then
$$\int_{\R^n} h \, dx \ge \left(\int_{\R^n} f \, dx\right)^{1-t} \left(\int_{\R^n} g \, dx\right)^{t}.$$

## Remarks

The integrals are [[Lebesgue integrals|DWJF7ABPR1]] and may be infinite.
The proof for $n = 1$ uses a transport map between $f$ and $g$ after normalisation, and the general case follows by induction on $n$ with Fubini's theorem.
Example: let $A, B$ be nonempty compact sets and $f = 1_A$, $g = 1_B$, $h = 1_{(1-t)A + tB}$.
The hypothesis holds, and the conclusion gives $\lambda((1-t) A + t B) \ge \lambda(A)^{1-t} \lambda(B)^{t}$.
This multiplicative form implies the [[Brunn–Minkowski theorem|9B02RPN7XD]] by scaling $A$ and $B$.
It is a reversed form of Hölder's inequality: Hölder bounds $\int f^{1-t} g^t$ from above, while here a function above the "sup-convolution" is bounded from below.

## Explanations

### L1 human

If a function $h$ is large at each weighted midpoint of points where $f$ and $g$ are large, then the integral of $h$ is large too.
It is the functional version of the Brunn–Minkowski inequality for volumes of sums of sets.

### L2 human

A main consequence is that log-concave functions and measures are stable: marginals and convolutions of log-concave densities are log-concave.
This makes the inequality a basic tool in convex geometry and in the concentration of measure, for example for Gaussian measures.
