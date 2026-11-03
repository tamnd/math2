---
tag: BADQNKM77K
kind: definition
name: Mixed state
msc: ["81P16", "46N50"]
defines: CKCMBP5S2P
uses: [4NQN47A92F, V1JTB52E8C, 21SXYJYC59, A1G25R99PY]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_state
---

## Definition

Let $\mathcal{H}$ be a complex Hilbert space.
A *mixed state* on $\mathcal{H}$ is a [[quantum state|4NQN47A92F]], that is, a [[density operator|V1JTB52E8C]] $\rho$, that is not pure.

## Remarks

The following conditions on a density operator $\rho$ are equivalent:

1. $\rho$ is a mixed state;
2. $\operatorname{tr}(\rho^2) < 1$;
3. $\rho$ has rank at least $2$;
4. $\rho = t \rho_1 + (1 - t) \rho_2$ for some density operators $\rho_1 \ne \rho_2$ and some $0 < t < 1$, a nontrivial [[convex combination|21SXYJYC59]].

By the [[spectral theorem for compact self-adjoint operators|A1G25R99PY]], $\rho = \sum_k p_k \lvert e_k \rangle\langle e_k \rvert$ with an orthonormal family $(e_k)$, numbers $p_k \ge 0$ and $\sum_k p_k = 1$; then $\operatorname{tr}(\rho^2) = \sum_k p_k^2$.

Example: $\rho = \frac12 I$ on $\C^2$ is a density operator with $\operatorname{tr}(\rho^2) = \frac12 < 1$, so it is mixed.
It has two different decompositions into pure states: $\frac12 I = \frac12 \lvert 0 \rangle\langle 0 \rvert + \frac12 \lvert 1 \rangle\langle 1 \rvert = \frac12 \lvert + \rangle\langle + \rvert + \frac12 \lvert - \rangle\langle - \rvert$, where $\lvert 0 \rangle, \lvert 1 \rangle$ is the standard basis and $\lvert \pm \rangle = (\lvert 0 \rangle \pm \lvert 1 \rangle)/\sqrt{2}$.

Non-example: $\rho = \lvert 0 \rangle\langle 0 \rvert = \mathrm{diag}(1, 0)$ has $\operatorname{tr}(\rho^2) = 1$, so it is pure, not mixed.
