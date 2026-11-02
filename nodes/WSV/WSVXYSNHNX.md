---
tag: WSVXYSNHNX
kind: statement
role: theorem
name: Lebesgue's density theorem
msc: [28A15, 28A75]
uses: [2Z2QVWZ262, RARTMA0ZEC, 0YE5868HZB]
about: [2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue's_density_theorem
same_as:
  wikidata: Q842953
  wikipedia: Lebesgue's density theorem
---

## Statement

Let $n \ge 1$, let $\lambda$ be [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$, and let $A \subseteq \R^n$ be Lebesgue measurable.
For $x \in \R^n$ and $r > 0$, let $B(x, r)$ be the [[open ball|0YE5868HZB]] of centre $x$ and radius $r$.
Then for [[almost every|RARTMA0ZEC]] $x \in A$,
$$\lim_{r \to 0^+} \frac{\lambda(A \cap B(x, r))}{\lambda(B(x, r))} = 1,$$
and for almost every $x \in \R^n \setminus A$ the same limit equals $0$.

## Remarks

Apply the Lebesgue differentiation theorem to the indicator function $\mathbf{1}_{A \cap B(0, R)}$ for each integer $R$.
Its ball averages are exactly the ratios in the statement, and its values are $1$ on $A \cap B(0,R)$ and $0$ off it.

Example: for $A = [0, \infty) \subseteq \R$, the density is $1$ at every $x > 0$, $0$ at every $x < 0$, and $1/2$ at $x = 0$.
The exceptional set $\{0\}$ has measure zero, as the theorem allows.

The theorem says that a measurable set cannot be spread out evenly at small scales: near almost every one of its points it fills almost all of a small ball.
For instance, no measurable $A \subseteq [0,1]$ can satisfy $\lambda(A \cap I) = \lambda(I)/2$ for every interval $I \subseteq [0,1]$.

## Explanations

### L1 human

Pick a measurable set and zoom in on one of its points.
For almost every point of the set, the set fills almost the whole view as one zooms in.
For almost every point outside the set, the set almost disappears from view.

### L2 human

The points where the density is $1$ are called density points.
The density theorem is used to show that measurable sets are, up to null sets, sets of density points, which leads to the density topology on $\R$.
It can also be used to prove the Steinhaus theorem that $A - A$ contains an interval around $0$ when $\lambda(A) > 0$.
