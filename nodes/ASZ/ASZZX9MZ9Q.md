---
tag: ASZZX9MZ9Q
kind: definition
name: BSSN formalism
msc: ["83C05", "83-08", "65M06"]
defines: P458KSQTWV
uses: [CFAFAPV7HB, Z8XNDJSCJS, XQG2VCBMKQ]
sources:
  - url: https://en.wikipedia.org/wiki/BSSN_formalism
---

## Definition

Let $h_{ij}$, $K_{ij}$, $N$ and $N^i$ be the spatial metric, extrinsic curvature, lapse and shift of the [[ADM formalism|CFAFAPV7HB]] in coordinates $(t, x^1, x^2, x^3)$.
The *BSSN variables* are:

1. the conformal factor $\phi = \tfrac{1}{12} \ln \det(h_{ij})$;
2. the conformal metric $\tilde\gamma_{ij} = e^{-4\phi} h_{ij}$, so that $\det(\tilde\gamma_{ij}) = 1$;
3. the trace $K = h^{ij} K_{ij}$;
4. the conformal trace-free extrinsic curvature $\tilde A_{ij} = e^{-4\phi} \bigl( K_{ij} - \tfrac13 h_{ij} K \bigr)$;
5. the conformal connection functions $\tilde\Gamma^i = \tilde\gamma^{jk} \tilde\Gamma^i_{jk}$, where $\tilde\Gamma^i_{jk}$ are the [[Christoffel symbols|Z8XNDJSCJS]] of $\tilde\gamma$.

The *BSSN formalism* is the system of evolution equations for these variables obtained from the vacuum Einstein equations.
In it $\tilde\Gamma^i$ is evolved as an independent variable, and the momentum constraint is added to its evolution equation.

## Remarks

Since $\det(\tilde\gamma_{ij}) = 1$, one has $\tilde\Gamma^i = -\partial_j \tilde\gamma^{ij}$.
The relations $\det(\tilde\gamma_{ij}) = 1$, $\tilde\gamma^{ij} \tilde A_{ij} = 0$ and $\tilde\Gamma^i = -\partial_j \tilde\gamma^{ij}$ are constraints of the new system, in addition to the Hamiltonian and momentum constraints.
Example: for Minkowski space in inertial coordinates, $\phi = 0$, $\tilde\gamma_{ij} = \delta_{ij}$, $K = 0$, $\tilde A_{ij} = 0$ and $\tilde\Gamma^i = 0$.
Non-example: the pair $(h_{ij}, K_{ij})$ itself is not a set of BSSN variables; evolving it directly is the ADM system, which is only weakly [[hyperbolic|XQG2VCBMKQ]].
Many codes use $\chi = e^{-4\phi}$ or $W = e^{-2\phi}$ in place of $\phi$, because they stay regular near black hole punctures.
A common gauge is the 1+log slicing for the lapse with the Gamma-driver condition for the shift, the moving puncture gauge.

## Explanations

### L1 human

The BSSN formalism is a change of variables for the Einstein evolution equations that makes them stable enough for computer simulations.
