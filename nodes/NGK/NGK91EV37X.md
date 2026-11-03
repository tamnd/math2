---
tag: NGK91EV37X
kind: example
name: Ellis wormhole
msc: [83C15, 83C99]
instance_of: [MXBVB858GR]
uses: [4GTNM0WHDH, ENWD1YR20P]
sources:
  - url: https://en.wikipedia.org/wiki/Ellis_wormhole
same_as:
  wikidata: Q25313226
  wikipedia: Ellis wormhole
---

## Example

Use units where the gravitational constant and the speed of light equal $1$.
Fix $n > 0$.
On $\R \times \R \times S^2$ with coordinates $(t, \ell, \theta, \phi)$, the *Ellis wormhole* is the metric
$$g = -dt^2 + d\ell^2 + \left(\ell^2 + n^2\right)\left(d\theta^2 + \sin^2\theta\, d\phi^2\right).$$

Check that it is a [[wormhole|MXBVB858GR]]: the areal radius $r(\ell) = \sqrt{\ell^2 + n^2}$ has its minimum $n$ at $\ell = 0$, which is the throat.
As $\ell \to \pm\infty$, $r(\ell)/\abs{\ell} \to 1$, so the two ends are asymptotically flat, and $g_{tt} = -1$ never vanishes, so there is no horizon.

Its [[Ricci curvature|4GTNM0WHDH]] has one nonzero component,
$$R_{\ell\ell} = -\frac{2n^2}{\left(\ell^2 + n^2\right)^2}.$$
For the null vector $k = \partial_t + \partial_\ell$ this gives $R_{ab}k^ak^b < 0$ everywhere, so the null [[energy condition|ENWD1YR20P]] fails.
This Ricci tensor is the one produced by a massless scalar field $\varphi = \frac{1}{\sqrt{4\pi}}\arctan(\ell/n)$ whose kinetic energy has the opposite of the usual sign, through $R_{ab} = -8\pi\, \partial_a\varphi\, \partial_b\varphi$.
Indeed $8\pi(\varphi')^2 = 2n^2/(\ell^2 + n^2)^2$.

The Ellis wormhole has zero mass at both ends: $g_{tt} = -1$ means that a particle at rest feels no gravitational pull.
A free particle can cross the throat from one end to the other in finite time.

## Explanations

### L1 human

The Ellis wormhole is the simplest traversable wormhole: a static tunnel connecting two flat universes, with a throat of radius $n$.
Nothing pulls you in or pushes you out; you can drift through the throat at any speed.
To hold it open one needs an unusual field with negative kinetic energy, called a phantom field.
Homer Ellis presented it in 1973, and it is often used as a test case for questions about wormholes.
