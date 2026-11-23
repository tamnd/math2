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

The theorem says that two ordinals in Cantor normal form are compared like two words in a dictionary: the first term where they differ decides.

All [[ordinals|0YSCSX5YZC]] and operations below are those of [[ordinal arithmetic|KAEDCQ8RM6]].
A *normal form* is a finite sum

$$\omega^{\beta_1} \cdot c_1 + \omega^{\beta_2} \cdot c_2 + \cdots + \omega^{\beta_k} \cdot c_k$$

with $k \ge 0$, ordinals $\beta_1 > \beta_2 > \cdots > \beta_k$ and positive integers $c_1, \ldots, c_k$; the empty sum is $0$.
Its *term list* is the sequence of pairs $(\beta_1, c_1), \ldots, (\beta_k, c_k)$.
Order pairs by $(\beta, c) \lhd (\beta', c')$ if $\beta < \beta'$, or if $\beta = \beta'$ and $c < c'$.

**Theorem.**
Let $\alpha$ and $\alpha'$ be given by normal forms with term lists $(\beta_i, c_i)_{i \le k}$ and $(\beta'_i, c'_i)_{i \le m}$.
Then $\alpha < \alpha'$ if and only if one of the following holds.

1. $k < m$, and $(\beta_i, c_i) = (\beta'_i, c'_i)$ for all $i \le k$.
2. There is an index $j \le \min(k, m)$ with $(\beta_i, c_i) = (\beta'_i, c'_i)$ for all $i < j$ and $(\beta_j, c_j) \lhd (\beta'_j, c'_j)$.

**Corollary.**
Two normal forms with different term lists name different ordinals; this is the uniqueness part of the [[Cantor normal form|6GD30FGYDZ]].
The [[proof by leading terms|JYXQF7533K]] proves both.

## Remarks

### A first comparison

Which is larger, $\omega^2 + \omega \cdot 3 + 1$ or $\omega^\omega$?
Both are normal forms, with term lists $(2, 1), (1, 3), (0, 1)$ and $(\omega, 1)$.
The leading exponents are $2$ and $\omega$, and $2 < \omega$, so condition 2 holds with $j = 1$:

$$\omega^2 + \omega \cdot 3 + 1 < \omega^\omega.$$

Check: the left side is below $\omega^3$, because $\omega^2 + \omega \cdot 3 + 1 < \omega^2 \cdot 2 \le \omega^3$, and $\omega^3 < \omega^\omega$.
The tail $\omega \cdot 3 + 1$ played no part, since a smaller leading exponent loses whatever follows it.

### Why each hypothesis is needed

The exponents must decrease.
The sum $\omega^0 + \omega^1$ has the list $(0, 1), (1, 1)$, which is lexicographically below the list $(1, 1)$ of $\omega$.
But $1 + \omega = \omega$, so the two ordinals are equal and the rule gives the wrong answer.

The exponents must be distinct.
The lists $(1, 1), (1, 1)$ and $(1, 2)$ differ, yet $\omega + \omega = \omega \cdot 2$.

The coefficients must be positive.
The lists $(1, 0), (0, 1)$ and $(0, 1)$ differ, yet $\omega \cdot 0 + 1 = 1$.

### Watch out: order of the factors

Ordinal arithmetic is not commutative, and the rule only works after a sum is put into normal form.
For example, $1 + \omega = \omega$ but $\omega + 1 > \omega$, and $2 \cdot \omega = \omega$ but $\omega \cdot 2 = \omega + \omega > \omega$.
A small term on the left is absorbed by a larger power after it, by the rule $\omega^\beta + \omega^\gamma = \omega^\gamma$ for $\beta < \gamma$.
So first rewrite $\omega^0 + \omega^1 + \omega^1$ as $\omega \cdot 2$, and only then compare.

### What it gives you

Comparison becomes an algorithm on notations.
Below [[epsilon nought|KT50SMH3EC]] each exponent is again written in normal form, and it is a smaller ordinal, so the comparison calls itself only on shorter notations and ends.
With a coding by natural numbers, the order is a primitive recursive relation, and Gentzen's consistency proof uses [[transfinite induction|0ZHQMQ2C1N]] along it.
The leading term also locates the size: a normal form with leading pair $(\beta_1, c_1)$ lies in the interval $[\omega^{\beta_1} c_1, \omega^{\beta_1}(c_1 + 1))$.

### The converse and generalizations

The theorem is an equivalence, so both directions hold, but only for normal forms.
The same rule compares natural numbers in base $b \ge 2$: compare the number of digits, then the digits from the left.
Normal forms built with the [[Veblen function|JQFAE9S2F4]] are compared by a similar recursive rule, which reaches past $\varepsilon_0$.

### Try it

Compare $\omega^\omega \cdot 2 + \omega^5$ with $\omega^\omega \cdot 3$.
The leading exponents are both $\omega$, and the coefficients are $2 < 3$, so the first is smaller.

Is $\omega + \omega^2$ larger than $\omega^2$?
No: $\omega + \omega^2 = \omega^2$, since $\omega^1 + \omega^2 = \omega^2$; it is not a normal form until rewritten.

## History

Cantor introduced the normal form, with its uniqueness, in his work on transfinite ordinal arithmetic in the 1890s.
Gentzen's work on arithmetic from 1936 on uses the comparison rule as a computable order on notations.

## Explanations

### L1 human

Ordinals below $\varepsilon_0$ can be written as sums like $\omega^2 \cdot 3 + \omega + 4$, with the powers going down.
To see which of two such sums is larger, look at the first terms.
The larger power of $\omega$ wins, whatever comes after it.
If the powers are equal, the larger number of copies wins, and if the first terms agree, move on to the second terms.
For example, $\omega^2 \cdot 3 + 1000$ is smaller than $\omega^2 \cdot 3 + \omega$, because $\omega$ beats every number.

### L2 human

Compare $\alpha = \omega^{\omega^2} \cdot 2 + \omega^{\omega + 5} \cdot 7 + 3$ with $\alpha' = \omega^{\omega^2} \cdot 2 + \omega^{\omega \cdot 2}$.
Both are normal forms, since $\omega^2 > \omega + 5 > 0$ and $\omega^2 > \omega \cdot 2$.
The term lists are $(\omega^2, 2), (\omega + 5, 7), (0, 3)$ and $(\omega^2, 2), (\omega \cdot 2, 1)$.
The first pairs agree, so we look at $j = 2$ and compare the exponents $\omega + 5$ and $\omega \cdot 2$ by the same rule.
Their lists are $(1, 1), (0, 5)$ and $(1, 2)$, and the first pairs differ in the coefficient, $1 < 2$, so $\omega + 5 < \omega \cdot 2$.
So $(\omega + 5, 7) \lhd (\omega \cdot 2, 1)$, and the theorem gives $\alpha < \alpha'$.
This is the typical use: in a notation system the order is computed by recursion, not looked up.

### L3 human

The ordinal $\omega^\gamma$ is order isomorphic to the set of functions $f : \gamma \to \mathbb{N}$ with finite support, ordered by the value at the largest point where two functions differ.
A normal form below $\omega^\gamma$ is such a function, with $f(\beta_i) = c_i$, and the theorem says that this correspondence respects the order.
This is the ordinal form of comparing polynomials by degree, and it is the base case of every [[ordinal notation system|7MBX59Y7N9]].
Stronger systems, built from the Veblen function or from collapsing functions, keep the pattern: a normal form theorem gives unique terms, and a recursive rule gives a decidable order.
