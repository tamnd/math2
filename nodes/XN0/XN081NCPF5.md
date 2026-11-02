---
tag: XN081NCPF5
kind: concept
name: Hyperbolic conservation law
msc: [35L65, 35L40]
specializes: [8RA7AMWSAF, 92C3S03AQZ]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_partial_differential_equation
---

## Summary

A hyperbolic conservation law is a system of [[conservation laws|8RA7AMWSAF]] whose flux Jacobian, in every direction, has real eigenvalues and a full set of eigenvectors.
The eigenvalues are the speeds at which small disturbances travel, so information moves at finite speed along several families of waves.
The equations of gas dynamics, shallow water and traffic flow are of this type.
Their solutions typically form [[shock waves|JSDMGGTG7G]], and the main results concern weak entropy solutions.
See the [[definition|WBYJ7A0HY7]].

## Explanations

### L1 human

In a gas, a small push creates sound waves that travel left and right at finite speeds.
A hyperbolic conservation law is a conservation law with this behaviour: every small disturbance splits into waves with real speeds.
The condition is that a certain matrix built from the flux has only real eigenvalues and enough eigenvectors.
For a single equation $u_t + F(u)_x = 0$ the matrix is the number $F'(u)$, which is always real, so every scalar conservation law is hyperbolic.
