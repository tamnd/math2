---
tag: RWVHZ4KDBY
kind: definition
name: Hill sphere
msc: [70F07, 70F15, 85A04]
defines: P3760VW2WD
uses: [Y2R2QRPD1B, WDJNQVGTX0, CSVPJAA75E]
sources:
  - url: https://en.wikipedia.org/wiki/Hill_sphere
    locator: Definition
---

## Definition

Let $M > 0$ and $m > 0$ be masses with $m \ll M$.
Suppose a body of mass $m$ moves around a body of mass $M$ on a circular orbit of radius $a > 0$.
This is a solution of the [[two-body problem|CSVPJAA75E]].
The *Hill radius* of the body of mass $m$ is
$$r_H = a \sqrt[3]{\frac{m}{3 M}}.$$
The *Hill sphere* of the body is the ball of radius $r_H$ centred at it.

## Remarks

Origin of the formula: in the [[circular restricted three-body problem|Y2R2QRPD1B]] with mass parameter $\mu = m / (M + m)$, the [[Lagrange points|WDJNQVGTX0]] $L_1$ and $L_2$ lie at distance $a \left( (\mu / 3)^{1/3} + O(\mu^{2/3}) \right)$ from the small body, as $\mu \to 0$.
Some authors write $m / (3 (M + m))$ instead of $m / (3M)$, which agrees to first order when $m \ll M$.
For an elliptic orbit with semi-major axis $a$ and eccentricity $e$, the radius at pericentre is usually taken as $a (1 - e) \sqrt[3]{m / (3M)}$.

Example: for the Earth around the Sun, $m / M \approx 3.0 \times 10^{-6}$ and $a \approx 1.496 \times 10^8$ km.
Then $\sqrt[3]{m / (3M)} \approx \sqrt[3]{1.0 \times 10^{-6}} = 0.01$, and $r_H \approx 1.5 \times 10^6$ km.
The Moon, at about $3.84 \times 10^5$ km, lies well inside.

Non-example: for two stars of equal mass the condition $m \ll M$ fails, and the formula does not give a meaningful region of dominance.

The Hill sphere is only an approximation.
Numerical studies show that orbits of satellites are typically stable only well inside it, out to a fraction of $r_H$.

## Explanations

### L1 human

The Hill radius measures how far from a planet its gravity can hold a moon against the pull of the star.
It grows like the cube root of the mass ratio, and in proportion to the distance from the star.
