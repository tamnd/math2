---
tag: 3SMMPJ6DVN
kind: proof
name: Proof of Eisenstein's lemma
msc: [11A15]
proves: 0XSDBCP4RZ
uses: [01J8AMV9RS, 0M7DEDKSYB, 051VYKA1EX, 0CHQKZFK5S, 0YVRNEDSVG, 072D5G4SK6, 0TPW25CBN6]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_of_quadratic_reciprocity
    locator: Proof of Eisenstein's lemma
---

## Proof

1. Let $p$ be an odd prime, $a$ a positive integer with $p \nmid a$, and $h = (p-1)/2$. Let $E = \set{2, 4, \dots, p - 1}$, a set of $h$ even numbers.
2. For $u \in E$, let $r(u)$ be the least positive residue of $au$ modulo $p$. By [[Euclid's lemma|051VYKA1EX]], $p \nmid au$, so $1 \le r(u) \le p - 1$.
3. Let $e(u) = r(u)$ if $r(u)$ is even, and $e(u) = p - r(u)$ if $r(u)$ is odd. In both cases $e(u)$ is even with $1 \le e(u) \le p - 1$, because $p$ is odd. So $e(u) \in E$.
4. In both cases $r(u) \equiv (-1)^{r(u)} e(u) \pmod p$.
5. The map $u \mapsto e(u)$ is injective on $E$. Suppose $e(u) = e(v)$. Then $r(u) \equiv \pm r(v)$, so $au \equiv \pm av$, and $p \mid u - v$ or $p \mid u + v$ by Euclid's lemma.
6. Here $\abs{u - v} < p$. Also $u + v$ is even with $4 \le u + v \le 2p - 2$, and the only multiple of $p$ in this range is the odd number $p$. So $u - v = 0$.
7. Since $E$ is finite, $u \mapsto e(u)$ is a bijection of $E$. So $\prod_{u \in E} e(u) = \prod_{u \in E} u$.
8. By step 4 and [[products of congruences|072D5G4SK6]], $a^h \prod_{u \in E} u = \prod_{u \in E} au \equiv \prod_{u \in E} r(u) \equiv (-1)^{\sum_u r(u)} \prod_{u \in E} u \pmod p$.
9. Each $u \in E$ is less than $p$, so $p \nmid \prod_{u \in E} u$ by Euclid's lemma. Hence $a^h \equiv (-1)^{\sum_u r(u)} \pmod p$.
10. By the [[division algorithm|0CHQKZFK5S]], $au = p q(u) + r(u)$ with $q(u) = \lfloor au/p \rfloor$, since $0 < r(u) < p$ and the [[floor function|0YVRNEDSVG]] picks the integer part.
11. Here $au$ is even and $p$ is odd. So $0 \equiv q(u) + r(u) \pmod 2$, and $r(u) \equiv q(u) \pmod 2$. Thus $(-1)^{\sum_u r(u)} = (-1)^{\sum_u \lfloor au/p \rfloor}$.
12. By [[Euler's criterion|0M7DEDKSYB]], $\left(\frac{a}{p}\right) \equiv a^h \equiv (-1)^{\sum_u \lfloor au/p \rfloor} \pmod p$.
13. Both sides are $\pm 1$, since $p \nmid a$ and by the definition of the [[Legendre symbol|01J8AMV9RS]]. Two signs that agree modulo $p \ge 3$ are equal, which proves the lemma.

## Idea

Fold each residue $r(u)$ to an even number by replacing it with $p - r(u)$ when it is odd. The folded numbers are again the even numbers $2, \dots, p - 1$, so the sign picked up is $(-1)^{\sum r(u)}$. The parity of $r(u)$ equals the parity of $\lfloor au/p \rfloor$, because $au$ is even and $p$ is odd.
