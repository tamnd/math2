---
tag: D3N4PQ89ME
kind: definition
name: Fourier number
msc: [80A19, 35K05]
defines: HYWTTMTKKM
uses: [T3R5FWV91P, CS4ZZX092Z, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_number
---

## Definition

Let a body of [[thermal diffusivity|CS4ZZX092Z]] $\alpha > 0$ conduct heat, and let $L > 0$ be a characteristic length of the body.
For a time $t \ge 0$, the *Fourier number* is the [[dimensionless number|T3R5FWV91P]]
$$\mathrm{Fo} = \frac{\alpha \, t}{L^2}.$$

## Remarks

The substitution $\tau = \alpha t / L^2$ and $\xi = x / L$ turns the [[heat equation|VP2HN86VAG]] $\partial_t T = \alpha \Delta_x T$ into $\partial_\tau T = \Delta_\xi T$.
So $\mathrm{Fo}$ is the time variable of the dimensionless heat equation.

Example: a steel plate with $\alpha = 1.2 \cdot 10^{-5}$ square metres per second and half-thickness $L = 0.01$ metres, after $t = 10$ seconds.
Then $\mathrm{Fo} = 1.2 \cdot 10^{-5} \cdot 10 / 10^{-4} = 1.2$.

Non-example: $\alpha t / L$ is not the Fourier number; it has the unit of a length, so it is not dimensionless.
