---
tag: DD4D0EKX74
kind: statement
role: theorem
name: Adams spectral sequence
msc: [55T15, 55Q45, 55S10]
uses: [JWTTXSGD0E, 4P7GBWJ4RR, 1GHF4EKBXS, 26GTNMAF7B, 14CGGHA85T, HGZAYPQBXW]
about: [HGZAYPQBXW]
sources:
  - url: https://en.wikipedia.org/wiki/Adams_spectral_sequence
same_as:
  wikidata: Q4680481
  wikipedia: Adams spectral sequence
---

## Statement

Let $p$ be a prime, let $\mathcal{A}$ be the mod $p$ [[Steenrod algebra|JWTTXSGD0E]], and write $H^*(-)$ for mod $p$ cohomology of [[spectra|1GHF4EKBXS]].
Let $X$ be a finite CW spectrum, and let $Y$ be a bounded-below spectrum whose homotopy groups are finitely generated in each degree.
For $n \in \Z$, let $[X, Y]_n$ be the group of maps $\Sigma^n X \to Y$ in the [[stable homotopy category|26GTNMAF7B]].
Then there is a spectral sequence $(E_r^{s,t}, d_r)_{r \ge 2}$ with $s \ge 0$.
Its differentials are $d_r \colon E_r^{s,t} \to E_r^{s+r, t+r-1}$.
Its second page is
$$E_2^{s,t} = \operatorname{Ext}_{\mathcal{A}}^{s,t}\big(H^*(Y), H^*(X)\big).$$
Here $\operatorname{Ext}^{s,t}$ is the [[Ext group|4P7GBWJ4RR]] of $\mathcal{A}$-modules in homological degree $s$ and internal degree $t$.
The spectral sequence converges strongly to $[X, Y]_{t-s} \otimes \Z_p$, where $\Z_p$ is the ring of $p$-adic integers.

## Remarks

The construction resolves $Y$ by a tower of spectra built from mod $p$ Eilenberg–MacLane spectra, the Adams resolution, and applies $[X, -]_*$.
The filtration degree $s$ counts how many maps in the tower a class passes through.

The main case is $X = Y = S$, the [[sphere spectrum|14CGGHA85T]].
Then $E_2^{s,t} = \operatorname{Ext}_{\mathcal{A}}^{s,t}(\F_p, \F_p)$ and the abutment is the $p$-primary part of the [[stable homotopy groups of spheres|HGZAYPQBXW]] $\pi_{t-s}^s$ for $t - s > 0$.
For $p = 2$, the group $\operatorname{Ext}^{1,t}$ has a basis of classes $h_j$ with $t = 2^j$, one for each $j \ge 0$, coming from the indecomposable squares $Sq^{2^j}$.
The classes $h_0, h_1, h_2, h_3$ detect $2$, $\eta$, $\nu$ and $\sigma$, while $d_2(h_j) = h_0 h_{j-1}^2 \neq 0$ for $j \ge 4$; this is Adams' theorem on Hopf invariant one.

Without the finiteness hypotheses the spectral sequence still exists, but it may converge only to the homotopy of a $p$-completion of $Y$, or not converge at all.

## Explanations

### L1 human

Stable homotopy groups of spheres are very hard to compute directly.
The Adams spectral sequence starts from a purely algebraic object, built from the Steenrod operations on mod $p$ cohomology.
After a series of corrections, it gives the $p$-primary part of these groups.

### L2 human

The $E_2$ term can be computed by machine with minimal resolutions over the Steenrod algebra.
In a range of degrees the differentials are known, and this gives the stable stems far beyond what other methods reach.
Its algebraic structure, such as Massey products and the May spectral sequence for $E_2$, controls much of the computation.
The Adams–Novikov spectral sequence replaces mod $p$ cohomology by complex cobordism and is better suited for periodic phenomena.
