---
tag: 8NEK35QMPH
kind: counterexample
name: Norton's dome
msc: [70A05, 34A12]
uses: [KNBP19FG6K, 0FXDW992DS, 0AW1E6YTJY]
sources:
  - url: https://en.wikipedia.org/wiki/Norton%27s_dome
same_as:
  wikidata: Q18354955
  wikipedia: Norton's dome
---

## Counterexample

A point mass slides without friction on a rigid dome under constant gravity $g > 0$.
The dome is symmetric about a vertical axis through its apex.
Let $r \ge 0$ be the arc length along the surface from the apex.
In suitable units, let the dome lie at depth $h(r) = \frac{2}{3g}\, r^{3/2}$ below the apex.
The tangential component of gravity at arc distance $r$ is $g\, h'(r) = \sqrt r$.
So, for a radial motion, [[Newton's second law|KNBP19FG6K]] for a unit mass reads
$$\ddot r = \sqrt r.$$
Take the [[initial value problem|0FXDW992DS]] with $r(0) = 0$ and $\dot r(0) = 0$: the mass starts at rest on the apex.
One solution is $r(t) = 0$ for all $t$.
For each $T \ge 0$, another solution is $r_T$, given by $r_T(t) = 0$ for $t \le T$ and $r_T(t) = (t - T)^4 / 144$ for $t \ge T$.
Check: for $t \ge T$, $\ddot r_T = \dfrac{12 (t - T)^2}{144} = \dfrac{(t-T)^2}{12} = \sqrt{r_T(t)}$, and $r_T$, $\dot r_T$ and $\ddot r_T$ vanish at $t = T$, so the pieces join into a $C^2$ solution.
So Newton's equation has infinitely many solutions with the same initial state.

## Remarks

The right-hand side $\sqrt r$ is continuous but does not satisfy a [[Lipschitz condition|0AW1E6YTJY]] at $r = 0$.
This is why the uniqueness part of the Picard–Lindelöf theorem does not apply.
The dome itself is not smooth at the apex: its curvature there is infinite.
On a dome with a smooth profile, the force would be Lipschitz in $r$ and the mass at rest on the apex would stay there.
The example shows that Newtonian mechanics is deterministic only under regularity assumptions on the forces.

## Explanations

### L1 human

Put a ball exactly on top of a specially shaped dome.
The equations of motion allow the ball to stay there forever, but they also allow it to start rolling down at any moment, in any direction, with no cause.
The trick is the shape of the top of the dome, which is sharp in a subtle way.
The example shows that Newton's laws only predict a unique future when the forces are smooth enough.
