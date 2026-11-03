---
tag: XDSE93QMNM
kind: example
name: Taylor–von Neumann–Sedov blast wave
msc: [76L05, 76N15]
instance_of: [579J5K9K5Z]
uses: [FRVV0NHBXT, RW0JK9VDZE]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor%E2%80%93von_Neumann%E2%80%93Sedov_blast_wave
---

## Example

An energy $E > 0$ is released at a point at time $t = 0$ in a polytropic gas at rest, of uniform density $\rho_0$, with adiabatic exponent $\gamma > 1$.
Assume the pressure of the undisturbed gas is negligible, so the outgoing spherical [[shock wave|FRVV0NHBXT]] is strong.
Then the flow is a self-similar solution of the [[Euler equations|RW0JK9VDZE]].
The shock radius is
$$R(t) = \xi_0 \left( \frac{E t^2}{\rho_0} \right)^{1/5},$$
where $\xi_0$ is a dimensionless constant that depends only on $\gamma$.
Behind the shock, the density, velocity and pressure are fixed profiles in the variable $r / R(t)$, scaled by powers of $t$.

Check by dimensions: the only parameters are $E$, of dimension mass times length squared over time squared, and $\rho_0$, of dimension mass over length cubed.
So $E t^2 / \rho_0$ has dimension length to the fifth power, and $(E t^2/\rho_0)^{1/5}$ is the only length that can be formed from $E$, $\rho_0$ and $t$.
The shock speed is $R'(t) = \tfrac{2}{5} R(t)/t$, which decreases in time as the energy spreads over a growing volume.

## Remarks

The profiles solve a system of ordinary differential equations, with the strong-shock Rankine–Hugoniot conditions at $r = R(t)$.
Taylor, von Neumann and Sedov found this solution independently, and Sedov and von Neumann gave it in closed form.
G. I. Taylor used the formula $R \propto (E t^2/\rho_0)^{1/5}$ with published photographs of the first atomic explosion to estimate its energy.
The solution stops being accurate at late times, when the shock weakens and the pressure of the undisturbed gas matters.

## Explanations

### L1 human

A very strong explosion sends out a spherical shock wave.
At early times its growth depends only on the energy released and the density of the air.
Dimension counting alone shows that the radius grows like the time to the power $2/5$.
So from a few photographs of the fireball at known times one can read off the energy of the explosion.
