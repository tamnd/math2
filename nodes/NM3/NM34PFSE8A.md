---
tag: NM34PFSE8A
kind: example
name: Kerr–Newman metric
msc: [83C22, 83C57, 83C15]
instance_of: [GAZKQEMJJ6]
uses: [2NJH36SR8A, X3FZC85THY, 8YYV4NRRMB, WRZJRJS44W]
sources:
  - url: https://en.wikipedia.org/wiki/Kerr–Newman_metric
same_as:
  wikidata: Q1190600
  wikipedia: Kerr–Newman metric
---

## Example

Use geometrized Gaussian units.
Fix a mass $M > 0$, a rotation parameter $a$ and a charge $Q$, and set $\Sigma = r^2 + a^2\cos^2\theta$ and $\Delta = r^2 - 2Mr + a^2 + Q^2$.
The *Kerr–Newman metric* is the metric $g$ written in [[Boyer–Lindquist coordinates|2NJH36SR8A]] with these $\Sigma$ and $\Delta$, together with the electromagnetic potential
$$A = -\frac{Q r}{\Sigma}\left(dt - a\sin^2\theta\, d\phi\right), \qquad F = dA.$$
The pair $(g, F)$ is an [[electrovacuum solution|GAZKQEMJJ6]]: $F$ solves the source-free Maxwell equations and $g$ solves the Einstein equations with the electromagnetic stress–energy of $F$.

Checks of the special cases follow.
For $Q = 0$ the field vanishes and $g$ is the [[Kerr metric|X3FZC85THY]].
For $a = 0$, $\Sigma = r^2$, the cross term vanishes, $A = -\frac{Q}{r} dt$, and $(g, F)$ is the [[Reissner–Nordström metric|8YYV4NRRMB]].
For $a = Q = 0$ it is the [[Schwarzschild metric|6Y50T68WKY]].
Since $dF = d(dA) = 0$, half of Maxwell's equations hold automatically.

The parameters have a physical meaning: $M$ is the mass, $J = aM$ the angular momentum, $Q$ the charge, and the magnetic dipole moment is $Qa$.
If $a^2 + Q^2 \le M^2$, the zeros of $\Delta$ are $r_\pm = M \pm \sqrt{M^2 - a^2 - Q^2}$, and $r_+$ is the [[event horizon|D8NZ32Z3SQ]].
If $a^2 + Q^2 > M^2$ there is no horizon.

## Explanations

### L1 human

The Kerr–Newman metric describes a black hole that both rotates and carries electric charge.
It contains all the simpler black holes as special cases: switch off the charge to get Kerr, switch off the rotation to get Reissner–Nordström, switch off both to get Schwarzschild.
The rotating charge also produces a magnetic field, like a spinning charged ball.
By the [[no-hair theorem|RAEHHEPX7F]], mass, angular momentum and charge are all that a stationary black hole in electrovacuum can have.
