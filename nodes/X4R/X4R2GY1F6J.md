---
tag: X4R2GY1F6J
kind: statement
role: theorem
name: Mittag-Leffler's theorem
msc: ["30D30"]
uses: [01ZQQDCERP, 0NSD1TPHR0, 0WPQYW8MTE, 0X3XD2ATB0, 0DG0Z72CQD]
about: [0NSD1TPHR0]
sources:
  - url: https://en.wikipedia.org/wiki/Mittag-Leffler%27s_theorem
same_as:
  wikidata: Q1315949
  wikipedia: Mittag-Leffler's theorem
---

## Statement

Let $U \subseteq \C$ be an [[open set|01ZQQDCERP]], and let $A \subseteq U$ be a set with no accumulation point in $U$.
For each $a \in A$, let
$$p_a(z) = \sum_{k=1}^{N_a} \frac{c_{a,k}}{(z - a)^k}$$
be a nonzero finite sum, with $N_a \ge 1$ and complex coefficients $c_{a,k}$.
Then there is a [[meromorphic function|0NSD1TPHR0]] $f$ on $U$ such that:

1. $f$ is [[holomorphic|0DG0Z72CQD]] on $U \setminus A$;
2. for each $a \in A$, the function $f - p_a$ is holomorphic near $a$.

In particular $f$ has a [[pole|0WPQYW8MTE]] at each $a \in A$ with principal part $p_a$.

## Remarks

For $U = \C$ the proof is explicit.
List $A$ as $a_1, a_2, \dots$ with $\abs{a_n}$ nondecreasing, and subtract from $p_{a_n}$ a Taylor polynomial $q_n$ at $0$ (empty when $a_n = 0$) so that $\abs{p_{a_n} - q_n} \le 2^{-n}$ on the disc $\abs{z} \le \abs{a_n}/2$.
Then $\sum_n (p_{a_n} - q_n)$ converges uniformly on compact sets away from $A$ and gives $f$.
For a general open set, Runge's theorem on rational approximation replaces the Taylor polynomials.
A classical example is
$$\frac{\pi^2}{\sin^2(\pi z)} = \sum_{n \in \Z} \frac{1}{(z - n)^2},$$
where here the plain sum already converges.

## Explanations

### L1 human

The theorem lets one place poles at any points that do not pile up inside the region, with any chosen principal parts.
Summing the principal parts directly may diverge, so each term gets a correction that is holomorphic and does not change the pole.
It is the counterpart for poles of the [[Weierstrass factorization theorem|11VC51YHQJ]], which places zeros.

### L2 human

The function $f$ is not unique: one can add any holomorphic function on $U$.
The theorem gives partial fraction expansions of meromorphic functions, such as $\pi \cot(\pi z) = 1/z + \sum_{n \ne 0} \left(1/(z-n) + 1/n\right)$.
Combined with Weierstrass products, it shows that one can prescribe both the principal parts at $A$ and finitely many Taylor coefficients at other points.
In the language of sheaf cohomology, it says that the first Cousin problem is solvable on every open subset of $\C$; see also [[Runge's theorem|6DG4CTGXJD]].
