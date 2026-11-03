---
tag: TK6JCG9AVZ
kind: definition
name: Equation of state in cosmology
msc: ["83F05", "83C55"]
defines: 6A915X05CK
uses: [H4FNPG6ZY1, J70F32P86W, PPHFS2P4G4]
sources:
  - url: https://en.wikipedia.org/wiki/Equation_of_state_(cosmology)
---

## Definition

Let a component of the matter in a Friedmann–Lemaître–Robertson–Walker model be a [[perfect fluid|H4FNPG6ZY1]] with energy density $\rho \neq 0$ and pressure $p$, in units with $c = 1$.
Its *equation of state parameter* is $w = p / \rho$.
The component has a *linear equation of state* when $w$ is a constant, so that $p = w \rho$.

## Remarks

Suppose the component is separately conserved and $w \neq -1$ is constant.
Then the continuity equation $\dot\rho + 3 (\dot a / a)(\rho + p) = 0$ from the [[Friedmann equations|PPHFS2P4G4]] integrates to
$$\rho \propto a^{-3(1 + w)},$$
where $a$ is the [[scale factor|J70F32P86W]]; for $w = -1$ the density is constant.
Example: radiation has $p = \rho/3$, so $w = 1/3$ and $\rho \propto a^{-4}$.
Pressureless dust has $w = 0$ and $\rho \propto a^{-3}$; a cosmological constant has $w = -1$.
Non-example: a homogeneous scalar field with $\rho = \tfrac{1}{2}\dot\phi^2 + V(\phi)$ and $p = \tfrac{1}{2}\dot\phi^2 - V(\phi)$ has $w = p/\rho$, but $w$ varies in time in general, so it has no linear equation of state.
In a spatially flat model filled with one component with constant $w > -1$, the scale factor is $a \propto t^{2/(3(1 + w))}$.
