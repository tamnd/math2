---
tag: KASWZJ5TVM
kind: definition
name: Electrovacuum solution
msc: [83C22, 83C15, 83C50]
defines: GAZKQEMJJ6
uses: [BY4QYYS788, 3MCZ97SW6V, WRZJRJS44W, 5BNCD886T7, N22WEQ3GWH]
sources:
  - url: https://en.wikipedia.org/wiki/Electrovacuum_solution
---

## Definition

Work in geometrized Gaussian units, where the gravitational constant and the speed of light equal $1$.
Let $(M, g)$ be a four-dimensional [[Lorentzian manifold|BY4QYYS788]] and let $F$ be a nonzero real $2$-form on $M$, the [[electromagnetic field tensor|WRZJRJS44W]].
The pair $(g, F)$ is an *electrovacuum solution* if:

1. $F$ solves the source-free [[Maxwell equations in curved spacetime|5BNCD886T7]], $dF = 0$ and $d{\star F} = 0$, where $\star$ is the Hodge star of $g$;
2. $g$ solves the [[Einstein field equations|3MCZ97SW6V]] $G_{ab} = 8\pi T_{ab}$, where $G_{ab}$ is the Einstein tensor of $g$ and $T_{ab}$ is the [[electromagnetic stress–energy tensor|N22WEQ3GWH]]
$$T_{ab} = \frac{1}{4\pi}\left(F_{ac} F_b{}^{c} - \frac{1}{4} g_{ab} F_{cd} F^{cd}\right).$$

## Remarks

Example: the [[Reissner–Nordström metric|8YYV4NRRMB]] with charge $Q \ne 0$ and the radial field $F = \frac{Q}{r^2}\, dr \wedge dt$ is an electrovacuum solution.
Clause 1 holds because $F = d(-Q\, dt / r)$ is exact, and $\star F$ is a multiple of $Q \sin\theta \, d\theta \wedge d\phi$, which is closed.
Clause 2 is a direct computation of the Ricci tensor.

Non-example: the [[interior Schwarzschild metric|P5SCM8NKMQ]] is not an electrovacuum solution.
Its source is a perfect fluid with positive pressure, whose stress–energy tensor has nonzero trace, while the trace $T^a{}_a$ of the electromagnetic stress–energy tensor is always $0$.

Equivalent form: since $T_{ab}$ is trace-free in dimension four, the scalar curvature vanishes, and clause 2 becomes
$$R_{ab} = 2\left(F_{ac} F_b{}^{c} - \frac{1}{4} g_{ab} F_{cd} F^{cd}\right),$$
where $R_{ab}$ is the [[Ricci curvature|4GTNM0WHDH]] of $g$.
If $F = 0$ were allowed, the definition would reduce to a [[vacuum solution|JRV1T69FYJ]].
