---
tag: 3PGXH0T1K6
kind: statement
role: theorem
name: Lyusternik's theorem on tangent spaces
msc: [49K27, 46G05, 58C20]
uses: [06GZ956657, 06EH97V2A7, 0S23E6YE83, 03YEM7JEDN]
about: [06EH97V2A7]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_multipliers_on_Banach_spaces
---

## Statement

Let $X$ and $Y$ be real [[Banach spaces|06GZ956657]], let $U \subseteq X$ be open, and let $g \colon U \to Y$ be continuously [[Fréchet differentiable|06EH97V2A7]].
Let $x_0 \in U$ with $g(x_0) = 0$, and suppose that the derivative $Dg(x_0) \colon X \to Y$ is surjective.
Let $M = \set{x \in U : g(x) = 0}$.
Then for every $h$ in the [[kernel|0S23E6YE83]] of $Dg(x_0)$ there are $\varepsilon > 0$ and a map $r \colon (-\varepsilon, \varepsilon) \to X$ with
$$\lim_{t \to 0} \frac{\norm{r(t)}}{\abs{t}} = 0 \quad \text{and} \quad x_0 + t h + r(t) \in M \text{ for all } \abs{t} < \varepsilon.$$
Consequently, the set of tangent vectors to $M$ at $x_0$ is exactly $\ker Dg(x_0)$.

## Remarks

The converse inclusion is easy: if $x_0 + th + r(t) \in M$ with $r(t) = o(t)$, then differentiating $g(x_0 + th + r(t)) = 0$ at $t = 0$ gives $Dg(x_0) h = 0$.
The main inclusion is proved by a Newton-type iteration that corrects $x_0 + th$ back onto $M$.
The [[open mapping theorem|03YEM7JEDN]] gives a constant $C$ such that each $v \in Y$ equals $Dg(x_0) w$ for some $w$ with $\norm{w} \le C \norm{v}$, and this makes the corrections converge.
When $\ker Dg(x_0)$ has a closed complement, for example when $X$ is a Hilbert space, the result also follows from the implicit function theorem.

Surjectivity cannot be dropped.
For $g \colon \R^2 \to \R$, $g(x_1, x_2) = x_1^2 + x_2^2$, one has $M = \set{0}$ and $Dg(0) = 0$, so $\ker Dg(0) = \R^2$, while the only tangent vector to the single point $M$ is $0$.

## Explanations

### L1 human

The zero set of a nice map looks, near a regular point, like a flat space: the kernel of the derivative.
The theorem says that each direction in this kernel is really followed by a curve inside the zero set, up to an error that is small compared with the step.
It works in infinite dimensions, where no coordinates are available.

### L2 human

This is the key step in the proof of [[Lagrange multipliers on Banach spaces|Q7QK3PF806]].
In the calculus of variations, $X$ is a function space and $g$ encodes constraints such as a fixed integral, so the theorem describes the admissible variations of a constrained problem.
The condition that $Dg(x_0)$ is onto plays the role of the constraint qualification.
