---
tag: VPA41PWRR1
kind: concept
name: Infinitesimal generator of a Markov process
msc: [60J35, 47D07, 47D06]
sources:
  - url: https://en.wikipedia.org/wiki/Infinitesimal_generator_(stochastic_processes)
same_as:
  wikidata: Q915487
  wikipedia: Infinitesimal generator (stochastic processes)
---

## Summary

The infinitesimal generator of a Markov process is the operator that gives the rate of change of expected values at time $0$.
It is the derivative at $t = 0$ of the transition [[semigroup|0XMEM406JM]] of the process.
For a [[Feller process|4HS3C12472]] the generator determines the law of the process.
It links Markov processes with differential operators: Brownian motion has generator $\tfrac12 \Delta$.

## Explanations

### L1 human

Take a function $f$ of the state and ask how fast its average value changes when the process has just started at $x$.
The answer, as a function of $x$, is $Af(x)$, and $A$ is the generator.
For a chain with finitely many states, the generator is the matrix of jump rates.
For a particle that jumps from $x$ to $x + 1$ at rate $\lambda$, one gets $Af(x) = \lambda (f(x+1) - f(x))$.
For Brownian motion it is half the second derivative, which is why the heat equation appears.
