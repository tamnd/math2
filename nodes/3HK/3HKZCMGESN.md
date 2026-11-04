---
tag: 3HKZCMGESN
kind: proof
name: Proof of Gauss's lemma on quadratic residues
msc: [11A15]
proves: 037ACYXB5Z
uses: [01J8AMV9RS, 0M7DEDKSYB, 051VYKA1EX, 072D5G4SK6, 0TPW25CBN6]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%27s_lemma_(number_theory)
    locator: Proof
---

## Proof

1. Let $p$ be an odd prime, $a$ an integer with $p \nmid a$, and $h = (p-1)/2$. For $k = 1, \dots, h$, let $r_k$ be the least positive residue of $ka$ modulo $p$.
2. By [[Euclid's lemma|051VYKA1EX]], $p \nmid ka$, so $1 \le r_k \le p - 1$. Since $p$ is odd, $r_k \ne p/2$.
3. Put $s_k = r_k$ and $\varepsilon_k = 1$ if $r_k < p/2$. Put $s_k = p - r_k$ and $\varepsilon_k = -1$ if $r_k > p/2$.
4. Then $1 \le s_k \le h$ and $ka \equiv \varepsilon_k s_k \pmod p$. Exactly $n$ of the $\varepsilon_k$ equal $-1$, where $n$ is the number in the statement.
5. The $s_k$ are distinct. Suppose $s_k = s_l$ with $1 \le k, l \le h$. Then $ka \equiv \pm la$, so $p \mid (k \mp l) a$. As $p \nmid a$, Euclid's lemma gives $p \mid k - l$ or $p \mid k + l$.
6. But $\abs{k - l} < p$ and $2 \le k + l \le p - 1$. So $k + l$ is not a multiple of $p$, and $k - l = 0$.
7. So $s_1, \dots, s_h$ are $h$ distinct numbers in $\set{1, \dots, h}$. Hence they are $1, \dots, h$ in some order.
8. Multiplying the congruences of step 4 with [[products of congruences|072D5G4SK6]] gives $a^h \cdot h! = \prod_{k=1}^{h} ka \equiv \prod_{k=1}^{h} \varepsilon_k s_k = (-1)^n h! \pmod p$.
9. So $p \mid h! \left(a^h - (-1)^n\right)$. Every factor of $h!$ is less than $p$, so $p \nmid h!$ by Euclid's lemma. Thus $a^h \equiv (-1)^n \pmod p$.
10. By [[Euler's criterion|0M7DEDKSYB]], $\left(\frac{a}{p}\right) \equiv a^h \equiv (-1)^n \pmod p$.
11. Since $p \nmid a$, the [[Legendre symbol|01J8AMV9RS]] is $\pm 1$. Two signs that agree modulo $p \ge 3$ are equal. So $\left(\frac{a}{p}\right) = (-1)^n$.

## Idea

Fold each residue of $ka$ into the range $1, \dots, h$ by replacing $r$ with $p - r$ when $r > p/2$. The folded numbers are exactly $1, \dots, h$, so the product of the $ka$ is $h!$ up to the sign $(-1)^n$. Comparing with $a^h h!$ and using Euler's criterion gives the lemma.
