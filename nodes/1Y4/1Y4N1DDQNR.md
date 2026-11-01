---
tag: 1Y4N1DDQNR
kind: statement
role: theorem
name: Lebesgue's theorem on differentiability of monotone functions
msc: [26A48, 26A24]
uses: [0WFF6AZPBP, 0F1WR9C83K, 36DXKAD2RZ, NPBYYK63FE, KDT3E0VE0K, 01A0MK1730, XDEJCKRVQ4]
about: [0A7KV2WB7A, 0F1WR9C83K]
sources:
  - url: https://en.wikipedia.org/wiki/Monotonic_function
---

## Statement

Let $a < b$ and let $f \colon [a, b] \to \R$ be a [[monotone function|0WFF6AZPBP]].
Then $f$ is [[differentiable|0F1WR9C83K]] at almost every point of $[a, b]$.
That is, the set of points of $(a, b)$ where $f$ has no finite derivative is a null set.

## Remarks

The standard proof uses the [[Dini derivatives|36DXKAD2RZ]] of $f$ and the Vitali covering lemma.
For nondecreasing $f$, one shows that each set $\set{x : D^+ f(x) > q > p > D_- f(x)}$ with rationals $p < q$ is null.
One also shows that the set where $D^+ f(x) = \infty$ is null.
Together with the same argument for the other pairs of Dini derivatives, this gives a finite derivative almost everywhere.

For nondecreasing $f$, the derivative $f'$ is moreover Lebesgue integrable, and $\int_a^b f'(x) \, dx \le f(b) - f(a)$ for the Lebesgue integral.
The inequality can be strict: for the [[Cantor function|NPBYYK63FE]], the left side is $0$ and the right side is $1$.
Monotonicity cannot be replaced by continuity: the [[Weierstrass function|01A0MK1730]] is continuous and differentiable at no point.
The theorem extends to functions of bounded variation, which are differences of monotone functions by the [[Jordan decomposition|KDT3E0VE0K]].

## Explanations

### L1 human

A monotone function only goes up, or only goes down.
It can have jumps and corners, even infinitely many.
The theorem says that it is still differentiable at almost every point: the bad points take up no length at all.

### L2 human

The theorem is the starting point of the theory of differentiation of real functions in measure theory.
It leads to the differentiation of indefinite Lebesgue integrals and to the fundamental theorem of calculus for absolutely continuous functions.
[[Fubini's theorem on differentiation|XDEJCKRVQ4]] refines it for series of monotone functions.
In contrast with the Cantor function, absolutely continuous functions satisfy $\int_a^b f' = f(b) - f(a)$.
