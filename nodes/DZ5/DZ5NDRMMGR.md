---
tag: DZ5NDRMMGR
kind: proof
name: Proof that −1 is a square modulo p if and only if p is not 3 modulo 4
msc: [11A15]
proves: 00DW862T78
uses: [0PHBS78HKT, 01J8AMV9RS, 0SQDB87Z3T, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_reciprocity
    locator: Proofs of the supplements
---

## Proof

1. Let $p$ be a [[prime number|0SN0MAEKYX]]. If $p = 2$, then $x = 1$ gives $x^2 = 1 \equiv -1 \pmod 2$. Also $2 \not\equiv 3 \pmod 4$. So the statement holds for $p = 2$.
2. Let $p$ be odd. Then $p \equiv 1$ or $p \equiv 3 \pmod 4$.
3. There is an integer $x$ with $x^2 \equiv -1 \pmod p$ exactly when $-1$ is a [[quadratic residue|0SQDB87Z3T]] modulo $p$.
4. Since $p \nmid -1$, this holds exactly when the [[Legendre symbol|01J8AMV9RS]] $\left(\frac{-1}{p}\right)$ equals $1$.
5. By the [[first supplement|0PHBS78HKT]], $\left(\frac{-1}{p}\right) = (-1)^{(p-1)/2}$. This is $1$ exactly when $(p-1)/2$ is even, that is, when $4 \mid p - 1$.
6. So for odd $p$, a solution exists exactly when $p \equiv 1 \pmod 4$. By step 2, this means $p \not\equiv 3 \pmod 4$.

## Idea

For odd $p$, the first supplement gives the answer as the sign $(-1)^{(p-1)/2}$, which is $+1$ exactly for $p \equiv 1 \pmod 4$. The prime $2$ is checked by hand.
