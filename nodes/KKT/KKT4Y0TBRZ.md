---
tag: KKT4Y0TBRZ
kind: example
name: Milne problem
msc: ["45E10", 85A25, 82D75]
instance_of: [QYY4NMDY5H]
uses: [EV6ZDQ0NDY, H4NXEY6QTZ, QYY4NMDY5H]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener%E2%80%93Hopf_method
---

## Example

Let $E_1(x) = \int_1^\infty e^{-x\mu}\, \mu^{-1}\, d\mu$ for $x > 0$ be the [[exponential integral|EV6ZDQ0NDY]], and more generally $E_n(x) = \int_1^\infty e^{-x\mu}\, \mu^{-n}\, d\mu$.
The *Milne problem* asks for a nonzero function $J$ on $[0, \infty)$ of at most linear growth with
$$J(\tau) = \frac{1}{2} \int_0^\infty E_1(\abs{\tau - t})\, J(t)\, dt, \quad \tau \ge 0.$$
This is a homogeneous [[Wiener–Hopf equation|QYY4NMDY5H]] with kernel $k(x) = \frac{1}{2} E_1(\abs{x})$.
In astrophysics $\tau$ is the optical depth in a plane-parallel grey atmosphere in radiative equilibrium, and $J$ is the mean intensity.

Check of the main features.
The kernel has total mass $1$: $\int_{\R} \frac{1}{2} E_1(\abs{x})\, dx = \int_1^\infty \mu^{-2}\, d\mu = 1$.
So on the whole line every linear function is a solution, and the cut at $\tau = 0$ makes the problem nontrivial.
Using $E_n' = -E_{n-1}$ for $n \ge 2$, one computes for $\tau \ge 0$
$$\frac{1}{2} \int_0^\infty E_1(\abs{\tau - t})\, dt = 1 - \frac{1}{2} E_2(\tau), \qquad \frac{1}{2} \int_0^\infty E_1(\abs{\tau - t})\, t\, dt = \tau + \frac{1}{2} E_3(\tau).$$
Hence the Eddington guess $J = \tau + \frac{2}{3}$ gives a right side that differs from $J$ by $\frac{1}{2} E_3(\tau) - \frac{1}{3} E_2(\tau)$.
This error tends to $0$ as $\tau \to \infty$, but at $\tau = 0$ it is $\frac{1}{4} - \frac{1}{3} = -\frac{1}{12}$, since $E_2(0) = 1$ and $E_3(0) = \frac{1}{2}$.

## Remarks

The exact solution, up to a constant factor, is $J(\tau) = \tau + q(\tau)$, where $q$ is the Hopf function.
It is found by the [[Wiener–Hopf method|H4NXEY6QTZ]].
The function $q$ increases from $q(0) = 1/\sqrt{3}$ to a limit $q(\infty) \approx 0.7104$.
The Fourier symbol of the kernel is $\frac{\arctan \xi}{\xi}$, which equals $1$ at $\xi = 0$, so $1 - \hat k$ vanishes at $0$; this zero is why the solution grows linearly.

## Explanations

### L1 human

Light travels through the outer layers of a star, is absorbed and is re-emitted in all directions.
In equilibrium, the light at each depth is an average of the light at all other depths, weighted by how much of it survives the trip.
Deep inside, the intensity grows linearly with depth, but near the surface there is a correction because no light comes in from outside.
The Milne problem asks for this correction, and its exact answer was one of the first successes of the Wiener–Hopf method.
