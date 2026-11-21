---
tag: 96Q4P7PZVY
kind: statement
role: theorem
name: Kechris-Pestov-Todorcevic correspondence
aliases: [kechris-pestov-todorcevic-correspondence, kpt-correspondence, extreme-amenability-and-ramsey-classes]
msc: ["03C15", "05D10", "22F50", "37B05"]
topics: [ZS8X8KS54R]
audience: research
about: [8XS8FCTF8T, HJVRBDQSGG]
uses: [HJVRBDQSGG, 8XS8FCTF8T, H8VM37SSAX, 0QPHW703PV, 0S1FJ8VEX9, 0YSE802YCQ, FVGB8ZP67B, 92700QAB5Y, CEAT9BESKK]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_Ramsey_theory
    locator: The Kechris–Pestov–Todorčević correspondence
---

## Statement

Let $L$ be a countable relational signature containing a binary symbol $<$.
Let $\mathcal{K}$ be a Fraïssé class of finite $L$-structures in which $<$ is a linear order, with [[Fraïssé limit|HJVRBDQSGG]] $F$.
Give $G = \operatorname{Aut}(F)$ the [[topology of pointwise convergence|FVGB8ZP67B]].
Then the following are equivalent:

1. $G$ is *extremely amenable*: every continuous [[action|0YSE802YCQ]] of $G$ on a nonempty [[compact|0QPHW703PV]] [[Hausdorff space|0S1FJ8VEX9]] has a fixed point;
2. $\mathcal{K}$ is a [[Ramsey class|8XS8FCTF8T]]: for $A \le B$ in $\mathcal{K}$ and $k \ge 2$, some $C \in \mathcal{K}$ has the property that every $k$-coloring of the copies of $A$ in $C$ is constant on the copies of $A$ inside some copy of $B$.

## Remarks

### Why each hypothesis is needed

- The order: the class of finite sets satisfies the coloring condition, by Ramsey's theorem, but $\operatorname{Sym}(\N)$ is not extremely amenable. It acts on the compact space of linear orders on $\N$ without a fixed point.
- Fraïssé class: the group of a structure that is not ultrahomogeneous does not act transitively on copies of $A$, and the passage between colorings and orbits breaks down.

### Consequences

- $\operatorname{Aut}(\Q, <)$ is extremely amenable, since finite linear orders form a Ramsey class by Ramsey's theorem.
- The automorphism group of the ordered Rado graph is extremely amenable, by the Nešetřil-Rödl theorem.
- An extremely amenable group is [[amenable|CEAT9BESKK]]; for locally compact groups it must be trivial, so the phenomenon is specific to large groups.

### Converse

The statement is an equivalence, and both directions are used: Ramsey theorems give fixed points, and fixed point results give new Ramsey theorems.

### Generalizations

- The equivalence holds for Fraïssé classes of finite rigid structures, without a named order.
- For a Fraïssé class without the Ramsey property, an expansion by orders with the Ramsey and ordering properties computes the universal minimal flow of the group.
- For $\operatorname{Sym}(\N)$, that flow is the space of linear orders on $\N$.

## History

Kechris, Pestov and Todorcevic published the correspondence in 2005.
Pestov had earlier shown that $\operatorname{Aut}(\Q, <)$ is extremely amenable.

## Explanations

### L1 human

Two very different properties turn out to be the same.
One is combinatorial: however one colors small pieces, some larger piece has all its small pieces the same color.
The other is about symmetry: whenever the symmetry group acts on a compact space, some point stays fixed.

### L2 human

We see why $\operatorname{Sym}(\N)$ has no fixed point on the space $\mathrm{LO}$ of linear orders of $\N$.

1. A fixed point would be a linear order $\prec$ preserved by all permutations.
2. The transposition swapping $0$ and $1$ sends $0 \prec 1$ to $1 \prec 0$.
3. So no order is fixed, and $\operatorname{Sym}(\N)$ is not extremely amenable.

The typical use is to prove extreme amenability of an automorphism group from a known Ramsey theorem.
A trap is to apply the correspondence to unordered classes; rigidity is essential.

### L3 human

The [[proof|9Z6YVQE20S]] identifies left cosets of a pointwise stabilizer $G_A$ with copies of $A$, using rigidity and [[ultrahomogeneity|H8VM37SSAX]].
A coloring of copies is then a function on $G / G_A$, and Ramsey's condition becomes a finite oscillation stability statement for functions on $G$.
