---
tag: KDYPN9NKXC
kind: definition
name: Trace distance
msc: [81P16, 81P18, 15A60]
defines: 2Q85WTJ07A
uses: [V1JTB52E8C, 3JY5HNFRMF, 0XC1RDBY7A, A8D05RKX8M]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_distance
---

## Definition

Let $H$ be a finite-dimensional complex Hilbert space, and let $\rho$ and $\sigma$ be [[density operators|V1JTB52E8C]] on $H$.
The *trace distance* between $\rho$ and $\sigma$ is
$$T(\rho, \sigma) = \frac{1}{2} \norm{\rho - \sigma}_1 = \frac{1}{2} \tr \abs{\rho - \sigma},$$
where $\abs{A} = \sqrt{A^* A}$ is the [[positive square root|3JY5HNFRMF]] and $\tr$ is the [[trace|0XC1RDBY7A]].

## Remarks

Since $\rho - \sigma$ is self-adjoint with eigenvalues $\lambda_i$, the definition reads $T(\rho, \sigma) = \frac12 \sum_i \abs{\lambda_i}$.

Example: for $\rho = \lvert 0 \rangle \langle 0 \rvert$ and $\sigma = \lvert 1 \rangle \langle 1 \rvert$, the difference has eigenvalues $1$ and $-1$, so $T = 1$.
For qubit states with Bloch vectors $r$ and $s$, $\rho - \sigma = \frac12 (r - s)\cdot \vec\sigma$ has eigenvalues $\pm \frac12 \abs{r - s}$, so $T = \frac12 \abs{r - s}$.

Non-example: half the trace without the absolute value, $\frac12 \tr(\rho - \sigma)$, is always $0$, because both states have trace $1$; it is not a distance.

Equivalent form: $T(\rho, \sigma) = \max_{0 \le P \le I} \tr(P(\rho - \sigma))$, and the maximum is reached at the projection onto the positive part of $\rho - \sigma$.
It is a metric with values in $[0, 1]$, and it does not increase under quantum channels.
It is related to the [[fidelity|A8D05RKX8M]] by $1 - \sqrt{F(\rho,\sigma)} \le T(\rho, \sigma) \le \sqrt{1 - F(\rho, \sigma)}$.
