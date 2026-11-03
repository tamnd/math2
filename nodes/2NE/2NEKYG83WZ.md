---
tag: 2NEKYG83WZ
kind: statement
role: theorem
name: Bass cancellation theorem
msc: [19A13, 13C10]
uses: [0310REJJY8, 0670T59HGE, MVGBS3J1P7, HQA9YHDSH5, 1WTNGZ5T5A]
about: [HQA9YHDSH5]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_range_condition
---

## Statement

Let $R$ be a commutative [[Noetherian ring|0670T59HGE]] of finite [[Krull dimension|MVGBS3J1P7]] $d$.
Let $P$, $P'$ and $Q$ be [[finitely generated projective|HQA9YHDSH5]] $R$-modules.
Assume that the [[rank|1WTNGZ5T5A]] of $P$ is greater than $d$ at every prime ideal of $R$.
If $P \oplus Q \cong P' \oplus Q$, then $P \cong P'$.

## Remarks

Since $Q$ is a direct summand of some $R^k$, it suffices to treat $Q = R$ and then use induction on $k$.
For $Q = R$, an isomorphism $P \oplus R \cong P' \oplus R$ gives a unimodular element of $P \oplus R$.
The theorem then follows from the fact that the automorphisms of $P \oplus R$ act transitively on unimodular elements when the rank of $P$ exceeds $d$.
This transitivity is proved with Bass's [[stable range|DZBM27VRAF]] methods and Serre's general position arguments.

Example: over a Dedekind domain ($d \le 1$), finitely generated projective modules of rank at least $2$ cancel.
For rank $1$ cancellation also holds there, because $I \oplus R \cong J \oplus R$ implies $I \cong J$ by taking [[determinants|1FJ4F9HK8S]].

The rank hypothesis cannot be removed.
Let $A = \R[x, y, z]/(x^2 + y^2 + z^2 - 1)$, a ring of Krull dimension $2$, and let $P$ be the kernel of $(u, v, w) \mapsto ux + vy + wz$ from $A^3$ to $A$.
Then $P \oplus A \cong A^2 \oplus A$, but $P$, of rank $2 = d$, is not isomorphic to $A^2$, by the hairy ball theorem.

## Explanations

### L1 human

Cancellation asks whether one can remove a common summand from both sides of an isomorphism of modules, as one cancels a number from both sides of an equation.
This can fail: some modules become isomorphic only after adding a free module.
Bass's theorem says that cancellation always works when the modules are large compared with the dimension of the ring.

### L2 human

The theorem means that, in high rank, the class in [[$K_0(R)$|Q14JS2MA1C]] determines the module: if $[P] = [P']$ and the rank is greater than $d$, then $P \cong P'$.
Together with [[Serre's splitting theorem|FH0VE9PQXJ]], it reduces the study of projective modules to ranks at most $d$.
Bass's stable range also gives the analogous stability for $K_1$: the map $GL_n(R) \to K_1(R)$ is onto when $n$ is at least the stable rank of $R$.
