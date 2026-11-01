---
tag: TXC6PZT8CF
kind: example
name: Asymmetric simple exclusion process
msc: [60K35, 82C22]
instance_of: [GR49AM3PSZ]
sources:
  - url: https://en.wikipedia.org/wiki/Asymmetric_simple_exclusion_process
same_as:
  wikidata: Q297612
  wikipedia: Asymmetric simple exclusion process
---

## Example

Let $p \in [0, 1]$ and $q = 1 - p$.
The *asymmetric simple exclusion process* (ASEP) on $\Z$ is the [[interacting particle system|GR49AM3PSZ]] on $\set{0, 1}^{\Z}$ in which $\eta(x) = 1$ means that site $x$ holds a particle.
Each particle tries to jump one step to the right at rate $p$ and one step to the left at rate $q$.
A jump is suppressed if the target site is occupied.
Its generator, on functions $f$ that depend on finitely many coordinates, is
$$Lf(\eta) = \sum_{x \in \Z} \Big( p\, \eta(x) \big(1 - \eta(x+1)\big) + q\, \eta(x+1) \big(1 - \eta(x)\big) \Big) \big( f(\eta^{x,x+1}) - f(\eta) \big),$$
where $\eta^{x,x+1}$ exchanges the values at $x$ and $x + 1$.
This is the exclusion process with jump rates $p(x, x+1) = p$ and $p(x+1, x) = q$, so it is an interacting particle system.

## Remarks

Particles are never created or destroyed, and two particles never share a site.
For each $\rho \in [0, 1]$, the product measure under which the $\eta(x)$ are independent Bernoulli variables with mean $\rho$ is invariant.
The case $p = 1$ is the totally asymmetric simple exclusion process (TASEP), and the case $p = q = 1/2$ is the symmetric exclusion process.
In the asymmetric case the current of particles in the Bernoulli state of density $\rho$ is $(p - q)\rho(1 - \rho)$.

## Explanations

### L1 human

Picture cars on a one-lane road divided into cells, at most one car per cell.
Each car tries to move forward at random times, but it cannot move into a cell that is already taken.
This simple rule produces traffic jams and shock waves, and the ASEP is a basic model of such traffic.
