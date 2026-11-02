---
tag: RX7JSHMP8Z
kind: statement
role: theorem
name: Fundamental theorem of calculus for Lebesgue integrals
msc: [26A46, 28A15]
uses: [ZT6F4C2YHK, 2Z2QVWZ262, X7GTF3D98F, RARTMA0ZEC, 0V1EJCT8G6]
about: [ZT6F4C2YHK]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_continuity
---

## Statement

Let $a < b$ be real numbers, and let integrals on $[a, b]$ be taken with respect to [[Lebesgue measure|2Z2QVWZ262]].

1. Let $g \colon [a, b] \to \R$ be [[integrable|X7GTF3D98F]] and let $F(x) = \int_a^x g(t) \, dt$ for $x \in [a, b]$. Then $F$ is [[absolutely continuous|ZT6F4C2YHK]], and $F$ is [[differentiable|0V1EJCT8G6]] with $F'(x) = g(x)$ for [[almost every|RARTMA0ZEC]] $x \in [a, b]$.
2. Let $f \colon [a, b] \to \R$ be absolutely continuous. Then $f$ is differentiable at almost every point of $[a, b]$, the derivative $f'$ is integrable on $[a, b]$, and $f(x) = f(a) + \int_a^x f'(t) \, dt$ for every $x \in [a, b]$.

## Remarks

Part 1 follows from the Lebesgue differentiation theorem in dimension one; absolute continuity of $F$ comes from the absolute continuity of the integral.
For part 2, an absolutely continuous function has bounded variation, so it is a difference of two increasing functions and is differentiable almost everywhere with $f' \in L^1$.
The function $h = f - f(a) - \int_a^x f'$ is then absolutely continuous with $h' = 0$ almost everywhere, and an absolutely continuous function with zero derivative almost everywhere is constant.

Example: $f(x) = \abs{x}$ on $[-1, 1]$ is Lipschitz, hence absolutely continuous.
Its derivative is $-1$ on $(-1, 0)$ and $1$ on $(0, 1)$, undefined at $0$, and $\abs{x} = 1 + \int_{-1}^{x} f'(t) \, dt$ for every $x$.

Absolute continuity cannot be weakened to continuity in part 2.
The [[Cantor function|NPBYYK63FE]] $c$ is continuous and increasing on $[0, 1]$ with $c' = 0$ almost everywhere, but $c(1) - c(0) = 1 \ne 0 = \int_0^1 c'(t) \, dt$.

## Explanations

### L1 human

Integration and differentiation undo each other also for the Lebesgue integral, provided the functions are of the right kind.
Integrating an integrable function and then differentiating gives back the function, except on a set of length zero.
Differentiating and then integrating gives back the function exactly when the function is absolutely continuous.

### L2 human

The theorem shows that the absolutely continuous functions on $[a, b]$ are exactly the indefinite Lebesgue integrals.
It is the one-dimensional prototype of Sobolev spaces: absolutely continuous functions are the functions in $W^{1,1}(a, b)$, up to the choice of representative.
In the language of measures, it says that the Lebesgue–Stieltjes measure $df$ of an absolutely continuous $f$ has density $f'$ with respect to Lebesgue measure.
