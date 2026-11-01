---
tag: M3WQTN3FH2
kind: concept
name: Nevanlinna class
msc: [30H15, 30D50]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_type_(mathematics)
---

## Summary

The Nevanlinna class $N$ is the space of [[holomorphic functions|0DG0Z72CQD]] on the [[unit disc|8G5ABXRK85]] whose positive part of $\log \abs{f}$ has bounded averages on circles.
Its elements are exactly the quotients of two bounded holomorphic functions with zero-free denominator, the functions of bounded type.
It contains every [[Hardy space|PNNNFJVF6W]] $H^p$, and its nonzero elements still have radial limits almost everywhere and zeros satisfying the Blaschke condition.

## Explanations

### L1 human

Hardy spaces control the size of $\abs{f}^p$ on circles.
The Nevanlinna class only controls the size of $\log \abs{f}$ where $\abs{f} > 1$, which is a much weaker condition.
For example, $1/(1 - z)$ is not bounded but lies in $N$, since it is $1$ divided by the bounded zero-free function $1 - z$.
Even $\exp\left(\frac{1}{1 - z}\right)$ lies in $N$.
The quantity $\frac{1}{2\pi} \int \log^+ \abs{f(r e^{it})} \, dt$ is the proximity part of the [[Nevanlinna characteristic|YT6Z0GWS0W]], which explains the name.
