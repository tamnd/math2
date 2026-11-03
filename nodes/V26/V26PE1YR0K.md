---
tag: V26PE1YR0K
kind: definition
name: Motivic cohomology
msc: ["19E15", 14F42, 14C25]
defines: V1BB32NY3G
uses: [HV6YBS0YDH, EBEF6PEK4N, WQ82C0M3QB]
sources:
  - url: https://en.wikipedia.org/wiki/Motivic_cohomology
---

## Definition

Let $k$ be a field and let $X$ be a smooth quasi-projective [[variety|HV6YBS0YDH]] over $k$.
For $n \ge 0$, let $\Delta^n = \operatorname{Spec} k[t_0, \ldots, t_n]/(t_0 + \cdots + t_n - 1)$ be the algebraic $n$-simplex.
A face of $\Delta^n$ is a closed subscheme defined by equations $t_{i_1} = \cdots = t_{i_r} = 0$.
Let $Z \subseteq X \times \Delta^n$ be a closed subvariety of codimension $q$.
It meets the faces properly if, for every face $F$, each irreducible component of $Z \cap (X \times F)$ has codimension at least $q$ in $X \times F$.
Let $z^q(X, n)$ be the free abelian group on the integral closed subvarieties of codimension $q$ that meet the faces properly.
Let $\delta_i \colon \Delta^{n-1} \to \Delta^n$ be the inclusion of the face $t_i = 0$.
The groups $z^q(X, \bullet)$ form a [[chain complex|WQ82C0M3QB]] with differential $\partial = \sum_{i=0}^{n} (-1)^i (\id_X \times \delta_i)^*$, called Bloch's cycle complex.
Its homology groups $CH^q(X, n) = H_n(z^q(X, \bullet))$ are the *higher Chow groups*.
The *motivic cohomology* groups of $X$ are
$$H^p(X, \Z(q)) = CH^q(X, 2q - p).$$

## Remarks

For $p = 2q$ one gets $H^{2q}(X, \Z(q)) = CH^q(X, 0) = CH^q(X)$, the [[Chow group|EBEF6PEK4N]] of codimension $q$ cycles.
For $X = \operatorname{Spec} F$ with $F$ a field, $H^n(F, \Z(n))$ is isomorphic to the [[Milnor K-group|2YXDQ7Q445]] $K^M_n(F)$, by theorems of Nesterenko–Suslin and Totaro.
In particular $H^1(F, \Z(1)) \cong F^\times$.
Non-example: if $q > \dim X + n$, then $X \times \Delta^n$ has no subvariety of codimension $q$, so $z^q(X, n) = 0$ and these groups contribute nothing.
Voevodsky defined motivic cohomology through his triangulated category of motives, for all varieties; for smooth varieties over a field his groups agree with the higher Chow groups above.
With finite coefficients one writes $H^p(X, \Z/m(q))$, using the cycle complex tensored with $\Z/m$.
