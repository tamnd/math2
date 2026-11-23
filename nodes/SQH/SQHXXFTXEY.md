---
tag: SQHXXFTXEY
kind: example
name: Identifying the sum of 1/(n^2 C(2n,n))
msc: ["11Y60", "05A10"]
topics: [DME0TPC348]
audience: ug2
instance_of: [BPEPTN0TT9]
uses: [BPEPTN0TT9, 0JPH2Y4DFV, 00Z1YBJJW8, 0C1VYVNV2N]
sources:
  - url: https://en.wikipedia.org/wiki/Integer_relation_algorithm
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Central_binomial_coefficient
    locator: lead section
---

## Example

Add three fractions:
$$\frac{1}{1 \cdot 2} + \frac{1}{4 \cdot 6} + \frac{1}{9 \cdot 20} = 0.5 + 0.041667 + 0.005556 = 0.547222.$$
These are the first terms of
$$S = \sum_{n=1}^{\infty} \frac{1}{n^2 \binom{2n}{n}},$$
where $\binom{2n}{n}$ is the [[central binomial coefficient|0JPH2Y4DFV]].
The number $\pi^2/18 = 0.548311\ldots$ is already close.
We find the exact value by the chain of [[experimental mathematics|BPEPTN0TT9]]: compute, detect, test, prove.

1. The convergence.
   The ratio of the terms $n + 1$ and $n$ is $\dfrac{n^2}{(n+1)^2} \cdot \dfrac{(n+1)^2}{(2n+1)(2n+2)} = \dfrac{n^2}{(2n+1)(2n+2)}$, which tends to $1/4$.
   So each term gains about $0.6$ decimal digits.
2. The computation.
   The partial sums are $0.5$, $0.541667$, $0.547222$, $0.548115$, $0.548274$ for $N = 1, \ldots, 5$.
   The tail after $N = 40$ is below $2 \cdot 10^{-27}$, and $S = 0.5483113556160754788\ldots$.
3. The guess of a basis.
   The coefficient $\binom{2n}{n}$ appears in the series of $\arcsin$, so constants such as $\pi$, $\pi^2$, $\ln 2$ and $\zeta(3)$ are reasonable candidates.
4. The detection.
   An integer relation algorithm applied to $(S, 1, \pi^2, \pi, \ln 2, \zeta(3), \pi \ln 2)$ looks for integers, not all zero, that combine these numbers to $0$.
   It finds $(-18, 0, 1, 0, 0, 0, 0)$, which means $18 S = \pi^2$.
5. The test.
   The search at a higher precision returns the same vector, and $S$ and $\pi^2/18$ agree to all $100$ digits of a $100$-digit computation.
   This makes the guess almost certain, and it is still not a proof.
6. The proof, part 1.
   Let $f(x) = \arcsin^2 x$ for $|x| < 1$.
   Then $\sqrt{1-x^2}\, f'(x) = 2\arcsin x$.
   Differentiating once more and multiplying by $\sqrt{1-x^2}$ gives $(1 - x^2) f''(x) - x f'(x) = 2$.
7. The proof, part 2.
   Write $f(x) = \sum_{n \geq 1} c_n x^{2n}$, with $c_1 = 1$ because $\arcsin x = x + O(x^3)$.
   The coefficient of $x^{2n}$ in the equation of step 6 gives $(2n+1)(2n+2)c_{n+1} = (2n)^2 c_n$ for $n \geq 1$.
8. The proof, part 3.
   The numbers $c_n = \dfrac{2^{2n}}{2 n^2 \binom{2n}{n}}$ satisfy $c_1 = 1$ and the recursion of step 7.
   So $2\arcsin^2 x = \sum_{n \geq 1} \dfrac{(2x)^{2n}}{n^2 \binom{2n}{n}}$.
9. The proof, part 4.
   At $x = 1/2$ the factor $(2x)^{2n}$ is $1$, and $\arcsin(1/2) = \pi/6$.
   So $S = 2 \cdot \pi^2/36 = \pi^2/18$.

## Remarks

### Checks inside the proof

In step 8 the ratio $c_{n+1}/c_n$ is
$$4 \cdot \frac{n^2}{(n+1)^2} \cdot \frac{(n+1)^2}{(2n+1)(2n+2)} = \frac{(2n)^2}{(2n+1)(2n+2)},$$
as the recursion needs.
The power series of step 7 has radius of convergence $1$, so $x = 1/2$ is inside it.

### Constants that do not appear

Step 4 included constants that do not occur in the answer.
When the algorithm gives them zero coefficients, that is extra evidence: the relation is the simplest one in a larger space.
A related alternating sum, $\sum (-1)^{n+1}/(n^3 \binom{2n}{n}) = \frac25 \zeta(3)$, is used in Apéry's proof that $\zeta(3)$ is irrational; see [[Apéry's theorem|RT5MJT6CTB]].

### Watch out

A slowly convergent series, such as $\sum 1/n^2$, gives few digits for a lot of work.
It needs acceleration before an integer relation search, because the search needs many correct digits.

### Try it

Put $x = 1/\sqrt2$ in step 8, where $\arcsin(1/\sqrt2) = \pi/4$.
You get $\sum_{n \ge 1} 2^n / (n^2 \binom{2n}{n}) = \pi^2/8 = 1.2337\ldots$.
The first five terms are $1$, $0.1667$, $0.0444$, $0.0143$ and $0.0051$, with sum $1.2305$, and this series converges more slowly, since its ratio tends to $1/2$.

## Explanations

### L1 human

A computer adds the numbers $1/2$, $1/24$, $1/180$ and so on, and gets $0.548311355616\ldots$.
The number $\pi \times \pi$ divided by $18$ has the same first digits.
More digits still agree, so the guess becomes very believable.
Then a known formula for the arcsine function proves that the guess is exactly right.

### L2 human

We check the fourth and fifth terms by hand.
For $n = 4$, $\binom84 = 70$, so the term is $1/(16 \cdot 70) = 1/1120 = 0.000893$.
For $n = 5$, $\binom{10}{5} = 252$, so the term is $1/(25 \cdot 252) = 1/6300 = 0.000159$.
Adding them to $0.547222$ gives $0.548115$ and then $0.548274$, as in step 2.
The typical use: a fast convergent series gives many digits cheaply, and many digits make the detection reliable.
