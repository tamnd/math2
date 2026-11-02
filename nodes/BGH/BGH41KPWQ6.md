---
tag: BGH41KPWQ6
kind: definition
name: Canonical bundle
msc: [14C20, 14F10]
defines: W05VYY4HBR
uses: [EXKGG9X6J0, 6VC6HQTFSA, 0MDMZ965VE, 7JCF2TE3V5]
sources:
  - url: https://en.wikipedia.org/wiki/Canonical_bundle
---

## Definition

Let $k$ be a field and let $X$ be a scheme that is [[smooth|EXKGG9X6J0]] over $k$ and of pure dimension $n$.
Then the [[sheaf of differentials|6VC6HQTFSA]] $\Omega_{X/k}$ is locally free of rank $n$.
The *canonical bundle* of $X$ is the [[invertible sheaf|7JCF2TE3V5]]
$$\omega_X = \bigwedge^n \Omega_{X/k},$$
the top [[exterior power|0MDMZ965VE]] of $\Omega_{X/k}$.
A *canonical divisor* is a divisor $K_X$ with $\mathcal{O}_X(K_X) \cong \omega_X$.

## Remarks

Locally, if $x_1, \dots, x_n$ are local coordinates (an étale chart), then $\omega_X$ is free with basis $dx_1 \wedge \dots \wedge dx_n$.

Example: for $X = \mathbb{P}^n_k$, the Euler sequence $0 \to \Omega_X \to \mathcal{O}(-1)^{\oplus (n+1)} \to \mathcal{O}_X \to 0$ gives, by taking determinants, $\omega_X \cong \mathcal{O}(-n-1)$.
For $n = 1$ this is the degree $-2$ bundle on $\mathbb{P}^1_k$.

Non-example: for the cuspidal curve $y^2 = x^3$, $\Omega_{X/k}$ is not locally free at the cusp, so the definition does not apply.
For singular varieties one uses instead the dualizing sheaf, which agrees with $\omega_X$ on smooth projective varieties.
