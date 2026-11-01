---
tag: CG17WSS64W
kind: statement
role: theorem
name: Jacobi's four-square theorem
msc: ["11E25", 11F27]
uses: [0C4JS9RF5M, 04J4Z73J5B, 06TK51263Q, 2F5CYQJVAF, GWKN5VG78A, 1H6R856P3C]
about: [04J4Z73J5B]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi%27s_four-square_theorem
same_as:
  wikidata: Q3527095
  wikipedia: Jacobi's four-square theorem
---

## Statement

Let $n \ge 1$ be an integer, and let $r_4(n)$ be the number of quadruples $(a, b, c, d)$ of [[integers|0C4JS9RF5M]] with $a^2 + b^2 + c^2 + d^2 = n$.
Then
$$r_4(n) = 8 \sum_{\substack{d \mid n \\ 4 \nmid d}} d.$$
Let $\sigma$ be the [[sum of divisors|06TK51263Q]], and let $m$ be the largest odd divisor of $n$.
Equivalently, $r_4(n) = 8\sigma(n)$ if $n$ is odd, and $r_4(n) = 24\sigma(m)$ if $n$ is even.

## Remarks

One proof uses the series $\sum_{n \in \Z} q^{n^2}$ with $q = e^{2 \pi i \tau}$, which is $\theta(2\tau)$ for the theta constant $\theta$ of the [[theta function|2F5CYQJVAF]].
Its fourth power is $\sum_{n \ge 0} r_4(n) q^n$.
The function $\theta(2\tau)^4$ is a [[modular form|GWKN5VG78A]] of weight $2$ for the [[congruence subgroup|1H6R856P3C]] $\Gamma_0(4)$.
That space has dimension $2$ and is spanned by Eisenstein series, and comparing two coefficients gives the formula.
Elementary proofs also exist.
Example: $n = 4$ has divisors $1, 2$ not divisible by $4$, so $r_4(4) = 8 \cdot 3 = 24$.
Check: the solutions are the $8$ quadruples with one entry $\pm 2$ and three zeros, and the $16$ quadruples with all entries $\pm 1$.
Since the sum always contains $d = 1$, $r_4(n) \ge 8 > 0$, which gives [[Lagrange's four-square theorem|0KYYSMEVHH]].

## Explanations

### L1 human

Every positive integer is a sum of four squares, and this theorem says exactly in how many ways.
The count is $8$ times the sum of the divisors of $n$ that are not multiples of $4$.
Order and signs count: $1 = 1^2 + 0^2 + 0^2 + 0^2$ gives $8$ representations, one for each position and sign.
It turns an existence result into an exact formula.

### L2 human

The theorem is a model case of how modular forms solve counting problems.
A generating function of a counting problem is shown to be modular, and the finite dimension of the space of modular forms identifies it.
For two squares the same method gives $r_2(n) = 4 \sum_{d \mid n,\, d \text{ odd}} \chi(d)$, where $\chi(d) = (-1)^{(d-1)/2}$.
For larger numbers of squares, cusp forms can appear, and the exact formula then has a cusp form term besides the divisor sums.
