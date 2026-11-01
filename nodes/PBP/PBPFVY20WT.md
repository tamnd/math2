---
tag: PBPFVY20WT
kind: statement
role: theorem
name: Muirhead's inequality
msc: [26D15, "05E05"]
uses: [5K7VT2VKZT, 0BQMWCNS8S]
about: [5K7VT2VKZT]
sources:
  - url: https://en.wikipedia.org/wiki/Muirhead%27s_inequality
same_as:
  wikidata: Q930173
  wikipedia: Muirhead's inequality
---

## Statement

Let $a = (a_1, \dots, a_n)$ and $b = (b_1, \dots, b_n)$ be vectors of nonnegative real numbers.
For $x_1, \dots, x_n > 0$, write
$$[a](x) = \frac{1}{n!} \sum_{\sigma \in S_n} x_{\sigma(1)}^{a_1} x_{\sigma(2)}^{a_2} \cdots x_{\sigma(n)}^{a_n},$$
where $S_n$ is the set of [[permutations|0BQMWCNS8S]] of $\set{1, \dots, n}$.
Then $[b](x) \le [a](x)$ for all $x_1, \dots, x_n > 0$ if and only if $a$ [[majorizes|5K7VT2VKZT]] $b$.

## Remarks

Proof idea: suppose $a$ majorizes $b$.
Then $b$ can be reached from $a$ by finitely many steps, each of which moves two entries closer together while keeping their sum.
For one such step it suffices to compare two variables, where the claim reduces to $x^{s} y^{t} + x^{t} y^{s} \ge x^{s'} y^{t'} + x^{t'} y^{s'}$ for $s + t = s' + t'$ and $\abs{s - t} \ge \abs{s' - t'}$, which follows by factoring.
Conversely, letting all $x_i$ but some tend to $0$ or $\infty$ shows that the partial sum conditions of majorization are needed.

Example: $a = (2, 0)$ majorizes $b = (1, 1)$, which gives $\frac{1}{2}(x^2 + y^2) \ge x y$.
With $a = (n, 0, \dots, 0)$ and $b = (1, 1, \dots, 1)$ one gets $\frac{1}{n}\sum_i x_i^n \ge x_1 x_2 \cdots x_n$, the [[AM–GM inequality|0DRF0F3XC9]] for $x_1^n, \dots, x_n^n$.

## Explanations

### L1 human

Muirhead's inequality compares symmetric sums of monomials in positive numbers.
Each such sum is labelled by its exponent vector.
The sum whose exponents are more spread out is never the smaller one, and this order is exactly majorization.

### L2 human

Muirhead's inequality settles many symmetric polynomial inequalities at once, and it is a standard tool in olympiad problems.
To use it, write both sides as combinations of symmetric sums $[a]$ and check majorization of the exponent vectors.
It does not apply directly when the two sides have different total degree, or when some coefficients are negative; then one combines it with other tools such as [[Schur's inequality|958TMJZ51Y]].
