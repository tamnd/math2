---
tag: A2KSJSQSF6
kind: example
name: Patterns that eventually fail
msc: ["00A35", "11A41", "42A38"]
topics: [DME0TPC348]
audience: ug2
instance_of: [8AFXPXCE3N]
uses: [8AFXPXCE3N, H75AB4EJT5, VDZY463EKP, M225KZAV4F, P1T98BECWR]
sources:
  - url: https://en.wikipedia.org/wiki/Borwein_integral
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Moser%27s_circle_problem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Fermat_number
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Formula_for_primes
    locator: lead section
---

## Example

Four patterns hold in their first cases and then fail.
Each one is an instance of the [[strong law of small numbers|8AFXPXCE3N]].

1. A polynomial. $f(n) = n^2 + n + 41$ is prime for $n = 0, 1, \ldots, 39$. Then $f(40) = 1681 = 41^2$. The full story is on the page [[forty prime values of n^2 + n + 41|H75AB4EJT5]].
2. Fermat numbers. $F_n = 2^{2^n} + 1$ gives the primes $3, 5, 17, 257, 65537$ for $n = 0, \ldots, 4$. Then $F_5 = 4294967297 = 641 \cdot 6700417$; see [[Fermat's conjecture on Fermat numbers|VDZY463EKP]].
3. Regions of a circle. Put $n$ points on a circle, in general position, and draw all chords between them. The numbers of regions for $n = 1, \ldots, 6$ are $1, 2, 4, 8, 16, 31$. The exact count is $\binom{n}{4} + \binom{n}{2} + 1$; see [[Moser's circle problem|M225KZAV4F]].
4. Integrals. With the [[sinc function|P1T98BECWR]] $\operatorname{sinc} x = \sin x / x$, the integral $I_m = \displaystyle\int_0^\infty \prod_{k=0}^{m} \operatorname{sinc}\!\left(\frac{x}{2k+1}\right) dx$ equals $\pi/2$ for $m = 0, 1, \ldots, 6$. For $m = 7$, with the last factor $\operatorname{sinc}(x/15)$, the value is $\dfrac{467807924713440738696537864469}{935615849440640907310521750000}\,\pi$. This is less than $\pi/2$ by about $2.31 \cdot 10^{-11}$.

In each case the first values suggest a rule, and a later value breaks it.

## Remarks

Each failure has a mechanism.

1. For $f(n) = n^2 + n + 41$, the value $f(40) = 40 \cdot 41 + 41$ is a multiple of $41$, and so is $f(41)$.
2. For Fermat numbers, a prime factor of $F_n$ with $n \geq 2$ has the form $k \cdot 2^{n+2} + 1$. For $n = 5$ the primes of this form are $257, 641, \ldots$, and $641$ divides $F_5$. Nothing in the first five cases forces the later ones to be prime.
3. For the circle, $\binom{n}{4} + \binom{n}{2} + 1 = \sum_{k=0}^{4} \binom{n-1}{k}$, which equals $2^{n-1}$ only while $n - 1 \leq 4$.
4. For the integrals, David and Jonathan Borwein showed in 2001 that $I_m = \pi/2$ exactly while $\frac13 + \frac15 + \cdots + \frac{1}{2m+1} < 1$. The sum up to $\frac1{13}$ is $0.955\ldots$, and adding $\frac1{15}$ gives $1.021\ldots$.

The Borwein integrals also illustrate Guy's second law: a computer that computes $I_7$ with $10$ correct digits reports $\pi/2$.
So a numerical test of a pattern needs more precision than the size of a possible deviation, as in [[experimental mathematics|BPEPTN0TT9]].

## Explanations

### L1 human

Here are four patterns that look certain and then break.
The formula $n^2 + n + 41$ gives primes forty times and then gives $41 \times 41$.
Points on a circle cut it into $1, 2, 4, 8, 16$ pieces, and then into $31$ pieces, not $32$.
A chain of integrals gives exactly $\pi/2$ seven times and then a number a tiny bit smaller.
The lesson: a pattern in the first cases is a guess, and only a proof makes it safe.

### L2 human

We check the circle count for $n = 6$ points.

1. Each set of $4$ points gives two chords that cross once inside the circle. So there are $\binom64 = 15$ crossing points.
2. There are $\binom62 = 15$ chords.
3. Each chord adds one region plus one region for each crossing on it, which gives the count $1 + \binom62 + \binom64 = 1 + 15 + 15 = 31$.
4. The doubling rule predicts $2^5 = 32$, and the true count is $31$.

The typical use: a formula with a counting proof explains both the early agreement and the later failure.
A trap: the points must be in general position; if three chords meet at one point, the count is smaller.
