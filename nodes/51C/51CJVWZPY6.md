---
tag: 51CJVWZPY6
kind: definition
name: Gravity assist
msc: [70M20, 70F15]
defines: WDDS09PPV4
uses: [BV6ACVR5TV, BXFSBB8Q46, 0WN5G117YC]
sources:
  - url: https://en.wikipedia.org/wiki/Gravity_assist
---

## Definition

Work in the [[patched conic approximation|BV6ACVR5TV]].
Let a planet with gravitational parameter $\mu > 0$ move with velocity $V$ relative to the Sun, taken as constant during the flyby.
A spacecraft enters the planet's sphere of influence with velocity $v_{\mathrm{in}}$ relative to the Sun.
Inside it moves on a [[hyperbolic|0WN5G117YC]] [[Kepler orbit|BXFSBB8Q46]] about the planet, with arrival velocity $u_{\mathrm{in}} = v_{\mathrm{in}} - V$ relative to the planet and periapsis distance $r_p > 0$.
It leaves with velocity $u_{\mathrm{out}}$ relative to the planet, where $\norm{u_{\mathrm{out}}} = \norm{u_{\mathrm{in}}} = v_\infty$ and the angle $\delta$ between $u_{\mathrm{in}}$ and $u_{\mathrm{out}}$ satisfies
$$\sin \frac{\delta}{2} = \frac{1}{e}, \qquad e = 1 + \frac{r_p v_\infty^2}{\mu}.$$
The change of heliocentric velocity $v_{\mathrm{out}} - v_{\mathrm{in}} = u_{\mathrm{out}} - u_{\mathrm{in}}$, with $v_{\mathrm{out}} = V + u_{\mathrm{out}}$, is the *gravity assist*.

## Remarks

The size of the change is $\norm{u_{\mathrm{out}} - u_{\mathrm{in}}} = 2 v_\infty \sin(\delta/2)$.
The heliocentric speed changes because $\norm{V + u_{\mathrm{out}}}$ differs from $\norm{V + u_{\mathrm{in}}}$ in general.
It grows when the craft passes behind the planet, so that $u_{\mathrm{out}}$ turns towards $V$.

Example: let $u$ be parallel to $V$ with $\norm{u} = v_\infty$, and let $u_{\mathrm{in}} = -u$ and $u_{\mathrm{out}} = u$.
Then the heliocentric speed goes from $\norm{V} - v_\infty$ to $\norm{V} + v_\infty$, a gain of $2 v_\infty$.
This is the limit $\delta \to \pi$, which needs $r_p \to 0$.

Non-example: if the attracting body does not move, $V = 0$, then $\norm{v_{\mathrm{out}}} = \norm{v_{\mathrm{in}}}$, so the flyby only turns the craft and its speed relative to the body is unchanged.

The total energy of the craft and the planet is conserved; the planet's change of speed is negligible because of its large mass.
