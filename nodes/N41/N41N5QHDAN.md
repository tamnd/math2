---
tag: N41N5QHDAN
kind: statement
role: theorem
name: Fefferman duality theorem
msc: [42B30, 42B35, 30H35]
uses: [75WGJ014GR, QJYTXFT8Y4, 4A82S5FVRT, FRNDFJ9WQ5, AQ15060AAA]
about: [75WGJ014GR, QJYTXFT8Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_mean_oscillation
---

## Statement

Let $n \ge 1$, let $H^1(\R^n)$ be the [[real Hardy space|75WGJ014GR]], and let $\mathrm{BMO}(\R^n)$ be the space of functions of [[bounded mean oscillation|QJYTXFT8Y4]], modulo constants.
Let $H^1_0$ be the dense subspace of $H^1(\R^n)$ of finite linear combinations of atoms.

1. For every $b \in \mathrm{BMO}(\R^n)$ the linear functional $\ell_b(f) = \int_{\R^n} f b \, dx$ on $H^1_0$ extends to a bounded linear functional on $H^1(\R^n)$, with $\norm{\ell_b} \le C \norm{b}_{\mathrm{BMO}}$.
2. Every bounded linear functional $\ell$ on $H^1(\R^n)$ is of the form $\ell_b$ for a function $b \in \mathrm{BMO}(\R^n)$, unique up to an additive constant, with $\norm{b}_{\mathrm{BMO}} \le C \norm{\ell}$.

Here $C$ depends only on $n$.
So the [[continuous dual space|4A82S5FVRT]] of $H^1(\R^n)$ is $\mathrm{BMO}(\R^n)$.

## Remarks

The theorem is due to Charles Fefferman, and a full account appeared in the work of Fefferman and Stein on $H^p$ spaces.

With the [[atomic decomposition|AQ15060AAA]], part 1 is short.
For an atom $a$ on a ball $B$, the cancellation $\int a = 0$ gives $\abs{\int a b} = \abs{\int_B a (b - b_B)} \le \frac{1}{\abs{B}} \int_B \abs{b - b_B} \le C \norm{b}_{\mathrm{BMO}}$, and the bound passes to sums of atoms.
For part 2, the definition of $H^1$ through the [[Riesz transforms|FRNDFJ9WQ5]] embeds $H^1$ isometrically into a closed subspace of $L^1 \times \cdots \times L^1$ ($n + 1$ factors).
By the Hahn–Banach theorem, $\ell$ is given by bounded functions $b_0, \dots, b_n$, so $b = b_0 - \sum_j R_j b_j$, and each $R_j$ maps $L^\infty$ into BMO.

The pairing $\int f b$ need not converge absolutely for general $f \in H^1$ and $b \in \mathrm{BMO}$, which is why it is first defined on $H^1_0$.
An analogous duality on the circle identifies the dual of the real $H^1$ of the circle with BMO of the circle.

## Explanations

### L1 human

Every continuous linear way of measuring functions in the Hardy space $H^1$ is given by integrating against a function of bounded mean oscillation, and every BMO function gives one.
This is like the familiar fact that the dual of $L^1$ is $L^\infty$, with $L^1$ replaced by the smaller space $H^1$ and $L^\infty$ by the larger space BMO.

### L2 human

The theorem explains why BMO appears so often as the endpoint of $L^p$ theory at $p = \infty$.
Since Calderón–Zygmund operators map $H^1$ into $L^1$, their adjoints map $L^\infty$ into BMO by duality.
It is also the basis for interpolation between $H^1$ and $L^p$, or between $L^p$ and BMO.
Combined with the Carleson measure characterization of BMO, it links the real-variable theory with harmonic extensions to the half-space.
