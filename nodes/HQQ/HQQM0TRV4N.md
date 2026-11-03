---
tag: HQQM0TRV4N
kind: statement
role: proposition
name: Velocity-addition formula
msc: [83A05]
uses: [WEVGN4C7PQ, 2E9AJVZS6E, T639889CSD]
about: [WEVGN4C7PQ]
sources:
  - url: https://en.wikipedia.org/wiki/Velocity-addition_formula
same_as:
  wikidata: Q1715792
  wikipedia: Velocity-addition formula
---

## Statement

Let $S$ and $S'$ be inertial frames, where $S'$ moves with velocity $v$ along the $x$ axis of $S$ and $\abs{v} < c$.
Let $\gamma = 1/\sqrt{1 - v^2/c^2}$ be the [[Lorentz factor|2E9AJVZS6E]] of $v$.
Let a particle have constant velocity $\mathbf{u}' = (u'_x, u'_y, u'_z)$ in $S'$.
Then its velocity $\mathbf{u} = (u_x, u_y, u_z)$ in $S$ is
$$u_x = \frac{u'_x + v}{1 + v u'_x / c^2}, \qquad u_y = \frac{u'_y}{\gamma (1 + v u'_x / c^2)}, \qquad u_z = \frac{u'_z}{\gamma (1 + v u'_x / c^2)}.$$
In particular, for motion along the $x$ axis, $u = (u' + v)/(1 + u' v / c^2)$.

## Remarks

Proof idea: apply the inverse [[Lorentz transformation|WEVGN4C7PQ]] $x = \gamma (x' + v t')$, $t = \gamma (t' + v x' / c^2)$, $y = y'$, $z = z'$ to the differentials along the world line and divide by $dt$.
Example: $u' = 0.6 c$ and $v = 0.6 c$ give $u = 1.2 c / 1.36 = 15 c / 17 \approx 0.88 c$, below $c$.
If $\abs{u'} < c$ and $\abs{v} < c$ then $\abs{u} < c$, and $u' = c$ gives $u = c$, so the speed of light is the same in both frames.
In terms of [[rapidities|T639889CSD]], collinear velocities add: $\operatorname{artanh}(u/c) = \operatorname{artanh}(u'/c) + \operatorname{artanh}(v/c)$, which is the addition formula of $\tanh$.
For $\abs{u'} \ll c$ and $\abs{v} \ll c$ the formula reduces to the Galilean rule $u = u' + v$.

## Explanations

### L1 human

In everyday life, if you walk at $1$ m/s on a train moving at $30$ m/s, your speed relative to the ground is $31$ m/s.
In relativity this rule is slightly wrong, and badly wrong near the speed of light.
The correct formula divides by a correction factor, so the combined speed never exceeds $c$.
Adding the speed of light to anything still gives the speed of light.

### L2 human

The formula is a direct computation from the Lorentz transformation, and it shows that boosts along one axis form a group isomorphic to $(\R, +)$ via rapidity.
The transverse components get the extra factor $1/\gamma$ because of time dilation.
For non-collinear velocities, the composition of two boosts is not a pure boost but a boost followed by a rotation, the Wigner rotation.
