---
tag: ZYY3FJ57NQ
kind: definition
name: Thom–Boardman singularities
msc: [57R45, 58K30, 58K05]
defines: A9TYDPD5D7
uses: [1JG3HFWX3T, F45VQ47GPV, 6P9PXQDSEN, 1QE0Z0756D, A2PDZ8GA9C]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
---

## Definition

Let $f \colon M \to N$ be a smooth map between [[smooth manifolds|F45VQ47GPV]].
For an integer $i \ge 0$ let
$$\Sigma^{i}(f) = \set{p \in M : \dim \ker df_p = i},$$
where $df_p$ is the [[differential|6P9PXQDSEN]] of $f$ at $p$.
Inductively, let $I = (i_1, \ldots, i_k)$ and suppose that $\Sigma^{I}(f)$ is a submanifold of $M$.
For $j \ge 0$ let $\Sigma^{i_1, \ldots, i_k, j}(f)$ be the set of points of $\Sigma^{I}(f)$ where the restriction $f|_{\Sigma^I(f)}$ has kernel of dimension $j$, that is, $\Sigma^{j}(f|_{\Sigma^I(f)})$.
A point $p$ has *Thom–Boardman symbol* $I$ when $p \in \Sigma^I(f)$, whenever these sets are defined.

## Remarks

Since $\Sigma^{i_1, \ldots, i_k}(f) \subseteq \Sigma^{i_1, \ldots, i_{k-1}}(f)$, the kernel of $f$ restricted to the smaller set lies in the kernel of $f$ restricted to the larger one.
So the symbols are non-increasing: $i_1 \ge i_2 \ge \cdots \ge i_k$.
Boardman constructed submanifolds $\Sigma^I$ of the [[jet space|1QE0Z0756D]] $J^k(M, N)$, depending only on $I$.
Suppose the jet extension $j^k f$ is [[transverse|A2PDZ8GA9C]] to all of them.
Then each $\Sigma^I(f) = (j^k f)^{-1}(\Sigma^I)$ is a submanifold and agrees with the inductive definition.
By Thom's transversality theorem, this holds for a dense set of maps.
If $\dim M = m$ and $\dim N = n$, the subset $\Sigma^i$ of $J^1(M, N)$ has codimension $i(n - m + i)$.
Example: for $f(x, y) = (x, y^3 + xy)$ on $\R^2$, $\Sigma^1(f)$ is the curve $x = -3y^2$.
Parametrising it by $y \mapsto (-3y^2, y)$, the restriction of $f$ is $y \mapsto (-3y^2, -2y^3)$, whose derivative vanishes only at $y = 0$.
So the origin lies in $\Sigma^{1,1}(f)$, and the other points of the curve lie in $\Sigma^{1,0}(f)$.
Non-example: for $f(x, y) = (x, y^3 - x^2 y)$, $\Sigma^1(f)$ is the set $3y^2 = x^2$, a pair of crossing lines.
It is not a submanifold at the origin, so the inductive definition breaks down there; the jet of $f$ is not transverse to $\Sigma^1$.

## Explanations

### L1 human

The symbol of a singular point records how badly a map degenerates, one layer at a time.
The first entry counts the directions crushed by the map.
The next entry counts the directions crushed by the map along the set of points that share the first entry.
The construction is clean only for generic maps, where all these sets are smooth.
