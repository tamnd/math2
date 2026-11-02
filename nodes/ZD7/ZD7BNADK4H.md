---
tag: ZD7BNADK4H
kind: statement
role: theorem
name: Barratt–Priddy–Quillen theorem
msc: [55P47, 55R35, 20J06]
uses: [0RJMNEN3BJ, 7XRBR7AV3C, M0Q5CFJ7ZH, A7VB2NSGJ2, HGZAYPQBXW]
about: [7XRBR7AV3C, HGZAYPQBXW]
sources:
  - url: https://en.wikipedia.org/wiki/Barratt–Priddy_theorem
same_as:
  wikidata: Q4863268
  wikipedia: Barratt–Priddy theorem
---

## Statement

For $n \ge 1$, let $\Sigma_n$ be the [[symmetric group|0RJMNEN3BJ]] on $n$ letters, and let $\Sigma_\infty = \bigcup_n \Sigma_n$ be the infinite symmetric group, with $B\Sigma_\infty$ its [[classifying space|7XRBR7AV3C]].
Let $QS^0 = \operatorname{colim}_n \Omega^n S^n$, an [[infinite loop space|A7VB2NSGJ2]], and let $Q_0 S^0$ be its path component of the basepoint.
Then there is a natural map $B\Sigma_\infty \to Q_0 S^0$ that induces an isomorphism
$$H_*(B\Sigma_\infty; \Z) \cong H_*(Q_0 S^0; \Z)$$
in [[singular homology|M0Q5CFJ7ZH]].
Equivalently, $QS^0$ is the group completion of the topological monoid $\coprod_{n \ge 0} B\Sigma_n$, and $\Z \times B\Sigma_\infty^+ \simeq QS^0$, where $B\Sigma_\infty^+$ is Quillen's plus construction.

## Remarks

Barratt and Priddy, and independently Quillen, proved the theorem in the early 1970s.
One proof uses the group completion theorem: the homology of the group completion of $M = \coprod_n B\Sigma_n$ is $H_*(M)[\pi_0(M)^{-1}] = \Z[\Z] \otimes H_*(B\Sigma_\infty)$.
The other input is that $\coprod_n B\Sigma_n$ is the free $E_\infty$ space on a point, and that the group completion of the free $E_\infty$ space on $S^0$ is $QS^0$.

At work: taking homotopy groups gives $\pi_k(B\Sigma_\infty^+) \cong \pi_k^s$ for $k \ge 1$, the [[stable homotopy groups of spheres|HGZAYPQBXW]].
For $k = 1$ this says $\pi_1^s \cong \Z/2$, which matches the abelianization $\Sigma_\infty / A_\infty \cong \Z/2$, where $A_\infty$ is the infinite alternating group and the quotient map is the sign of a permutation.

## Explanations

### L1 human

The theorem links two very different objects: the symmetric groups, which permute finite sets, and the stable homotopy groups of spheres.
It says that, after the plus construction, the classifying space of the infinite symmetric group has exactly the stable homotopy groups of spheres as its homotopy groups.
For this reason the stable homotopy of spheres is often described as the algebraic K-theory of the "field with one element", modelled by finite sets.

### L2 human

Since $\pi_1(B\Sigma_\infty^+)$ is the abelianization of $\Sigma_\infty$, the theorem recovers $\pi_1^s \cong \Z/2$, and the higher groups give a description of all stable stems in terms of permutations.
Together with Nakaoka's homological stability for symmetric groups, it computes $H_*(Q_0 S^0)$ from the homology of the groups $\Sigma_n$.
Quillen's analogue for general linear groups over finite fields led to his computation of the algebraic K-theory of finite fields.
