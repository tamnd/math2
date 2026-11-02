---
tag: CB4Y87RC4V
kind: definition
name: Rigid analytic space
msc: [14G22, 12J25]
defines: YAH6MZVG7K
uses: [1H5F1BP6XS, BT6T702C28, KNDXDE7K8M, TB6TM6R4MD]
sources:
  - url: https://en.wikipedia.org/wiki/Rigid_analytic_space
---

## Definition

Let $K$ be a field complete for a nontrivial [[non-archimedean absolute value|1H5F1BP6XS]] $\abs{\cdot}$.
The *Tate algebra* in $n$ variables is
$$T_n = K\langle x_1, \dots, x_n \rangle = \set{\textstyle\sum_{\nu \in \N^n} a_\nu x^\nu : a_\nu \in K,\ \abs{a_\nu} \to 0 \text{ as } \abs{\nu} \to \infty},$$
the algebra of power series that converge on the closed unit polydisc.
An *affinoid algebra* is a $K$-algebra $A$ isomorphic to a quotient $T_n / I$ for some $n$ and some ideal $I$.
The *affinoid space* $\operatorname{Sp} A$ is the set of maximal ideals of $A$ with a Grothendieck topology and a structure [[sheaf|TB6TM6R4MD]] $\mathcal{O}$.
In this topology the admissible opens are the finite unions of affinoid subdomains.
The admissible coverings are the finite coverings by such sets.
A *rigid analytic space* over $K$ is a set $X$ with a Grothendieck topology and a sheaf of $K$-algebras, as a [[ringed space|KNDXDE7K8M]].
It must have an admissible covering by open subsets each isomorphic, with these structures, to an affinoid space.

## Remarks

That $\mathcal{O}$ is a sheaf for finite affinoid coverings is Tate's acyclicity theorem.
The general admissible opens and coverings are defined from these by a standard extension of the topology.

Example: $\operatorname{Sp} T_1$ is the closed unit disc.
Its points are the maximal ideals of $T_1$, which correspond to elements $x$ of an algebraic closure of $K$ with $\abs{x} \le 1$, up to conjugation over $K$.

Non-example of an admissible covering: for $K = \Q_p$, the closed disc $\operatorname{Sp} T_1$ is the disjoint union of the open disc $\set{\abs{x} < 1}$ and the circle $\set{\abs{x} = 1}$.
This covering is not admissible.
Every affinoid subdomain of the open disc lies in a disc $\set{\abs{x} \le r}$ with $r < 1$.
So no finite family of affinoid subdomains of the two pieces covers the points with $r < \abs{x} < 1$.
This is what keeps the closed disc connected in rigid geometry.

The analytification of a variety of finite type over $K$ is a rigid analytic space, and a rigid GAGA theorem compares coherent sheaves on both sides for proper varieties.
