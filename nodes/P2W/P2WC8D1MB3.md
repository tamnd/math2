---
tag: P2WC8D1MB3
kind: definition
name: Binet equation
msc: [70F05, 70F15]
defines: JQMZ5Y3E8G
uses: [APR7XN00N3, 7147M98XNR, 0NT64JV96A, 00HJCMC2CD]
sources:
  - url: https://en.wikipedia.org/wiki/Binet_equation
---

## Definition

Let $f \colon (0, \infty) \to \R$ be continuous.
Consider a particle in a plane that moves in the [[central force|APR7XN00N3]] field with radial acceleration $f(r)$.
Here $r$ is the distance to the centre, and $f > 0$ means repulsion.
In polar coordinates $(r, \theta)$ the motion satisfies $r'' - r \theta'^2 = f(r)$ and $r^2 \theta' = h$, where the constant $h$ is the [[angular momentum|7147M98XNR]] per unit mass.
Assume $h \neq 0$, so that $\theta$ is a strictly monotone function of time, and write $u = 1/r$ as a function of $\theta$.
The *Binet equation* is the [[differential equation|0NT64JV96A]]
$$\frac{d^2 u}{d \theta^2} + u = - \frac{f(1/u)}{h^2 u^2}.$$

## Remarks

Derivation: from $\theta' = h u^2$ one gets $r' = - h \, \frac{du}{d\theta}$ and $r'' = - h^2 u^2 \, \frac{d^2 u}{d\theta^2}$; substituting in $r'' - r \theta'^2 = f(r)$ and dividing by $- h^2 u^2$ gives the equation.

Example: for the attractive inverse-square force $f(r) = - k / r^2$ with $k > 0$, the right side is $k / h^2$.
The solutions are $u = \frac{k}{h^2} (1 + e \cos(\theta - \theta_0))$ with constants $e \ge 0$ and $\theta_0$.
So $r = \frac{h^2 / k}{1 + e \cos(\theta - \theta_0)}$ is a [[conic section|00HJCMC2CD]] with a focus at the centre.

The equation does not apply to a radial motion, where $h = 0$ and the angle stays constant, so $u$ cannot be written as a function of $\theta$.

Read backwards, the equation gives the force from the orbit: for the circle $r = 2 a \cos \theta$ through the centre, it gives $f(r) = - 8 a^2 h^2 / r^5$.

## Explanations

### L1 human

The Binet equation is the equation of motion in a central force, rewritten so that it gives the shape of the orbit rather than the timing.
