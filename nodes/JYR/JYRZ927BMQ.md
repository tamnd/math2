---
tag: JYRZ927BMQ
kind: statement
role: theorem
name: Jensen's inequality for integrals
msc: [26D15, 28A25, "60E15"]
uses: [0VGMEBVW1M, 0VV0HSW1ZS, X7GTF3D98F, DWJF7ABPR1]
about: [0VV0HSW1ZS, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Jensen%27s_inequality
---

## Statement

Let $(X, \Sigma, \mu)$ be a measure space with $\mu$ a [[probability measure|0VGMEBVW1M]], that is, $\mu(X) = 1$.
Let $-\infty \le a < b \le \infty$ and let $g \colon X \to (a, b)$ be an [[integrable function|X7GTF3D98F]].
Let $\varphi \colon (a, b) \to \R$ be a [[convex function|0VV0HSW1ZS]].
Then $\int_X g \, d\mu$ lies in $(a, b)$, and the negative part of $\varphi \circ g$ is integrable.
Moreover,
$$\varphi\Big( \int_X g \, d\mu \Big) \le \int_X \varphi \circ g \, d\mu,$$
where the integrals are [[Lebesgue integrals|DWJF7ABPR1]] and the right side may be $+\infty$.

## Remarks

Proof idea: let $m = \int g \, d\mu$.
A convex function on an open interval has a supporting line at $m$: there is $c \in \R$ with $\varphi(y) \ge \varphi(m) + c (y - m)$ for all $y \in (a, b)$.
Put $y = g(x)$ and integrate over $X$; the term $c(g - m)$ has integral $0$ because $\mu(X) = 1$.

Example: with $\varphi(y) = y^2$ it gives $(\int g \, d\mu)^2 \le \int g^2 \, d\mu$.
In probability this is $\operatorname{Var}(Y) \ge 0$.
With $\varphi = \exp$ it gives $\exp(\int g \, d\mu) \le \int e^{g} \, d\mu$.

The normalisation $\mu(X) = 1$ is needed.
For $\mu = 2 \cdot$ Lebesgue measure on $[0, 1]$, $g = 1$ and $\varphi(y) = y^2$, the left side is $4$ and the right side is $2$.
When $\mu$ is the probability measure with masses $w_i$ at finitely many points, the statement is the finite [[Jensen's inequality|0RWMRTPC87]].

## Explanations

### L1 human

The value of a convex function at an average is at most the average of its values.
Here the average is an integral against a probability measure, so it covers both weighted sums and continuous averages.
The graph of a convex function bends upwards, which is why averaging after applying the function gives the larger result.

### L2 human

In probability the inequality reads $\varphi(\mathbb{E}[Y]) \le \mathbb{E}[\varphi(Y)]$ for an integrable random variable $Y$.
It yields the comparison $\norm{f}_p \le \norm{f}_q$ for $p \le q$ on probability spaces, the AM–GM inequality, and the non-negativity of the Kullback–Leibler divergence.
There is also a version for conditional expectations, used in martingale theory.
