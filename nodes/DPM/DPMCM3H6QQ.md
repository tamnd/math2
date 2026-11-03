---
tag: DPMCM3H6QQ
kind: definition
name: Unified neutral theory of biodiversity
msc: [92D40, 92D25]
defines: 3KWX3V8MPZ
uses: [A9M7VKRRV9, 033TJBZDG0]
sources:
  - url: https://en.wikipedia.org/wiki/Unified_neutral_theory_of_biodiversity
---

## Definition

Fix an integer $J \ge 2$, the size of the community, and a speciation probability $\nu$ with $0 < \nu < 1$.
The *neutral model* is the [[Markov chain|033TJBZDG0]] on species labellings of $J$ individuals with the following step.

1. One individual is chosen uniformly at random and dies.
2. With probability $\nu$, the vacant place is taken by an individual of a species that is new to the community.
3. With probability $1 - \nu$, the vacant place is taken by the offspring of a survivor chosen uniformly at random.
   The offspring has the species of its parent.

The *unified neutral theory of biodiversity* is the study of community structure under this model and its extensions.
In all of them, every individual has the same per capita rates of birth, death, dispersal and speciation.

## Remarks

The number of individuals stays equal to $J$ at every step; this is the zero-sum assumption.
Without step 2 the model is the neutral [[Moran process|A9M7VKRRV9]] with many types, in which one species eventually takes over.
Speciation keeps the diversity from vanishing, and the chain has a stationary distribution on species abundances.
Hubbell summarises the metacommunity parameters by the fundamental biodiversity number $\theta = 2 J_M \nu$, where $J_M$ is the size of the metacommunity.
In the extension with a local community, the local community receives an immigrant from the metacommunity with probability $m$ at each replacement.

Example: with $J = 2$, each step replaces one of the two individuals.
With probability $\nu$ the two individuals then belong to different species, and with probability $1 - \nu$ they belong to the same species.

Non-example: a model in which one species has a higher birth rate than the others is not neutral, since the parent in step 3 is then not chosen uniformly.
