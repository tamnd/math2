---
tag: 1YZQ7H0THE
kind: example
name: Totally asymmetric simple exclusion process
msc: [82C22, 60K35, 82C23]
instance_of: [GR49AM3PSZ]
uses: [TXC6PZT8CF, GR49AM3PSZ]
sources:
  - url: https://en.wikipedia.org/wiki/Asymmetric_simple_exclusion_process
---

## Example

The *totally asymmetric simple exclusion process* (TASEP) on $\Z$ is the [[asymmetric simple exclusion process|TXC6PZT8CF]] in which particles jump only to the right.
A configuration is $\eta \in \set{0, 1}^{\Z}$, where $\eta(x) = 1$ means that site $x$ holds a particle.
Each particle carries an independent rate-one exponential clock.
When it rings, the particle at $x$ moves to $x + 1$ if that site is empty, and otherwise stays.
Its generator, on functions $f$ that depend on finitely many coordinates, is
$$Lf(\eta) = \sum_{x \in \Z} \eta(x)\big(1 - \eta(x + 1)\big)\big(f(\eta^{x, x+1}) - f(\eta)\big),$$
where $\eta^{x, x+1}$ exchanges the values at $x$ and $x + 1$.
This is an [[interacting particle system|GR49AM3PSZ]]: the ASEP with $p = 1$ and $q = 0$.

## Remarks

For each density $\rho \in [0, 1]$, the Bernoulli product measure of density $\rho$ is invariant.
In that state the mean current across a bond is $\rho(1 - \rho)$, the rate of a jump times the probability that the site is occupied and its right neighbour empty.
On the hydrodynamic scale the density solves the inviscid Burgers equation $\partial_t \rho + \partial_x\big(\rho(1 - \rho)\big) = 0$.
Start from the step initial condition, with all sites $x \le 0$ occupied and all sites $x > 0$ empty.
Rost (1981) proved that the macroscopic density at time $t$ is the rarefaction fan $\rho = \tfrac12(1 - x/t)$ for $\abs{x} \le t$.
For the same initial condition, Johansson (2000) proved that the number of particles that have crossed the origin has fluctuations of order $t^{1/3}$ with the Tracy–Widom GUE law.
This makes TASEP a basic exactly solvable model of the Kardar–Parisi–Zhang universality class.

## Explanations

### L1 human

Picture a one-lane road where cars only drive forward and a car moves only if the cell in front is free.
Every car tries to move at random times, at the same average rate.
With a uniform traffic density $\rho$, the flow of cars is $\rho(1 - \rho)$: few cars give little flow, and a jam gives little flow too.
Starting with a solid block of cars, the block melts into a linear ramp of density that spreads at speed one in both directions.
