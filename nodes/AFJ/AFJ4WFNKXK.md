---
tag: AFJ4WFNKXK
kind: statement
role: theorem
name: Levinson's theorem
msc: [81U05, 81U20]
uses: [CSHWP5PK4P, YDC9XBJDE1, 3XZFX39KH9, EPZR6H2WJN]
about: [YDC9XBJDE1, 3XZFX39KH9]
sources:
  - url: https://en.wikipedia.org/wiki/Levinson%27s_theorem
same_as:
  wikidata: Q25110385
  wikipedia: Levinson's theorem
---

## Statement

Let $V \colon (0, \infty) \to \R$ be a spherically symmetric potential on $\R^3$, written as a function of $r = \abs{x}$, with $\int_0^\infty r (1 + r) \abs{V(r)}\, dr < \infty$.
Use units in which the [[Schrödinger equation|EPZR6H2WJN]] is $-\Delta \psi + V \psi = E \psi$.
Fix an integer $l \ge 0$ and $k > 0$, and consider the radial equation
$$-u''(r) + \Big( \frac{l(l+1)}{r^2} + V(r) \Big) u(r) = k^2 u(r).$$
Let $u$ be its solution that vanishes at $r = 0$.
Define the phase shift $\delta_l(k)$ by $u(r) \sim A \sin(kr - l\pi/2 + \delta_l(k))$ as $r \to \infty$, with $A \ne 0$.
Normalize $\delta_l$ so that it is continuous in $k$ and $\delta_l(k) \to 0$ as $k \to \infty$.
Let $n_l$ be the number of [[bound states|3XZFX39KH9]] of angular momentum $l$.
These are the energies $-\kappa^2 < 0$ for which the radial equation, with $k^2$ replaced by $-\kappa^2$, has a nonzero square-integrable solution vanishing at $r = 0$.
Assume that there is no zero-energy bound state or zero-energy resonance in the channel $l$.
Then
$$\delta_l(0) = n_l \pi.$$
For $l = 0$, if instead there is a zero-energy resonance, then $\delta_0(0) = \big(n_0 + \tfrac{1}{2}\big)\pi$.

## Remarks

The proof applies the argument principle to the Jost function $f_l(k)$ of the channel.
It is analytic in the upper half-plane, tends to $1$ at infinity, and satisfies $\delta_l(k) = -\arg f_l(k)$ for $k > 0$.
Its zeros in the upper half-plane lie at the points $k = i\kappa$ with $-\kappa^2$ a bound state energy, so the change of phase along the real axis counts the bound states.
Example: for the attractive square well $V = -V_0$ on $r < a$ and $V = 0$ outside, with $\sqrt{V_0}\, a$ slightly larger than $\pi/2$, there is exactly one bound $s$-state, and $\delta_0(0) = \pi$.
Without the exclusion of zero-energy resonances, the formula fails for $l = 0$: the extra term $\pi/2$ appears.
In terms of the [[S-matrix|YDC9XBJDE1]] element $S_l(k) = e^{2i\delta_l(k)}$, the theorem relates the winding of $S_l$ along the positive real axis to the number of bound states.

## Explanations

### L1 human

When a wave scatters off a potential, it comes out shifted in phase compared with a free wave.
Levinson's theorem says that this phase shift at very low energy, measured from its value at very high energy, counts the bound states of the potential.
Each bound state adds $\pi$ to the phase shift.
So a property of scattering at positive energy reveals how many states are trapped at negative energy.

### L2 human

The theorem is a first instance of the link between the continuous spectrum and the discrete spectrum of a Schrödinger operator.
It is used to count bound states from scattering data.
It is also a key step in the inverse scattering problem on the half-line, where the phase shifts determine the potential only once the bound state data are added.
Its analytic content is the argument principle for the Jost function, the same tool that locates resonances.
Versions exist in one dimension, in two dimensions and for Dirac operators, with different half-integer corrections at zero energy.
