---
tag: S1BHE358VX
kind: statement
role: theorem
name: Erdős–Rado theorem
msc: ["03E02", 05D10]
uses: [0QKPNZKNEA, ZC4BHVHWE9, 00TQV3F5S4]
about: [0QKPNZKNEA]
sources:
  - url: https://en.wikipedia.org/wiki/Erdős–Rado_theorem
same_as:
  wikidata: Q1366581
  wikipedia: Erdős–Rado theorem
---

## Statement

For [[cardinals|0QKPNZKNEA]] $\kappa$, $\lambda$, $\mu$ and an integer $n \ge 1$, write $\kappa \to (\lambda)^n_\mu$ for the following property.
Let $X$ be a set of size $\kappa$, and let $c$ map the $n$-element subsets of $X$ to $\mu$.
Then some $H \subseteq X$ of size $\lambda$ has all its $n$-element subsets of the same colour under $c$.
For an infinite cardinal $\kappa$, let $\beth_0(\kappa) = \kappa$ and $\beth_{m+1}(\kappa) = 2^{\beth_m(\kappa)}$, as for the [[beth numbers|ZC4BHVHWE9]].
Then, for each infinite cardinal $\kappa$ and each integer $n \ge 0$,
$$\beth_n(\kappa)^+ \to (\kappa^+)^{n+1}_\kappa.$$

## Remarks

The case $n = 0$ is the pigeonhole principle: a map from $\kappa^+$ points to $\kappa$ colours is constant on $\kappa^+$ points.
The case $n = 1$ reads $(2^\kappa)^+ \to (\kappa^+)^2_\kappa$, and for $\kappa = \aleph_0$ it gives $(2^{\aleph_0})^+ \to (\aleph_1)^2_{\aleph_0}$.
The proof goes by induction on $n$.
It builds a long sequence in which the colour of an $(n+1)$-element set depends only on its $n$ smallest elements, and then applies the case $n - 1$.
The bound is sharp for $n = 1$: by a theorem of Sierpiński, $2^{\aleph_0} \not\to (\aleph_1)^2_2$, so $2^{\aleph_0}$ points do not suffice even for two colours.
The theorem extends the infinite [[Ramsey theorem|00TQV3F5S4]] $\aleph_0 \to (\aleph_0)^n_k$ to uncountable homogeneous sets.

## Explanations

### L1 human

Colour the pairs of points of a set with a small number of colours.
Ramsey's theorem says that an infinite set always contains an infinite set whose pairs all have one colour.
For uncountable sets this is no longer free: to get an uncountable one-coloured set, the starting set must be large.
The Erdős–Rado theorem says how large is enough: more than continuum many points always suffice for pairs.

### L2 human

The notation $\kappa \to (\lambda)^n_\mu$ is the arrow notation of the partition calculus of Erdős and Rado.
The theorem is the basic positive result of uncountable Ramsey theory, and Sierpiński's colouring shows that it cannot be improved for pairs.
It is used in model theory, for example to find indiscernible sequences in large models, and in the study of large cardinals defined by partition properties.
