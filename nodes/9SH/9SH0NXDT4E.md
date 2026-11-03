---
tag: 9SH0NXDT4E
kind: definition
name: Kepler's equation
msc: [70F05, 70F15, 65H05]
defines: MSB4ZTG422
uses: [M1A7XV292M, 0VKCCEXBJ1, 0HVX863SAJ, 0RBKKNH4GV, 07EXVNF9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Kepler%27s_equation
---

## Definition

Consider a body moving on an elliptic Kepler orbit, as in [[Kepler's laws|M1A7XV292M]].
Let $a > 0$ be the semi-major axis of the [[ellipse|0VKCCEXBJ1]], let $e \in [0, 1)$ be its [[eccentricity|0HVX863SAJ]], and let $b = a \sqrt{1 - e^2}$.
Let $T > 0$ be the period, and let $\tau$ be a time at which the body passes the pericentre.
Place the attracting [[focus|0RBKKNH4GV]] at the origin and the pericentre on the positive $x$-axis, with the body moving anticlockwise.

1. The *mean anomaly* at time $t$ is $M(t) = \frac{2 \pi}{T} (t - \tau)$.
2. The *eccentric anomaly* at time $t$ is the angle $E(t)$ such that the position of the body is $\left( a (\cos E - e), \; b \sin E \right)$.
3. *Kepler's equation* is the relation $$M = E - e \sin E$$ between them, which holds at all times along the orbit.

## Remarks

For each $M \in \R$ and $e \in [0, 1)$ the equation has exactly one solution $E \in \R$, because $E \mapsto E - e \sin E$ is continuous, has derivative $1 - e \cos E \ge 1 - e > 0$, and tends to $\pm \infty$ as $E \to \pm \infty$.
Example: at the apocentre $E = \pi$, and the equation gives $M = \pi$, so the body reaches the apocentre half a period after the pericentre, as symmetry requires.
Example with numbers: for $e = 0.5$ and $M = \pi/2$, [[Newton's method|07EXVNF9VP]] started at $E_0 = M$ converges to $E \approx 2.0210$.

The definition fails for $e \ge 1$, where the orbit is not an ellipse.
For a hyperbolic orbit, with $e > 1$, the analogous relation is $M = e \sinh H - H$ with a hyperbolic anomaly $H$.

The distance to the focus is $\norm{r} = a (1 - e \cos E)$, and the true anomaly $\theta$ satisfies $\tan \frac{\theta}{2} = \sqrt{\frac{1 + e}{1 - e}} \tan \frac{E}{2}$.

## Explanations

### L1 human

The mean anomaly is a clock that runs at a steady rate and goes around once per orbit.
The eccentric anomaly is an angle that tells where the body actually is.
Kepler's equation converts the clock reading into the position.
