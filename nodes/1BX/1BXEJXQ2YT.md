---
tag: 1BXEJXQ2YT
kind: statement
role: theorem
name: Banach–Alaoglu theorem
msc: [46A50, 46A20, 46B10]
uses: [0ZCY0Z80B6, 4A82S5FVRT, P6KHVSTPZV, 0R6EWFKRCF]
about: [4A82S5FVRT, P6KHVSTPZV]
sources:
  - url: https://en.wikipedia.org/wiki/Banach–Alaoglu_theorem
same_as:
  wikidata: Q537618
  wikipedia: Banach–Alaoglu theorem
---

## Statement

Let $\mathbb{K}$ be $\R$ or $\C$, and let $E$ be a topological vector space over $\mathbb{K}$ with [[continuous dual|4A82S5FVRT]] $E'$.
Let $U$ be a [[neighbourhood|0ZCY0Z80B6]] of $0$ in $E$.
Then the polar
$$U^\circ = \set{f \in E' : \abs{f(x)} \le 1 \text{ for all } x \in U}$$
is [[compact|0R6EWFKRCF]] in the weak-\* topology $\sigma(E', E)$, the [[weak topology|P6KHVSTPZV]] on $E'$.
In particular, if $E$ is a normed space, the closed unit ball $\set{f \in E' : \norm{f} \le 1}$ is weak-\* compact.

## Remarks

Since $U$ is absorbing, each $x \in E$ lies in $r_x U$ for some $r_x > 0$, so $\abs{f(x)} \le r_x$ for $f \in U^\circ$.
Hence $U^\circ$ sits inside the product $P = \prod_{x \in E} \set{c \in \mathbb{K} : \abs{c} \le r_x}$, which is compact by [[Tychonoff's theorem|0JTRSJKCFB]], and the weak-\* topology is the topology induced by the product topology.
The functions in $P$ that are linear and bounded by $1$ on $U$ form a closed subset of $P$.
Each such function is continuous, since it is bounded on a neighbourhood of $0$.
So this closed subset is $U^\circ$, and it is compact.
Example: for $E = c_0$, the dual is $\ell^1$, and the closed unit ball of $\ell^1$ is weak-\* compact, although it is not compact in norm.
The weak-\* topology is needed: in an infinite-dimensional normed space $E$, the closed unit ball of $E'$ is never compact in the norm topology.
The theorem gives compactness, not sequential compactness.
If $E$ is a separable normed space, the closed unit ball of $E'$ is weak-\* metrizable, and every bounded sequence in $E'$ has a weak-\* convergent subsequence.

## Explanations

### L1 human

In infinite dimension, closed bounded sets are usually not compact, which makes it hard to find limits.
The theorem rescues compactness by weakening the topology.
On the dual of a normed space, the unit ball becomes compact once convergence means convergence at each vector separately.
This is often enough to extract a limit from a bounded family of functionals.

### L2 human

The Banach–Alaoglu theorem is the standard source of compactness in functional analysis.
It is used to prove existence results, for instance minimizers in the calculus of variations, weak solutions of partial differential equations, and invariant means and measures.
With [[Goldstine's theorem|K4S9G3AQBM]], it characterizes reflexive Banach spaces by the weak compactness of their unit ball.
With the [[Krein–Milman theorem|RSRAY0Q68S]], it shows that the dual unit ball has many extreme points.
In duality theory, it says that polars of neighbourhoods of $0$ are weak-\* compact, which is a key step of the [[Mackey–Arens theorem|RKKWS7CDNF]].
