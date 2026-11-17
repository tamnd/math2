---
tag: DXKWBFWCE0
kind: statement
role: theorem
name: Comparison of Cantor normal forms
msc: ["03E10", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
uses: [0YSCSX5YZC, KAEDCQ8RM6, 6GD30FGYDZ]
about: [6GD30FGYDZ, KT50SMH3EC]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_arithmetic
    locator: Cantor normal form
---

## Statement

All [[ordinals|0YSCSX5YZC]] and operations below are those of [[ordinal arithmetic|KAEDCQ8RM6]].
A *normal form* is a finite sum
$$\omega^{\beta_1} \cdot c_1 + \omega^{\beta_2} \cdot c_2 + \cdots + \omega^{\beta_k} \cdot c_k$$
with $k \ge 0$, ordinals $\beta_1 > \beta_2 > \cdots > \beta_k$ and positive integers $c_1, \ldots, c_k$.
The empty sum ($k = 0$) is $0$.
Its *term list* is the finite sequence of pairs $(\beta_1, c_1), \ldots, (\beta_k, c_k)$.
Order pairs by $(\beta, c) \lhd (\beta', c')$ if and only if $\beta < \beta'$, or $\beta = \beta'$ and $c < c'$.

**Theorem.**
Let $\alpha$ and $\alpha'$ be given by normal forms with term lists $(\beta_i, c_i)_{i \le k}$ and $(\beta'_i, c'_i)_{i \le m}$.
Then $\alpha < \alpha'$ if and only if one of the following holds.

1. $k < m$, and $(\beta_i, c_i) = (\beta'_i, c'_i)$ for all $i \le k$.
2. There is an index $j \le \min(k, m)$ such that $(\beta_i, c_i) = (\beta'_i, c'_i)$ for all $i < j$, and $(\beta_j, c_j) \lhd (\beta'_j, c'_j)$.

In words: compare the term lists lexicographically, from the leading term, with $\lhd$ on the terms, and a proper initial segment is smaller.

**Corollary.**
Two normal forms with different term lists name different ordinals.
This is the uniqueness part of the [[Cantor normal form|6GD30FGYDZ]].

A full proof is in [[the proof by leading terms|JYXQF7533K]].

## Remarks

### Why each hypothesis is needed

- Strictly decreasing exponents: the sum $\omega^0 + \omega^1$ has the term list $(0, 1), (1, 1)$, which is lexicographically below the list $(1, 1)$ of $\omega$. But $1 + \omega = \omega$, so the two ordinals are equal.
- Distinct exponents: the lists $(1, 1), (1, 1)$ and $(1, 2)$ differ, but $\omega + \omega = \omega \cdot 2$.
- Positive coefficients: the lists $(1, 0), (0, 1)$ and $(0, 1)$ differ, but $\omega \cdot 0 + 1 = 1$.

### Consequences

- Comparison is an algorithm on notations. Below [[epsilon nought|KT50SMH3EC]], each exponent is again written in normal form, and it is a smaller ordinal. So the comparison of two notations calls itself only on shorter notations, and it ends.
- With a coding of notations by natural numbers, this order is a primitive recursive relation. This is the order along which Gentzen's consistency proof uses [[transfinite induction|0ZHQMQ2C1N]].
- The leading term decides the size up to a bound: a normal form with leading pair $(\beta_1, c_1)$ lies in the interval $[\omega^{\beta_1} c_1, \omega^{\beta_1}(c_1 + 1))$.

### Converse

The theorem is an equivalence, so both directions hold.
The comparison rule fails for sums that are not normal forms, as the examples above show.
So a sum must first be put into normal form, by the rule $\omega^\beta + \omega^\gamma = \omega^\gamma$ for $\beta < \gamma$.

### Generalizations

- The same rule compares natural numbers written in base $b \ge 2$: compare the number of digits, then the digits from the left. Here the number of digits plays the role of the leading exponent.
- Normal forms with the [[Veblen function|JQFAE9S2F4]] are compared by a similar recursive rule, which reaches past $\varepsilon_0$.

## History

Georg Cantor introduced the normal form, with its uniqueness, in his work on transfinite ordinal arithmetic in the 1890s.
The use of the comparison rule as a computable order on notations is the basis of Gentzen's work on arithmetic from 1936 on.

## Explanations

### L1 human

Ordinals below $\varepsilon_0$ can be written as sums like $\omega^2 \cdot 3 + \omega + 4$, with the powers going down.
To see which of two such sums is larger, look at the first terms.
The larger power of $\omega$ wins, whatever comes after it.
If the powers are equal, the larger number of copies wins.
If the first terms are the same, move on to the second terms.
For example, $\omega^2 \cdot 3 + 1000$ is smaller than $\omega^2 \cdot 3 + \omega$, because $\omega$ beats every number.

### L2 human

We compare $\alpha = \omega^{\omega^2} \cdot 2 + \omega^{\omega + 5} \cdot 7 + 3$ with $\alpha' = \omega^{\omega^2} \cdot 2 + \omega^{\omega \cdot 2}$.

1. Both are normal forms: the exponents $\omega^2 > \omega + 5 > 0$ and $\omega^2 > \omega \cdot 2$ decrease.
2. The term lists are $(\omega^2, 2), (\omega + 5, 7), (0, 3)$ and $(\omega^2, 2), (\omega \cdot 2, 1)$.
3. The first pairs are equal, so we go to $j = 2$.
4. We compare the exponents $\omega + 5$ and $\omega \cdot 2$ by the same rule. Their term lists are $(1, 1), (0, 5)$ and $(1, 2)$.
5. The first exponents are equal, and the coefficient $1$ is less than $2$. So $\omega + 5 < \omega \cdot 2$.
6. So $(\omega + 5, 7) \lhd (\omega \cdot 2, 1)$, and the theorem gives $\alpha < \alpha'$.

The coefficient $7$ and the term $3$ play no part, because a smaller exponent loses whatever its coefficient.
The typical use is in a notation system: the order on notations is computed, not looked up.
The trap is to compare sums before they are in normal form: $1 + \omega$ looks larger than $\omega$, but the two are equal.

### L3 human

The ordinal $\omega^\gamma$ is order isomorphic to the set of functions $f : \gamma \to \N$ with finite support, ordered by the value at the largest point where two functions differ.
A normal form below $\omega^\gamma$ is such a function, with $f(\beta_i) = c_i$, and the theorem says that this isomorphism respects the order.
This is the ordinal form of the comparison of polynomials by degree, and it is the base case of every [[ordinal notation system|7MBX59Y7N9]].
Stronger notation systems, such as those built from the Veblen function or from collapsing functions, keep the same pattern.
A normal form theorem gives unique terms, and a recursive comparison rule gives a decidable order.
