---
tag: KD9BP7YJK5
kind: definition
name: Approximation property
msc: [46B28]
defines: 8CKE0V6ANK
uses: [06GZ956657, 03TM135G0N, 0R6EWFKRCF]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_property
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]] over $\R$ or $\C$.
A [[continuous linear map|03TM135G0N]] $T \colon X \to X$ has *finite rank* if its image $T(X)$ is finite-dimensional.
The space $X$ has the *approximation property* if the following holds.
For every [[compact|0R6EWFKRCF]] set $K \subseteq X$ and every $\varepsilon > 0$ there is a continuous linear map $T \colon X \to X$ of finite rank such that $\norm{Tx - x} < \varepsilon$ for all $x \in K$.

## Remarks

Example: let $X$ have a Schauder basis $(e_n)$, and let $P_n$ be the projection $\sum_k a_k e_k \mapsto \sum_{k \le n} a_k e_k$.
Each $P_n$ is continuous (a theorem of Banach) and has finite rank, $P_n x \to x$ for every $x$, and $\sup_n \norm{P_n} < \infty$ by the [[uniform boundedness principle|YG0042V8CJ]].
Pointwise convergence of a uniformly bounded sequence of operators is uniform on compact sets, so the $P_n$ witness the approximation property.
In particular $\ell^p$ for $1 \le p < \infty$ and $c_0$ have it.
Every [[Hilbert space|HM2HHE3J51]] has it too, using orthogonal projections onto finite-dimensional subspaces, even when it has no countable basis.
Non-example: the space built in [[Enflo's counterexample|ZKP5KGFWCK]] fails the definition for some compact set $K$ and some $\varepsilon > 0$.
Grothendieck's equivalent form: $X$ has the approximation property if and only if for every Banach space $Y$, every compact operator $Y \to X$ is a norm limit of finite-rank operators.
