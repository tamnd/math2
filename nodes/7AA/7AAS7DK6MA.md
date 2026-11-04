---
tag: 7AAS7DK6MA
kind: proof
name: Proof of Fermat's theorem on sums of two squares by Thue's lemma
msc: ["11E25"]
proves: 043B3ENSTY
uses: [0SN0MAEKYX, 0PHBS78HKT, 01J8AMV9RS, 0SQDB87Z3T, 0HGVCWQGY3, 0N10YRNNWV, 0TPW25CBN6]
sources:
  - url: https://en.wikipedia.org/wiki/Thue%27s_lemma
---

## Proof

Let $p$ be an odd [[prime|0SN0MAEKYX]]. Congruences are [[modulo|0TPW25CBN6]] the stated modulus.

**If $p = x^2 + y^2$, then $p \equiv 1 \pmod 4$.**

1. An even integer $2k$ has square $4k^2 \equiv 0 \pmod 4$. An odd integer $2k + 1$ has square $4k^2 + 4k + 1 \equiv 1 \pmod 4$.
2. So $x^2 + y^2$ is $0$, $1$ or $2$ modulo $4$.
3. Since $p$ is odd, $p$ is $1$ or $3$ modulo $4$. With $p = x^2 + y^2$, step 2 leaves only $p \equiv 1 \pmod 4$.

**If $p \equiv 1 \pmod 4$, then $p = x^2 + y^2$.**

4. Since $(p - 1)/2$ is even, the [[first supplement to quadratic reciprocity|0PHBS78HKT]] gives $\left(\frac{-1}{p}\right) = 1$, a [[Legendre symbol|01J8AMV9RS]].
5. So $-1$ is a [[quadratic residue|0SQDB87Z3T]] modulo $p$: there is an integer $a$ with $a^2 \equiv -1 \pmod p$.
6. Let $k$ be the largest integer with $k^2 \le p$. Since $p$ is prime, it is not a perfect square, so $k < \sqrt p < k + 1$ by [[irrationality of square roots of non-squares|0N10YRNNWV]].
7. Let $S$ be the set of pairs $(u, v)$ of integers with $0 \le u, v \le k$. It has $(k + 1)^2 > p$ elements.
8. Map $(u, v)$ to the residue of $u - av$ modulo $p$. There are only $p$ residues. By the [[pigeonhole principle|0HGVCWQGY3]], two distinct pairs $(u, v) \ne (u', v')$ have $u - av \equiv u' - av'$.
9. Put $x = u - u'$ and $y = v - v'$. Then $x \equiv ay \pmod p$, the pair $(x, y)$ is not $(0, 0)$, and $\abs{x}, \abs{y} \le k$.
10. By steps 5 and 9, $x^2 + y^2 \equiv a^2y^2 + y^2 = (a^2 + 1)y^2 \equiv 0 \pmod p$.
11. By steps 6 and 9, $0 < x^2 + y^2 \le 2k^2 < 2p$.
12. The only multiple of $p$ strictly between $0$ and $2p$ is $p$. So $p = x^2 + y^2$.

## Idea

Squares are $0$ or $1$ modulo $4$, which gives one direction. For the other, $-1$ is a square $a^2$ modulo $p$. The pigeonhole principle finds small $x$ and $y$ with $x \equiv ay$, so $p$ divides $x^2 + y^2$, and smallness forces $x^2 + y^2 = p$.
