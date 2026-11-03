---
tag: W3PMXQGA4Y
kind: definition
name: Conjugate variables
msc: [80A05, 80A10]
defines: 3W28H76A82
uses: [H9F9CNPBSN, F6JVQ12X43, SPY89W0RJ7, AJ8M9MGZGF, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_variables_(thermodynamics)
---

## Definition

Let a system in equilibrium have [[internal energy|F6JVQ12X43]] $U = U(X_1, \dots, X_k)$, a differentiable function of [[extensive|H9F9CNPBSN]] variables $X_1, \dots, X_k$.
For each $i$, the variable conjugate to $X_i$ is the intensive variable
$$Y_i = \frac{\partial U}{\partial X_i},$$
where the [[partial derivative|09EGC6F8PT]] is taken with the other $X_j$ fixed.
The pairs $(Y_i, X_i)$ are the *conjugate pairs*, and $dU = \sum_{i=1}^{k} Y_i \, dX_i$.

## Remarks

For a simple fluid with [[entropy|SPY89W0RJ7]] $S$, volume $V$ and particle number $N$, one has
$$dU = T \, dS - p \, dV + \mu \, dN.$$
So [[thermodynamic temperature|AJ8M9MGZGF]] $T$ is conjugate to $S$, the pressure $p$ to $V$ up to sign, and the chemical potential $\mu$ to $N$.
Each product $T S$, $p V$ and $\mu N$ has the dimension of energy.
Temperature and pressure are not a conjugate pair: both are intensive, and neither is the derivative of $U$ with respect to the other.
Other pairs are magnetic field and magnetic moment, and surface tension and area.
