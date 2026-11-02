---
tag: K1YKXVPVDG
kind: statement
role: lemma
name: Calderón–Zygmund lemma
msc: [42B20, 42B25]
uses: [2Z2QVWZ262, DWJF7ABPR1]
about: [HTMCEARGDD]
sources:
  - url: https://en.wikipedia.org/wiki/Calder%C3%B3n%E2%80%93Zygmund_lemma
same_as:
  wikidata: Q1707076
  wikipedia: Calderón–Zygmund lemma
---

## Statement

Let $n \ge 1$, let $f \in L^1(\R^n)$ be an integrable function, and let $\alpha > 0$.
Then there are disjoint sets $F$ and $U$ with $\R^n = F \cup U$ such that:

1. $\abs{f(x)} \le \alpha$ for almost every $x \in F$;
2. $U$ is a countable union of closed cubes $Q_k$ with sides parallel to the axes and pairwise disjoint interiors;
3. for every $k$,
$$\alpha < \frac{1}{\abs{Q_k}}\int_{Q_k} \abs{f(x)} \, dx \le 2^n\alpha,$$
where $\abs{Q_k}$ is the [[Lebesgue measure|2Z2QVWZ262]] of $Q_k$.

## Remarks

The proof is a stopping-time argument on dyadic cubes.
Cut $\R^n$ into a grid of cubes so large that the average of $\abs{f}$ on each is at most $\alpha$.
Divide each cube into $2^n$ subcubes by halving its sides, keep the subcubes on which the average exceeds $\alpha$, and continue dividing the others.
A kept cube has a parent with average at most $\alpha$, which gives the bound $2^n\alpha$, and the Lebesgue differentiation theorem gives $\abs{f} \le \alpha$ almost everywhere on the points never kept.

Clause 3 gives $\abs{U} = \sum_k \abs{Q_k} \le \alpha^{-1}\norm{f}_{L^1}$.
Setting $g = f$ on $F$ and $g$ equal to the average of $f$ on each $Q_k$, and $b = f - g$, one obtains the Calderón–Zygmund decomposition $f = g + b$.
Here $\abs{g} \le 2^n\alpha$ almost everywhere, and $b$ has mean zero on each cube $Q_k$ and vanishes off $U$.

Example: for $n = 1$, $f = \mathbf{1}_{[0, 1]}$ and $\alpha = 1/2$, one may take $U = [0, 1]$ and $F = \R \setminus [0, 1]$; the average of $\abs{f}$ on $[0, 1]$ is $1$, which lies in $(1/2, 1]$.

## Explanations

### L1 human

The lemma splits space into a part where $f$ is small, at most $\alpha$, and a collection of cubes where $f$ is large on average, but not too large.
The large part occupies little volume, at most $\norm{f}_{L^1}/\alpha$.
It is the basic tool for studying functions that are only integrable, without any better bound.

### L2 human

The lemma, through the decomposition $f = g + b$, is the key step in proving that [[singular integral operators|HTMCEARGDD]] are of weak type $(1, 1)$.
The good part $g$ is bounded and integrable, so it lies in $L^2$, where the operator is bounded.
The bad part $b$ has mean zero on each cube, and the smoothness of the kernel controls the operator on it away from the cubes.
The same stopping-time idea gives the weak type $(1, 1)$ bound for the [[Hardy–Littlewood maximal function|VX1A56P5KQ]] and the John–Nirenberg inequality.
