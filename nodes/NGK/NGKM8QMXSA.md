---
tag: NGKM8QMXSA
kind: statement
role: theorem
name: Generalized binomial theorem
msc: [05A10]
sources:
  - wikipedia: en:4677@r1376224919
    locator: Binomial theorem, section Generalizations > Generalized binomial theorem
    note: adopted
    mention: wikipedia://en/4677#N93F
    sections: [Statement]
inventory: [DV0VPXYAC7]
---

## Statement

The standard binomial theorem, as discussed above, is concerned with $(x+y)^n$ where the exponent $n$ is a nonnegative integer. The generalized binomial theorem allows for non-integer, negative, or even [[complex|09FTAET5Z4]] exponents, at the expense of replacing the finite sum by an infinite series.

In order to do this, one needs to give meaning to binomial coefficients with an arbitrary upper index, which cannot be done using the usual formula with factorials. However, for an arbitrary number $r$, one can define

$${\binom{r}{k}}=\frac{r(r-1) \cdots (r-k+1)}{k!} =\frac{r^{\underline{k}}}{k!},$$

where the last equation introduces modern notation for the falling factorial. This agrees with the usual definitions when $r$ is a nonnegative integer. Then, if $x$ and $y$ are real numbers with $\lvert x\rvert > \lvert y\rvert$, and $r$ is any complex number, one has

$$\begin{aligned} (x+y)^r & =\sum_{k=0}^\infty {\binom{r}{k}} x^{r-k} y^k \\ &= x^r + r x^{r-1} y + \frac{r(r-1)}{2!} x^{r-2} y^2 + \frac{r(r-1)(r-2)}{3!} x^{r-3} y^3 + \cdots. \end{aligned}$$

When $r$ is a nonnegative integer, the binomial coefficients for $k > r$ are zero, so this equation reduces to the usual binomial theorem, and there are at most $r + 1$ nonzero terms. For other values of $r$, the series has infinitely many nonzero terms.

For example, $r = 1/2$ gives the following series for the square root:

$$\sqrt{1+x} = 1 + \frac{1}{2}x - \frac{1}{8}x^2 + \frac{1}{16}x^3 - \frac{5}{128}x^4 + \frac{7}{256}x^5 - \cdots.$$

With $r = -1$, the generalized binomial series becomes:

$$(1+x)^{-1} = \frac{1}{1+x} = 1 - x + x^2 - x^3 + x^4 - x^5 + \cdots.$$

which is the [[geometric series sum formula|01X5CVV1Q5]] for the convergent case $\lvert x\rvert < 1$, whose common ratio is $-x$.

More generally, with $r = -s$, we have for $\lvert x\rvert < 1$:

$$\frac{1}{(1+x)^s} = \sum_{k=0}^\infty {\binom{-s}{k}} x^k = \sum_{k=0}^\infty {\binom{s+k-1}{k}} (-1)^k x^k.$$

So, for instance, when $s = 1/2$,

$$\frac{1}{\sqrt{1+x}} = 1 - \frac{1}{2}x + \frac{3}{8}x^2 - \frac{5}{16}x^3 + \frac{35}{128}x^4 - \frac{63}{256}x^5 + \cdots.$$

Replacing $x$ with $-x$ yields:

$$\frac{1}{(1-x)^s} = \sum_{k=0}^\infty {\binom{s+k-1}{k}} (-1)^k (-x)^k = \sum_{k=0}^\infty {\binom{s+k-1}{k}} x^k.$$

So, for instance, when $s = 1/2$, we have for $\lvert x\rvert < 1$:

$$\frac{1}{\sqrt{1-x}} = 1 + \frac{1}{2}x + \frac{3}{8}x^2 + \frac{5}{16}x^3 + \frac{35}{128}x^4 + \frac{63}{256}x^5 + \cdots.$$
