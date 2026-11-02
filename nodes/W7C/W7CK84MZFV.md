---
tag: W7CK84MZFV
kind: concept
name: Neural network approximation
msc: [41A46, 68T07, 41A30]
specializes: [YS1GRQRVY7]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_approximation_theorem
---

## Summary

Neural network approximation studies how well functions can be approximated by the functions that neural networks compute.
A shallow network computes a sum $\sum_{k=1}^n c_k \sigma(w_k \cdot x + b_k)$ of ridge functions built from one activation function $\sigma$; a deep network composes several such layers.
The universal approximation theorem says that shallow networks with a continuous non-polynomial activation are dense in the [[continuous functions|0X3WGX95FE]] on every [[compact set|0TVJZYB6SH]] of $\R^d$.
Rates of approximation in terms of the number of neurons or parameters are a main topic of [[nonlinear approximation|YS1GRQRVY7]].

## Explanations

### L1 human

A neural network adds up many copies of one simple function, each one shifted, stretched and pointed in its own direction.
With enough copies, such sums can follow any continuous shape on a bounded region as closely as one likes.
With the ReLU activation $\sigma(t) = \max(t, 0)$, each copy is a hinge, and sums of hinges in one variable are exactly the continuous piecewise linear functions with finitely many pieces.
For example, $\abs{x} = \sigma(x) + \sigma(-x)$ is a network with two neurons.
Approximation theory asks how many neurons or layers are needed to reach a given accuracy, and for which functions.
