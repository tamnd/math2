---
tag: VQZVSFF179
kind: concept
name: Hebbian learning
msc: [92B20, 68T05, 92C20]
sources:
  - url: https://en.wikipedia.org/wiki/Hebbian_theory
---

## Summary

Hebbian learning is the principle that a connection between two neurons grows stronger when the two are active together.
It goes back to the psychologist Donald Hebb, who proposed it in his 1949 book *The Organization of Behavior*.
In models, the change of a synaptic weight is proportional to the product of the input and output activities.
The plain rule is unstable, and its stabilised variants, such as Oja's rule and the BCM rule, are basic models of unsupervised learning.

## Explanations

### L1 human

The slogan is "cells that fire together wire together".
If neuron A often helps to make neuron B fire, the link from A to B gets stronger.
For a single model neuron with inputs $x_1, x_2$ and output $y$, the rule adds $\eta x_i y$ to the weight of input $i$, for a small rate $\eta > 0$.
So inputs that are active when the output is active gain weight, and the neuron comes to respond to patterns that it has seen often.
