---
tag: EMVECB93EQ
kind: statement
role: theorem
name: Cubic reciprocity
msc: [11A15, 11R18]
uses: [0YV2CKP2AV, 01826KMG2H, 085MJS6907, EQ6A3ZN48K, 2767J23XHN]
about: [EMVECB93EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cubic_reciprocity
same_as:
  wikidata: Q2443110
  wikipedia: Cubic reciprocity
---

## Statement

Let $\omega = e^{2\pi i/3}$ be a primitive cube [[root of unity|0YV2CKP2AV]], and let $\Z[\omega] = \set{a + b\omega : a, b \in \Z}$ be the ring of Eisenstein integers, with norm $N(a + b\omega) = a^2 - ab + b^2$.
Let $\pi$ be a prime element of $\Z[\omega]$ with $N(\pi) \ne 3$.
For $\alpha \in \Z[\omega]$ not divisible by $\pi$, the cubic residue character $\left(\frac{\alpha}{\pi}\right)_3$ is the unique element of $\set{1, \omega, \omega^2}$ with
$$\alpha^{(N(\pi) - 1)/3} \equiv \left(\frac{\alpha}{\pi}\right)_3 \pmod{\pi}.$$
A prime $\pi$ is called primary if $\pi \equiv 2 \pmod 3$ in $\Z[\omega]$.
Let $\pi_1$ and $\pi_2$ be primary primes of $\Z[\omega]$ with $N(\pi_1) \ne 3$, $N(\pi_2) \ne 3$ and $N(\pi_1) \ne N(\pi_2)$.
Then
$$\left(\frac{\pi_1}{\pi_2}\right)_3 = \left(\frac{\pi_2}{\pi_1}\right)_3.$$

## Remarks

The standard proof uses cubic [[Gauss sums|EQ6A3ZN48K]] and [[Jacobi sums|2767J23XHN]].
For a prime $\pi$ of norm $p \equiv 1 \pmod 3$, the Jacobi sum of the cubic character is a primary element of norm $p$.
The cube of the Gauss sum equals $p$ times this Jacobi sum.
Comparing this identity modulo the other prime gives the law.
Each prime of $\Z[\omega]$ not dividing $3$ has exactly one primary associate, so the hypothesis "primary" only fixes the choice among the six associates.
A classical consequence: for a prime $p \equiv 1 \pmod 3$, the integer $2$ is a cube modulo $p$ if and only if $p = x^2 + 27y^2$ for some integers $x, y$.
For example, $31 = 2^2 + 27 \cdot 1^2$, and indeed $4^3 = 64 \equiv 2 \pmod{31}$.
The prime $7$ is not of this form, and the cubes modulo $7$ are only $0$, $1$ and $6$.

## Explanations

### L1 human

Cubic reciprocity is the analogue of [[quadratic reciprocity|085MJS6907]] for cubes instead of squares.
It relates the question "is $\pi_1$ a cube modulo $\pi_2$?" to the question "is $\pi_2$ a cube modulo $\pi_1$?".
To state it cleanly one must work in the Eisenstein integers, which contain the cube roots of unity.
There the answer to both questions is the same.

### L2 human

The law is usually completed by supplementary laws for the units and for the prime $1 - \omega$ above $3$.
Together they let one compute any cubic residue character by repeated swapping and reduction, just as with the Legendre symbol.
The proof through Gauss and Jacobi sums is the model for the higher reciprocity laws, and the general case is part of class field theory through the [[Artin reciprocity law|7938EKMMVR]].
