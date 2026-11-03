---
tag: 3ZKRM0GG7M
kind: definition
name: Cyclotomic trace
msc: [19D55, 55P42]
defines: 5AWJ6ZEG26
uses: [2C1M0NWPB0, 6RQS843SE5, PFW77RAAY3, 4YDCBSAJZ0, BAW0T68GWK]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_Hochschild_homology
---

## Definition

Let $R$ be a connective associative [[ring spectrum|BAW0T68GWK]], for example an ordinary ring.
Let $K(R)$ be its [[K-theory spectrum|2C1M0NWPB0]], $THH(R)$ its [[topological Hochschild homology|PFW77RAAY3]] and $TC(R)$ its [[topological cyclic homology|6RQS843SE5]].
The *Bökstedt trace* is a natural map $K(R) \to THH(R)$.
It comes from topological Hochschild homology of the category of finitely generated projective $R$-modules, by including the identity morphisms.
The *cyclotomic trace* is the natural map of spectra
$$\mathrm{trc} \colon K(R) \to TC(R)$$
whose composite with the canonical map $TC(R) \to THH(R)$ is the Bökstedt trace.

## Remarks

The lift through $TC(R)$ exists because the Bökstedt trace lands in the part of $THH(R)$ that is fixed by the circle action and compatible with the Frobenius maps.
Blumberg, Gepner and Tabuada showed that the cyclotomic trace is the unique multiplicative natural transformation from $K$ to $TC$, up to homotopy.
Composing the Bökstedt trace with the linearization $THH(R) \to HH(R)$ gives on homotopy groups the [[Dennis trace map|4YDCBSAJZ0]].
Example: for $R = \mathbb{F}_p$, after $p$-completion, the cyclotomic trace on $\pi_0$ is an isomorphism from $K_0(\mathbb{F}_p) \otimes \Z_p \cong \Z_p$ to $\pi_0 TC(\mathbb{F}_p)^\wedge_p \cong \Z_p$.
Non-example: the cyclotomic trace is not an equivalence in general; for $R = \mathbb{F}_p$ the group $\pi_{-1} TC(\mathbb{F}_p)^\wedge_p$ is not zero, while $K_{-1}(\mathbb{F}_p) = 0$.
