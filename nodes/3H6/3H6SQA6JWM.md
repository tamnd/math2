---
tag: 3H6SQA6JWM
kind: statement
role: theorem
name: Removable singularities for harmonic functions
msc: [31B05, 35B60]
uses: [0DEB0JMN0W, T62HHSRHP5, PCZBE7EX01, BSJ8X2XRN9]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Removable_singularity
---

## Statement

Let $n \ge 2$, let $U \subseteq \R^n$ be an open set, let $a \in U$, and let $u$ be [[harmonic|0DEB0JMN0W]] on $U \setminus \set{a}$.
Assume that
$$\lim_{x \to a} \frac{u(x)}{\log(1/\abs{x - a})} = 0 \quad (n = 2), \qquad \lim_{x \to a} \abs{x - a}^{n-2} \, u(x) = 0 \quad (n \ge 3).$$
Then $u$ extends to a harmonic function on $U$.
In particular this holds when $u$ is bounded on a punctured neighbourhood of $a$.

## Remarks

Proof idea for $n \ge 3$ and $a = 0$: take a closed ball $\overline{B}(0, r) \subseteq U$.
Let $h$ be harmonic on $B(0, r)$ and continuous on its closure, with $h = u$ on the sphere, given by the [[Poisson integral formula|PCZBE7EX01]].
For $\varepsilon > 0$, the functions $u - h \mp \varepsilon(\abs{x}^{2-n} - r^{2-n})$ are harmonic on the punctured ball and have the right sign near $0$ and on the outer sphere.
The [[maximum principle|T62HHSRHP5]] on annuli gives $\abs{u - h} \le \varepsilon(\abs{x}^{2-n} - r^{2-n})$, and letting $\varepsilon \to 0$ gives $u = h$ off $0$.
In the plane the same argument works with $\log(r/\abs{x})$.
The growth condition is sharp: the [[fundamental solution of the Laplacian|BSJ8X2XRN9]], $\abs{x}^{2-n}$ for $n \ge 3$ or $\log(1/\abs{x})$ for $n = 2$, is harmonic off $0$ and has no harmonic extension.
Example: $u(x, y) = \frac{x}{x^2 + y^2}$ is harmonic on $\R^2 \setminus \set{0}$, and on the positive $x$-axis it equals $1/x$, which grows faster than $\log(1/x)$.
So the hypothesis fails, and indeed $u$ is unbounded near $0$ and has no harmonic extension.

## Explanations

### L1 human

An isolated bad point of a harmonic function can be repaired, as long as the function does not blow up too fast there.
Bounded is certainly fine: a bounded harmonic function on a punctured ball is really harmonic on the whole ball once one fills in the right value at the centre.

### L2 human

This is the harmonic counterpart of Riemann's theorem on removable singularities of holomorphic functions.
The precise threshold is the growth of the fundamental solution, which is the only kind of singularity a positive harmonic function can have at an isolated point, by Bôcher's theorem.
For larger exceptional sets, bounded harmonic functions extend across closed sets of zero capacity, which shows the role of capacity in describing negligible sets.
