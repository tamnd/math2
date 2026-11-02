---
tag: YJM07BT0KK
kind: statement
role: theorem
name: Wedderburn's theorem on simple Artinian rings
msc: [16K99, 16P20, 16D60]
uses: [62M0NC3E2T, 20QEAM8AX2, 0FHVPRAE60, 0EA5BTA0CX]
about: [62M0NC3E2T]
sources:
  - url: https://en.wikipedia.org/wiki/Wedderburn%E2%80%93Artin_theorem
---

## Statement

Let $R$ be a [[simple ring|62M0NC3E2T]] that is left [[Artinian|20QEAM8AX2]].
Then there are an integer $n \ge 1$ and a [[division ring|0EA5BTA0CX]] $D$ such that $R \cong M_n(D)$, the [[matrix ring|0FHVPRAE60]] of $n \times n$ matrices over $D$.
The integer $n$ is unique, and $D$ is unique up to isomorphism.

## Remarks

Let $L$ be a minimal left ideal of $R$, which exists because $R$ is Artinian.
The sum of the right translates $La$ is a nonzero two-sided ideal, so it equals $R$.
Hence $R$ is a finite direct sum of copies of $L$, say $n$ of them.
Then $R^{\mathrm{op}} \cong \End_R(R) \cong M_n(\End_R(L))$, and $\End_R(L)$ is a division ring by Schur's lemma, so $R \cong M_n(D)$ with $D = \End_R(L)^{\mathrm{op}}$.
For example, a finite-dimensional simple algebra over $\R$ is $M_n(\R)$, $M_n(\C)$ or $M_n(\mathbb{H})$.
The Artinian hypothesis is needed: the Weyl algebra over $\C$ is simple and is not a matrix ring over a division ring.

## Explanations

### L1 human

Every simple ring that satisfies the finiteness condition "Artinian" is a ring of square matrices over a division ring.
For finite-dimensional algebras over a field this condition holds automatically.
So all such simple rings are known as soon as the division rings are known.

### L2 human

The theorem is the case of one factor in the Artin–Wedderburn theorem.
It is the starting point of the theory of central simple algebras: a central simple algebra over a field $K$ is $M_n(D)$ for a central division algebra $D$ over $K$.
This is why the Brauer group, which collects these $D$, classifies central simple algebras up to matrix size.
Uniqueness of $D$ follows because $D^{\mathrm{op}}$ is the endomorphism ring of the unique simple left module of $R$.
