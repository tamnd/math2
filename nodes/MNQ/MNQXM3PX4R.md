---
tag: MNQXM3PX4R
kind: example
name: Rössler attractor
msc: [34C28, 37D45]
instance_of: [0673D85QKZ]
uses: [0G4X36AE0X]
sources:
  - url: https://en.wikipedia.org/wiki/R%C3%B6ssler_attractor
---

## Example

Let $a, b, c$ be real parameters.
The Rössler system is the [[autonomous system|0673D85QKZ]] in $\R^3$
$$x' = -y - z, \qquad y' = x + a y, \qquad z' = b + z (x - c).$$
Otto Rössler proposed it in 1976 with $a = b = 0.2$ and $c = 5.7$.
For these values, numerical solutions approach a bounded set with a folded band shape, the Rössler attractor.

The [[equilibrium points|0G4X36AE0X]] are found as follows.
The equation $y' = 0$ gives $x = -a y$, and $x' = 0$ gives $z = -y$.
Then $z' = 0$ becomes $a y^2 + c y + b = 0$.
So for $a \ne 0$ and $c^2 > 4ab$ there are exactly two equilibria, with $y = \left(-c \pm \sqrt{c^2 - 4ab}\right)/(2a)$.

## Remarks

The only nonlinear term is $z x$, so the system is simpler than the Lorenz system, which has two.
In the $(x, y)$-plane, the first two equations give a spiral that moves outward when $0 < a < 2$.
When $x$ exceeds $c$, the variable $z$ grows fast and folds the solution back toward the centre.
This stretching and folding is the mechanism of the chaotic behaviour seen in simulations.

## Explanations

### L1 human

The Rössler system is a three-dimensional flow built to show chaos with as few terms as possible.
A solution spirals outward in a plane, then is lifted up and thrown back to the middle.
Repeating this stretch and fold mixes nearby solutions, like kneading dough.
