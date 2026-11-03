---
tag: FM8H50AYZJ
kind: example
name: Lorenz 96 model
msc: [37N10, 34C28, 86A10]
illustrates: [G0ZT1SDQGS]
uses: [BBZP1R872N, NJ1FJSNK6A]
sources:
  - url: https://en.wikipedia.org/wiki/Lorenz_96_model
same_as:
  wikidata: Q6680551
  wikipedia: Lorenz 96 model
---

## Example

Fix an integer $N \ge 4$ and a constant forcing $F \in \R$.
The *Lorenz 96 model* is the system of ordinary differential equations for $x = (x_1, \dots, x_N) \in \R^N$
$$\frac{dx_i}{dt} = (x_{i+1} - x_{i-2}) \, x_{i-1} - x_i + F, \qquad i = 1, \dots, N,$$
with cyclic indices $x_{-1} = x_{N-1}$, $x_0 = x_N$ and $x_{N+1} = x_1$.
The variables stand for an atmospheric quantity at $N$ equally spaced points around a circle of latitude.
The quadratic term models advection, $-x_i$ models damping and $F$ models forcing.
It was introduced by Edward Lorenz in 1996 as a test bed for questions of predictability.

Check of two properties.
The state $x_i = F$ for all $i$ is an equilibrium, since $(F - F) F - F + F = 0$.
The quadratic term conserves energy: with $E = \frac12 \sum_i x_i^2$,
$$\sum_i x_i (x_{i+1} - x_{i-2}) x_{i-1} = \sum_i x_{i-1} x_i x_{i+1} - \sum_i x_{i-2} x_{i-1} x_i = 0,$$
because the second sum is the first with the index shifted by one.
Hence $dE/dt = -2E + F \sum_i x_i$.
By the Cauchy–Schwarz inequality $\abs{F \sum_i x_i} \le \abs{F} \sqrt{2NE}$, so $dE/dt < 0$ whenever $E > N F^2 / 2$, and every solution enters and stays in a bounded ball.

For small positive $F$ the equilibrium is stable.
For the standard choice $N = 40$ and $F = 8$, numerical studies show chaotic behaviour with several positive [[Lyapunov exponents|NJ1FJSNK6A]].
Two solutions that start very close separate exponentially fast, which is the [[butterfly effect|G0ZT1SDQGS]].
This makes the model a standard test for data assimilation methods.

## Explanations

### L1 human

The Lorenz 96 model is a toy weather system: a ring of numbers, one per site around the globe.
Each number is pushed by its neighbours, slowed by friction and kept going by a steady forcing.
It is small enough to run on a laptop yet behaves like real weather: it is chaotic.
Change one number in the tenth decimal place, and after a while the two runs look completely different.
Scientists use it to try out new ways of forecasting and of combining models with observations before using them on real weather models.
