---
tag: 8P5SH4PHM9
kind: definition
name: Topological Hochschild homology
msc: [19D55, 55P42, "16E40"]
defines: PFW77RAAY3
uses: [BAW0T68GWK, 2ZJ2G308QV, S5H153HFWC, 04EAFVFTF7, XJPYJT9Z1P]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_Hochschild_homology
---

## Definition

Work in a symmetric monoidal model of spectra, with [[smash product|2ZJ2G308QV]] $\wedge$ over the sphere spectrum $\mathbb{S}$.
Let $R$ be an associative [[ring spectrum|BAW0T68GWK]] with multiplication $\mu \colon R \wedge R \to R$ and unit $\eta \colon \mathbb{S} \to R$.
The *cyclic bar construction* of $R$ is the simplicial spectrum with $q$-simplices $R^{\wedge (q+1)}$ and these structure maps:

1. for $0 \le i < q$, the face $d_i$ multiplies the factors in positions $i$ and $i+1$;
2. the face $d_q$ moves the last factor to the front and then multiplies it with the first factor;
3. the degeneracy $s_i$ inserts the unit $\eta$ after position $i$.

The *topological Hochschild homology* $THH(R)$ is the geometric realization of the cyclic bar construction.
For an ordinary ring $A$, one sets $THH(A) = THH(HA)$, where $HA$ is the [[Eilenberg–MacLane spectrum|XJPYJT9Z1P]] of $A$.

## Remarks

The cyclic permutations of the factors make the cyclic bar construction a cyclic object, so $THH(R)$ carries an action of the [[circle group|04EAFVFTF7]].
Replacing $\mathbb{S}$ by $\Z$ and $\wedge$ by $\otimes$ in the same construction gives the Hochschild complex, so there is a linearization map $THH(A) \to HH(A)$ to [[Hochschild homology|S5H153HFWC]] over $\Z$.
It induces an isomorphism $\pi_0 THH(A) \cong HH_0(A) = A/[A, A]$.
Example: Bökstedt computed $\pi_* THH(\mathbb{F}_p) = \mathbb{F}_p[u]$ with $\abs{u} = 2$.
Non-example of agreement with Hochschild homology: Bökstedt also computed $\pi_{2k-1} THH(\Z) = \Z/k$ for $k \ge 1$, so $\pi_3 THH(\Z) = \Z/2$, while $HH_3(\Z) = 0$.
Rationally the two theories agree: $\pi_* THH(A) \otimes \Q \cong HH_*(A \otimes \Q / \Q)$.
