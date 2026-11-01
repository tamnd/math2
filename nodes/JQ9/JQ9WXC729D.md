---
tag: JQ9WXC729D
kind: statement
role: theorem
name: Hölder's inequality
msc: [26D15, "46E30", 28A25]
uses: [07VHQ31EYJ]
sources:
  - url: https://en.wikipedia.org/wiki/Hölder%27s_inequality
same_as:
  wikidata: Q731894
  wikipedia: Hölder's inequality
---

## Statement

Let $(S, \Sigma, \mu)$ be a measure space.
Let $p, q \in (1, \infty)$ with $\frac{1}{p} + \frac{1}{q} = 1$.
Let $f, g \colon S \to \R$ be measurable functions.
Then, with the integrals taking values in $[0, \infty]$ and the convention $0 \cdot \infty = 0$,
$$\int_S \abs{f g} \, d\mu \le \Big( \int_S \abs{f}^p \, d\mu \Big)^{1/p} \Big( \int_S \abs{g}^q \, d\mu \Big)^{1/q}.$$

## Remarks

Proof idea: if a factor on the right is $0$ or $\infty$ the claim is easy.
Otherwise scale $f$ and $g$ so that both factors are $1$, apply [[Young's inequality|07VHQ31EYJ]] $ab \le \frac{a^p}{p} + \frac{b^q}{q}$ pointwise to $\abs{f(s)}$ and $\abs{g(s)}$, and integrate.
When the right side is finite, equality holds if and only if there are constants $\alpha, \beta \ge 0$, not both $0$, with $\alpha \abs{f}^p = \beta \abs{g}^q$ almost everywhere.

With the counting measure on $\set{1, \dots, n}$ the statement becomes [[Hölder's inequality for sums|0BKDAGMGX9]].
For $p = q = 2$ it is the [[Cauchy–Schwarz inequality|0RFWW56Y22]] for integrals.
The same bound holds for $p = 1$ and $q = \infty$, with the essential supremum of $\abs{g}$ in place of the second factor.

## Explanations

### L1 human

Hölder's inequality bounds the integral of a product by the sizes of the two factors.
The size of $f$ is measured with the exponent $p$ and the size of $g$ with the matching exponent $q$.
It is the main tool for showing that a product of two functions is integrable.

### L2 human

In the language of Lp spaces, it says $\norm{f g}_1 \le \norm{f}_p \norm{g}_q$.
So each $g \in L^q$ gives a bounded linear functional on $L^p$, which is the start of the duality between $L^p$ and $L^q$.
It is also the key step in the proof of the [[Minkowski inequality|N4QZS912MT]], the triangle inequality in $L^p$.
