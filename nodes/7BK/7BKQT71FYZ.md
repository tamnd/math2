---
tag: 7BKQT71FYZ
kind: concept
name: p-harmonic function
msc: [31C45, 35J92]
sources:
  - url: https://en.wikipedia.org/wiki/P-Laplacian
---

## Summary

A $p$-harmonic function is a solution of the [[p-Laplace equation|XJMYGY0ZZF]] $\operatorname{div}(\abs{\nabla u}^{p-2} \nabla u) = 0$, where $1 < p < \infty$.
For $p = 2$ these are the classical [[harmonic functions|0DEB0JMN0W]].
They are the minimizers of the energy $\int \abs{\nabla u}^p \, dx$ with given boundary values, and they are the central objects of [[nonlinear potential theory|M923VKQVZM]].
The equation is nonlinear for $p \ne 2$, so sums of $p$-harmonic functions are in general not $p$-harmonic.

## Explanations

### L1 human

A harmonic function makes the energy $\int \abs{\nabla u}^2$ as small as possible among functions with the same boundary values.
A $p$-harmonic function does the same for the energy $\int \abs{\nabla u}^p$.
Changing the exponent changes how strongly steep slopes are penalized.
Linear functions are $p$-harmonic for every $p$, because their gradient is constant.
Many properties of harmonic functions survive, such as the maximum principle and a Harnack inequality, but the mean value property does not.
