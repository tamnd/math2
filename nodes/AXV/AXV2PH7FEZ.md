---
tag: AXV2PH7FEZ
kind: concept
name: Fisher's equation
msc: [35K57, 35K58, 35Q92]
specializes: [TAAHWE917M]
sources:
  - url: https://en.wikipedia.org/wiki/KPP%E2%80%93Fisher_equation
same_as:
  wikidata: Q1763840
  wikipedia: KPP–Fisher equation
---

## Summary

Fisher's equation, also called the KPP–Fisher equation, is the scalar [[reaction–diffusion equation|TAAHWE917M]] $u_t = D u_{xx} + r u(1 - u)$.
It couples diffusion with logistic growth.
It was proposed by Fisher in 1937 for the spread of an advantageous gene, and studied in the same year by Kolmogorov, Petrovsky and Piskunov.
It is the model example of an equation with [[travelling wave|M37M411KP7]] fronts that invade an unstable state.

## Explanations

### L1 human

Think of a population that spreads by random motion and grows until it reaches the carrying capacity $1$.
Where $u$ is near $0$ the population grows, and diffusion pushes it into empty space.
The result is a front that moves at constant speed, with the full state $u = 1$ behind it and the empty state $u = 0$ ahead.
With $D = r = 1$, the slowest such front has speed $2$.
