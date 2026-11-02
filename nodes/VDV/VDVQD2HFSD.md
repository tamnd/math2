---
tag: VDVQD2HFSD
kind: problem
name: Smale's fourteenth problem
msc: ["37D45", "37C10", "37M10"]
uses: [WYRC41CQN9, 9WKCZGG906, 7FWX24X5MW]
about: [WYRC41CQN9]
sources:
  - url: https://en.wikipedia.org/wiki/Lorenz_system
  - url: https://en.wikipedia.org/wiki/Smale%27s_problems
history:
  posed_by: "Stephen Smale"
  first_stated: "1998"
---

## Problem

Consider the [[Lorenz system|WYRC41CQN9]] in $\R^3$,
$$\dot x = \sigma (y - x), \qquad \dot y = x(\rho - z) - y, \qquad \dot z = xy - \beta z,$$
with the classical parameters $\sigma = 10$, $\rho = 28$ and $\beta = 8/3$.
Does the flow of this system have a [[strange attractor|9WKCZGG906]], with the dynamics of the geometric Lorenz attractor?

## Remarks

The geometric Lorenz attractor is a model flow, built in the 1970s from the features seen in numerical simulations.
For the model, the existence of a robust [[attractor|7FWX24X5MW]] with sensitive dependence on initial conditions was proved.
The question was whether the actual Lorenz equations behave like the model.
Smale included it as the fourteenth problem of his 1998 list of problems for the next century.
Warwick Tucker gave a positive answer with a computer-assisted proof, published in 2002.
His proof combines rigorous numerics with interval arithmetic, far from the origin, with normal form theory near the equilibrium at the origin.

## Explanations

### L1 human

The Lorenz system is a simple model of convection whose solutions trace the famous butterfly-shaped figure on a computer.
Pictures are not proofs: rounding errors might hide a stable cycle, and the figure might then be an illusion.
Smale asked for a proof that the butterfly is a true chaotic attractor.
The answer is yes, and its proof was a major use of computers to settle a question in dynamics.
