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
Each is an instance of the [[strong law of small numbers|8AFXPXCE3N]], and each failure can be checked by hand or with a short computation.

**A polynomial.**
The values of $f(n) = n^2 + n + 41$ for $n = 0, 1, 2, 3$ are $41, 43, 47, 53$, and all forty values for $n = 0$ to $39$ are prime.
At $n = 40$ the pattern breaks:
$$f(40) = 1600 + 40 + 41 = 1681 = 41^2.$$
[[Forty prime values of n^2 + n + 41 do not prove a statement|H75AB4EJT5]] tells the full story.

**Fermat numbers.**
The numbers $F_n = 2^{2^n} + 1$ for $n = 0$ to $4$ are $3, 5, 17, 257, 65537$, and all five are prime.
Fermat believed that every $F_n$ is prime, and in 1732 Euler found
$$F_5 = 2^{32} + 1 = 4294967297 = 641 \cdot 6700417;$$
see [[Fermat's conjecture on Fermat numbers|VDZY463EKP]].

**Regions of a circle.**
Put $n$ points on a circle, draw all chords between them, and let no three chords meet at one point.
For $n = 1$ to $6$ the numbers of regions are $1, 2, 4, 8, 16, 31$.
The exact count is $\binom{n}{4} + \binom{n}{2} + 1$; see [[Moser's circle problem|M225KZAV4F]].

**Integrals.**
With the [[sinc function|P1T98BECWR]] $\operatorname{sinc} x = \sin x / x$, put
$$I_m = \int_0^\infty \prod_{k=0}^{m} \operatorname{sinc}\!\left(\frac{x}{2k+1}\right) dx.$$
Then $I_m = \pi/2$ for $m = 0$ to $6$, that is, for every product up to the factor $\operatorname{sinc}(x/13)$.
For $m = 7$, with the factor $\operatorname{sinc}(x/15)$, the value is
$$I_7 = \frac{467807924713440738696537864469}{935615849440640907310521750000} \, \pi,$$
which is less than $\pi/2$ by about $2.31 \cdot 10^{-11}$.

## Remarks

### Why each pattern breaks

Each failure has a mechanism, and the mechanism explains both the early run and its end.
For the polynomial, $f(40) = 40 \cdot 41 + 41$ is a multiple of $41$, and so is $f(41) = 41 \cdot 43$.
For Fermat numbers, Euler and Lucas showed that a prime factor of $F_n$ with $n \ge 2$ has the form $k \cdot 2^{n+2} + 1$.
For $n = 5$ the candidates are $129, 257, 385, 513, 641, \ldots$, the first primes among them are $257$ and $641$, and $641$ divides $F_5$.
Nothing in the first five cases forced the later ones to be prime.

For the circle, the count can be rewritten as
$$\binom{n}{4} + \binom{n}{2} + 1 = \sum_{k=0}^{4} \binom{n-1}{k},$$
which equals $2^{n-1}$ only while $n - 1 \le 4$.
For the integrals, David and Jonathan Borwein showed in 2001 that $I_m = \pi/2$ exactly while $\frac13 + \frac15 + \cdots + \frac{1}{2m+1} < 1$.
The sum up to $\frac{1}{13}$ is $0.955\ldots$, and adding $\frac{1}{15}$ gives $1.021\ldots$.

### What the four cases show

A pattern that holds in many cases is not a proof, even when the cases number forty.
The Borwein integrals also show Guy's second law: a computation of $I_7$ correct to $10$ digits reports $\pi/2$.
So a numerical test needs more precision than the size of a possible deviation, as in [[experimental mathematics|BPEPTN0TT9]].
The same lesson at a much larger scale is in [[numerical evidence for conjectures|JFD3QWCX8Z]], where the Pólya conjecture fails first at $906150257$.

### Watch out

In the circle problem the points must be in general position.
For $n = 6$ points at the corners of a regular hexagon, the three long diagonals meet at the center, and the count drops from $31$ to $30$.
So a failure of a pattern can also come from a hidden hypothesis, not only from a wrong formula.

### Try it

Find a value of $n$ other than $40$ and $41$ where $n^2 + n + 41$ is divisible by $41$.
Any multiple of $41$ works, for example $n = 82$, since then every term is a multiple of $41$.

Is $\frac13 + \frac15 + \frac17$ less than $1$, and what does that say about $I_3$?
The sum is $0.676\ldots$, so $I_3 = \pi/2$ exactly by the Borwein criterion.

## Explanations

### L1 human

Here are four patterns that look certain and then break.
The formula $n^2 + n + 41$ gives primes forty times and then gives $41 \times 41$.
Points on a circle cut it into $1, 2, 4, 8, 16$ pieces, and then into $31$ pieces, not $32$.
A chain of integrals gives exactly $\pi/2$ seven times and then a number a tiny bit smaller.
A pattern in the first cases is a guess, and only a proof makes it safe.

### L2 human

We check the circle count for $n = 6$ points.
Each set of $4$ points gives two chords that cross once inside the circle, so there are $\binom{6}{4} = 15$ crossing points.
There are $\binom{6}{2} = 15$ chords.
Start with $1$ region, the whole disc.
Each chord adds one region, and each crossing on it adds one more, so
$$1 + \binom{6}{2} + \binom{6}{4} = 1 + 15 + 15 = 31.$$
The doubling rule predicts $2^5 = 32$, and the true count is $31$.
The typical use: a formula with a counting proof explains both the early agreement and the later failure.
