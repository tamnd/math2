---
tag: EEHQSWFHSB
kind: concept
name: Bedford–Taylor theory
msc: [32W20, 32U40, 32U20]
sources:
  - url: https://en.wikipedia.org/wiki/Plurisubharmonic_function
---

## Summary

Bedford–Taylor theory defines the [[complex Monge–Ampère operator|MXRC891TQS]] $(dd^c u)^n$ for plurisubharmonic functions $u$ that are only locally bounded, not differentiable.
The products $dd^c u_1 \wedge \cdots \wedge dd^c u_k$ are defined inductively as closed [[positive currents|BYJHP6A906]], and they are continuous along decreasing sequences of plurisubharmonic functions.
Eric Bedford and B. A. Taylor developed the theory in work published in 1976 and 1982.
It gives the Monge–Ampère capacity and solves the Dirichlet problem for the complex Monge–Ampère equation with continuous data on strongly pseudoconvex domains.
It is the starting point of modern pluripotential theory.

## Explanations

### L1 human

For a smooth function the Monge–Ampère operator is a determinant of second derivatives, but many important plurisubharmonic functions are not smooth.
For example, $\max(\log\abs{z_1}, \log\abs{z_2}, 0)$ is continuous and plurisubharmonic on $\C^2$, but it has corners.
Bedford and Taylor showed how to give a meaning to the Monge–Ampère measure of such functions by using derivatives in the sense of distributions, one factor at a time.
For the function above, the Monge–Ampère measure turns out to be a constant multiple of the uniform measure on the torus $\abs{z_1} = \abs{z_2} = 1$.
