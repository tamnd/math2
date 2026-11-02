---
tag: NM28RE8CHQ
kind: definition
name: Hermitian kernel
msc: [45C05, 45P05]
defines: 2ZB3NFZ94T
uses: [GSMBXT7FPK, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Schmidt_integral_operator
---

## Definition

Let $a < b$.
A *Hermitian kernel* on $[a, b]$ is a [[kernel|GSMBXT7FPK]] $K \colon [a, b] \times [a, b] \to \C$ such that
$$K(x, s) = \overline{K(s, x)} \quad \text{for all } x, s \in [a, b],$$
where the bar is the [[complex conjugate|0FTH2E9TAS]].

## Remarks

Example: $K(x, s) = e^{i (x - s)}$.
The check: $\overline{K(s, x)} = \overline{e^{i (s - x)}} = e^{-i (s - x)} = e^{i (x - s)} = K(x, s)$.

Non-example: $K(x, s) = i$, the constant kernel.
Here $\overline{K(s, x)} = -i \ne i$.

On the diagonal a Hermitian kernel is real, since $K(x, x) = \overline{K(x, x)}$.
A real-valued kernel is Hermitian exactly when it is symmetric.
For square-integrable kernels the condition is often required only for almost all $(x, s)$.
Then the integral operator $K$ on $L^2(a, b)$ satisfies $\ip{K u}{v} = \ip{u}{K v}$ for the inner product $\ip{u}{v} = \int_a^b u \bar v \, dx$.
