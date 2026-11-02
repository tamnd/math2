---
tag: QC4TP5D6HE
kind: statement
role: theorem
name: Dixon's identity
msc: [33C20, 05A19]
uses: [VDBAW9PN88, 0H5SYBSED9, 0GBZM0MT0F]
about: [VDBAW9PN88]
sources:
  - url: https://en.wikipedia.org/wiki/Dixon%27s_identity
same_as:
  wikidata: Q5284938
  wikipedia: Dixon's identity
---

## Statement

1. For every nonnegative integer $a$, the [[binomial coefficients|0GBZM0MT0F]] satisfy
$$\sum_{k = -a}^{a} (-1)^k \binom{2a}{a + k}^3 = \frac{(3a)!}{(a!)^3}.$$
2. For nonnegative integers $a, b, c$, with $k$ running over all integers and $\binom{n}{j}$ read as $0$ for $j < 0$ or $j > n$,
$$\sum_{k} (-1)^k \binom{a + b}{a + k} \binom{b + c}{b + k} \binom{c + a}{c + k} = \frac{(a + b + c)!}{a!\, b!\, c!}.$$
3. Let $a, b, c$ be complex numbers such that $1 + a - b$, $1 + a - c$ and $1 + \frac{a}{2}$ are not in $\set{0, -1, -2, \dots}$ and $\operatorname{Re}\left( \frac{a}{2} - b - c \right) > -1$.
Then, with $\Gamma$ the [[gamma function|0H5SYBSED9]] and ${}_3F_2$ the [[generalized hypergeometric series|VDBAW9PN88]],
$${}_3F_2\left( \begin{matrix} a,\ b,\ c \\ 1 + a - b,\ 1 + a - c \end{matrix} ; 1 \right) = \frac{\Gamma(1 + \frac{a}{2})\, \Gamma(1 + a - b)\, \Gamma(1 + a - c)\, \Gamma(1 + \frac{a}{2} - b - c)}{\Gamma(1 + a)\, \Gamma(1 + \frac{a}{2} - b)\, \Gamma(1 + \frac{a}{2} - c)\, \Gamma(1 + a - b - c)}.$$

## Remarks

Part 1 is the case $a = b = c$ of part 2.
The ${}_3F_2$ in part 3 is *well-poised*: each upper parameter plus the matching lower parameter gives $1 + a$.
Part 3 is the case $d = \frac{a}{2}$ of the summation of a well-poised ${}_5F_4$.
That series has upper parameters $a, 1 + \frac{a}{2}, b, c, d$ and lower parameters $\frac{a}{2}, 1 + a - b, 1 + a - c, 1 + a - d$.
For $d = \frac{a}{2}$, two upper and two lower parameters cancel.
The condition on $\operatorname{Re}\left( \frac{a}{2} - b - c \right)$ is exactly the condition for the series at $1$ to converge.
For $a = 1$ in part 1, the sum is $-1 + 8 - 1 = 6 = 3!/(1!)^3$.

## Explanations

### L1 human

Take row $2a$ of Pascal's triangle, cube each entry, and add the cubes with alternating signs.
Dixon's identity says the result is the multinomial coefficient $\frac{(3a)!}{(a!)^3}$, the number of ways to split $3a$ objects into three groups of $a$.
For $a = 1$ the row is $1, 2, 1$, and $-1 + 8 - 1 = 6$.

### L2 human

The binomial forms are the terminating cases of the hypergeometric form in part 3.
Part 3 is one of the classical closed-form evaluations of ${}_3F_2(1)$, next to the Pfaff–Saalschütz theorem for balanced series and Watson's and Whipple's sums.
Dixon's identity also has a short proof by the Wilf–Zeilberger method of certificate proofs.
