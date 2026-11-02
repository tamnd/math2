---
tag: 5WHXGHBCY9
kind: statement
role: theorem
name: Stein interpolation theorem
msc: [46B70, 42B35, 47A30]
uses: [SASP14MA1Z, 0NAHXR1FRH, VX1R6FN6PS, AGRKRG1TMJ, WHS58R43N0]
about: [VX1R6FN6PS]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz%E2%80%93Thorin_theorem
---

## Statement

Let $(X, \mu)$ and $(Y, \nu)$ be $\sigma$-finite measure spaces, and let $S = \set{z \in \C : 0 \le \operatorname{Re} z \le 1}$.
Call a simple function admissible if its support has finite measure.
For each $z \in S$ let $T_z$ be a linear operator from the admissible simple functions on $X$ to the measurable functions on $Y$.
Assume that $(T_z)$ is an admissible analytic family, which means the following.
Let $f$ on $X$ and $g$ on $Y$ be admissible simple functions.
It is required that $T_z(f) g$ is integrable for each $z$, and that $\Phi(z) = \int_Y T_z(f) \, g \, d\nu$ is continuous on $S$ and [[holomorphic|0NAHXR1FRH]] in the interior of $S$.
Moreover $\log \abs{\Phi(z)} \le C e^{a \abs{\operatorname{Im} z}}$ on $S$ for some constants $C$ and $a < \pi$.

Let $1 \le p_0, p_1, q_0, q_1 \le \infty$.
Let $M_0, M_1 \colon \R \to (0, \infty)$ satisfy $\log M_j(y) \le C' e^{b \abs{y}}$ for some constants $C'$ and $b < \pi$.
Assume that for all admissible simple $f$ on $X$ and all $y \in \R$,
$$\norm{T_{iy} f}_{L^{q_0}} \le M_0(y) \norm{f}_{L^{p_0}}, \qquad \norm{T_{1 + iy} f}_{L^{q_1}} \le M_1(y) \norm{f}_{L^{p_1}}.$$
Let $0 < \theta < 1$ and define $p$ and $q$ by
$$\frac{1}{p} = \frac{1 - \theta}{p_0} + \frac{\theta}{p_1}, \qquad \frac{1}{q} = \frac{1 - \theta}{q_0} + \frac{\theta}{q_1}.$$
Then $\norm{T_\theta f}_{L^q} \le M_\theta \norm{f}_{L^p}$ for all admissible simple $f$ on $X$, where
$$\log M_\theta = \frac{\sin \pi\theta}{2} \int_{\R} \left( \frac{\log M_0(y)}{\cosh \pi y - \cos \pi\theta} + \frac{\log M_1(y)}{\cosh \pi y + \cos \pi\theta} \right) dy.$$

## Remarks

The proof follows the proof of the [[Riesz–Thorin theorem|AGRKRG1TMJ]].
For fixed simple $f$ and $g$ one builds families $f_z$, $g_z$ of simple functions whose absolute values are powers of $\abs{f}$ and $\abs{g}$ depending on $z$.
Then one studies the holomorphic function $z \mapsto \int_Y T_z(f_z) g_z \, d\nu$ on the strip.
The hypotheses bound it on the two boundary lines.
A form of the [[Hadamard three-lines theorem|WHS58R43N0]] for functions of admissible growth, proved with the Poisson kernel of the strip, then bounds it at $z = \theta$.
The two kernels in the formula for $M_\theta$ are the Poisson kernels of the strip at the point $\theta$.

If $T_z = T$ does not depend on $z$ and $M_0$, $M_1$ are constants, the formula gives $M_\theta = M_0^{1 - \theta} M_1^{\theta}$, which is the Riesz–Thorin theorem.
A typical use is the family of fractional integration or Bochner–Riesz type operators $T_z$, where the exponent of a kernel depends analytically on $z$.
The bound $a < \pi$ in the growth condition cannot be relaxed to $a = \pi$.
The function $h(z) = \exp(i e^{-i\pi z})$ has modulus $1$ on both boundary lines of $S$, but $\abs{h(\tfrac12 + iy)} = \exp(e^{\pi y})$ is unbounded.

## Explanations

### L1 human

Suppose a family of operators depends on a complex parameter in a smooth, holomorphic way.
If the operators are bounded between two pairs of $L^p$ spaces on the two edges of a strip, then the operator in the middle is bounded between the intermediate spaces.
This is a version of Riesz–Thorin interpolation in which the operator itself is allowed to move.

### L2 human

The Riesz–Thorin theorem interpolates one fixed operator.
Many problems in harmonic analysis come instead with a natural family, for example operators whose kernel contains a power $\abs{x}^{z}$ or a factor $(1 - \abs{\xi}^2)^{z}_+$.
At one end of the strip the family is easy to bound in $L^2$ by Plancherel's theorem.
At the other end it is bounded in $L^\infty$ by a pointwise estimate of the kernel.
Stein's theorem gives the bounds in between, as in results on Bochner–Riesz means and on Fourier restriction.
It belongs to the complex method of interpolation, while the [[Marcinkiewicz interpolation theorem|R1PHMVBJ9J]] belongs to the real method.
