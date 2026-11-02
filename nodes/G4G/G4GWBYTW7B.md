---
tag: G4GWBYTW7B
kind: example
name: Abel's integral equation
msc: [45D05, "45E10"]
instance_of: [H6ZGEDM4VV, SNFYTC1TTA]
uses: [94TNBAAJYX, QHNWVSC6AQ]
sources:
  - url: https://en.wikipedia.org/wiki/Abel_transform
---

## Example

Let $b > 0$ and let $f$ be a given function on $[0, b]$.
*Abel's integral equation* is the equation
$$\int_0^x \frac{\varphi(t)}{\sqrt{x - t}} \, dt = f(x), \quad 0 \le x \le b,$$
for an unknown function $\varphi$ on $[0, b]$.
It is a [[Volterra equation of the first kind|H6ZGEDM4VV]], of [[convolution type|SNFYTC1TTA]], with the [[weakly singular kernel|94TNBAAJYX]] $k(x - t) = (x - t)^{-1/2}$.
More generally, Abel's equation with exponent $\alpha \in (0, 1)$ has the kernel $(x - t)^{-\alpha}$.

Check on an instance: take $\varphi = 1$.
Then $\int_0^x (x - t)^{-1/2} \, dt = 2 \sqrt{x}$, so $\varphi = 1$ solves the equation with $f(x) = 2\sqrt{x}$.
Take $\varphi(t) = t$.
The substitution $t = xu$ gives $\int_0^x t (x - t)^{-1/2} \, dt = x^{3/2} \int_0^1 u (1 - u)^{-1/2} \, du = \tfrac43 x^{3/2}$, using the [[Beta function|QHNWVSC6AQ]] value $B(2, \tfrac12) = \tfrac43$.

## Remarks

The kernel is not continuous on the diagonal, so the reduction to an equation of the second kind by differentiation does not apply.
The solution is instead given by the [[Abel inversion formula|TDMXFY06A2]], $\varphi(x) = \frac{1}{\pi} \frac{d}{dx} \int_0^x \frac{f(t)}{\sqrt{x - t}} \, dt$.
For $f(x) = 2\sqrt{x}$ this gives $\frac{1}{\pi} \frac{d}{dx} (\pi x) = 1$, as expected.
Abel met this equation in a mechanical problem that generalizes the [[tautochrone problem|A56P5S5D6Z]].

## Explanations

### L1 human

Abel's equation asks to recover a function from a weighted running integral, where the weight $1/\sqrt{x - t}$ blows up at the current point $x$.
The left side is, up to the factor $\sqrt{\pi}$, the Riemann–Liouville integral of order one half of $\varphi$.
So solving the equation means taking a "half derivative" of $f$.
It is one of the oldest integral equations, and it appears in mechanics, in tomography and in the study of fractional calculus.
