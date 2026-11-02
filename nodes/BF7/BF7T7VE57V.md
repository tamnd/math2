---
tag: BF7T7VE57V
kind: statement
role: theorem
name: Hardy–Littlewood maximal inequality
msc: [42B25]
uses: [VX1A56P5KQ, SASP14MA1Z, 2Z2QVWZ262, 9534R6VMY0, FCA0J1X07K, R1PHMVBJ9J]
about: [VX1A56P5KQ]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_maximal_function
---

## Statement

Let $n \ge 1$ and let $\abs{E}$ be the [[Lebesgue measure|2Z2QVWZ262]] of a set $E \subseteq \R^n$.
For a locally integrable function $f$ on $\R^n$, let $Mf$ be its [[Hardy–Littlewood maximal function|VX1A56P5KQ]].

1. For every $f \in L^1(\R^n)$ and every $\lambda > 0$,
$$\abs{\set{x \in \R^n : Mf(x) > \lambda}} \le \frac{3^n}{\lambda} \norm{f}_{L^1}.$$
2. For every $p$ with $1 < p \le \infty$ there is a constant $C = C(n, p)$ such that $\norm{Mf}_{L^p} \le C \norm{f}_{L^p}$ for every $f \in L^p(\R^n)$.

Here $L^p(\R^n)$ is the [[Lp space|SASP14MA1Z]] of Lebesgue measure.

## Remarks

Part 1 says that $M$ is of [[weak type|9534R6VMY0]] $(1, 1)$.
Its proof uses the [[Vitali covering lemma|FCA0J1X07K]].
Each point of a compact subset $K$ of $\set{Mf > \lambda}$ is the centre of a ball $B$ with $\int_B \abs{f} > \lambda \abs{B}$.
The covering lemma selects finitely many disjoint such balls $B_1, \dots, B_m$ whose dilates $3B_k$ cover $K$, so $\abs{K} \le 3^n \sum_k \abs{B_k} \le 3^n \lambda^{-1} \norm{f}_1$.
For $p = \infty$, part 2 is the trivial bound $Mf \le \norm{f}_\infty$, and for $1 < p < \infty$ it follows from part 1 by the [[Marcinkiewicz interpolation theorem|R1PHMVBJ9J]].

The constant in part 2 grows like $1/(p - 1)$ as $p \to 1$, and part 2 fails for $p = 1$.
For example, $f = \mathbf{1}_{[0, 1]}$ on $\R$ has $Mf(x) = 1/(2x)$ for $x > 1$, which is not integrable.
In fact $Mf$ is integrable only when $f = 0$ almost everywhere.

## Explanations

### L1 human

The maximal function records, at each point, the largest average of $\abs{f}$ over balls centred there.
One might fear that taking the largest of infinitely many averages makes the function huge.
The theorem says that this does not happen.
For $p > 1$, the $L^p$ norm of $Mf$ is at most a constant times that of $f$.
For $p = 1$, a weaker bound holds on the size of the sets where $Mf$ is large.

### L2 human

The inequality is the main tool for proving that averages converge almost everywhere.
Combined with density of continuous functions it gives the Lebesgue differentiation theorem: the averages of $f$ over balls shrinking to $x$ tend to $f(x)$ for almost every $x$.
Many operators in harmonic analysis, such as convolutions with radially decreasing integrable kernels, are bounded pointwise by a multiple of $Mf$, so they inherit its $L^p$ bounds.
The weighted version of the inequality leads to the Muckenhoupt $A_p$ condition.
