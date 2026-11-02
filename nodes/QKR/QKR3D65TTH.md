---
tag: QKR3D65TTH
kind: concept
name: Bidual and canonical embedding
msc: [46B10]
sources:
  - url: https://en.wikipedia.org/wiki/Reflexive_space
---

## Summary

The bidual $X^{**}$ of a normed space $X$ is the dual of its [[continuous dual space|4A82S5FVRT]] $X^*$.
The canonical embedding $J \colon X \to X^{**}$ sends a vector $x$ to the functional "evaluate at $x$".
By the [[Hahn–Banach theorem|QB5AE3VYZZ]], $J$ is a linear isometry, so every normed space sits inside its bidual.
Spaces for which $J$ is onto are the [[reflexive spaces|NN8RWPC8WG]].

## Explanations

### L1 human

A vector $x$ can be turned into a machine that eats a functional $f$ and returns the number $f(x)$.
This machine is linear and bounded, so it is an element of the bidual.
In finite dimensions every element of the bidual arises this way, which is the familiar fact that a space is naturally the dual of its dual.
In infinite dimensions the bidual can be bigger: the bidual of the space $c_0$ of null sequences is the space $\ell^\infty$ of bounded sequences.
