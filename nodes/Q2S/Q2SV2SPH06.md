---
tag: Q2SV2SPH06
kind: concept
name: Perceptron
msc: [68T07, 92B20, 68T05]
sources:
  - url: https://en.wikipedia.org/wiki/Perceptron
same_as:
  wikidata: Q690207
  wikipedia: Perceptron
---

## Summary

A perceptron is a model neuron that outputs $1$ when a weighted sum of its inputs exceeds a threshold and $0$ otherwise.
Frank Rosenblatt introduced it in the late 1950s together with a learning rule that adjusts the weights from labelled examples.
A single perceptron can separate two classes exactly when they can be divided by a hyperplane.
It is the building block of multilayer neural networks.

## Explanations

### L1 human

A perceptron decides yes or no by adding up evidence with weights and comparing the total with a bar.
For two inputs it draws a straight line in the plane and says yes on one side.
It can learn logical AND: with weights $1, 1$ and bar $1.5$, only the input $(1, 1)$ passes.
It cannot learn exclusive or, because no single line separates $(0,1), (1,0)$ from $(0,0), (1,1)$.
