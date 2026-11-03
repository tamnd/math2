---
tag: 5T5GAKQD3S
kind: definition
name: Potential energy
msc: [70A05, 70F10]
defines: DF7DKHTQ7A
uses: [05R9NF2J49, 0NS2QYVC4Y]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_energy
---

## Definition

Let $U \subseteq \R^n$ be open and let $F \colon U \to \R^n$ be a continuous force field.
A *potential energy* for $F$ is a function $V \colon U \to \R$ of class $C^1$ such that
$$F(x) = -\nabla V(x) \quad \text{for all } x \in U,$$
where $\nabla V$ is the [[gradient|0NS2QYVC4Y]] of $V$.
For $N$ particles in $\R^3$, take $n = 3N$, so that $V(x_1, \dots, x_N)$ and the force on particle $i$ is $F_i = -\nabla_{x_i} V$.

## Remarks

A potential energy exists exactly when $F$ is a [[conservative vector field|05R9NF2J49]], and then $-V$ is a scalar potential of $F$.
On a connected set $U$, the potential energy is unique up to an additive constant.
Example: uniform gravity $F(x) = (0, 0, -mg)$ on $\R^3$ has the potential energy $V(x) = m g x_3$, since $-\nabla V = (0, 0, -mg)$.
A spring force $F(x) = -k x$ with $k > 0$ has $V(x) = \frac{k}{2}\abs{x}^2$.
Non-example: the field $F(x) = (-x_2, x_1, 0)$ has no potential energy on $\R^3$, since its line integral around the unit circle in the plane $x_3 = 0$ is $2\pi \ne 0$.

## Explanations

### L1 human

A potential energy is a "height function" for a force: the force always points in the direction in which this height falls fastest, with strength equal to the slope.
Only forces that do no net work around closed loops have one.
