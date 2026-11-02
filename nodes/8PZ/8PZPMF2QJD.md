---
tag: 8PZPMF2QJD
kind: statement
role: theorem
name: Ramanujan's series for 1/pi
msc: [11Y60, "33E05", 65D20]
uses: [0C1VYVNV2N, 0XWG0JGDFW, 0AF7X08PCR]
about: [0C1VYVNV2N]
sources:
  - url: https://en.wikipedia.org/wiki/Ramanujan%E2%80%93Sato_series
---

## Statement

The [[series|0AF7X08PCR]] below converges, and
$$\frac{1}{\pi} = \frac{2\sqrt2}{9801}\sum_{k=0}^{\infty} \frac{(4k)!\,(1103 + 26390k)}{(k!)^4\,396^{4k}},$$
where $\pi$ is the number [[pi|0C1VYVNV2N]] and $n!$ is the [[factorial|0XWG0JGDFW]].

## Remarks

Convergence: by Stirling's formula $(4k)!/(k!)^4$ grows like a constant times $256^k k^{-3/2}$, while $396^4 \approx 2.46 \times 10^{10}$, so the ratio of successive terms tends to $256/396^4 \approx 1.04 \times 10^{-8}$.
So each term adds about eight correct decimal digits.
Example: the $k = 0$ term alone gives $\pi \approx 9801/(2\sqrt2 \cdot 1103) = 3.14159273\ldots$, against $\pi = 3.14159265\ldots$.
Ramanujan published this series in 1914 among several series of the same shape, without a complete proof.
Proof idea: the series comes from the theory of [[complete elliptic integrals|RM54CPPE12]] and modular equations.
It uses a singular value of the modulus attached to the imaginary quadratic field $\Q(\sqrt{-58})$, which is reflected in $e^{\pi\sqrt{58}} \approx 396^4 - 104$.
Identities such as [[Legendre's relation|8GSKDNZ4TK]] convert the resulting relations between elliptic integrals into a formula for $1/\pi$.
A complete proof was given later by Jonathan and Peter Borwein.

## Explanations

### L1 human

This is a formula that writes $1/\pi$ as an infinite sum of fractions built from factorials and powers of $396$.
Its terms shrink so fast that each new term gives about eight more digits of $\pi$.
The first term alone already gives $\pi$ to six decimal places.

### L2 human

The series is the most famous member of the family of Ramanujan–Sato series, in which $1/\pi$ equals a sum of hypergeometric-type terms $\frac{(4k)!}{(k!)^4}(a + bk)x^k$ or similar.
Each such series comes from a singular value of the modulus, where the elliptic curve has complex multiplication.
The same idea with the $j$-invariant and the field $\Q(\sqrt{-163})$ gives the [[Chudnovsky algorithm|JKCKXDT5B5]], which gains about fourteen digits per term.
