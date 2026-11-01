---
tag: HN5XRJTHND
kind: definition
name: Nevanlinna theory
msc: ["30D35"]
defines: 1EHH63VNAD
uses: [0NSD1TPHR0, 0CDMXGPSES, YT6Z0GWS0W, 0P8BA7T7S5, 0H4R3RESGV]
sources:
  - url: https://en.wikipedia.org/wiki/Nevanlinna_theory
---

## Definition

Let $f$ be a [[meromorphic function|0NSD1TPHR0]] on $\C$ that is not constant, and write $\log^+ x = \max(\log x, 0)$ for $x \ge 0$, with $\log^+ 0 = 0$.
Nevanlinna theory studies $f$ through the following functions of $r > 0$, for $a$ in the [[Riemann sphere|0CDMXGPSES]] $\C \cup \set{\infty}$.

1. The number $n(t, a)$ of solutions of $f(z) = a$ in the disc $\abs{z} \le t$, counted with multiplicity; for $a = \infty$ these are the poles of $f$. The number $\overline{n}(t, a)$ counts the same points without multiplicity.
2. The *counting function* $N(r, a) = \int_0^r \dfrac{n(t, a) - n(0, a)}{t} \, dt + n(0, a) \log r$, and $\overline{N}(r, a)$ defined in the same way from $\overline{n}$.
3. The *proximity function* $m(r, a) = \dfrac{1}{2\pi} \displaystyle\int_0^{2\pi} \log^+ \frac{1}{\abs{f(re^{i\theta}) - a}} \, d\theta$ for $a \in \C$, and $m(r, \infty) = \dfrac{1}{2\pi} \displaystyle\int_0^{2\pi} \log^+ \abs{f(re^{i\theta})} \, d\theta$.
4. The [[Nevanlinna characteristic|YT6Z0GWS0W]] $T(r, f) = m(r, \infty) + N(r, \infty)$.
5. The *defect* $\delta(a) = \liminf_{r \to \infty} \dfrac{m(r, a)}{T(r, f)}$, using the [[limit inferior|0H4R3RESGV]].

## Remarks

Example: for $f(z) = e^z$ there are no poles and no zeros, so $N(r, \infty) = N(r, 0) = 0$.
The proximity functions are $m(r, \infty) = m(r, 0) = \frac{1}{2\pi}\int_0^{2\pi} \max(r \cos\theta, 0) \, d\theta = r/\pi$, so $T(r, e^z) = r/\pi$ and $\delta(0) = \delta(\infty) = 1$.
For a value $a \ne 0, \infty$, the solutions of $e^z = a$ have $n(t, a) \sim t/\pi$, so $N(r, a) \sim r/\pi$ and $\delta(a) = 0$.
By the [[first main theorem|QJWCFAK4AK]], $\delta(a) = 1 - \limsup_{r \to \infty} N(r, a)/T(r, f)$ when $f$ is transcendental, and $0 \le \delta(a) \le 1$.
A value that $f$ omits has defect $1$.
