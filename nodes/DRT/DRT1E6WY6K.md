---
tag: DRT1E6WY6K
kind: statement
role: theorem
name: Sokhotski–Plemelj formulae
msc: ["30E25", "30E20", "45E05"]
uses: [MGBKF52TQE, 0SYR10HD4R, 012PBA0FMD, RNB6QX0GCA]
about: [MGBKF52TQE]
sources:
  - url: https://en.wikipedia.org/wiki/Sokhotski%E2%80%93Plemelj_theorem
---

## Statement

Let $\Gamma$ be a smooth simple closed curve in $\C$, oriented counterclockwise, with interior domain $D^+$ and exterior domain $D^-$.
Let $\varphi \colon \Gamma \to \C$ be [[Hölder continuous|012PBA0FMD]], and let $\Phi(z) = \frac{1}{2\pi i} \int_\Gamma \frac{\varphi(\tau)}{\tau - z} \, d\tau$ for $z \notin \Gamma$ be its [[Cauchy-type integral|MGBKF52TQE]].
Let $t \in \Gamma$.
Then the limit $\Phi^+(t)$ of $\Phi(z)$ as $z \to t$ with $z \in D^+$ exists, and so does the limit $\Phi^-(t)$ as $z \to t$ with $z \in D^-$.
They are
$$\Phi^{\pm}(t) = \pm \frac12 \varphi(t) + \frac{1}{2\pi i} \, \mathrm{p.v.} \int_\Gamma \frac{\varphi(\tau)}{\tau - t} \, d\tau,$$
where $\mathrm{p.v.}$ is the [[Cauchy principal value|0SYR10HD4R]].
Equivalently,
$$\Phi^+(t) - \Phi^-(t) = \varphi(t), \qquad \Phi^+(t) + \Phi^-(t) = \frac{1}{\pi i} \, \mathrm{p.v.} \int_\Gamma \frac{\varphi(\tau)}{\tau - t} \, d\tau.$$

## Remarks

Proof idea: write $\int_\Gamma \frac{\varphi(\tau)}{\tau - z} \, d\tau = \int_\Gamma \frac{\varphi(\tau) - \varphi(t)}{\tau - z} \, d\tau + \varphi(t) \int_\Gamma \frac{d\tau}{\tau - z}$.
The last integral is $2\pi i$ for $z \in D^+$ and $0$ for $z \in D^-$.
The Hölder condition makes the first integral continuous up to $\Gamma$ from both sides, with value $\mathrm{p.v.} \int_\Gamma \frac{\varphi(\tau) - \varphi(t)}{\tau - t} \, d\tau$ at $t$.
Finally, $\mathrm{p.v.} \int_\Gamma \frac{d\tau}{\tau - t} = \pi i$, half of $2\pi i$, because the excised small arc around $t$ leaves half a turn.

Example: on the unit circle with $\varphi(\tau) = \tau^{-1}$, one has $\Phi = 0$ on $D^+$ and $\Phi(z) = -1/z$ on $D^-$.
So $\Phi^+(t) - \Phi^-(t) = t^{-1} = \varphi(t)$, and the principal value integral equals $\pi i (\Phi^+(t) + \Phi^-(t)) = -\pi i \, t^{-1}$.

Continuity of $\varphi$ alone is not enough: there are continuous densities whose principal value integral fails to exist at some points.
The formulae also hold on a smooth open arc, at every point other than the endpoints.
There $\Phi^+$ is the limit from the left of the arc and $\Phi^-$ the limit from the right.
For the real line they reduce to the [[Sokhotski–Plemelj theorem|RNB6QX0GCA]].

## Explanations

### L1 human

A Cauchy-type integral defines two holomorphic functions, one inside the curve and one outside.
At the curve, the inside one and the outside one have limits.
Their difference is the density $\varphi$, and their average is a principal value integral over the curve.
So the integral jumps by exactly $\varphi$ when one crosses the curve.

### L2 human

The formulae are the bridge between boundary value problems for holomorphic functions and singular integral equations.
The Riemann–Hilbert problem $\Phi^+ = G \Phi^- + g$ on $\Gamma$ is solved by writing the unknowns as Cauchy-type integrals.
Conversely, substituting $\Phi^\pm$ into the formulae turns the [[singular integral equation|E30EA6ETZ4]] $a \varphi + b S \varphi = f$, with $S \varphi = \frac{1}{\pi i} \mathrm{p.v.} \int_\Gamma \frac{\varphi(\tau)}{\tau - t} d\tau$, into the boundary condition $(a + b) \Phi^+ - (a - b) \Phi^- = f$.
This reduction is the basis of the theory of the [[index of a singular integral operator|GW3B4K1WA5]].
