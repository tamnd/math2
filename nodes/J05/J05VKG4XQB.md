---
tag: J05VKG4XQB
kind: conjecture
name: Schiffer's conjecture
msc: [35N25, 35P05, 35R30]
uses: [0E0B6RA8K0, 4VD8XXQ4P3]
about: [M1KYAQMF9W]
sources:
  - url: https://en.wikipedia.org/wiki/Pompeiu_problem
history:
  posed_by: "Menahem Max Schiffer"
---

## Statement

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded, simply connected domain with smooth boundary $\partial\Omega$ and outer unit normal $\nu$.
Suppose that for some $\lambda > 0$ and some constant $c$ there is a nonzero function $u$ with
$$\Delta u + \lambda u = 0 \text{ in } \Omega, \qquad \frac{\partial u}{\partial \nu} = 0 \text{ on } \partial\Omega, \qquad u = c \text{ on } \partial\Omega,$$
where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
The conjecture states that $\Omega$ is then a ball.

## Remarks

The boundary value problem is overdetermined: $u$ is a Neumann eigenfunction that is also constant on the boundary.
Every ball admits such a solution: a radial Neumann eigenfunction is constant on each sphere centred at the centre of the ball.
By a result of Williams (1976), for these domains the conjecture is equivalent to the [[Pompeiu problem|M1KYAQMF9W]], that only balls fail the Pompeiu property.
Consider the analogous problem for a Dirichlet eigenfunction with constant normal derivative.
By Serrin's theorem on overdetermined problems, when the Dirichlet eigenfunction is positive, the domain must be a ball.

## Explanations

### L1 human

Take a membrane with a free edge and look at one of its vibration patterns.
Suppose that along the whole edge the membrane sits at one common height.
Schiffer guessed that this can only happen when the membrane is round.
