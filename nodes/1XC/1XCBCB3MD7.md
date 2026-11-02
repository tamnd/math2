---
tag: 1XCBCB3MD7
kind: statement
role: theorem
name: Cartan–Thullen theorem
msc: [32D05, "32E05", 32T05]
uses: [4487CSC0MB, D5J6CP5V2Z, CD6SMMZSW8, 507C34W0ZT]
about: [4487CSC0MB, D5J6CP5V2Z]
sources:
  - url: https://en.wikipedia.org/wiki/Domain_of_holomorphy
---

## Statement

Let $D \subseteq \C^n$ be a domain, that is, a nonempty connected open set.
The following are equivalent.

1. $D$ is a [[domain of holomorphy|4487CSC0MB]].
2. $D$ is [[holomorphically convex|D5J6CP5V2Z]]: for every compact set $K \subseteq D$, its [[holomorphically convex hull|CD6SMMZSW8]] $\hat K_D$ is compact.
3. There is a [[holomorphic function|507C34W0ZT]] $f$ on $D$ that cannot be continued beyond $D$. That is, there are no nonempty open sets $U_1 \subseteq D \cap U_2$, with $U_2$ connected and $U_2 \not\subseteq D$, and no holomorphic $g$ on $U_2$ with $g = f$ on $U_1$.

## Remarks

Clause 3 implies clause 1 directly from the definition.
For 1 implies 2, the key estimate concerns a domain of holomorphy $D$.
The distance from $\hat K_D$ to the boundary of $D$ equals the distance from $K$ to the boundary, measured with polydiscs.
It comes from the Cauchy estimates: the Taylor series at points of $\hat K_D$ of every holomorphic function on $D$ converge on polydiscs of a fixed radius.
For 2 implies 3, take a sequence of points of $D$ that accumulates at every boundary point.
Holomorphic convexity gives holomorphic functions that are large at chosen points of the sequence.
An infinite product or series of them gives a function unbounded near every boundary point.

Example: a convex domain is holomorphically convex, because $\abs{e^{\ell}} = e^{\operatorname{Re} \ell}$ for complex linear $\ell$ shows that $\hat K_D$ lies in the convex hull of $K$; so it is a domain of holomorphy.

## Explanations

### L1 human

There are three ways to say that a domain has no hidden extensions.
One can ask that not all functions extend across any boundary point, or that one single function refuses to extend anywhere, or a convexity condition defined with holomorphic functions.
The theorem says these three conditions are the same.

### L2 human

Holomorphic convexity is an intrinsic condition, stated without reference to points outside $D$.
This makes it the right condition to generalise to complex manifolds, where it leads to the notion of a Stein manifold.
It reduces the Levi problem to showing that pseudoconvex domains are holomorphically convex.
For $n = 1$ every domain satisfies all three conditions.
