---
tag: PYBXE2C28T
kind: definition
name: String theory
msc: [81T30, "83E30"]
defines: GM58M1HFY0
uses: [99KYX4BDRD, 5K0N8QMV6Q, NK9ATH4WB6, TWJ4K9C8XV]
sources:
  - url: https://en.wikipedia.org/wiki/String_theory
---

## Definition

Perturbative bosonic string theory is defined as follows.

1. A string background is a two-dimensional [[conformal field theory|99KYX4BDRD]], the matter theory, with central charge $c = 26$.
   The standard example is the theory of $26$ free bosons $X^\mu$, describing maps from a surface to Minkowski space $\R^{1,25}$.
   Its classical action is the [[Polyakov action|HFEGZQB8SV]].
2. Tensor the matter theory with the $bc$ ghost system of central charge $-26$.
   The physical states of the string are the classes in the cohomology of the BRST operator on this tensor product.
3. The scattering amplitude of $n$ physical states is a sum over the genus $g \ge 0$, weighted by $g_s^{2g - 2}$.
   The term of genus $g$ is an integral over the moduli space $\mathcal{M}_{g,n}$ of [[Riemann surfaces|5K0N8QMV6Q]] of genus $g$ with $n$ marked points.
   The integrand is a density built from correlation functions of the conformal field theory on these surfaces.

Here $g_s$ is the string coupling constant.
*String theory* in general refers to this construction and its variants.
In superstring theories the worldsheet theory is superconformal with $c = 15$ in a suitable normalization.
Other variants are open strings, on surfaces with boundary, and non-perturbative extensions.

## Remarks

The condition $c = 26$ makes the total central charge $0$.
Then the Weyl anomaly cancels, the BRST operator $Q$ satisfies $Q^2 = 0$, and the integrand in clause 3 is a density on the [[moduli space of curves|NK9ATH4WB6]].
For $26$ free bosons, the lowest state of the closed string is a tachyon.
The first massless level contains states of spin $2$ (the graviton), an antisymmetric tensor and a scalar, the dilaton.

Example: the free bosons $X^\mu$ on a torus target $\R^{1, 25 - k} \times T^k$ give another background with $c = 26$, a toroidal compactification; it shows [[T-duality|RD9MTZ0PEP]], under which radii $R$ and $\alpha'/R$ give equivalent theories.

Non-example: $D$ free bosons with $D \ne 26$ give $c = D \ne 26$, and the construction fails.
The Weyl anomaly does not cancel, and in the old covariant quantization the spectrum contains states of negative norm when $D > 26$.
The classical [[Nambu–Goto action|W4GZMZ796R]] makes sense in every dimension; the critical dimension appears only in the quantum theory.

A non-perturbative definition of string theory is not known in general.
