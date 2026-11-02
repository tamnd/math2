---
tag: AA7XRZ4VAG
kind: concept
name: Linear difference equation
msc: [39A06]
specializes: [0FYX44GP92]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_recurrence_with_constant_coefficients
---

## Summary

A linear difference equation is a recurrence in which the unknown sequence appears only linearly: $a_k(n) u_{n+k} + \dots + a_0(n) u_n = b(n)$.
The coefficients may depend on $n$; when they are constant one gets a [[linear recurrence with constant coefficients|0NDVHBVBXB]].
Its solutions have the same structure as those of a linear differential equation.
The solutions of the homogeneous equation form a vector space, and the general solution is one particular solution plus a homogeneous solution.

## Explanations

### L1 human

In a linear difference equation each term of the sequence is a weighted sum of earlier terms, plus perhaps an outside input.
No products or powers of the unknown terms appear.
The Fibonacci rule $u_{n+2} = u_{n+1} + u_n$ is linear with constant weights.
The rule $u_{n+1} = (n + 1) u_n$, which produces the factorials from $u_0 = 1$, is linear with a weight that changes with $n$.
The rule $u_{n+1} = u_n^2$ is not linear.
