---
tag: A9M7VKRRV9
kind: concept
name: Moran process
msc: [92D15, 60J10]
sources:
  - url: https://en.wikipedia.org/wiki/Moran_process
same_as:
  wikidata: Q17157279
  wikipedia: Moran process
---

## Summary

The Moran process is a stochastic model of a finite population of constant size in which individuals are replaced one at a time.
At each step one individual reproduces and one individual dies, so the number of individuals of a given type changes by at most one.
It was introduced by Patrick Moran in 1958.
It is simpler to analyse than the [[Wright–Fisher model|SR4F169EKF]], and its fixation probabilities have closed forms.

## Explanations

### L1 human

Picture a room with $10$ chairs, all occupied, some people wearing red shirts and the others blue.
At each tick, one person is chosen to have a child, and one person is chosen to leave; the child takes the empty chair and copies the parent's shirt colour.
So the number of red shirts goes up by one, down by one, or stays the same.
Eventually all shirts are the same colour.
If red people are chosen as parents more often, red is more likely to win.
