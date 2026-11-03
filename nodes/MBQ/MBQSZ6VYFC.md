---
tag: MBQSZ6VYFC
kind: concept
name: Stochastic gradient descent
msc: [62L20, 90C15, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_gradient_descent
same_as:
  wikidata: Q7617819
  wikipedia: Stochastic gradient descent
---

## Summary

Stochastic gradient descent is a form of [[gradient descent|12317R8RTJ]] with random gradients.
At each step it replaces the exact gradient by a random estimate whose mean is the gradient.
It is used when the objective is an average over a huge data set, or an [[expected value|0WQNRCNY3M]] over a distribution.
Then exact gradients are too costly or unavailable.
It is a [[stochastic approximation|ZPCPW4W1Y9]] scheme in the line of the [[Robbins–Monro algorithm|CHHD44WDHJ]], and it is the main training method for neural networks.

## Explanations

### L1 human

Suppose the error of a model is the average of its errors on a million examples.
Computing the exact slope needs all million examples at every step.
Stochastic gradient descent looks at one example, or a small batch, picked at random, and steps according to its slope alone.
Each step is noisy, but on average it points the right way, and with shrinking steps the noise averages out.
