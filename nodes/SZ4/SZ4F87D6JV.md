---
tag: SZ4F87D6JV
kind: example
name: Vaidya metric
msc: [83C15, 83C57]
instance_of: [BY4QYYS788]
uses: [SG9GAYQT4R, 6Y50T68WKY, 4GTNM0WHDH, ENWD1YR20P]
sources:
  - url: https://en.wikipedia.org/wiki/Vaidya_metric
same_as:
  wikidata: Q7908710
  wikipedia: Vaidya metric
---

## Example

Use units where the gravitational constant and the speed of light equal $1$.
Let $m \colon \R \to \R$ be a smooth function.
In coordinates $(v, r, \theta, \phi)$ with $r > 0$, the ingoing *Vaidya metric* is
$$g = -\left(1 - \frac{2m(v)}{r}\right) dv^2 + 2\, dv\, dr + r^2\left(d\theta^2 + \sin^2\theta\, d\phi^2\right).$$
For constant $m$ this is the [[Schwarzschild metric|6Y50T68WKY]] in ingoing [[Eddington–Finkelstein coordinates|SG9GAYQT4R]].

Check: a computation of the [[Ricci curvature|4GTNM0WHDH]] gives one nonzero component,
$$R_{vv} = \frac{2\, m'(v)}{r^2},$$
and the scalar curvature is $0$.
So the Einstein equations $G_{ab} = 8\pi T_{ab}$ hold with
$$T_{ab} = \frac{m'(v)}{4\pi r^2}\, \ell_a \ell_b, \qquad \ell = dv.$$
The covector $\ell$ is null, so this is null dust: radiation falling inwards at the speed of light.
The null [[energy condition|ENWD1YR20P]] holds exactly when $m'(v) \ge 0$, that is, when the mass grows as radiation falls in.
The outgoing version, with $u$ in place of $v$ and $-2\, du\, dr$, describes a star that loses mass by emitting radiation.

## Explanations

### L1 human

The Vaidya metric is a Schwarzschild spacetime whose mass is allowed to change with time.
The change comes from a stream of light-like radiation, falling into the centre or flowing out of it.
It is the simplest exact model of a black hole that grows by swallowing radiation, or of a star that shines away its mass.
It is often used to study how horizons form and move in a dynamical situation.
