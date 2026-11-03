---
tag: 1XMWBVNRH5
kind: definition
name: Quantum phase transition
msc: [82B10, 82B26, 81V70]
defines: N8HS434PPV
uses: [0NEGN5CRSC, 0BF2DE2SYK, FPYQWE8X12]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_phase_transition
---

## Definition

Let $(\Lambda_L)_{L \ge 1}$ be finite sets of sites with $\abs{\Lambda_L} \to \infty$, and let $\mathcal{H}_L = \bigotimes_{x \in \Lambda_L} \C^q$ for a fixed $q \ge 2$.
Let $I \subset \R$ be an open interval.
For $g \in I$, let $H_L(g)$ be a [[self-adjoint operator|0NEGN5CRSC]] on $\mathcal{H}_L$ that is a sum of uniformly bounded local terms depending analytically on $g$.
Let $E_L(g)$ be the smallest eigenvalue of $H_L(g)$, and assume that the ground-state energy density $e(g) = \lim_{L \to \infty} E_L(g) / \abs{\Lambda_L}$ exists for all $g \in I$.
The family has a *quantum phase transition* at $g_c \in I$ if $e$ is not real-analytic at $g_c$.

## Remarks

The limit is the zero-temperature version of the [[thermodynamic limit|FPYQWE8X12]], and $e(g)$ plays the role of the free energy density.
At a continuous quantum phase transition the gap between the two lowest eigenvalues of $H_L(g_c)$ tends to $0$ as $L \to \infty$.

Example: the transverse-field Ising chain $H_L(g) = -J \sum_{i} \sigma^z_i \sigma^z_{i+1} - g \sum_i \sigma^x_i$ on a ring of $L$ sites, with $J > 0$ and $g \ge 0$.
The Jordan–Wigner transformation maps it to free fermions with energies $\varepsilon_k = 2\sqrt{J^2 + g^2 - 2 J g \cos k}$.
This gives $e(g) = -\frac{1}{2\pi} \int_{-\pi}^{\pi} \sqrt{J^2 + g^2 - 2Jg \cos k} \, dk$, which is not analytic at $g = J$.
The gap $\min_k \varepsilon_k = 2\abs{J - g}$ closes exactly there.
Check of the formula at $g = 0$: $e(0) = -J$, the energy per bond of the two aligned ground states.

Non-example: $H_L(g) = -g \sum_{i} \sigma^x_i$ for $g > 0$ has $e(g) = -g$, which is analytic, so there is no transition.
