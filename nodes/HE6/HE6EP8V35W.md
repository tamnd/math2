---
tag: HE6EP8V35W
kind: example
name: Hyperbolic motion
msc: [83A05, 70B05]
instance_of: [Z788G6MJ9E]
illustrates: [J0D8VKDCK2]
uses: [Z788G6MJ9E, J0D8VKDCK2, Y59V040THG, YG74WHC3S9, T639889CSD, TWXJH5ZEHA, 01PPDSDP2N]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_motion_(relativity)
same_as:
  wikidata: Q3866303
  wikipedia: Hyperbolic motion (relativity)
---

## Example

Fix the speed of light $c > 0$ and a proper acceleration $\alpha > 0$.
*Hyperbolic motion* is the [[world line|Z788G6MJ9E]] in Minkowski space given, as a function of [[proper time|YG74WHC3S9]] $\tau \in \R$, by
$$ct(\tau) = \frac{c^2}{\alpha} \sinh\frac{\alpha \tau}{c}, \qquad x(\tau) = \frac{c^2}{\alpha} \cosh\frac{\alpha \tau}{c}, \qquad y = z = 0.$$
Its points satisfy $x^2 - c^2 t^2 = c^4 / \alpha^2$, so the world line is one branch of a hyperbola.

Check that $\tau$ is proper time: the [[four-velocity|Y59V040THG]] is
$$U = \frac{d(ct, x)}{d\tau} = \left( c \cosh\frac{\alpha\tau}{c}, \ c \sinh\frac{\alpha\tau}{c} \right),$$
and $\eta(U, U) = -c^2 \cosh^2 + c^2 \sinh^2 = -c^2$.
The [[four-acceleration|J0D8VKDCK2]] is
$$A = \frac{dU}{d\tau} = \left( \alpha \sinh\frac{\alpha\tau}{c}, \ \alpha \cosh\frac{\alpha\tau}{c} \right),$$
with $\eta(A, A) = \alpha^2 (\cosh^2 - \sinh^2) = \alpha^2$.
So the proper acceleration is the constant $\alpha$: this is the motion of a rocket that feels a constant acceleration $\alpha$.

The ordinary velocity is $dx/dt = c \tanh(\alpha \tau / c)$, so the [[rapidity|T639889CSD]] is $\alpha \tau / c$, growing linearly in proper time, while the speed stays below $c$.
In [[Rindler coordinates|TWXJH5ZEHA]] this world line is the curve $\rho = c^2 / \alpha$, $\eta = \alpha \tau / c$.

## Explanations

### L1 human

A rocket whose passengers always feel the same push, say $1 g$, does not reach the speed of light; its speed creeps closer and closer to $c$.
Drawn in spacetime, its path is a hyperbola that approaches the light ray $x = ct$ without touching it.
A light signal sent after the rocket from far enough behind never catches up, which makes the line $x = ct$ a horizon for the rocket.
At $1 g$, the term $c^2/\alpha$ is about one light-year, so after about a year of its own time the rocket is already moving at a large fraction of $c$.
