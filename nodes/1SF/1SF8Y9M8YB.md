---
tag: 1SF8Y9M8YB
kind: statement
role: theorem
name: Cap set problem
msc: [05D40, 11B25, 05B25]
uses: [0ZXZ82FTX2, 000AYPA9AJ, 0TGV80E6A4]
about: [DMYGZ3YZ6V]
sources:
  - url: https://en.wikipedia.org/wiki/Cap_set
---

## Statement

Let $n \ge 1$ and let $\F_3^n$ be the [[vector space|000AYPA9AJ]] of dimension $n$ over the [[field|0ZXZ82FTX2]] $\F_3$ with three elements.
A *cap set* is a set $A \subseteq \F_3^n$ that contains no three distinct elements $x, y, z$ with $x + y + z = 0$, that is, no three distinct points on a line.
Let $m_n$ be the number of monomials $x_1^{e_1} \cdots x_n^{e_n}$ with each $e_i \in \set{0, 1, 2}$ and $e_1 + \cdots + e_n \le 2n/3$.
Then every cap set $A \subseteq \F_3^n$ satisfies $|A| \le 3 m_n$.
In particular $|A| = o(2.756^n)$ as $n \to \infty$, in the sense of [[asymptotic notation|0TGV80E6A4]].

## Remarks

This bound is due to Ellenberg and Gijswijt, following a method of Croot, Lev and Pach for $(\Z/4\Z)^n$.
The proof is an instance of the [[linear algebra method|DMYGZ3YZ6V]].
The function $T(x, y, z) = 1$ if $x + y + z = 0$ and $0$ otherwise, restricted to $A \times A \times A$, is diagonal with $|A|$ nonzero entries, so its slice rank is $|A|$.
Writing $T(x, y, z) = \prod_{i} \left(1 - (x_i + y_i + z_i)^2\right)$ and expanding, each monomial has degree at most $2n/3$ in one of the three variables, which gives slice rank at most $3 m_n$.
Earlier bounds, by Fourier methods, were of the form $3^n / n^{1 + c}$.

Example: in $\F_3^2$ the set $\set{(0,0), (0,1), (1,0), (1,1)}$ is a cap set of size $4$.
The sums of its four triples of distinct points are $(1,1)$, $(1,2)$, $(2,1)$ and $(2,2)$, none of which is $0$.
Cap sets of size larger than $2.2^n$ are known for large $n$, so the base of the exponential lies between $2.2$ and $2.756$.

## Explanations

### L1 human

In the card game SET, a cap set is a collection of cards that contains no SET.
The question is how large such a collection can be when cards have $n$ attributes instead of four.
The answer was long known to be a vanishing fraction of all $3^n$ cards, and the 2016 theorem showed it is exponentially smaller: at most about $2.756^n$.

### L2 human

The cap set problem is the analogue in $\F_3^n$ of [[Roth's theorem|E7H8NWXESF]] on three-term arithmetic progressions, since three distinct points $x, y, z$ with $x + y + z = 0$ form an arithmetic progression in $\F_3^n$.
The polynomial proof is very short and gives a power saving, which Fourier methods could not.
It introduced the slice rank of tensors and led to new bounds on related problems, such as sunflower-free families and matrix multiplication barriers.
In the integers, by contrast, there are sets without three-term progressions of size $N^{1 - o(1)}$, so the polynomial method does not transfer directly.
