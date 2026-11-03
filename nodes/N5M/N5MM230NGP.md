---
tag: N5MM230NGP
kind: definition
name: Palatini variation
msc: ["83C05", "49S05"]
defines: QDHBZZE8XS
uses: [JPE3A1SN7V, JX65KSVHSJ, BY4QYYS788, 4GTNM0WHDH, PS0VV149ET, CAZYGE1T4E, 3MCZ97SW6V]
sources:
  - url: https://en.wikipedia.org/wiki/Palatini_variation
---

## Definition

Let $M$ be a manifold of dimension $n \ge 3$.
Let $g$ be a [[Lorentzian metric|BY4QYYS788]] on $M$ and let $\Gamma$ be a torsion-free [[affine connection|JX65KSVHSJ]] on $M$, not assumed to be related to $g$.
Let $R_{\mu\nu}(\Gamma)$ be the symmetric part of the [[Ricci tensor|4GTNM0WHDH]] of $\Gamma$; it depends on $\Gamma$ only.
The *Palatini action* is
$$S[g, \Gamma] = \frac{1}{16\pi G} \int_M g^{\mu\nu} R_{\mu\nu}(\Gamma) \sqrt{-\det g} \, d^n x + S_{\mathrm{m}}[g, \psi].$$
Here $G$ is the gravitational constant and units have $c = 1$.
The term $S_{\mathrm{m}}$ is a matter action that depends on $g$ and matter fields $\psi$ but not on $\Gamma$.
The *Palatini variation* is the derivation of the [[Euler–Lagrange equations|PS0VV149ET]] of $S$ in which $g$ and $\Gamma$ are varied independently of each other.

## Remarks

For a torsion-free connection, the variation of the Ricci tensor obeys the Palatini identity $\delta R_{\mu\nu} = \nabla_\lambda \delta\Gamma^\lambda_{\mu\nu} - \nabla_\nu \delta\Gamma^\lambda_{\lambda\mu}$, where $\nabla$ is the covariant derivative of $\Gamma$.
The equation from varying $\Gamma$ reduces to $\nabla_\lambda\left(\sqrt{-\det g}\, g^{\mu\nu}\right) = 0$.
Since $n \ge 3$, this gives $\nabla g = 0$, so $\Gamma$ is the [[Levi-Civita connection|CAZYGE1T4E]] of $g$.
The equation from varying $g$ is $R_{\mu\nu}(\Gamma) - \tfrac12 g_{\mu\nu} g^{\rho\sigma} R_{\rho\sigma}(\Gamma) = 8\pi G\, T_{\mu\nu}$, where $T_{\mu\nu}$ is the stress–energy tensor of $S_{\mathrm{m}}$.
With $\Gamma$ the Levi-Civita connection, these are the [[Einstein field equations|3MCZ97SW6V]].

Example: in vacuum on $\R^4$ with the Minkowski metric $\eta$ and the flat connection $\Gamma = 0$ in Cartesian coordinates, both equations hold, since $\partial_\lambda \eta^{\mu\nu} = 0$ and $R_{\mu\nu} = 0$.

Non-example: the usual metric variation of the [[Einstein–Hilbert action|JPE3A1SN7V]] is not a Palatini variation.
There $\Gamma$ is fixed as the Levi-Civita connection of $g$ and is not varied on its own.
The two give the same field equations in general relativity, but they can differ in modified theories such as $f(R)$ gravity.
