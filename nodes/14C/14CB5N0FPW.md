---
tag: 14CB5N0FPW
kind: conjecture
name: Baum–Connes conjecture
msc: [19K35, 46L80, 58B34]
uses: [JKANN4VBYH, 41XX3KF72X, BP86XQRZD2, 7NTVTHC7CG, 1W9Q7W378J]
about: [JKANN4VBYH, 41XX3KF72X]
sources:
  - url: https://en.wikipedia.org/wiki/Baum%E2%80%93Connes_conjecture
same_as:
  wikidata: Q2993305
  wikipedia: Baum–Connes conjecture
history:
  posed_by: "Paul Baum and Alain Connes"
  first_stated: "1982"
---

## Statement

Let $G$ be a second countable, locally compact group.
Let $\underline{E}G$ be a universal proper $G$-space, the classifying space for proper actions of $G$.
Let $K_*^G(\underline{E}G)$, $* = 0, 1$, be its equivariant [[K-homology|41XX3KF72X]] with $G$-compact supports.
Let $C_r^*(G)$ be the reduced [[group C*-algebra|JKANN4VBYH]] of $G$, with K-groups [[K0|BP86XQRZD2]] and [[K1|7NTVTHC7CG]].
The conjecture states that the assembly map
$$\mu \colon K_*^G(\underline{E}G) \to K_*(C_r^*(G)), \qquad * = 0, 1,$$
is an isomorphism.

## Remarks

The assembly map sends an equivariant elliptic operator on a proper cocompact $G$-space to its higher index in the K-theory of $C_r^*(G)$; it is built with [[KK-theory|1W9Q7W378J]].
The conjecture in this form is due to Baum, Connes and Higson (1994), refining the 1982 formulation of Baum and Connes.
It is open in general.
It is proved for a-T-menable groups, which include amenable groups, by Higson and Kasparov, and for hyperbolic groups, by Lafforgue and by Mineyev and Yu.
The version with coefficients in an arbitrary $G$-C*-algebra is false: Higson, Lafforgue and Skandalis gave counterexamples using groups that contain expanders.
For discrete torsion-free $G$, injectivity of $\mu$ implies the Novikov conjecture on higher signatures, and surjectivity implies the Kadison–Kaplansky conjecture that $C_r^*(G)$ has no projections other than $0$ and $1$.

## Explanations

### L1 human

For a group $G$ there is an operator algebra $C_r^*(G)$ that encodes its unitary representations, and its K-theory is hard to compute directly.
The left side of the conjecture is a topological object, built from spaces on which $G$ acts nicely, and it is often computable.
The conjecture says that the analytic K-theory is exactly the topological one, with the map given by taking indices of elliptic operators.
It ties together geometry, topology and operator algebras, and it implies several other well-known conjectures.
