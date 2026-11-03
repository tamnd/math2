---
tag: 4ZZX6Q8AGZ
kind: concept
name: Conditionally negative definite function
msc: [43A35, 22D55]
sources:
  - url: https://en.wikipedia.org/wiki/Positive-definite_kernel
---

## Summary

A conditionally negative definite function on a group $G$ is a real function $\psi$ with $\psi(e) = 0$ and $\psi(g^{-1}) = \psi(g)$ and one more condition.
The sums $\sum_{i,j} c_i c_j \psi(g_j^{-1} g_i)$ are $\le 0$ whenever the real coefficients $c_i$ add up to $0$.
The typical example is $\psi(g) = \norm{b(g)}^2$, the squared displacement of a point under an affine isometric action on a real Hilbert space.
By [[Schoenberg's theorem|7C0F34FGE3]], $\psi$ is conditionally negative definite exactly when $e^{-t\psi}$ is a [[positive-definite function|3PRZ02APFA]] for every $t > 0$.
These functions measure how a group can act on Hilbert spaces.
They appear in the theory of [[property (T)|GTFZ277047]], of the Haagerup property, and of Lévy processes.

## Explanations

### L1 human

The function $\psi(x) = \abs{x}^2$ on $\R^n$ is the model: it is a squared distance from the origin.
Squared distances in Euclidean space satisfy a special inequality, and "conditionally negative definite" is the name of that inequality.
A function on a group with this property behaves like the squared distance that each group element moves a fixed point.
For example, on the integers $\psi(n) = \abs{n}$ is conditionally negative definite, while $\psi(n) = -n^2$ is not.
