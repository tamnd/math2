---
tag: XQ70R88HCE
kind: definition
name: Reduced mass
msc: [70F05, 70F15]
defines: X5G1A3A4VR
uses: [0HNK6KT05K, C9YCMAPKMT]
sources:
  - url: https://en.wikipedia.org/wiki/Reduced_mass
---

## Definition

Let $m_1 > 0$ and $m_2 > 0$ be the masses of two bodies.
Their *reduced mass* is
$$\mu = \frac{m_1 m_2}{m_1 + m_2}.$$
Equivalently, $\frac{1}{\mu} = \frac{1}{m_1} + \frac{1}{m_2}$.

## Remarks

Let the bodies be at $x_1, x_2 \in \R^3$, let $M = m_1 + m_2$, let $R = (m_1 x_1 + m_2 x_2)/M$ be the [[centre of mass|0HNK6KT05K]] and let $r = x_2 - x_1$.
Then the total [[kinetic energy|C9YCMAPKMT]] splits as
$$\frac{m_1}{2} \norm{x_1'}^2 + \frac{m_2}{2} \norm{x_2'}^2 = \frac{M}{2} \norm{R'}^2 + \frac{\mu}{2} \norm{r'}^2.$$
Check: $x_1 = R - \frac{m_2}{M} r$ and $x_2 = R + \frac{m_1}{M} r$; the cross terms cancel because $m_1 \frac{m_2}{M} - m_2 \frac{m_1}{M} = 0$, and the $r$ terms give $\frac{m_1 m_2^2 + m_2 m_1^2}{2 M^2} \norm{r'}^2 = \frac{\mu}{2} \norm{r'}^2$.
So if the force between the bodies depends only on $r$, the relative motion obeys $\mu r'' = F(r)$, the equation of one body of mass $\mu$.

Example: for the Earth and the Moon, with mass ratio about $81$, the reduced mass is about $\frac{81}{82}$ of the mass of the Moon.
The formula needs both masses finite and positive; if $m_1 \to \infty$, then $\mu \to m_2$, which is the case of a fixed centre.
$\mu$ is less than $\min(m_1, m_2)$, and $\mu = m/2$ when $m_1 = m_2 = m$.

## Explanations

### L1 human

The reduced mass is half the harmonic mean of the two masses.
It is the effective mass of the relative motion of two bodies that act only on each other.
