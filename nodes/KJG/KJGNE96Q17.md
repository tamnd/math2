---
tag: KJGNE96Q17
kind: statement
role: theorem
name: Nash bargaining solution
msc: [91B26, 91A12]
uses: [93STGYCSTS]
about: [93STGYCSTS]
sources:
  - url: https://en.wikipedia.org/wiki/Cooperative_bargaining
    locator: Nash bargaining solution
---

## Statement

Consider rules $f$ that assign to each two-person [[bargaining problem|93STGYCSTS]] $(F, d)$ a point $f(F, d) \in F$.
Say that $f$ satisfies:

1. *Pareto efficiency* if there is no $y \in F$ with $y_1 \ge f_1(F, d)$, $y_2 \ge f_2(F, d)$ and $y \ne f(F, d)$;
2. *symmetry* if $f_1(F, d) = f_2(F, d)$ whenever $d_1 = d_2$ and $F$ is invariant under $(x_1, x_2) \mapsto (x_2, x_1)$;
3. *invariance under affine transformations* if $f(T(F), T(d)) = T(f(F, d))$ for every map $T(x_1, x_2) = (a_1 x_1 + b_1, a_2 x_2 + b_2)$ with $a_1, a_2 > 0$;
4. *independence of irrelevant alternatives* if $f(G, d) = f(F, d)$ whenever $G \subseteq F$ is a bargaining problem with $f(F, d) \in G$.

Then exactly one rule satisfies all four conditions.
It is the *Nash bargaining solution*: $f(F, d)$ is the unique point that maximises the product $(x_1 - d_1)(x_2 - d_2)$ over the points $x \in F$ with $x_1 \ge d_1$ and $x_2 \ge d_2$.

## Remarks

The maximiser is unique because the product is strictly quasiconcave on the region where both factors are positive and $F$ is convex.
One checks directly that this rule satisfies the four conditions.
For uniqueness, apply an affine map so that $d = (0, 0)$ and the maximiser is $(1, 1)$.
Then $F$ lies in the half-plane $x_1 + x_2 \le 2$, whose boundary touches the hyperbola $x_1 x_2 = 1$ at $(1, 1)$.
Enlarge $F$ to a symmetric compact convex set inside this half-plane, where symmetry and efficiency force the answer $(1, 1)$.
Independence of irrelevant alternatives then brings the answer back to $F$.
Example: when two players divide one dollar with disagreement point $d$, the solution gives player $i$ the amount $d_i + (1 - d_1 - d_2)/2$, her fallback plus half of the surplus.

## Explanations

### L1 human

Nash asked what a fair deal between two bargainers should look like, and wrote down four reasonable requirements.
Only one rule meets all of them: choose the deal that maximises the product of the two players' gains over their fallback positions.
When the gains can be shared like money, this means splitting the surplus equally.

### L2 human

The theorem is the founding result of axiomatic bargaining theory.
Dropping symmetry gives the asymmetric solutions that maximise $(x_1 - d_1)^{\alpha} (x_2 - d_2)^{1 - \alpha}$ with $0 < \alpha < 1$.
Replacing independence of irrelevant alternatives by a monotonicity axiom gives the Kalai–Smorodinsky solution instead.
The Rubinstein bargaining model gives a noncooperative foundation: as the players become patient, its equilibrium division tends to the Nash bargaining solution.
