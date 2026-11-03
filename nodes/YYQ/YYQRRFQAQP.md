---
tag: YYQRRFQAQP
kind: statement
role: theorem
name: Thermodynamic stability conditions
msc: [80A10, 80A05]
uses: [F6JVQ12X43, SPY89W0RJ7, SYYGZ18FF5, 1BPF2AA6VR, JXKY6C8JTA, C2QNWE50TW, 0SCSQWXRA4]
about: [5EKTEE00FZ, SYYGZ18FF5, 1BPF2AA6VR]
sources:
  - url: https://en.wikipedia.org/wiki/Thermodynamic_equilibrium
---

## Statement

Let a simple system with a fixed amount of matter have an [[internal energy|F6JVQ12X43]] $U(S, V)$, a function of the [[entropy|SPY89W0RJ7]] $S$ and the volume $V$.
Assume that $U$ is twice continuously differentiable.
Let $T = (\partial U / \partial S)_V > 0$ be the temperature and $p = -(\partial U / \partial V)_S$ the pressure.
Let $C_V$ be its [[heat capacity|SYYGZ18FF5]] at constant volume and $\kappa_T$ its [[isothermal compressibility|1BPF2AA6VR]].
Then the [[Hessian matrix|0SCSQWXRA4]] of $U$ with respect to $(S, V)$ is positive definite at a state if and only if, at that state,
$$C_V > 0 \quad \text{and} \quad \kappa_T > 0.$$

## Remarks

By the [[principle of minimum energy|C2QNWE50TW]], a stable equilibrium requires $U$ to be convex in $(S, V)$, and local stability in the strict sense is positive definiteness of the Hessian.
The proof computes the Hessian entries.
First, $U_{SS} = (\partial T / \partial S)_V = T / C_V$, which is positive if and only if $C_V > 0$.
Second, the [[Helmholtz free energy|JXKY6C8JTA]] $F(T, V)$ is the Legendre transform of $U$ in $S$, and $F_{VV} = U_{VV} - U_{SV}^2 / U_{SS} = \det(\text{Hessian}) / U_{SS}$.
Since $F_{VV} = -(\partial p / \partial V)_T = 1/(V \kappa_T)$, the determinant is positive if and only if $\kappa_T > 0$, given $U_{SS} > 0$.

Consequences are $C_p \ge C_V > 0$ and $\kappa_T \ge \kappa_S > 0$, through the identities $C_p - C_V = T V \alpha^2 / \kappa_T$ and $\kappa_T - \kappa_S = T V \alpha^2 / C_p$, where $\alpha$ is the thermal expansion coefficient.
Example: an ideal gas has $C_V = \tfrac{3}{2} nR > 0$ (monatomic case) and $\kappa_T = 1/p > 0$, so all its states are stable.
The van der Waals isotherms below the critical temperature contain a stretch with $(\partial p / \partial V)_T > 0$, that is $\kappa_T < 0$; these states are unstable, and the fluid separates into liquid and vapour instead.

## Explanations

### L1 human

An equilibrium is stable when a small push is undone rather than amplified.
For a fluid this comes down to two common-sense facts.
Adding heat must raise the temperature, and squeezing must reduce the volume.
If either failed, a tiny fluctuation would grow on its own, and the state could not last.

### L2 human

The conditions are the second-order part of the extremum principles of thermodynamics: entropy is concave and energy is convex in the extensive variables.
Each Legendre transform turns convexity in one variable into concavity in its conjugate, which is why $F$ is concave in $T$ and convex in $V$.
Where the conditions fail, the system is unstable against splitting into phases, and the boundary $(\partial p / \partial V)_T = 0$ is the spinodal; the Maxwell construction then gives the actual coexisting phases.
With more variables, such as several species, the same statement holds with the full Hessian of $U$ in all extensive variables but one.
