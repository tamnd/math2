---
tag: REV37M7H5W
kind: definition
name: Borel regulator
msc: ["19F27", "11R70", "11R42"]
defines: D22EZ3CNAF
uses: [4HXFKW55WJ, MWBDFS2KJ5, 6N7BC70CX0, KXS5DQDFYD]
sources:
  - url: https://en.wikipedia.org/wiki/Beilinson_regulator
---

## Definition

Let $F$ be an [[algebraic number field|MWBDFS2KJ5]] with ring of integers $\mathcal{O}_F$, let $\Sigma$ be the set of field embeddings $\sigma \colon F \to \C$, and let $m \ge 2$.
Let $b_m \in H^{2m-1}(B\mathrm{GL}(\C)^\delta; \R)$ be the Borel class.
It is a stable class in the cohomology of the discrete group $\mathrm{GL}(\C)$, obtained from continuous cohomology of $\mathrm{GL}_N(\C)$ by the van Est isomorphism.
For $\sigma \in \Sigma$ let $r_\sigma$ be the composite
$$K_{2m-1}(\mathcal{O}_F) \xrightarrow{\sigma_*} K_{2m-1}(\C) = \pi_{2m-1}\big(B\mathrm{GL}(\C)^{\delta +}\big) \xrightarrow{h} H_{2m-1}(B\mathrm{GL}(\C)^\delta; \Z) \xrightarrow{\langle b_m, \cdot \rangle} \R,$$
where $h$ is the Hurewicz map and the last map pairs with $b_m$ in [[singular cohomology|6N7BC70CX0]].
The *Borel regulator* is the homomorphism
$$r_m \colon K_{2m-1}(\mathcal{O}_F) \to \R^{\Sigma}, \qquad x \mapsto (r_\sigma(x))_{\sigma \in \Sigma}.$$

## Remarks

Complex conjugation acts on $\R^\Sigma$ through $\Sigma$.
The image of $r_m$ lies in the subspace on which conjugation acts by the sign $(-1)^{m-1}$.
This subspace has dimension $d_m$, where $d_m = r_1 + r_2$ for $m$ odd and $d_m = r_2$ for $m$ even.
Borel proved that $r_m$ has finite kernel and that its image is a lattice in this subspace.
The covolume $R_m(F)$ of this lattice is the *Borel regulator* of $F$ in degree $m$.
Let $\zeta_F^*(1 - m)$ be the leading coefficient of the [[Dedekind zeta function|KXS5DQDFYD]] at $s = 1 - m$.
Borel proved that $\zeta_F^*(1 - m) / R_m(F)$ is a nonzero rational number.
Normalisations of $b_m$ vary between authors by rational factors and powers of $2 \pi i$.

Example: the analogue for $m = 1$ is the map $\mathcal{O}_F^\times = K_1(\mathcal{O}_F) \to \R^\Sigma$, $u \mapsto (\log \abs{\sigma(u)})_\sigma$, whose image has covolume equal, up to a simple factor, to the classical regulator.

Non-example: for $F = \Q$ and $m$ even, $d_m = 0$, so $r_m$ is zero; this matches the finiteness of $K_{2m-1}(\Z)$ for even $m$.
