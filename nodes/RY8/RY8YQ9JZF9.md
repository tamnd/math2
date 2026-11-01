---
tag: RY8YQ9JZF9
kind: problem
name: Riemann–Hilbert problem
msc: ["30E25", 34M50]
uses: [0NAHXR1FRH, 0WZTM0EFR6, 0X7SBS8E0F, RNB6QX0GCA]
about: [0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Hilbert_problem
same_as:
  wikidata: Q5986515
  wikipedia: Riemann–Hilbert problem
history:
  posed_by: "Bernhard Riemann and David Hilbert"
  first_stated: "1900"
---

## Problem

Let $\Gamma \subset \C$ be a smooth simple closed curve, oriented counterclockwise.
Let $D^+$ be its interior domain and $D^-$ its exterior domain.
Let $G \colon \Gamma \to \C \setminus \set{0}$ and $g \colon \Gamma \to \C$ be [[Hölder continuous|0WZTM0EFR6]] functions.
Find a function $\Phi$ that is [[holomorphic|0NAHXR1FRH]] on $D^+$ and on $D^-$ and vanishes at $\infty$.
It must have continuous boundary values $\Phi^+$ from $D^+$ and $\Phi^-$ from $D^-$ on $\Gamma$ with
$$\Phi^+(t) = G(t)\, \Phi^-(t) + g(t) \quad \text{for } t \in \Gamma.$$
In the matrix form of the problem, $\Phi$ takes values in $\C^n$.
Then $G$ is a Hölder continuous map from $\Gamma$ to the invertible $n \times n$ complex matrices.

## Remarks

The scalar problem is solved explicitly.
Let $\kappa$ be the [[winding number|0X7SBS8E0F]] of the curve $G(\Gamma)$ about $0$, called the index of the problem.
Assume $0 \in D^+$; taking a branch of $\log$ of $t^{-\kappa} G(t)$, which has winding number $0$, turns the problem into a jump problem $\Psi^+ - \Psi^- = h$.
The Cauchy integral $\frac{1}{2\pi i} \int_\Gamma \frac{h(\tau)}{\tau - z}\, d\tau$ solves it by the [[Sokhotski–Plemelj theorem|RNB6QX0GCA]].
If $\kappa \ge 0$, the problem is solvable for every $g$, and the solutions form an affine space of dimension $\kappa$.
If $\kappa < 0$, it is solvable if and only if $g$ satisfies $-\kappa$ linear conditions, and then the solution is unique.

Example: for $G = 1$ the index is $0$ and the unique solution is the Cauchy integral of $g$.

The matrix problem cannot be solved by logarithms, since matrices do not commute.
It is closely tied to Hilbert's twenty-first problem on linear differential equations with prescribed monodromy, and it underlies the Riemann–Hilbert method for integrable systems and random matrices.

## Explanations

### L1 human

One looks for a function that is holomorphic on both sides of a curve and jumps across the curve in a prescribed way.
The jump says that the value from inside equals a given function times the value from outside, plus another given function.
For scalar functions this is solved completely, and the answer depends on how many times the given function $G$ winds around $0$.
For matrix functions the problem is much harder and connects to differential equations and mathematical physics.
