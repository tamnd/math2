---
tag: 1JE4AC4QFF
kind: statement
role: theorem
name: Crocco's theorem
msc: [76N15, 76A02]
uses: [ZJH90RWYQ5, B3SXT9TWFA]
about: [B3SXT9TWFA]
sources:
  - url: https://en.wikipedia.org/wiki/Crocco%27s_theorem
same_as:
  wikidata: Q580245
  wikipedia: Crocco's theorem
---

## Statement

Consider a steady, [[inviscid|ZJH90RWYQ5]] flow of a compressible fluid without body forces, with velocity $u$, density $\rho > 0$ and pressure $p$, all smooth.
Let $T$ be the temperature, $s$ the specific entropy and $h$ the specific enthalpy, related by $dh = T \, ds + dp / \rho$.
Let $h_0 = h + \abs{u}^2 / 2$ be the stagnation enthalpy and $\omega = \nabla \times u$ the [[vorticity|B3SXT9TWFA]].
Then
$$u \times \omega = \nabla h_0 - T \nabla s.$$

## Remarks

The steady Euler equation is $(u \cdot \nabla) u = -\nabla p / \rho$.
The identity $(u \cdot \nabla) u = \nabla(\abs{u}^2/2) - u \times \omega$ and the thermodynamic relation $\nabla p / \rho = \nabla h - T \nabla s$ turn it into the formula.

Example: behind a curved shock wave in a uniform supersonic stream, $h_0$ is still uniform but the entropy jump differs from one streamline to the next.
So $\nabla s \ne 0$, and the theorem forces $\omega \ne 0$: a curved shock creates vorticity.

Conversely, if $h_0$ and $s$ are uniform, then $u \times \omega = 0$, so the flow is either irrotational or has its vorticity parallel to the velocity.

## Explanations

### L1 human

Crocco's theorem links three things in a steady ideal gas flow: swirl, changes of total energy, and changes of entropy.
If the total energy and the entropy are the same everywhere, the flow cannot swirl across its own direction of motion.
So swirl in such a flow points to differences in entropy or energy, such as those made by a curved shock.

### L2 human

The theorem is the compressible counterpart of the relation $\nabla H = u \times \omega$ behind [[Bernoulli's principle|7XFWQVWPG1]].
In a plane flow the vorticity is perpendicular to the velocity, so uniform $h_0$ and $s$ force $\omega = 0$ wherever $u \ne 0$.
This justifies a velocity potential for such flows, and it shows where this fails, for instance downstream of curved shocks.
