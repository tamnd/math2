---
tag: RHPQG175AH
kind: statement
role: theorem
name: Graeffe's method
msc: [65H04]
uses: [019MA1VTR2, 09FTAET5Z4]
about: [019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Graeffe%27s_method
same_as:
  wikidata: Q5592179
  wikipedia: Graeffe's method
---

## Statement

Let $p(x) = a \prod_{i=1}^n (x - x_i)$ be a polynomial of degree $n \ge 1$ with [[complex|09FTAET5Z4]] coefficients and [[roots|019MA1VTR2]] $x_1, \dots, x_n$.

1. There is a unique polynomial $q$ with $q(x^2) = (-1)^n p(x) p(-x)$, and $q(y) = a^2 \prod_{i=1}^n (y - x_i^2)$. So the roots of $q$ are the squares of the roots of $p$.
2. Let $p_0 = p$, let $p_{k+1}$ be obtained from $p_k$ as in clause 1, and write $p_k(y) = \sum_{j=0}^n b_j^{(k)} y^j$. Suppose that $\abs{x_1} > \abs{x_2} > \cdots > \abs{x_n} > 0$. Then for each $m = 1, \dots, n$,
$$\abs{x_m} = \lim_{k \to \infty} \abs{\frac{b_{n-m}^{(k)}}{b_{n-m+1}^{(k)}}}^{1/2^k}.$$

## Remarks

Clause 1: $p(-x) = a \prod_i (-x - x_i) = (-1)^n a \prod_i (x + x_i)$, so $(-1)^n p(x) p(-x) = a^2 \prod_i (x^2 - x_i^2)$.
Clause 2: the roots of $p_k$ are $y_i = x_i^{2^k}$, and their moduli separate very fast.
By the relations between roots and coefficients, $b_{n-m}^{(k)} / b_{n-m+1}^{(k)}$ is a ratio of elementary symmetric functions of the $y_i$, and the ratio is dominated by $-y_m$ as $k \to \infty$.
For example, $p(x) = x^2 - 3x + 2$ has roots $2$ and $1$, and one step gives $q(y) = y^2 - 5y + 4$, with roots $4$ and $1$.
The hypothesis of distinct moduli is needed for clause 2.
For $p(x) = x^3 - 1$ the three roots have modulus $1$, but every $p_k$ equals $y^3 - 1$, so $b_2^{(k)} / b_3^{(k)} = 0$ and the formula gives $0$ instead of $1$ for $m = 1$.
The method gives only the moduli of the roots; the signs or arguments need extra work.

## Explanations

### L1 human

Squaring numbers that differ in size makes the gap between them much larger.
Graeffe's method repeatedly replaces a polynomial by one whose roots are the squares of the old roots.
After a few rounds one root dominates each coefficient ratio, and the sizes of the roots can be read off directly from the coefficients.

### L2 human

Each squaring step costs about $n^2$ operations and needs no starting guess.
The coefficients grow or shrink very fast, so a practical version must work with scaled numbers or logarithms.
The squaring step, also called the Dandelin–Graeffe step, reappears in modern root finders, for example to estimate root moduli in the splitting circle method.
