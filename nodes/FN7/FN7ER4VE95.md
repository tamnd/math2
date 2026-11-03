---
tag: FN7ER4VE95
kind: statement
role: proposition
name: Tsiolkovsky rocket equation
msc: [70F99, 70M20]
uses: [Z82XBYZD1P, T1SHG5MD9R]
about: [Z82XBYZD1P]
sources:
  - url: https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation
same_as:
  wikidata: Q834199
  wikipedia: Tsiolkovsky rocket equation
---

## Statement

Let a rocket move along a line with no external force.
Assume that it ejects mass backwards at a constant speed $v_e > 0$ relative to itself.
So it is a [[variable-mass system|Z82XBYZD1P]], and its mass decreases from $m_0$ to $m_f$, with $m_0 > m_f > 0$.
Then its change of velocity is
$$\Delta v = v_e \ln \frac{m_0}{m_f}.$$

## Remarks

The equation of motion of the variable-mass system is $m\, dv/dt = -v_e\, dm/dt$, a consequence of [[conservation of momentum|T1SHG5MD9R]].
So $dv = -v_e\, dm / m$, and integrating from $m_0$ to $m_f$ gives the result.
The result does not depend on how fast the fuel is burnt.
Example: to reach $\Delta v = v_e$ the mass ratio must be $m_0 / m_f = e \approx 2.72$; to reach $\Delta v = 3 v_e$ it must be $e^3 \approx 20$.
With gravity or drag the hypothesis of no external force fails, and the actual gain in speed is smaller, by the time integral of these forces divided by the mass.
Tsiolkovsky published the equation in 1903.

## Explanations

### L1 human

A rocket's gain in speed depends only on how fast its exhaust leaves and on how much lighter it becomes.
The dependence on the mass ratio is only logarithmic, so each extra unit of speed costs a multiplication of the starting mass.
That is why rockets are mostly fuel and why they drop empty stages.

### L2 human

The equation is the budget rule of spaceflight: every manoeuvre has a $\Delta v$, computed with the vis-viva equation, and the sum fixes the needed mass ratio.
For a multistage rocket, the $\Delta v$ of the stages add, which lets the total exceed what one stage of the same propellant could reach.
It is the simplest application of the general equation $m\, dv/dt = F + u\, dm/dt$ of a variable-mass system, with $F = 0$ and $u = -v_e$.
