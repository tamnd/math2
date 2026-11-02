---
tag: 7H3YSSDEBK
kind: statement
role: theorem
name: Schaefer's fixed point theorem
msc: [47H10, 47J05]
uses: [06GZ956657, 0X3WGX95FE, DCPFVVZZ54]
about: [06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Schauder_fixed-point_theorem
---

## Statement

Let $X$ be a real [[Banach space|06GZ956657]] and let $A \colon X \to X$ be a [[continuous|0X3WGX95FE]] map.
Assume that $A$ is compact: it maps each bounded subset of $X$ into a relatively compact set.
Assume that the set
$$\set{u \in X : u = \lambda A(u) \text{ for some } \lambda \in [0, 1]}$$
is bounded.
Then $A$ has a fixed point: there is $u \in X$ with $A(u) = u$.

## Remarks

The proof uses the [[Schauder fixed-point theorem|DCPFVVZZ54]].
Choose $M$ larger than the norm of every $u$ in the bounded set of the hypothesis, and let $B$ be the closed ball of radius $M$.
On $B$, define $\tilde A(u) = A(u)$ if $\norm{A(u)} \le M$ and $\tilde A(u) = M A(u)/\norm{A(u)}$ otherwise.
Then $\tilde A$ maps $B$ continuously into a compact subset of $B$, so it has a fixed point $u$.
If $\norm{A(u)} > M$, then $u = \lambda A(u)$ with $\lambda = M/\norm{A(u)} < 1$ and $\norm{u} = M$, which contradicts the choice of $M$; so $A(u) = u$.

The hypothesis is an a priori bound: one shows that all solutions of the family of problems $u = \lambda A(u)$ lie in a fixed ball, without knowing in advance that any exists.

Example: on $X = \R$, let $A(u) = 1 + \frac{1}{2}\sin u$.
If $u = \lambda A(u)$ with $\lambda \in [0, 1]$, then $\abs{u} \le 3/2$, so the set is bounded, and $A$ has a fixed point.

The a priori bound is necessary: $A(u) = u + 1$ on $\R$ is continuous and compact, but has no fixed point, and the solutions $u = \lambda/(1 - \lambda)$ of $u = \lambda A(u)$ are unbounded as $\lambda \to 1$.

## Explanations

### L1 human

To show that an equation $u = A(u)$ has a solution, it is enough to deform it into a trivial problem, $u = 0$, through the family $u = \lambda A(u)$.
If all the solutions along the way stay in a bounded region, a solution survives at the end.
This turns an existence question into the often easier task of proving estimates.

### L2 human

The theorem is a standard tool for nonlinear elliptic and parabolic equations, as in Evans's book on partial differential equations.
One writes the equation as $u = A(u)$, where $A$ solves a linear problem with the nonlinearity frozen, and gets compactness of $A$ from elliptic regularity and a compact Sobolev embedding.
The a priori bound is then proved by energy estimates or the maximum principle.
It is a special case of the Leray–Schauder continuation principle, which is based on degree theory.
