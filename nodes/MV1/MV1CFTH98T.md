---
tag: MV1CFTH98T
kind: statement
role: theorem
name: Zaslavsky's theorem
msc: [52C35, 05B35, "06A07"]
uses: [N602W0WAVT, 2Y75S8NG5B, 0QV2JS9RJ3, PX31ZNYS3Z, 0B621RBVS9]
about: [N602W0WAVT]
sources:
  - url: https://en.wikipedia.org/wiki/Arrangement_of_hyperplanes
---

## Statement

Let $\mathcal{A}$ be a [[hyperplane arrangement|N602W0WAVT]] in $\R^d$.
Let $L(\mathcal{A})$ be its intersection poset: the nonempty intersections of subsets of $\mathcal{A}$, with $\R^d$ included.
It is [[ordered|0QV2JS9RJ3]] by reverse inclusion, so that $\R^d$ is the least element.
For $x \in L(\mathcal{A})$ let $\mu(x) = \mu(\R^d, x)$, where $\mu$ is the [[Möbius function|2Y75S8NG5B]] of $L(\mathcal{A})$.
The characteristic polynomial of $\mathcal{A}$ is
$$\chi_{\mathcal{A}}(t) = \sum_{x \in L(\mathcal{A})} \mu(x) \, t^{\dim x}.$$
Let $r(\mathcal{A})$ be the number of regions of $\mathcal{A}$, the connected components of $\R^d \setminus \bigcup_{H \in \mathcal{A}} H$, and let $b(\mathcal{A})$ be the number of bounded regions.
Let $\rank \mathcal{A}$ be the dimension of the span of the normal vectors of the hyperplanes of $\mathcal{A}$.
Then:

1. $r(\mathcal{A}) = (-1)^d \chi_{\mathcal{A}}(-1) = \sum_{x \in L(\mathcal{A})} \abs{\mu(x)}$.
2. $b(\mathcal{A}) = (-1)^{\rank \mathcal{A}} \chi_{\mathcal{A}}(1)$.

## Remarks

The theorem is due to Thomas Zaslavsky, in 1975.
Proof idea: fix $H \in \mathcal{A}$, and let $\mathcal{A}'$ be $\mathcal{A}$ without $H$ and $\mathcal{A}''$ the arrangement induced on $H$.
Each region of $\mathcal{A}'$ is either untouched by $H$ or cut in two, and the cut regions correspond to regions of $\mathcal{A}''$, so $r(\mathcal{A}) = r(\mathcal{A}') + r(\mathcal{A}'')$.
The characteristic polynomial satisfies the matching recursion $\chi_{\mathcal{A}} = \chi_{\mathcal{A}'} - \chi_{\mathcal{A}''}$, and induction on the number of hyperplanes finishes the proof; the second count is similar.

Example: $n$ lines in general position in $\R^2$, no two parallel and no three through a point.
Here $\chi(t) = t^2 - n t + \binom{n}{2}$, so $r = 1 + n + \binom{n}{2}$ and $b = 1 - n + \binom{n}{2} = \binom{n-1}{2}$.
For $n = 3$ this gives $7$ regions, $1$ of them bounded.

Example: the braid arrangement of the hyperplanes $x_i = x_j$, $1 \le i < j \le n$, in $\R^n$ has $\chi(t) = t(t-1)\cdots(t-n+1)$, so it has $n!$ regions, one for each ordering of the coordinates.

## Explanations

### L1 human

Cut space with finitely many flat walls; how many pieces do you get?
Zaslavsky's theorem says that the answer depends only on how the walls meet, not on their exact positions.
You record which intersections occur, compute one polynomial from this data, and evaluate it at $-1$ to count all pieces and at $1$ to count the bounded ones.

### L2 human

The theorem turns a geometric counting problem into a computation in the intersection poset, through its [[Möbius function|2Y75S8NG5B]].
For a central arrangement, $L(\mathcal{A})$ is a geometric lattice, and $\chi_{\mathcal{A}}$ is the characteristic polynomial of the associated [[matroid|PX31ZNYS3Z]].
The graphic arrangement of a graph $G$ on $n$ vertices has the hyperplanes $x_i = x_j$ for the edges $ij$.
Its characteristic polynomial is the [[chromatic polynomial|0B621RBVS9]] $\chi_G$ of $G$.
So the theorem says that $(-1)^n \chi_G(-1)$ counts the acyclic orientations of $G$, a result of Stanley.
When the hyperplanes have integer equations, $\chi_{\mathcal{A}}(q)$ counts the points of $\F_q^d$ off the reduced hyperplanes for every large enough prime $q$, which gives another route to computing it.
