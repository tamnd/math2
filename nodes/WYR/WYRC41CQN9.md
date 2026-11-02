---
tag: WYRC41CQN9
kind: example
name: Lorenz system
msc: [34C28, 37D45]
instance_of: [0673D85QKZ]
uses: [0G4X36AE0X, F5H8GW1XYS, P88X34MSVV]
sources:
  - url: https://en.wikipedia.org/wiki/Lorenz_system
---

## Example

Let $\sigma, \rho, \beta > 0$.
The Lorenz system is the [[autonomous system|0673D85QKZ]] in $\R^3$
$$x' = \sigma (y - x), \qquad y' = x (\rho - z) - y, \qquad z' = x y - \beta z.$$
The classical parameter values are $\sigma = 10$, $\beta = 8/3$ and $\rho = 28$.

The origin is an [[equilibrium point|0G4X36AE0X]] for all parameters.
For $\rho > 1$ there are two more equilibria $C_\pm = \left(\pm\sqrt{\beta(\rho - 1)}, \pm\sqrt{\beta(\rho - 1)}, \rho - 1\right)$.
Check: $x = y$ makes the first equation vanish, then $z = \rho - 1$ makes the second vanish, and $x^2 = \beta(\rho - 1)$ makes the third vanish.

## Remarks

The divergence of the vector field is $-(\sigma + 1 + \beta) < 0$, so the flow shrinks volumes at a constant exponential rate.
At $\rho = 1$, the two equilibria $C_\pm$ branch off the origin in a [[pitchfork bifurcation|P88X34MSVV]].
For $\sigma > \beta + 1$, the linearisation at $C_\pm$ has a pair of purely imaginary eigenvalues at $\rho = \sigma(\sigma + \beta + 3)/(\sigma - \beta - 1)$.
For $\sigma = 10$ and $\beta = 8/3$ this value is $470/19 \approx 24.74$, and there $C_\pm$ lose stability in a subcritical [[Hopf bifurcation|F5H8GW1XYS]].
At the classical values, numerical solutions approach a butterfly-shaped set, the Lorenz attractor, and nearby solutions separate quickly.
Warwick Tucker gave a computer-assisted proof in 2002 that this set is a strange attractor.

## Explanations

### L1 human

Edward Lorenz found these three equations in 1963 as a very simplified model of convection in the atmosphere.
Solutions wind around two lobes and switch between them in an unpredictable way.
Two solutions that start very close soon look completely different.
This sensitivity is the "butterfly effect" and the Lorenz system is its standard example.
