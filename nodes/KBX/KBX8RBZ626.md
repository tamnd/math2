---
tag: KBX8RBZ626
kind: statement
role: theorem
name: Isoperimetric inequality
msc: [52A40, 28A75, 51M16]
uses: [2Z2QVWZ262, 0S29Y4ZW0Y, 9B02RPN7XD]
about: [2Z2QVWZ262, 0S29Y4ZW0Y]
sources:
  - url: https://en.wikipedia.org/wiki/Isoperimetric_inequality
same_as:
  wikidata: Q617417
  wikipedia: Isoperimetric inequality
---

## Statement

Let $n \ge 2$, and let $\omega_n$ be the volume of the unit ball of $\R^n$.
Let $\Omega \subseteq \R^n$ be a bounded open set with $C^1$ boundary.
Let $\abs{\Omega}$ be its [[Lebesgue measure|2Z2QVWZ262]] and let $\abs{\partial \Omega}$ be the [[surface area|0S29Y4ZW0Y]] of its boundary.
Then
$$\abs{\partial \Omega}^n \ge n^n \omega_n \abs{\Omega}^{n-1},$$
and equality holds if and only if $\Omega$ is a ball.

## Remarks

The inequality follows from the [[Brunn–Minkowski theorem|9B02RPN7XD]].
Let $B$ be the closed unit ball and $\bar\Omega$ the closure of $\Omega$.
Then $\abs{\bar\Omega + \varepsilon B} \ge (\abs{\Omega}^{1/n} + \varepsilon \omega_n^{1/n})^n$.
For a $C^1$ boundary, $\abs{\partial \Omega}$ is the limit of $(\abs{\bar\Omega + \varepsilon B} - \abs{\Omega}) / \varepsilon$ as $\varepsilon \to 0$, and this limit is at least $n \omega_n^{1/n} \abs{\Omega}^{(n-1)/n}$.
Raising to the power $n$ gives the inequality; the equality case needs a separate argument.
For $n = 2$ it reads $L^2 \ge 4 \pi A$ for a region of area $A$ bounded by curves of total length $L$.
Example: a square of side $1$ has $L = 4$ and $A = 1$, and indeed $16 \ge 4\pi$.

## Explanations

### L1 human

Among all shapes with a given volume, the ball has the smallest surface.
Equivalently, among all shapes with a given surface area, the ball holds the most volume.
This is why soap bubbles are round: surface tension makes the surface as small as possible.

### L2 human

The inequality has a version for sets of finite perimeter, which is the natural setting in geometric measure theory.
It is equivalent to the sharp Sobolev inequality $\norm{u}_{n/(n-1)} \le C_n \norm{\nabla u}_1$ for smooth compactly supported $u$, through the coarea formula.
In the plane it is often proved with Fourier series or by Steiner symmetrisation.
