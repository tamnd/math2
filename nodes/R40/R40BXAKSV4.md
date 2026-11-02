---
tag: R40BXAKSV4
kind: definition
name: Aitken's delta-squared process
msc: [65B05, 40A25]
defines: WF08BMN6Q6
uses: [0QE8STGJH2, 90ANMX55DP]
sources:
  - url: https://en.wikipedia.org/wiki/Aitken's_delta-squared_process
---

## Definition

Let $(s_n)_{n \ge 0}$ be a [[sequence|0QE8STGJH2]] of real or complex numbers.
Write $\Delta s_n = s_{n+1} - s_n$ and $\Delta^2 s_n = s_{n+2} - 2 s_{n+1} + s_n$.
For each $n$ with $\Delta^2 s_n \ne 0$, *Aitken's delta-squared process* gives
$$A_n = s_n - \frac{(\Delta s_n)^2}{\Delta^2 s_n}.$$

## Remarks

Equivalently, $A_n = \dfrac{s_n s_{n+2} - s_{n+1}^2}{s_{n+2} - 2 s_{n+1} + s_n}$.
Example: if $s_n = s + c \lambda^n$ with $c \ne 0$ and $\lambda \ne 0, 1$, then $\Delta s_n = c\lambda^n(\lambda - 1)$ and $\Delta^2 s_n = c \lambda^n (\lambda - 1)^2$, so $A_n = s_n - c\lambda^n = s$ for every $n$.
Non-example: for an arithmetic sequence such as $s_n = n$ one has $\Delta^2 s_n = 0$, so $A_n$ is not defined.
A classical result: if $s_n \to s$, $s_n \ne s$, and $\frac{s_{n+1} - s}{s_n - s} \to \lambda$ with $\lambda \ne 1$, then $(A_n)$ [[accelerates|90ANMX55DP]] the convergence of $(s_n)$.

## Explanations

### L1 human

The formula subtracts from $s_n$ the correction that a perfectly geometric error would require.
It uses only the first and second differences of the sequence.
