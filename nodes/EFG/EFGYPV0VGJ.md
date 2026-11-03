---
tag: EFGYPV0VGJ
kind: statement
role: theorem
name: DiPerna–Lions renormalized solutions of the Boltzmann equation
msc: [35Q20, 82C40, 76P05]
uses: [MH6CSWD7F0, BMA7D1Z2W6]
about: [MH6CSWD7F0]
sources:
  - url: https://en.wikipedia.org/wiki/Boltzmann_equation
---

## Statement

Consider the [[Boltzmann equation|MH6CSWD7F0]] on $\R^3_x \times \R^3_v$,
$$\partial_t f + v \cdot \nabla_x f = Q(f, f), \qquad Q(f, f)(v) = \int_{\R^3} \int_{S^2} B(v - v_*, \omega) \big( f' f_*' - f f_* \big) \, d\omega \, dv_*,$$
where $v' = v - ((v - v_*) \cdot \omega)\, \omega$ and $v_*' = v_* + ((v - v_*) \cdot \omega)\, \omega$, and $f$, $f'$, $f_*$, $f_*'$ are evaluated at $v$, $v'$, $v_*$, $v_*'$.
Assume the collision kernel $B \ge 0$ depends only on $\abs{z}$ and $\abs{z \cdot \omega}$, that $A(z) = \int_{S^2} B(z, \omega)\, d\omega$ is locally integrable on $\R^3$, and that for every $R > 0$
$$\frac{1}{1 + \abs{v}^2} \int_{\abs{z} \le R} A(v - z) \, dz \to 0 \quad \text{as } \abs{v} \to \infty.$$
Let $f_0 \ge 0$ be measurable with $\int\!\!\int f_0 \big( 1 + \abs{x}^2 + \abs{v}^2 + \abs{\log f_0} \big) \, dx \, dv < \infty$.
Write $Q = Q^+ - Q^-$, where the gain term $Q^+$ contains $f' f_*'$ and the loss term $Q^-$ contains $f f_*$.
Then there exists $f \in C\big( [0, \infty); L^1(\R^3 \times \R^3) \big)$ with $f \ge 0$ and $f(0) = f_0$ that is a renormalized solution.
That is, $Q^\pm(f, f)/(1 + f) \in L^1_{\mathrm{loc}}$ and
$$\big( \partial_t + v \cdot \nabla_x \big) \log(1 + f) = \frac{Q(f, f)}{1 + f}$$
in the sense of distributions on $(0, \infty) \times \R^3 \times \R^3$.

## Remarks

The difficulty is that the bounds available for large data, on mass, energy and the entropy $\int f \log f$ from the [[H-theorem|BMA7D1Z2W6]], do not make $Q(f, f)$ locally integrable.
Dividing by $1 + f$ gives a term that these bounds control.
The proof solves approximate problems with truncated collision terms and passes to the limit with these a priori bounds.
The key tool is the velocity averaging lemma, which gives compactness in $x$ of averages in $v$.
The result was published by Ronald DiPerna and Pierre-Louis Lions in 1989.

The hard-sphere kernel $B(z, \omega) = \abs{z \cdot \omega}$ satisfies the hypotheses, since $A(z) = c\abs{z}$ for a constant $c > 0$ and $\int_{\abs{z} \le R} \abs{v - z}\, dz$ grows only linearly in $\abs{v}$.

Uniqueness of renormalized solutions is not known.
Nor is it known in general that they satisfy the local conservation laws of momentum and energy.

## Explanations

### L1 human

The Boltzmann equation describes a gas through the distribution of its molecules in position and velocity.
For general initial data, nobody knew whether solutions exist for all time, because the collision term could be too large to make sense.
DiPerna and Lions found a weaker meaning of solution, obtained by looking at $\log(1 + f)$ instead of $f$, and proved that such solutions always exist.

### L2 human

This is the basic global existence theorem for the Boltzmann equation with large data in the whole space.
It relies on the H-theorem for the entropy bound and on velocity averaging for compactness.
The renormalized solutions are the starting point of the Bardos–Golse–Levermore program towards [[Hilbert's sixth problem|T1KAGHT39X]], which derives Leray solutions of the Navier–Stokes equations from them.
Smooth solutions near equilibrium are known by other methods, but for large data the renormalized solutions remain the main existence result.
