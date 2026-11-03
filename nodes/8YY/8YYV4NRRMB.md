---
tag: 8YYV4NRRMB
kind: example
name: Reissner–Nordström metric
msc: [83C22, 83C57, 83C15]
instance_of: [GAZKQEMJJ6]
uses: [6Y50T68WKY, WRZJRJS44W, 5BNCD886T7]
sources:
  - url: https://en.wikipedia.org/wiki/Reissner–Nordström_metric
same_as:
  wikidata: Q540664
  wikipedia: Reissner–Nordström metric
---

## Example

Use geometrized Gaussian units, where the gravitational constant, the speed of light and the Coulomb constant equal $1$.
Fix a mass $M > 0$ and a charge $Q \in \R$, and set
$$f(r) = 1 - \frac{2M}{r} + \frac{Q^2}{r^2}.$$
On the region where $f(r) > 0$, with coordinates $(t, r, \theta, \phi)$, the *Reissner–Nordström metric* and its field are
$$g = -f(r)\, dt^2 + f(r)^{-1} dr^2 + r^2\left(d\theta^2 + \sin^2\theta\, d\phi^2\right), \qquad F = \frac{Q}{r^2}\, dr \wedge dt.$$
The pair $(g, F)$ is an [[electrovacuum solution|GAZKQEMJJ6]].

Check of Maxwell's equations: $F = dA$ with $A = -\frac{Q}{r}\, dt$, so $dF = 0$.
The only nonzero components are $F_{rt} = -F_{tr} = Q/r^2$.
Since $g^{tt} g^{rr} = -1$, one gets $F^{tr} = -F_{tr} = Q/r^2$, and with $\sqrt{-\det g} = r^2 \sin\theta$,
$$\partial_r\left(\sqrt{-\det g}\, F^{tr}\right) = \partial_r(Q \sin\theta) = 0.$$
So the source-free equation $\nabla_a F^{ab} = 0$ holds, and the field is a Coulomb field of charge $Q$.
The Einstein equations follow from a computation of the [[Ricci curvature|4GTNM0WHDH]], which gives $R_{ab} = 2(F_{ac}F_b{}^c - \frac14 g_{ab} F_{cd}F^{cd})$.

For $Q = 0$ the metric is the [[Schwarzschild metric|6Y50T68WKY]].
If $Q^2 < M^2$, then $f$ has two zeros $r_\pm = M \pm \sqrt{M^2 - Q^2}$, an outer [[event horizon|D8NZ32Z3SQ]] $r_+$ and an inner Cauchy horizon $r_-$.
If $Q^2 = M^2$ the two coincide (the extremal case), and if $Q^2 > M^2$ there is no horizon and the singularity at $r = 0$ is naked.

## Explanations

### L1 human

This is the spacetime outside a round, non-rotating body that carries an electric charge.
Far away it looks like the Schwarzschild spacetime with a Coulomb electric field on top.
The energy of the electric field also curves spacetime, which is why the charge appears in the metric through the term $Q^2/r^2$.
A charged black hole has two horizons instead of one.
If the charge were larger than the mass in these units, there would be no horizon at all, which is believed not to happen in nature.
