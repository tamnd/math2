---
tag: VPQJEFJ0HZ
kind: definition
name: Proj construction
msc: [14A15, 13A02]
defines: A39XQHCVNW
uses: [8KB4SQGC0C, 6ZBNGS0P98, 00MHHZ9SNE, 4C1AE84N5N, 5A35TYZD02, B3V3XJ2W8G]
sources:
  - url: https://en.wikipedia.org/wiki/Proj_construction
---

## Definition

Let $S = \bigoplus_{d \ge 0} S_d$ be a commutative [[graded ring|8KB4SQGC0C]], and let $S_+ = \bigoplus_{d > 0} S_d$.
As a set, $\operatorname{Proj} S$ is the set of [[homogeneous|6ZBNGS0P98]] [[prime ideals|00MHHZ9SNE]] $\mathfrak{p}$ of $S$ with $S_+ \not\subseteq \mathfrak{p}$.
Its closed sets are the sets $V_+(\mathfrak{a}) = \set{\mathfrak{p} \in \operatorname{Proj} S : \mathfrak{a} \subseteq \mathfrak{p}}$ for homogeneous ideals $\mathfrak{a}$.
For a homogeneous $f \in S_+$, let $D_+(f) = \set{\mathfrak{p} \in \operatorname{Proj} S : f \notin \mathfrak{p}}$.
Let $S_{(f)}$ be the ring of elements of degree $0$ in the [[localization|4C1AE84N5N]] $S_f$, that is, the fractions $a / f^n$ with $a$ homogeneous of degree $n \deg f$.

The structure sheaf $\mathcal{O}$ on $\operatorname{Proj} S$ is the unique sheaf of rings such that, for every homogeneous $f \in S_+$:

1. $\mathcal{O}(D_+(f)) = S_{(f)}$;
2. $(D_+(f), \mathcal{O}|_{D_+(f)})$ is isomorphic to the [[affine scheme|B3V3XJ2W8G]] $\operatorname{Spec} S_{(f)}$, by $\mathfrak{p} \mapsto \mathfrak{p} S_f \cap S_{(f)}$.

The sets $D_+(f)$ cover $\operatorname{Proj} S$, so $(\operatorname{Proj} S, \mathcal{O})$ is a [[scheme|5A35TYZD02]].

## Remarks

Example: for a ring $A$, projective $n$-space over $A$ is $\mathbb{P}^n_A = \operatorname{Proj} A[x_0, \ldots, x_n]$, with $\deg x_i = 1$.
It is covered by the $n+1$ affine pieces $D_+(x_i) \cong \operatorname{Spec} A[x_0/x_i, \ldots, x_n/x_i]$.
Non-example: for $S = k[x_0, \ldots, x_n]$ over a field $k$, the ideal $S_+ = (x_0, \ldots, x_n)$ is a homogeneous prime ideal.
It is not a point of $\operatorname{Proj} S$, since it contains $S_+$; it would correspond to the excluded origin of $k^{n+1}$.
For a homogeneous polynomial $F$ in $x_0, \ldots, x_n$, the scheme $\operatorname{Proj} k[x_0, \ldots, x_n]/(F)$ is the projective hypersurface $F = 0$.
