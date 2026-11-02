---
tag: ZK55WHXEQX
kind: example
name: Laplace transform of a periodic function
msc: [44A10]
illustrates: [0V49JEZW06]
uses: [05XT5AVJBK, 089KWVYD69]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Example

Let $P > 0$ and let $f \colon [0, \infty) \to \C$ be [[periodic|089KWVYD69]] with period $P$, that is $f(t + P) = f(t)$ for $t \ge 0$, and integrable on $[0, P]$.
Its [[Laplace transform|05XT5AVJBK]] is
$$F(s) = \frac{1}{1 - e^{-Ps}} \int_0^P f(t) e^{-st}\, dt \quad (\operatorname{Re} s > 0).$$
Check: for $\operatorname{Re} s > 0$ the integral converges absolutely, since $\int_0^\infty \abs{f} e^{-\sigma t}\, dt = \sum_{k \ge 0} e^{-k P \sigma} \int_0^P \abs{f(t)} e^{-\sigma t}\, dt < \infty$ for $\sigma = \operatorname{Re} s$.
Split $[0, \infty)$ into the intervals $[kP, (k + 1)P]$ and substitute $t = u + kP$:
$$F(s) = \sum_{k \ge 0} e^{-kPs} \int_0^P f(u) e^{-su}\, du,$$
a geometric series with ratio $e^{-Ps}$, of modulus less than $1$.
Instance: $f(t) = \abs{\sin t}$ has period $\pi$, and $\int_0^\pi \sin t\, e^{-st}\, dt = \frac{1 + e^{-\pi s}}{s^2 + 1}$.
So
$$\mathcal{L}\{\abs{\sin t}\}(s) = \frac{1 + e^{-\pi s}}{(s^2 + 1)(1 - e^{-\pi s})} = \frac{\coth(\pi s / 2)}{s^2 + 1}.$$

## Explanations

### L1 human

A periodic function repeats the same piece forever.
Each copy of the piece is the first copy delayed by a multiple of the period, and a delay by $kP$ multiplies the transform by $e^{-kPs}$.
Adding up all copies gives a geometric series, so only the transform of one period is needed.
