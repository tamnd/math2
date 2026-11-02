---
tag: WZNF6Q5JBS
kind: definition
name: Pseudo-Anosov map
msc: ["37E30", "57K20"]
defines: GYW7GYABD9
uses: [VGJJVBZ1MQ, 0QT00PB5G2, 98HTB7MSPX, BSCZN8Y1AN, W890NRHGS4]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudo-Anosov_map
---

## Definition

Let $S$ be a closed orientable [[surface|VGJJVBZ1MQ]].
A *singular measured foliation* on $S$ is a [[foliation|98HTB7MSPX]] $\mathcal{F}$ of $S \setminus \Sigma$, for a finite set $\Sigma$, with a transverse measure $\mu$.
Here $\mu$ is a measure on arcs transverse to the leaves, invariant under sliding along the leaves.
Near each point of $\Sigma$ the foliation must be a $p$-prong singularity for some $p \ge 3$.
A [[homeomorphism|0QT00PB5G2]] $f \colon S \to S$ is *pseudo-Anosov* if there are $\lambda > 1$ and singular measured foliations $(\mathcal{F}^s, \mu^s)$, $(\mathcal{F}^u, \mu^u)$ on $S$ such that:

1. $\mathcal{F}^s$ and $\mathcal{F}^u$ have the same singular set $\Sigma$ and are transverse away from $\Sigma$.
2. $f$ maps the leaves of $\mathcal{F}^s$ to leaves of $\mathcal{F}^s$, and $f_* \mu^s = \lambda^{-1} \mu^s$.
3. $f$ maps the leaves of $\mathcal{F}^u$ to leaves of $\mathcal{F}^u$, and $f_* \mu^u = \lambda \mu^u$.

The number $\lambda$ is the *stretch factor* (or dilatation) of $f$.

## Remarks

Example: on the torus $\R^2 / \Z^2$, the map induced by $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, [[Arnold's cat map|BSCZN8Y1AN]], is pseudo-Anosov with no singular points.
The eigenvalues of $A$ are $\lambda = \frac{3 + \sqrt 5}{2} > 1$ and $\lambda^{-1}$.
The foliations by lines parallel to the two eigenvectors, with transverse measures given by distance across the lines, are contracted by $\lambda^{-1}$ and stretched by $\lambda$.

Non-example: the [[Dehn twist|W890NRHGS4]] induced by $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ on the torus has only the eigenvalue $1$.
It preserves the horizontal foliation without stretching it, so no $\lambda > 1$ fits clauses 2 and 3.

On a closed surface of genus $g \ge 2$, the Euler–Poincaré formula forces singular points, since the foliations cannot be nonsingular.
For surfaces with punctures, $1$-prong singularities are also allowed at the punctures.
The stretch factor $\lambda$ is an algebraic integer, and $\log \lambda$ is the topological entropy of $f$, the least entropy among all homeomorphisms isotopic to $f$.
