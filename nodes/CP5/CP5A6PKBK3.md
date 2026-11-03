---
tag: CP5A6PKBK3
kind: definition
name: Nicholson–Bailey model
msc: [92D25, 39A60, 92D40]
defines: 32BBSD1GRM
uses: [1YEMFQ1H32, 0FYX44GP92, 0N8NGKDZDZ]
sources:
  - url: https://en.wikipedia.org/wiki/Nicholson%E2%80%93Bailey_model
---

## Definition

Let $\lambda > 0$ be the host reproduction factor and $a > 0$ the searching efficiency of the parasitoids.
Let $c > 0$ be the number of parasitoids that emerge from one parasitised host.
The *Nicholson–Bailey model* is the [[recurrence relation|0FYX44GP92]]
$$H_{t+1} = \lambda \, H_t \, e^{-a P_t}, \qquad P_{t+1} = c \, H_t \left(1 - e^{-a P_t}\right), \qquad t = 0, 1, 2, \ldots,$$
where $H_t \ge 0$ and $P_t \ge 0$ are the numbers of hosts and of parasitoids in generation $t$.

## Remarks

The factor $e^{-a P_t}$ is the probability that a host escapes all parasitoids when their encounters are random, given by the zero term of a Poisson distribution with mean $a P_t$.
Example: for $\lambda > 1$, the positive [[equilibrium point|0N8NGKDZDZ]] is $P^* = \frac{\ln \lambda}{a}$ and $H^* = \frac{\lambda \ln \lambda}{(\lambda - 1) a c}$.
Check: $\lambda e^{-a P^*} = \lambda / \lambda = 1$, and $c H^* (1 - 1/\lambda) = \frac{\ln \lambda}{a} = P^*$.
This equilibrium is unstable for every choice of the parameters with $\lambda > 1$, and nearby solutions oscillate with growing amplitude.
Non-example: the Lotka–Volterra predator–prey equations are a model of the same kind of interaction, but in continuous time, so they are not a Nicholson–Bailey model.
