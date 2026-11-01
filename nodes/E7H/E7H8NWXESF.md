---
tag: E7H8NWXESF
kind: statement
role: theorem
name: Roth's theorem on arithmetic progressions
msc: [11B25, 11B30, 05D10]
uses: [0T3RZQXDYD]
about: [B23B0QEMN5]
sources:
  - url: https://en.wikipedia.org/wiki/Roth%27s_theorem_on_arithmetic_progressions
same_as:
  wikidata: Q56313802
  wikipedia: Roth's theorem on arithmetic progressions
---

## Statement

Let $A$ be a set of positive integers with
$$\limsup_{N \to \infty} \frac{\abs{A \cap \set{1, \dots, N}}}{N} > 0,$$
where $\limsup$ is the [[limit superior|0T3RZQXDYD]].
Then $A$ contains three terms $a, a + d, a + 2d$ of an arithmetic progression with $d \ge 1$.

## Remarks

Let $r_3(N)$ be the largest size of a subset of $\set{1, \dots, N}$ with no three-term arithmetic progression.
The theorem is equivalent to $r_3(N) / N \to 0$ as $N \to \infty$.
Roth's proof uses Fourier analysis and a density increment.
A set without three-term progressions has a large Fourier coefficient, so it is denser on some long sub-progression.
This step cannot repeat forever, because the density cannot exceed $1$.
Another proof goes through the [[triangle removal lemma|XMS1QRAQZC]].
Behrend constructed sets showing $r_3(N) \ge N \exp(-c\sqrt{\log N})$ for a constant $c > 0$, so $r_3(N)$ is not bounded by $N^{1 - \varepsilon}$ for any $\varepsilon > 0$.
Kelley and Meka proved in 2023 an upper bound of the form $r_3(N) \le N \exp(-c (\log N)^{\beta})$ with constants $c, \beta > 0$.
The analogue in $\F_3^n$ is the [[cap set problem|1SF8Y9M8YB]].

## Explanations

### L1 human

Take any set of whole numbers that fills a fixed positive fraction of the numbers.
Then it contains three numbers equally spaced, like $5, 9, 13$.
The odd numbers, for example, contain $1, 3, 5$.

### L2 human

Roth's theorem is the case $k = 3$ of [[Szemerédi's theorem|B23B0QEMN5]], and it was proved first.
Its Fourier-analytic density-increment argument is a model for many proofs in [[additive combinatorics|3NM362A2JG]].
The gap between Behrend's lower bound and the best upper bounds for $r_3(N)$ is still being studied.
