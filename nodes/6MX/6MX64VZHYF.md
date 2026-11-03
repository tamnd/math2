---
tag: 6MX64VZHYF
kind: statement
role: theorem
name: Bohr–Sommerfeld quantization condition
msc: [81Q20, 35P20]
uses: [89AA6XJY5K, PJWY3JJQQ7, EG41JQS3PC]
about: [89AA6XJY5K]
sources:
  - url: https://en.wikipedia.org/wiki/Old_quantum_theory
---

## Statement

Let $V \colon \R \to \R$ be smooth, let $m > 0$, and for $\hbar > 0$ let $P_\hbar = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V(x)$ on $L^2(\R)$.
Let $a < b$ be such that $\liminf_{\abs{x} \to \infty} V(x) > b$, and, for every $E \in [a, b]$, the set $\set{x : V(x) \le E}$ is a closed interval $[x_-(E), x_+(E)]$ with $V'(x_\pm(E)) \ne 0$.
For $E \in [a, b]$ let
$$A(E) = 2 \int_{x_-(E)}^{x_+(E)} \sqrt{2m (E - V(x))} \, dx$$
be the area enclosed by the classical orbit $p^2/2m + V(x) = E$ in the phase plane.
Then, for small $\hbar$, the eigenvalues of $P_\hbar$ in $[a, b]$ are simple.
They can be labelled $E_n(\hbar)$, with $n$ running over some integers $n \ge 0$, so that
$$A(E_n(\hbar)) = 2\pi\hbar \left( n + \tfrac12 \right) + O(\hbar^2) \quad \text{as } \hbar \to 0.$$
The bound $O(\hbar^2)$ is uniform in $n$.

## Remarks

In the old quantum theory of Bohr and Sommerfeld the rule was a postulate, written $\oint p \, dq = nh$ with $h = 2\pi\hbar$, without the term $\frac12$.
The modern form follows from the [[WKB approximation|EG41JQS3PC]].
The WKB solutions decaying on each side are glued across the two turning points.
Each turning point contributes a phase of $\pi/2$, the Maslov correction, and this gives the $\frac12$.

Example: for the harmonic oscillator $V(x) = \frac12 m\omega^2 x^2$ the orbit at energy $E$ is an ellipse of area $A(E) = 2\pi E/\omega$.
The condition gives $E = \hbar\omega(n + \frac12)$, which is the exact spectrum.

The hypothesis that $E$ is not a critical value of $V$ is needed.
Near the top of a barrier or at the bottom of a degenerate well, the turning points merge and the rule must be corrected.

## Explanations

### L1 human

Classically, a particle in a well moves on a closed curve in the plane of position and momentum.
The rule says that in quantum mechanics only those curves are allowed whose area is a half-integer multiple of $2\pi\hbar$.
For small $\hbar$ this predicts the energy levels with high accuracy.

### L2 human

The rule is the simplest bridge between classical and quantum mechanics: it computes the [[discrete spectrum|PJWY3JJQQ7]] of a one-dimensional [[Schrödinger operator|89AA6XJY5K]] from the classical action alone.
It also shows that the number of eigenvalues below $E$ is about $A(E)/(2\pi\hbar)$, a one-dimensional case of Weyl's law.
In several degrees of freedom it generalises, for integrable systems, to the Einstein–Brillouin–Keller conditions on invariant tori.
