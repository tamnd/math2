---
tag: GXX2WPVRJ2
kind: statement
role: proposition
name: Integration in the transform variable
msc: [44A10]
uses: [05XT5AVJBK, TKZAV3KR86, 0R0T1VWH5X]
about: [0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Statement

Let $f \colon [0, \infty) \to \C$ be piecewise continuous and of [[exponential order|TKZAV3KR86]] $a$, that is, $\abs{f(t)} \le M e^{a t}$ for all $t \ge 0$.
Assume that $\int_0^1 \abs{f(t)} / t \, dt < \infty$, which holds for example when $\lim_{t \to 0^+} f(t)/t$ exists.
Let $F$ be the [[Laplace transform|05XT5AVJBK]] of $f$.
Then for every real $s > a$,
$$\mathcal{L}\left\{\frac{f(t)}{t}\right\}(s) = \int_s^\infty F(\sigma) \, d\sigma,$$
where the integral on the right is taken along the real axis and converges.

## Remarks

Write $\int_s^\infty F(\sigma) \, d\sigma = \int_s^\infty \int_0^\infty f(t) e^{-\sigma t} \, dt \, d\sigma$ and swap the integrals with [[Fubini's theorem|0R0T1VWH5X]].
The swap is allowed because $\int_0^\infty \abs{f(t)} e^{-s t} / t \, dt < \infty$ under the hypotheses.
The inner integral is $\int_s^\infty e^{-\sigma t} \, d\sigma = e^{-s t} / t$.
Example: with $f(t) = \sin t$, one gets $\mathcal{L}\{\sin t / t\}(s) = \int_s^\infty d\sigma / (\sigma^2 + 1) = \pi/2 - \arctan s$.
The hypothesis at $0$ is needed: for $f = 1$, the function $1/t$ has no Laplace transform, and $\int_s^\infty d\sigma / \sigma$ diverges.

## Explanations

### L1 human

Dividing a function by $t$ corresponds to integrating its transform from $s$ out to infinity.
It is the reverse of the rule that multiplying by $t$ corresponds to differentiating the transform.

### L2 human

The rule gives transforms of functions such as $\sin t / t$ and $(1 - e^{-t})/t$ that are hard to compute directly.
Letting $s \to 0^+$ in the example, with a limit argument, recovers the Dirichlet integral $\int_0^\infty \sin t / t \, dt = \pi / 2$.
Compare [[differentiation in the transform variable|VEPJN1NK3C]].
