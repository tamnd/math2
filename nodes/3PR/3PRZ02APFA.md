---
tag: 3PRZ02APFA
kind: concept
name: Positive-definite function on a group
msc: ["43A35", "22D10"]
sources:
  - url: https://en.wikipedia.org/wiki/Positive-definite_function_on_a_group
same_as:
  wikidata: Q7233206
  wikipedia: Positive-definite function on a group
---

## Summary

A positive-definite function on a group $G$ is a complex function $\varphi$ on $G$ with the following property.
For all $g_1, \dots, g_n \in G$, the matrix $\big(\varphi(g_i^{-1}g_j)\big)_{i,j}$ is [[positive semidefinite|0KX66CZMBB]].
The diagonal matrix coefficients $g \mapsto \ip{\pi(g)v}{v}$ of [[unitary representations|74BPYJNZTM]] are positive-definite, and conversely every continuous positive-definite function arises in this way.
This correspondence links functions on a group with its representations, and it underlies Bochner's theorem and the Gelfand–Raikov theorem.

## Explanations

### L1 human

On the real line, the function $\cos x$ is positive-definite, while $-1$ is not.
The idea is that $\varphi(g^{-1}h)$ behaves like an inner product between the elements $g$ and $h$, so sums $\sum \bar c_i c_j \varphi(g_i^{-1}g_j)$ behave like squared lengths and cannot be negative.
Indeed $\cos(y - x) = \cos x \cos y + \sin x \sin y$ is the dot product of the unit vectors at angles $x$ and $y$.
Every positive-definite function is, in this sense, a hidden inner product, and the hidden space is a unitary representation of the group.
