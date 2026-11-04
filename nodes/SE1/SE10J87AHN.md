---
tag: SE10J87AHN
kind: proof
name: Proof of the first supplement to quadratic reciprocity from Euler's criterion
msc: [11A15]
proves: 0PHBS78HKT
uses: [01J8AMV9RS, 0M7DEDKSYB, 0TPW25CBN6]
sources:
  - url: https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Elementary_Number_Theory_(Raji)/05%3A_Primitive_Roots_and_Quadratic_Residues/5.05%3A_Legendre_Symbol
---

## Proof

1. Let $p$ be an odd prime. Then $(p-1)/2$ is a natural number.
2. By [[Euler's criterion|0M7DEDKSYB]] with $a = -1$, $\left(\frac{-1}{p}\right) \equiv (-1)^{(p-1)/2} \pmod p$.
3. Since $p \nmid -1$, the [[Legendre symbol|01J8AMV9RS]] $\left(\frac{-1}{p}\right)$ is $1$ or $-1$. Also $(-1)^{(p-1)/2}$ is $1$ or $-1$.
4. So the two sides of step 2 differ by $0$ or by $\pm 2$. Since $p \ge 3$ divides the difference, the difference is $0$.
5. Hence $\left(\frac{-1}{p}\right) = (-1)^{(p-1)/2}$.

## Idea

Euler's criterion computes the symbol as $(-1)^{(p-1)/2}$ modulo $p$. Both sides are signs, and two signs that agree modulo an odd prime are equal.
