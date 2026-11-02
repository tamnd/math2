---
tag: ZBSXSTQM2J
kind: concept
name: Radial basis function
msc: [41A30, 41A63, 65D12]
sources:
  - url: https://en.wikipedia.org/wiki/Radial_basis_function
same_as:
  wikidata: Q1588488
  wikipedia: Radial basis function
---

## Summary

A radial basis function is a function on $\R^d$ whose value depends only on the distance from a centre point.
Standard examples are the Gaussian $e^{-(\varepsilon r)^2}$, the multiquadric $\sqrt{1 + (\varepsilon r)^2}$ and the [[thin plate spline|P9ZPH7EC8K]] $r^2 \log r$, where $r$ is the distance.
Shifted copies centred at data points are used as building blocks for [[radial basis function interpolation|XZ33P3HBB9]] of scattered data in any dimension.
They also appear as kernels in machine learning and in meshfree methods for differential equations.

## Explanations

### L1 human

Drop a stone in a still pond: the height of the water depends only on the distance from where the stone fell.
A radial basis function has the same symmetry: it looks the same in every direction from its centre.
The Gaussian bump $e^{-\norm{x}^2}$ is the typical example; it equals $1$ at the centre and decays as one moves away.
Placing such bumps at many points and adding them with suitable weights gives flexible surfaces.
The [[definition|3SS5K8MHPK]] makes this precise.
