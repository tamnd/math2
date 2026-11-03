---
tag: R2HKASVGAF
kind: definition
name: Elasticity tensor
msc: [74B05, "74E10"]
defines: SX32X1D537
uses: [8QS6QMJF5Z, KG2XWEMJ30, 0VR671PHE5]
sources:
  - url: https://en.wikipedia.org/wiki/Elasticity_tensor
---

## Definition

Let $\mathrm{Sym}$ be the space of [[symmetric|0VR671PHE5]] $3 \times 3$ real matrices.
An *elasticity tensor* is a fourth-order tensor $C = (C_{ijkl})_{i,j,k,l = 1}^{3}$ of real numbers such that:

1. (minor symmetries) $C_{ijkl} = C_{jikl} = C_{ijlk}$ for all indices;
2. (major symmetry) $C_{ijkl} = C_{klij}$ for all indices;
3. (positivity) $\varepsilon_{ij} C_{ijkl} \varepsilon_{kl} > 0$ for every nonzero $\varepsilon \in \mathrm{Sym}$, with summation over repeated indices.

It acts on a [[strain|8QS6QMJF5Z]] $\varepsilon \in \mathrm{Sym}$ by $(C : \varepsilon)_{ij} = C_{ijkl} \varepsilon_{kl}$, and $C : \varepsilon$ is the [[stress|KG2XWEMJ30]] in a linear elastic material.

## Remarks

Example: the isotropic tensor $C_{ijkl} = \lambda \delta_{ij} \delta_{kl} + \mu (\delta_{ik} \delta_{jl} + \delta_{il} \delta_{jk})$ with $\mu > 0$ and $3\lambda + 2\mu > 0$.
Clauses 1 and 2 hold by inspection.
For clause 3, $\varepsilon : C : \varepsilon = \lambda (\tr \varepsilon)^2 + 2\mu \, \varepsilon : \varepsilon$; splitting $\varepsilon$ into its trace part and its trace-free part $\varepsilon'$ gives $(\lambda + \tfrac23 \mu)(\tr \varepsilon)^2 + 2\mu \, \varepsilon' : \varepsilon'$, which is positive for $\varepsilon \ne 0$.

Non-example: the same formula with $\mu = 0$ and $\lambda > 0$ fails clause 3, since any nonzero trace-free $\varepsilon$ gives $0$.
Such a "material" offers no resistance to shear.

Clause 1 says that $C$ maps $\mathrm{Sym}$ to $\mathrm{Sym}$ and ignores the skew part of the strain.
Clause 2 holds when the material has a stored energy $W(\varepsilon) = \tfrac12 \varepsilon : C : \varepsilon$; then $C$ is a symmetric positive definite operator on the $6$-dimensional space $\mathrm{Sym}$, which has $21$ independent entries.
In Voigt notation $C$ is written as a symmetric $6 \times 6$ matrix.
Some authors include only clause 1 in the definition and state clauses 2 and 3 as extra assumptions.
