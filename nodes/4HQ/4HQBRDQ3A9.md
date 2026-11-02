---
tag: 4HQBRDQ3A9
kind: concept
name: Bifurcation from a characteristic value
msc: [47J15, 45G10, 45C05]
sources:
  - url: https://en.wikipedia.org/wiki/Bifurcation_theory
---

## Summary

Consider a nonlinear equation $\varphi = \lambda\bigl(K\varphi + R(\varphi)\bigr)$ with a compact linear operator $K$ and a term $R$ that is small compared with $\varphi$ near $0$.
Then $\varphi = 0$ is a solution for every $\lambda$.
A value $\lambda_0$ is a bifurcation point if nonzero solutions branch off the trivial solution at $\lambda = \lambda_0$.
Such a point must be a [[characteristic value|DC7HMHVREP]] of $K$, that is, a value where the linearized equation $\varphi = \lambda K\varphi$ has a nonzero solution.
This is the classical setting of [[bifurcation theory|D9TW46P19Y]] for nonlinear integral equations, with results such as Krasnosel'skii's theorem on characteristic values of odd multiplicity.

## Explanations

### L1 human

A straight elastic rod pushed at its ends stays straight under a small load.
At a critical load it can suddenly bow sideways, and new bent shapes appear next to the straight one.
The critical loads are exactly the values where the linear approximation of the problem has a nonzero solution.
In the scalar model $\varphi = \lambda(\varphi - \varphi^3)$, nonzero solutions $\varphi = \pm\sqrt{1 - 1/\lambda}$ appear when $\lambda$ passes $1$, the characteristic value of the linear part.
