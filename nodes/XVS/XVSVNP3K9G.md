---
tag: XVSVNP3K9G
kind: statement
role: theorem
name: Bombieri–De Giorgi–Giusti theorem
msc: [49Q05, 53A10, 35J93]
uses: [NP948D6FR0, 3GV2E2YTZX, Y68BHXZJBV, 41X0YW2R9N, ED3DAZVQZ4]
about: [NP948D6FR0, 3GV2E2YTZX]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%27s_problem
---

## Statement

Write points of $\R^8$ as $(x, y)$ with $x, y \in \R^4$, and let $E = \set{(x, y) : \abs{x} < \abs{y}}$.

1. The set $E$ minimizes [[perimeter|Y68BHXZJBV]] in $\R^8$: $P(E, B) \le P(F, B)$ for every open ball $B$ and every measurable $F$ with $F \setminus B = E \setminus B$.
2. The [[Simons cone|ED3DAZVQZ4]] $\partial E = \set{\abs{x} = \abs{y}}$ is therefore an area-minimizing hypersurface with a singular point at the origin.
3. There is a smooth function $u \colon \R^8 \to \R$ that is not affine and solves the [[minimal surface equation|3GV2E2YTZX]]
$$\operatorname{div} \left( \frac{\nabla u}{\sqrt{1 + \abs{\nabla u}^2}} \right) = 0$$
on all of $\R^8$.

## Remarks

Enrico Bombieri, Ennio De Giorgi and Enrico Giusti proved these results in 1969.
For parts 1 and 2 they compared $E$ with a family of smooth minimal hypersurfaces that fill each side of the cone.
Such a family forces any competitor to have at least as much perimeter.
For part 3 they built a subsolution and a supersolution of the minimal surface equation, and found an entire solution between them.
At infinity both behave like a homogeneous function that vanishes on the Simons cone.
The function $u$ of part 3 gives, for every $m \ge 8$, a non-affine solution on $\R^m$ that does not depend on the last $m - 8$ variables.
So the answer to [[Bernstein's problem|NP948D6FR0]] is negative in all dimensions $m \ge 8$, while Simons had shown it is positive for $m \le 7$.
Part 2 shows that the bound $n - 8$ on the dimension of the singular set of area-minimizing hypersurfaces in $\R^n$ is sharp.

## Explanations

### L1 human

A minimal graph is a soap-film-like surface that lies over the whole of a flat space as the graph of a function.
In low dimensions such a graph must be flat.
This theorem shows that in eight dimensions there are curved minimal graphs.
It also shows that least-area surfaces in eight dimensions can have a sharp point, the tip of the Simons cone.

### L2 human

The minimizing cone and the minimal graph are linked through a blow-down argument.
If a non-affine entire minimal graph exists over $\R^m$, a blow-down argument of Fleming and De Giorgi produces a non-flat area-minimizing cone in $\R^m$.
Simons showed that there is no such cone in $\R^m$ for $m \le 7$, which gives Bernstein's theorem for $m \le 7$.
The theorem shows that this obstruction disappears in $\R^8$, and constructs the corresponding graph.
It is a standard example of how the regularity theory of minimal surfaces and the Liouville-type theorems for the minimal surface equation depend on the dimension.
