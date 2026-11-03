---
tag: AGAWK9A5CB
kind: definition
name: Four-acceleration
msc: [83A05, 70B05]
defines: J0D8VKDCK2
uses: [Y59V040THG, YG74WHC3S9, 2E9AJVZS6E, S8RKKKMSTG]
sources:
  - url: https://en.wikipedia.org/wiki/Four-acceleration
---

## Definition

Let $\tau \mapsto x(\tau)$ be a timelike world line in Minkowski space $(V, \eta)$, parametrised by [[proper time|YG74WHC3S9]] $\tau$, and let $U = dx / d\tau$ be its [[four-velocity|Y59V040THG]].
The *four-acceleration* is the [[four-vector|S8RKKKMSTG]]
$$A(\tau) = \frac{dU}{d\tau}(\tau) = \frac{d^2 x}{d\tau^2}(\tau).$$
The *proper acceleration* is $\alpha = \sqrt{\eta(A, A)}$.

## Remarks

Since $\eta(U, U) = -c^2$ is constant, differentiating gives $\eta(A, U) = 0$; so $A$ is orthogonal to a timelike vector, hence spacelike or zero, and $\alpha$ is real.
In an inertial frame, with velocity $\mathbf{u}$, ordinary acceleration $\mathbf{a} = d\mathbf{u}/dt$ and [[Lorentz factor|2E9AJVZS6E]] $\gamma = \gamma(\abs{\mathbf{u}})$,
$$A = \left( \frac{\gamma^4 \, \mathbf{u} \cdot \mathbf{a}}{c}, \ \gamma^2 \mathbf{a} + \frac{\gamma^4 (\mathbf{u} \cdot \mathbf{a})}{c^2} \mathbf{u} \right).$$
Example: in the instantaneous rest frame ($\mathbf{u} = 0$, $\gamma = 1$) one gets $A = (0, \mathbf{a})$ and $\alpha = \abs{\mathbf{a}}$.
Non-example: $d^2 x / dt^2 = (0, \mathbf{a})$, the second derivative in coordinate time, is not the four-acceleration.
It is not a four-vector: in a frame where the particle moves, it is not the Lorentz transform of its rest-frame value.
For a particle of mass $m$ under a four-force $F$, the equation of motion is $m A = F$.
