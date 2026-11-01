---
tag: SM1TJSAR75
kind: object
name: Golay code
msc: [94B25, 05B05]
instance_of: [TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Binary_Golay_code
same_as:
  wikidata: Q1534522
  wikipedia: Binary Golay code
---

## Description

The extended binary Golay code $G_{24}$ is a linear code of length $24$ over the field $\F_2$, of dimension $12$ and minimum distance $8$.
So it has $2^{12} = 4096$ codewords, and any two differ in at least $8$ of the $24$ positions; as an [[error-correcting code|X122TKFP9G]] it corrects $3$ errors.
Deleting one coordinate gives the perfect binary Golay code $G_{23}$, of length $23$, dimension $12$ and minimum distance $7$.
Check that $G_{23}$ is perfect: a Hamming ball of radius $3$ in $\F_2^{23}$ contains $1 + 23 + 253 + 1771 = 2048 = 2^{11}$ words.
The $2^{12}$ balls around the codewords are disjoint, since $7 \ge 2 \cdot 3 + 1$, and together they contain $2^{12} \cdot 2^{11} = 2^{23}$ words, which is all of $\F_2^{23}$.

## Remarks

The weights of the codewords of $G_{24}$ are $0, 8, 12, 16, 24$, with $1, 759, 2576, 759, 1$ codewords of each weight.
The $759$ codewords of weight $8$, seen as $8$-element subsets of the $24$ positions, are the blocks of the [[Steiner system|7BPSC4T4M3]] $S(5, 8, 24)$.
The automorphism group of $G_{24}$ is the Mathieu group $M_{24}$, one of the sporadic simple groups.
Besides the binary codes there is also a ternary Golay code.

## Explanations

### L1 human

The binary Golay code is a set of $4096$ strings of $24$ bits, chosen so that any two differ in at least $8$ bits.
If a string is damaged in up to $3$ bits, the original string can still be recovered.
Its shorter version of length $23$ is perfect: the spheres of radius $3$ around its codewords fill the whole space with no gap and no overlap.
