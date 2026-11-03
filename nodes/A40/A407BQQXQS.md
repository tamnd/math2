---
tag: A407BQQXQS
kind: definition
name: Ideal gas
msc: [80A10, 82D05]
defines: N7R0H2VNDJ
uses: [YPT3SJSS5T, F6JVQ12X43, AJ8M9MGZGF]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_gas
---

## Definition

Let $R$ be the molar gas constant.
An *ideal gas* is a fluid with the following property.
Every equilibrium state of $n$ moles of it, with pressure $p$, volume $V$ and [[thermodynamic temperature|AJ8M9MGZGF]] $T$, satisfies:

1. the thermal [[equation of state|YPT3SJSS5T]] $pV = nRT$;
2. its [[internal energy|F6JVQ12X43]] $U$ depends only on $T$ and $n$, not on $V$.

## Remarks

In the microscopic picture, the gas consists of point particles with no interactions besides elastic collisions; with $N$ particles and the Boltzmann constant $k$, the equation of state reads $pV = NkT$.
In thermodynamics, clause 2 follows from clause 1: the identity $(\partial U / \partial V)_T = T (\partial p / \partial T)_V - p$ gives $T \cdot nR/V - p = 0$.
An ideal gas whose heat capacities are constant is called calorically perfect; for a monatomic gas $U = \tfrac{3}{2} nRT$.

Example: helium at room temperature and atmospheric pressure satisfies $pV = nRT$ to within a small fraction of a percent, so it is well described as an ideal gas.

Non-example: a van der Waals gas, with $(p + a n^2 / V^2)(V - nb) = nRT$ and $a, b > 0$, fails clause 1, and its internal energy $U = U_{\mathrm{ideal}}(T) - a n^2 / V$ depends on $V$, so it also fails clause 2.
