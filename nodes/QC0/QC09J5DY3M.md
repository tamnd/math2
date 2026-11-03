---
tag: QC09J5DY3M
kind: definition
name: Mechanical similarity
msc: [70F10, 70A05]
defines: VZXCAFQFW9
uses: [5T5GAKQD3S, KNBP19FG6K]
sources:
  - url: https://en.wikipedia.org/wiki/Mechanical_similarity
---

## Definition

Let $U \subseteq \R^n$ be an open set with $\lambda U = U$ for all $\lambda > 0$.
Let $V \colon U \to \R$ be a [[potential energy|5T5GAKQD3S]] of class $C^1$ that is homogeneous of degree $k \in \R$, that is, $V(\lambda q) = \lambda^k V(q)$ for all $\lambda > 0$ and $q \in U$.
Consider the equations of motion $M \ddot q = -\nabla V(q)$ given by [[Newton's second law|KNBP19FG6K]], where $M$ is a fixed positive definite diagonal matrix of masses.
For $\alpha > 0$, set $\beta = \alpha^{1 - k/2}$.
The *mechanical similarity* with ratio $\alpha$ maps a curve $q(t)$ in $U$ to the curve
$$\tilde q(t) = \alpha\, q(t / \beta).$$
Two motions are *mechanically similar* if one is the image of the other under a mechanical similarity.

## Remarks

The key property: the image of a motion is again a motion.
Indeed $\nabla V$ is homogeneous of degree $k - 1$, so $M \ddot{\tilde q}(t) = \frac{\alpha}{\beta^2} M \ddot q(t/\beta) = -\frac{\alpha}{\beta^2} \nabla V(q(t/\beta))$, while $-\nabla V(\tilde q(t)) = -\alpha^{k-1} \nabla V(q(t/\beta))$, and $\alpha/\beta^2 = \alpha^{k-1}$.
Times scale by $\beta$ and the energy scales by $\alpha^k$.
Example: for the Kepler potential $V = -c/\abs{q}$, $k = -1$ and $\beta = \alpha^{3/2}$, so periods $P$ and sizes $a$ of similar orbits satisfy $P^2 \propto a^3$, as in Kepler's third law.
Non-example: for $V(q) = \abs{q}^2 + \abs{q}^4$, which is not homogeneous, no single exponent works, and the scaled curve of a motion is in general not a motion.

## Explanations

### L1 human

When the potential behaves like a power of distance, motions come in families of the same shape and different sizes.
Knowing one member of the family, the size, the duration and the energy of every other member follow from simple powers of the scale factor.
