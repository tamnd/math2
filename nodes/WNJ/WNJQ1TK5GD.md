---
tag: WNJQ1TK5GD
kind: definition
name: Huffman coding
msc: [94A45, 94A29, 68P30]
defines: JS11GWK9HF
uses: [GNB3T6TD0M, 0D6J4B671D, 0D7EZ10V2R]
sources:
  - url: https://en.wikipedia.org/wiki/Huffman_coding
---

## Definition

Let $\mathcal{X}$ be a finite set with $n \ge 2$ elements and let $p$ be a [[probability mass function|0D6J4B671D]] on $\mathcal{X}$.
A *binary Huffman code* for $(\mathcal{X}, p)$ is a binary [[prefix code|GNB3T6TD0M]] $C \colon \mathcal{X} \to \set{0,1}^*$ obtained by the following recursion.

1. If $n = 2$, with $\mathcal{X} = \set{a, b}$, put $C(a) = 0$ and $C(b) = 1$.
2. If $n > 2$, choose two distinct elements $a, b \in \mathcal{X}$ with the two smallest values of $p$, ties broken arbitrarily.
3. Replace $a$ and $b$ by one new symbol $z$ with $p(z) = p(a) + p(b)$, and let $C'$ be a Huffman code for the resulting set of $n - 1$ symbols.
4. Put $C(a) = C'(z)0$, $C(b) = C'(z)1$, and $C(x) = C'(x)$ for every other $x$.

## Remarks

The merges build a full [[binary tree|0D7EZ10V2R]] whose leaves are the symbols; a codeword is the path from the root to a leaf.
Example: for $p = (1/2, 1/4, 1/8, 1/8)$ on $\set{a, b, c, d}$, first merge $c, d$ into a symbol of weight $1/4$.
Then merge $b$ with it into a symbol of weight $1/2$, and finally merge with $a$.
This gives $C(a) = 0$, $C(b) = 10$, $C(c) = 110$, $C(d) = 111$, with expected length $1.75$.
Non-example: the fixed-length code $00, 01, 10, 11$ for the same $p$ is a prefix code but not a Huffman code.
In its code tree $a$ and $b$ are siblings, but Huffman's rule never merges $a$, of probability $1/2$, before the last step.
Its expected length $2$ is larger than $1.75$.
For a $D$-letter alphabet one merges the $D$ least likely symbols at each step, after adding dummy symbols of probability $0$ so that $n \equiv 1 \pmod{D-1}$.
