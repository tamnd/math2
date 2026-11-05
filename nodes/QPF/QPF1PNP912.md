---
tag: QPF1PNP912
kind: statement
role: proposition
name: Hurwitz's formula
sources:
  - wikipedia: en:406952@r1372701847
    locator: Hurwitz zeta function, section Hurwitz's formula
    note: adopted
    mention: wikipedia://en/406952#S879
    sections: [Statement]
inventory: [HC0F40V43S]
---

## Statement

The Hurwitz zeta function satisfies an identity which generalizes the functional equation of the Riemann zeta function:

$$\zeta(1-s,a) = \frac{\Gamma(s)}{(2\pi)^s} \left( e^{-\pi i s/2} \sum_{n=1}^\infty \frac{e^{2\pi ina}}{n^s} + e^{\pi i s/2} \sum_{n=1}^\infty \frac{e^{-2\pi ina}}{n^s} \right),$$

valid for Re(*s*) > 1 and 0 \< *a* ≤ 1. The Riemann zeta functional equation is the special case *a* = 1:

$$\zeta(1-s) = \frac{2\Gamma(s)}{(2\pi)^{s}} \cos\left(\frac{\pi s}{2}\right) \zeta(s)$$

Hurwitz's formula can also be expressed as

$$\zeta(s,a) = \frac{2\Gamma(1-s)}{(2\pi)^{1-s}} \left( \sin\left(\frac{\pi s}{2}\right) \sum_{n=1}^\infty \frac{\cos(2\pi na)}{n^{1-s}} + \cos\left(\frac{\pi s}{2}\right) \sum_{n=1}^\infty \frac{\sin(2\pi na)}{n^{1-s}} \right)$$

(for $\operatorname{Re}(s) < 0$ and $0 < a \le 1$).

Hurwitz's formula has a variety of different proofs. One proof uses the contour integration representation along with the [[residue theorem|032HKYS329]]. A second proof uses a theta function identity, or equivalently Poisson summation. These proofs are analogous to the two proofs of the functional equation for the Riemann zeta function in Riemann's 1859 paper. Another proof of the Hurwitz formula uses Euler–Maclaurin summation to express the Hurwitz zeta function as an integral

$$\zeta(s,a) = s \int_{-a}^\infty \frac{\lfloor x \rfloor - x + \frac{1}{2}}{(x+a)^{s+1}} dx$$

($-1 < \operatorname{Re}(s) < 0$ and $0 < a \le 1$) and then expanding the numerator as a Fourier series.. Yet another proof of Hurwitz's formula uses Hermite's integral

$$\zeta(s,a)=\frac{1}{2}a^{-s}+\frac{a^{1-s}}{s-1}+2\int_0^\infty\frac{\sin(s\tan^{-1}(x/a))}{(a^2+x^2)^{s/2}\left(e^{2\pi x}-1\right)}dx,$$

by first revealing a nice connection between the Hurwitz zeta function and the Lommel functions.

When *a* is a rational number, Hurwitz's formula leads to the following functional equation: For integers $1\leq m \leq n$,

$$\zeta{\left(1{-}s, \frac{m}{n} \right)} = \frac{2\Gamma(s)}{ \left(2\pi n\right)^s } \sum_{k=1}^n \left[ \cos \left( \frac {\pi s} {2} -\frac {2\pi k m} {n} \right)\, \zeta{\left( s, \frac {k}{n} \right)} \right]$$

holds for all values of *s*.

This functional equation can be written as another equivalent form:

$$\zeta{\left(1{-}s, \frac{m}{n} \right)} = \frac{\Gamma(s)}{ \left(2\pi n\right)^s} \sum_{k=1}^n \left[e^{\frac{\pi is}{2} - \frac{2\pi ikm}{n}} \zeta{\left( s, \frac {k}{n} \right)} + e^{-\frac{\pi is}{2}+\frac{2\pi ikm}{n}} \zeta{\left( s,\frac {k}{n} \right)} \right].$$
