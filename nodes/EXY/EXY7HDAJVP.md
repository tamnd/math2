---
tag: EXY7HDAJVP
kind: statement
role: theorem
name: Optimality of Huffman codes
msc: [94A45, 94A29, 68P30]
uses: [JS11GWK9HF, GNB3T6TD0M, MWBRNBXW1Y, G1ZAWMBNE1, PC8ASRWARE, 0WQNRCNY3M, 0D6J4B671D]
about: [JS11GWK9HF]
sources:
  - url: https://en.wikipedia.org/wiki/Huffman_coding
---

## Statement

Let $\mathcal{X}$ be a finite set with at least two elements and let $p$ be a [[probability mass function|0D6J4B671D]] on $\mathcal{X}$.
For a binary code $C \colon \mathcal{X} \to \set{0,1}^*$, let $L(C) = \sum_{x \in \mathcal{X}} p(x) \abs{C(x)}$ be its [[expected|0WQNRCNY3M]] length.
Let $H$ be a binary [[Huffman code|JS11GWK9HF]] for $(\mathcal{X}, p)$.
Then $L(H) \le L(C)$ for every binary [[uniquely decodable code|MWBRNBXW1Y]] $C$ that maps distinct symbols to distinct codewords.

## Remarks

By the [[Kraft–McMillan inequality|G1ZAWMBNE1]], every uniquely decodable code has the same codeword lengths as some [[prefix code|GNB3T6TD0M]], so it suffices to compare with prefix codes.
Among optimal prefix codes there is one in which the two least likely symbols are siblings of maximal depth in the code tree.
Merging these two symbols turns the problem into the same problem with one symbol less, and the cost changes by the constant $p(a) + p(b)$.
Induction on the number of symbols finishes the proof.

Example: for $p = (0.4, 0.2, 0.2, 0.1, 0.1)$ a Huffman code has lengths $2, 2, 2, 3, 3$ and expected length $2.2$.
No uniquely decodable code does better, although the entropy of $p$ is only about $2.12$ bits.

The optimality concerns codes that encode one symbol at a time.
Coding blocks of symbols can do better: for $p = (0.9, 0.1)$ the Huffman code has $L = 1$, while codes for long blocks approach the entropy, about $0.47$ bits per symbol.

## Explanations

### L1 human

Huffman's merging rule is greedy, but it is never beaten.
No other code that can be decoded unambiguously, letter by letter, has a shorter average length.

### L2 human

Combined with [[Shannon's source coding theorem|PC8ASRWARE]], the Huffman code $H$ satisfies $L(H) < \mathrm{H}(p) + 1$, where $\mathrm{H}(p)$ is the entropy.
The key lemma is the sibling property: in some optimal tree the two rarest symbols share a parent at the deepest level.
The same argument with $D$-ary trees proves optimality of $D$-ary Huffman codes.
