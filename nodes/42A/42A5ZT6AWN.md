---
tag: 42A5ZT6AWN
kind: statement
role: theorem
name: Riemann–Hurwitz formula
msc: [14H30, 30F10]
uses: [5K0N8QMV6Q, NJ787GZS1N, YARENZRXTD, RNDDWDAFJ5]
about: [YARENZRXTD, NJ787GZS1N]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Hurwitz_formula
same_as:
  wikidata: Q494995
  wikipedia: Riemann–Hurwitz formula
---

## Statement

Let $X$ and $Y$ be compact connected [[Riemann surfaces|5K0N8QMV6Q]] of [[genus|NJ787GZS1N]] $g_X$ and $g_Y$.
Let $f \colon X \to Y$ be a nonconstant holomorphic map of degree $n$.
For $P \in X$, let $e_P \ge 1$ be the ramification index of $f$ at $P$, so that near $P$ the map looks like $z \mapsto z^{e_P}$ in local coordinates.
Then $e_P = 1$ for all but finitely many $P$, and
$$2 g_X - 2 = n\,(2 g_Y - 2) + \sum_{P \in X} (e_P - 1).$$

## Remarks

Triangulate $Y$ so that every branch value is a vertex, and lift the triangulation to $X$ along the [[branched covering|YARENZRXTD]] $f$.
Each edge and face has exactly $n$ preimages, and a vertex $y$ has $n - \sum_{f(P) = y} (e_P - 1)$ preimages.
Comparing [[Euler characteristics|RNDDWDAFJ5]] with $\chi = 2 - 2g$ gives the formula.
The same formula holds for a finite separable morphism of smooth projective curves over an algebraically closed field when every $e_P$ is prime to the characteristic.
With wild ramification the term $e_P - 1$ must be replaced by a larger number.
Example: the map $z \mapsto z^n$ on the Riemann sphere has degree $n$ and ramifies only at $0$ and $\infty$ with $e = n$; the formula reads $-2 = n(-2) + 2(n - 1)$, which is true.
Example: a double cover $X \to \mathbb{P}^1$ branched at $2g + 2$ points has $2 g_X - 2 = -4 + 2g + 2$, so $g_X = g$; this is how the genus of a hyperelliptic curve is found.

## Explanations

### L1 human

A map between surfaces that wraps one surface $n$ times around another almost everywhere, except at finitely many branch points, links the numbers of holes of the two surfaces.
Without branch points, the Euler characteristic simply multiplies by $n$.
Each branch point, where several sheets come together, makes a correction.
The formula records this exactly.

### L2 human

The formula is the main tool to compute genera of curves given as covers, such as hyperelliptic curves, Fermat curves and modular curves.
It shows at once that there is no nonconstant map from a curve of genus $g$ to a curve of larger genus.
It also shows that an unramified cover of a genus-$1$ curve has genus $1$.
Applied to the quotient map by a group of automorphisms, it gives [[Hurwitz's automorphisms theorem|3GNKSCQSCD]].
It is the one-dimensional case of the comparison of canonical divisors $K_X = f^* K_Y + R$, where $R$ is the ramification divisor.
