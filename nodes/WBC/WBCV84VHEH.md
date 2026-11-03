---
tag: WBCV84VHEH
kind: statement
role: proposition
name: Aberration of light
msc: [85A04, 83A05]
uses: [W7GD4WR497]
about: [W7GD4WR497]
sources:
  - url: https://en.wikipedia.org/wiki/Aberration_(astronomy)
---

## Statement

Let $S$ be an inertial frame, and let an observer move with constant velocity $v$ relative to $S$.
Let $c$ be the speed of light, and let $\beta = \abs{v}/c$, with $0 \le \beta < 1$.
Let light from a distant source arrive at the observer.
Let $\theta \in [0, \pi]$ be the angle in $S$ between $v$ and the direction towards the source.
Then the observer sees the source at the angle $\theta'$ from the direction of motion, where
$$\cos\theta' = \frac{\cos\theta + \beta}{1 + \beta\cos\theta}.$$
In particular $\theta' \le \theta$, with equality only when $\beta = 0$ or $\sin\theta = 0$, and $\theta - \theta' = \beta\sin\theta + O(\beta^2)$.

## Remarks

The light travels in the direction $-n$, where $n$ is the unit vector towards the source.
Apply the Lorentz transformation to the photon's energy $E$ and momentum component $p_\parallel = -(E/c)\cos\theta$ along $v$.
This gives $E' = \gamma E (1 + \beta\cos\theta)$ and $c\,p'_\parallel = -\gamma E(\cos\theta + \beta)$, with $\gamma = (1 - \beta^2)^{-1/2}$, and the formula follows.
So a moving observer sees all sources shifted towards the point on the [[celestial sphere|W7GD4WR497]] towards which it moves.
Example: the Earth's orbital speed is about $29.8$ km/s, so $\beta \approx 9.9 \times 10^{-5}$.
In radians this is about $20.5''$, the constant of annual aberration.
Over a year each star traces a small ellipse of semi-major axis about $20.5''$.

## Explanations

### L1 human

Running through vertical rain, you must tilt your umbrella forward, because the rain seems to come from ahead.
Starlight behaves in the same way for an observer on the moving Earth.
Every star appears shifted a little towards the direction in which the Earth is moving.
As the Earth goes around the Sun, its direction of motion turns, and the stars trace small ellipses in the sky.

### L2 human

The exact formula is the relativistic transformation of directions of light rays between two inertial frames.
To first order in $\beta$ it agrees with the classical picture of adding the observer's velocity to the velocity of light.
In astrometry one distinguishes annual aberration, from the orbital motion of the Earth, and diurnal aberration, from its rotation, which is at most about $0.32''$.
Unlike parallax, aberration does not depend on the distance of the star, only on its direction.
James Bradley discovered annual aberration while he was looking for stellar parallax.
