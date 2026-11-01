---
tag: XK7H3YXBQT
kind: statement
role: theorem
name: Frobenius's theorem on Frobenius kernels
msc: [20D99, 20C15]
uses: [JXS91FGFHY, 0CB0DX5BVV, 0H3WZXCZNF, 0AYMP41THN, 0H11ZPX4ND, 0Q7MMQHC1P]
about: [JXS91FGFHY]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_group
---

## Statement

Let $G$ be a [[Frobenius group|JXS91FGFHY]] acting on a finite set $\Omega$, and let $H = G_\omega$ be the [[stabiliser|0AYMP41THN]] of a point $\omega \in \Omega$.
Let $K$ be the set of elements of $G$ that fix no point of $\Omega$, together with the identity $e$.
Then $K$ is a [[normal subgroup|0CB0DX5BVV]] of $G$, $K$ acts regularly on $\Omega$, and $G$ is the [[semidirect product|0H3WZXCZNF]] $K \rtimes H$.

## Remarks

Counting is easy.
Let $n = \abs{\Omega}$; the $n$ point stabilisers are the [[conjugates|0H11ZPX4ND]] of $H$, and any two of them meet only in $e$.
So their union has $n(\abs{H} - 1) + 1$ elements, and $K$ has $\abs{G} - n\abs{H} + n = n$ elements.
The hard part is that $K$ is closed under multiplication.
The standard proof uses characters.
Each irreducible character of $H$ is extended to a character of $G$, and $K$ is the intersection of the kernels of these characters.

Example: for the maps $x \mapsto ax + b$ with $a \ne 0$ acting on $\F_q$, the kernel $K$ is the group of translations $x \mapsto x + b$, and the complement $H$ is the group of maps $x \mapsto ax$.
For $S_3$ acting on $3$ points, $K = A_3$.

John Thompson later proved that the Frobenius kernel is always [[nilpotent|0Q7MMQHC1P]].

## Explanations

### L1 human

In a Frobenius group, the elements that move every point look like a loose collection.
Frobenius's theorem says they form a subgroup, and in fact a normal one.
So every Frobenius group splits into two pieces: the kernel, which moves points around freely, and a point stabiliser.

### L2 human

The theorem is a famous example of the power of character theory: its statement is purely about permutations, but the standard proof needs characters.
It gives the structure $G = K \rtimes H$ with $\abs{K} = \abs{\Omega}$ and $\abs{H}$ dividing $\abs{K} - 1$, since $H$ acts on $K \setminus \set{e}$ by conjugation with all orbits of size $\abs{H}$.
The Frobenius kernel and complement are central in the study of finite groups, for example in the proof of the Feit–Thompson theorem.
