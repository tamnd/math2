---
tag: 97CGS5KKRW
kind: statement
role: theorem
name: Uhlenbeck compactness theorem
msc: ["58E15", 53C07, 58D27]
uses: [7CBT4SM83Y, 8E37E74XVP, NJ21PN5ZGJ, ZAJFW1S078, M4CEZ5K9HP, 707DEWCCFX]
about: [NJ21PN5ZGJ, 707DEWCCFX]
sources:
  - url: https://en.wikipedia.org/wiki/Uhlenbeck%27s_compactness_theorem
same_as:
  wikidata: Q135397856
  wikipedia: Uhlenbeck's compactness theorem
---

## Statement

Let $X$ be a compact [[Riemannian manifold|7CBT4SM83Y]] of dimension $n$, let $G$ be a compact Lie group, and let $P \to X$ be a [[principal $G$-bundle|8E37E74XVP]].
Let $p > n/2$, and let $(A_i)$ be a sequence of [[connections|NJ21PN5ZGJ]] on $P$ of [[Sobolev class|M4CEZ5K9HP]] $L^p_1$ whose [[curvatures|ZAJFW1S078]] are bounded in $L^p$:
$$\sup_i \norm{F_{A_i}}_{L^p} < \infty.$$
Then there are a subsequence $(A_{i_j})$, [[gauge transformations|707DEWCCFX]] $u_j$ of class $L^p_2$, and a connection $A$ of class $L^p_1$ with this property.
The connections $u_j^* A_{i_j}$ converge to $A$ weakly in $L^p_1$.

## Remarks

The key step is Uhlenbeck's gauge fixing lemma: on a ball, a connection with small enough curvature in $L^{n/2}$ is gauge equivalent to one in Coulomb gauge, $d^* A = 0$, with $\norm{A}_{L^p_1} \le C \norm{F_A}_{L^p}$.
For $p > n/2$, Hölder's inequality turns the $L^p$ bound into a small $L^{n/2}$ bound on balls of a fixed small radius.
So one can fix the gauge on each ball of a finite cover, extract weakly convergent subsequences, and patch the local gauges together.
The condition $p > n/2$ is needed.
In dimension $4$ with only an $L^2$ bound on curvature, the scale-invariant case $p = n/2$, the curvature of instantons can concentrate at points.
Then a sequence may have no subsequence that converges, after gauge, on the whole of $X$.
For a sequence of instantons on a bundle of fixed charge, a refinement of the argument gives convergence after gauge on the complement of finitely many points.
By Uhlenbeck's removable singularity theorem the limit is a connection on a possibly different bundle; this is the bubbling picture.

## Explanations

### L1 human

A connection can be described in many ways, one for each choice of gauge, and in a bad gauge a harmless sequence can look as if it diverges.
The theorem says that if the curvature is bounded in a strong enough sense, then one can choose good gauges in which the sequence has a convergent subsequence.
So a bound on curvature, which is gauge invariant, controls the connections themselves.

### L2 human

The theorem plays for connections the role that the Rellich and Arzelà–Ascoli compactness theorems play for functions.
In dimension $4$ and at the critical exponent it underlies the Uhlenbeck compactification of instanton moduli spaces.
There, limits of instantons are instantons on a bundle with smaller charge, together with points where curvature has concentrated.

This compactification is a central tool in Donaldson theory.
