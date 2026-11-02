---
tag: BJ0X0T4SBA
kind: statement
role: theorem
name: Multijet transversality theorem
msc: [57R35, 58A20, 58K30]
uses: [F45VQ47GPV, 1QE0Z0756D, HC3VBBCJQP, 7PN9MD1PQB, A2PDZ8GA9C, VKFW27WXEZ, GRH8MCVN3N, KWNRS3RA09]
about: [A2PDZ8GA9C, HC3VBBCJQP]
sources:
  - url: https://en.wikipedia.org/wiki/Transversality_theorem
---

## Statement

Let $X$ and $Y$ be [[smooth manifolds|F45VQ47GPV]], and let $s \ge 1$ and $k \ge 0$ be integers.
Let $X^{(s)} = \set{(x_1, \dots, x_s) \in X^s : x_i \ne x_j \text{ for } i \ne j}$.
Let $J^k(X, Y)$ be the [[bundle of $k$-jets|HC3VBBCJQP]] of smooth maps from $X$ to $Y$, with source map $\alpha \colon J^k(X, Y) \to X$.
The $s$-fold *multijet bundle* is
$$J^k_s(X, Y) = \set{(\sigma_1, \dots, \sigma_s) \in J^k(X, Y)^s : (\alpha(\sigma_1), \dots, \alpha(\sigma_s)) \in X^{(s)}}.$$
For a smooth map $f \colon X \to Y$, its multijet extension is $j^k_s f \colon X^{(s)} \to J^k_s(X, Y)$, $(x_1, \dots, x_s) \mapsto (j^k f(x_1), \dots, j^k f(x_s))$, where $j^k f(x)$ is the [[$k$-jet|1QE0Z0756D]] of $f$ at $x$.
Let $W$ be a [[submanifold|VKFW27WXEZ]] of $J^k_s(X, Y)$, and give $C^\infty(X, Y)$ the [[Whitney $C^\infty$ topology|7PN9MD1PQB]].
Then the set of $f \in C^\infty(X, Y)$ such that $j^k_s f$ is [[transverse|A2PDZ8GA9C]] to $W$ is a [[residual set|GRH8MCVN3N]] in $C^\infty(X, Y)$.

## Remarks

For $s = 1$ this is the [[Thom transversality theorem|KWNRS3RA09]].
The proof follows the same pattern: one perturbs $f$ near the $s$ distinct points $x_1, \dots, x_s$ independently.
The perturbations are polynomial maps of degree at most $k$, multiplied by bump functions with disjoint supports.
The family of perturbed multijets is a submersion onto the fibres, so the parametric transversality theorem applies, and a countable covering argument gives a residual set.
The points must be distinct, since the jets of $f$ at the same point cannot be perturbed independently.

Example: let $s = 2$, $k = 0$, and let $W = \set{((x_1, y_1), (x_2, y_2)) : y_1 = y_2}$, which has codimension $\dim Y$ in $J^0_2(X, Y) = X^{(2)} \times Y \times Y$.
If $\dim Y > 2 \dim X = \dim X^{(2)}$, transversality to $W$ means that $j^0_2 f$ misses $W$, that is, $f$ is injective.
So injective maps are generic when $\dim Y > 2 \dim X$.
Combined with the genericity of immersions, this gives the easy form of the Whitney embedding theorem for compact $X$.

## Explanations

### L1 human

Thom's theorem says that a generic map behaves well at each single point.
The multijet version says that a generic map also behaves well at several points at once.
For example, two different points are not sent to the same place in a degenerate way.

This controls self-intersections of maps, not only their local shape.

### L2 human

The theorem is the main tool for global properties of generic maps.
It shows that generic immersions have only transverse self-intersections, that is, normal crossings, and it is a basic tool in the theory of stable maps.
