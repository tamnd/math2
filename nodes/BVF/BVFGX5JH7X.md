---
tag: BVFGX5JH7X
kind: example
name: Wiener filter equation
msc: [60G35, "93E11", "45E10"]
instance_of: [QYY4NMDY5H]
uses: [DT0QXJE705, 3ZXN26PW4G, H4NXEY6QTZ, QYY4NMDY5H]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_filter
---

## Example

Let $x(t)$ and $s(t)$, $t \in \R$, be real, jointly wide-sense [[stationary processes|DT0QXJE705]] with mean $0$.
Write $R_{xx}(\tau) = E[x(u + \tau)\, x(u)]$ and $R_{sx}(\tau) = E[s(u + \tau)\, x(u)]$; they do not depend on $u$.
The task is to estimate $s(t)$ by a causal linear filter of the observations, $\hat s(t) = \int_0^\infty h(\tau)\, x(t - \tau)\, d\tau$, with the smallest mean square error $E\bigl[(s(t) - \hat s(t))^2\bigr]$.
The optimal impulse response $h$ satisfies the *Wiener filter equation*
$$R_{sx}(\sigma) = \int_0^\infty h(\tau)\, R_{xx}(\sigma - \tau)\, d\tau, \quad \sigma \ge 0.$$
This is a [[Wiener–Hopf equation|QYY4NMDY5H]] of the first kind with kernel $R_{xx}$.

Check of the equation.
The error $e(t) = s(t) - \hat s(t)$ of the best filter is orthogonal to every observation $x(t - \sigma)$ with $\sigma \ge 0$.
Otherwise a small change of $h$ would lower the error.
So $E[s(t)\, x(t - \sigma)] = \int_0^\infty h(\tau)\, E[x(t - \tau)\, x(t - \sigma)]\, d\tau$.
The left side is $R_{sx}(\sigma)$ and the expectation under the integral is $R_{xx}(\sigma - \tau)$, which gives the equation.
The condition holds only for $\sigma \ge 0$, because the filter may use only the past.

## Remarks

Without the causality condition, the equation holds for all $\sigma \in \R$, and the Fourier transform solves it: $H = S_{sx} / S_{xx}$, with $S$ the spectral densities given by the [[Wiener–Khinchin theorem|3ZXN26PW4G]].
With causality, the [[Wiener–Hopf method|H4NXEY6QTZ]] applies.
One factors $S_{xx} = S^+ S^-$ into factors without zeros in the two half-planes.
The causal filter is then $H = \bigl[S_{sx}/S^-\bigr]_+ / S^+$, where $[\cdot]_+$ keeps the part that comes from a function supported on $[0, \infty)$.
This step is called spectral factorization.

## Explanations

### L1 human

One wants to clean up a noisy signal as it arrives, using only what has been seen so far.
The best linear way to do it makes the error uncorrelated with all past observations.
Writing this down gives an integral equation on a half-line, because only the past counts.
That half-line is what makes it a Wiener–Hopf equation instead of a plain convolution.
