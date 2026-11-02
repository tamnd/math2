---
tag: WDHHJHVP7N
kind: concept
name: Jacobi amplitude
msc: ["33E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_elliptic_functions
---

## Summary

The Jacobi amplitude $\operatorname{am}(u, k)$ is the inverse function of the incomplete [[elliptic integral|NXMCYGCB59]] of the first kind $u = F(\varphi, k)$.
It is the angle $\varphi$ whose sine and cosine are the [[Jacobi elliptic functions|P071B692JF]] $\operatorname{sn} u$ and $\operatorname{cn} u$.
For modulus $k = 0$ it is the identity, and for $k = 1$ it is the Gudermannian function.

## Explanations

### L1 human

The integral $F(\varphi, k)$ measures something like a distorted angle: it adds up $d\theta / \sqrt{1 - k^2\sin^2\theta}$ from $0$ to $\varphi$.
The amplitude goes the other way, from the value $u$ back to the angle $\varphi$.
For a pendulum, $u$ is proportional to time and the amplitude tracks the angle of an auxiliary variable that turns unevenly.
When $k = 0$ the integrand is $1$, so $F(\varphi, 0) = \varphi$ and $\operatorname{am}(u, 0) = u$.
