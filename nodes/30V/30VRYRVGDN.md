---
tag: 30VRYRVGDN
kind: concept
name: Parallel tempering
msc: [82M31, 65C05, 65C40]
specializes: [ZGNBR2SPZ0]
sources:
  - url: https://en.wikipedia.org/wiki/Parallel_tempering
same_as:
  wikidata: Q7135015
  wikipedia: Parallel tempering
---

## Summary

Parallel tempering, also called replica exchange Monte Carlo, is a [[Markov chain Monte Carlo|ZGNBR2SPZ0]] method that runs several copies of a system at different temperatures.
Each copy is updated by its own sampler, and from time to time two copies at neighbouring temperatures propose to exchange their configurations.
The exchange is accepted with a Metropolis probability that keeps the product of the [[Boltzmann distributions|GYNMZ9201M]] invariant.
Hot copies cross energy barriers easily, and the exchanges pass these moves down to the cold copies, which would otherwise be trapped in local minima.

## Explanations

### L1 human

At low temperature a simulation can get stuck in a valley of the energy landscape and never find the other valleys.
At high temperature it moves freely but sees only rough, typical states.
Parallel tempering runs both at once, plus several temperatures in between.
Now and then two neighbouring runs swap their states, so a state found by a hot run can cool down step by step.
This lets the coldest run explore all the valleys, as in spin glasses or protein folding.
