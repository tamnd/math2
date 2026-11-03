---
tag: E8AMG3JSHF
kind: definition
name: Quantization
msc: [94A29, 94A12, 94A34]
defines: H6TFN824YV
uses: [0PNRKMRC55, 05NZ1HHQMV]
sources:
  - url: https://en.wikipedia.org/wiki/Quantization_(signal_processing)
---

## Definition

A *quantizer* on $\R$ is a Borel measurable map $Q \colon \R \to \R$ whose image $\set{y_1, y_2, \dots}$ is finite or countable.
The values $y_i$ are the *reproduction levels*, and the sets $Q^{-1}(y_i)$ are the *cells*; the cells partition $\R$.
*Quantization* is the application of a quantizer to a signal or a [[random variable|0PNRKMRC55]] $X$.
The *quantization error* is $X - Q(X)$.

## Remarks

A quantizer with $N$ levels can be described by $\ceil{\log_2 N}$ bits per sample.
Its quality is usually measured by the [[mean squared error|05NZ1HHQMV]] $\mathbb{E}\,(X - Q(X))^2$.
Example: the *uniform quantizer* with step $\Delta > 0$ is $Q(x) = \Delta \floor{x / \Delta + 1/2}$.
Its image $\Delta \Z$ is countable, and its cells are the intervals $[(k - 1/2)\Delta, (k + 1/2)\Delta)$.
The error $x - Q(x)$ lies in $[-\Delta/2, \Delta/2)$.
If $X$ is uniform on one cell, then $\mathbb{E}\,(X - Q(X))^2 = \Delta^2 / 12$.
Non-example: the identity map of $\R$ is not a quantizer, since its image is uncountable.
