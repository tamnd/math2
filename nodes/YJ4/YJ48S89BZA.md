---
tag: YJ48S89BZA
kind: statement
role: theorem
name: Sphere packing in dimensions 8 and 24
msc: [52C17, 11H31, 11F11]
uses: [HF32CBN5MA, 4P5PSWADJD, 2CXH65EKY7, XETV3657DG]
about: [HF32CBN5MA]
sources:
  - url: https://en.wikipedia.org/wiki/Sphere_packing
---

## Statement

1. Every [[sphere packing|HF32CBN5MA]] of equal balls in $\R^8$ has upper [[packing density|4P5PSWADJD]] at most $\pi^4/384 \approx 0.2537$. This is the density of the lattice packing given by the [[E8 lattice|2CXH65EKY7]].
2. Every sphere packing of equal balls in $\R^{24}$ has upper packing density at most $\pi^{12}/12! \approx 0.00193$. This is the density of the lattice packing given by the [[Leech lattice|XETV3657DG]].

## Remarks

Maryna Viazovska proved the case of dimension $8$ in 2016.
Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko and Viazovska proved the case of dimension $24$ soon after.
Both proofs use the linear programming bound of Cohn and Elkies.
If $f \colon \R^n \to \R$ is a suitable integrable function with $f(0) = \hat f(0) > 0$, $f(x) \le 0$ for $\abs{x} \ge r$, and $\hat f \ge 0$, then every packing of balls of radius $r/2$ has density at most $\operatorname{vol}(B(0, r/2))$.
Viazovska built such a function for $r = \sqrt 2$ in dimension $8$ from modular forms and quasimodular forms, and the second paper did the same in dimension $24$.
The density values follow from the lattices.
$E_8$ has covolume $1$ and minimal length $\sqrt 2$, so the balls have radius $\sqrt 2/2$.
The Leech lattice has covolume $1$ and minimal length $2$, so the balls have radius $1$.

## Explanations

### L1 human

In most dimensions nobody knows the best way to pack equal balls.
Dimensions $8$ and $24$ are special: there are two extremely symmetric arrangements there, and these are now proved to be the best.
The proof is short compared with the proof in dimension $3$, but it uses deep tools from number theory.

### L2 human

The theorem completes the list of dimensions $1$, $2$, $3$, $8$, $24$ in which the sphere packing problem is solved.
The Cohn–Elkies bound is a Fourier analytic version of the [[Delsarte bound|7RPEDHAT7R]] for codes.
Numerical computations by Cohn and Elkies suggested that it is sharp in dimensions $2$, $8$ and $24$.
The work was to find the exact auxiliary function in dimensions $8$ and $24$.
Viazovska received the Fields Medal in 2022, partly for this work.
