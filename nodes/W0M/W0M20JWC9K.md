---
tag: W0M20JWC9K
kind: statement
role: theorem
name: Quartic reciprocity
msc: [11A15, 11R18]
uses: [074P7C85XH, 0YV2CKP2AV, 085MJS6907, EQ6A3ZN48K, 2767J23XHN]
about: [W0M20JWC9K]
sources:
  - url: https://en.wikipedia.org/wiki/Quartic_reciprocity
same_as:
  wikidata: Q4495708
  wikipedia: Quartic reciprocity
---

## Statement

Let $\Z[i]$ be the ring of [[Gaussian integers|074P7C85XH]], with norm $N(a + bi) = a^2 + b^2$.
Let $\pi$ be a prime element of $\Z[i]$ that does not divide $1 + i$.
For $\alpha \in \Z[i]$ not divisible by $\pi$, the quartic residue character $\left(\frac{\alpha}{\pi}\right)_4$ is the unique element of $\set{1, i, -1, -i}$ with
$$\alpha^{(N(\pi) - 1)/4} \equiv \left(\frac{\alpha}{\pi}\right)_4 \pmod{\pi}.$$
A prime $\pi$ is called primary if $\pi \equiv 1 \pmod{(1 + i)^3}$.
Let $\lambda$ and $\pi$ be primary primes of $\Z[i]$ that are not associates.
Then
$$\left(\frac{\lambda}{\pi}\right)_4 = \left(\frac{\pi}{\lambda}\right)_4 \cdot (-1)^{\frac{N(\lambda) - 1}{4} \cdot \frac{N(\pi) - 1}{4}}.$$

## Remarks

The proof follows the same pattern as for cubic reciprocity, with quartic [[Gauss sums|EQ6A3ZN48K]] and [[Jacobi sums|2767J23XHN]] over the field with $p$ elements for $p \equiv 1 \pmod 4$.
Each prime of $\Z[i]$ not dividing $1 + i$ has exactly one primary associate.
The sign is $-1$ only when both $\lambda$ and $\pi$ are congruent to $3 + 2i$ modulo $4$.
A classical consequence: for a prime $p \equiv 1 \pmod 8$, the integer $2$ is a fourth power modulo $p$ if and only if $p = x^2 + 64y^2$ for some integers $x, y$.
For example, $73 = 3^2 + 64 \cdot 1^2$, and $2^{18} \equiv 1 \pmod{73}$, so $2$ is a fourth power modulo $73$.
The prime $17$ is not of this form, and the nonzero fourth powers modulo $17$ are $1$, $4$, $13$ and $16$.

## Explanations

### L1 human

Quartic reciprocity is the analogue of [[quadratic reciprocity|085MJS6907]] for fourth powers.
It compares "is $\lambda$ a fourth power modulo $\pi$?" with "is $\pi$ a fourth power modulo $\lambda$?".
The natural place to state it is the Gaussian integers, which contain the fourth roots of unity $\pm 1, \pm i$.
The two answers agree up to an explicit sign.

### L2 human

With supplementary laws for $i$ and $1 + i$, the law lets one compute any quartic residue character by swapping and reducing.
It answers questions such as when $2$ is a fourth power modulo a prime, which quadratic reciprocity cannot decide.
Like cubic reciprocity, it is a special case of the [[Artin reciprocity law|7938EKMMVR]].
