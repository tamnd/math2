---
tag: 7ZR88SCSRF
kind: statement
role: lemma
name: Mazur's lemma
msc: [46B10, 46A55]
uses: [03J5RAKB30, P6KHVSTPZV, 0KJH6SRFZK]
about: [P6KHVSTPZV]
sources:
  - url: https://en.wikipedia.org/wiki/Mazur%27s_lemma
same_as:
  wikidata: Q2226764
  wikipedia: Mazur's lemma
---

## Statement

Let $X$ be a [[normed vector space|03J5RAKB30]] over $\R$ or $\C$.
Let $(x_n)_{n \ge 1}$ be a sequence in $X$ that converges to $x \in X$ in the [[weak topology|P6KHVSTPZV]].
For each $n \ge 1$ there are an integer $N(n) \ge n$ and real numbers $\lambda_{n,k} \ge 0$ for $n \le k \le N(n)$, with $\sum_{k=n}^{N(n)} \lambda_{n,k} = 1$, with the following property.
The convex combinations
$$y_n = \sum_{k=n}^{N(n)} \lambda_{n,k}\, x_k$$
converge to $x$ in norm.

## Remarks

Fix $n$ and let $C_n$ be the norm closure of the convex hull of $\set{x_k : k \ge n}$.
By the [[Hahn–Banach separation theorem|6GWMGFGFJJ]], a norm-closed convex set is weakly closed, so $C_n$ is weakly closed.
Since $x_k \to x$ weakly and $x_k \in C_n$ for $k \ge n$, the limit $x$ lies in $C_n$.
Hence some convex combination $y_n$ of finitely many $x_k$ with $k \ge n$ satisfies $\norm{y_n - x} < 1/n$.

In the sequence space $\ell^2$, the unit vectors $e_n$ converge weakly to $0$ but $\norm{e_n} = 1$ for all $n$.
The averages $y_n = \frac{1}{n}(e_n + e_{n+1} + \cdots + e_{2n-1})$ have $\norm{y_n} = 1/\sqrt{n}$, so they tend to $0$ in norm, as the lemma predicts.

## Explanations

### L1 human

Weak convergence is a loose kind of convergence, and a weakly convergent sequence may stay far from its limit.
The lemma says that averaging repairs this.
Suitable averages of the later terms of the sequence do converge in the usual sense of distance.

### L2 human

The lemma is a quantitative form of the fact that a convex set has the same closure in the norm topology and in the weak topology.
It is used in the calculus of variations and in partial differential equations: one obtains a weak limit from compactness.
Then one uses the lemma to pass to strong limits of averages, which interact well with convex functionals.
For example, it shows that a convex lower semicontinuous functional on a Banach space is weakly lower semicontinuous.
