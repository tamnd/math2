---
tag: 0R8J3ZQMJS
kind: definition
name: Subsequence
msc: [40A05]
defines: 0F1PR74BRX
uses: [0QE8STGJH2]
sources:
  - url: https://en.wikipedia.org/wiki/Sequence
    locator: Subsequences
  - url: https://en.wikipedia.org/wiki/Subsequence
    locator: lead section
---

## Definition

Let $(a_n)_{n \in \mathbb{N}}$ be a [[sequence|0QE8STGJH2]] in a set $X$.
Let $(n_k)_{k \in \mathbb{N}}$ be a strictly increasing sequence of natural numbers: $n_0 < n_1 < n_2 < \cdots$.
The sequence $(a_{n_k})_{k \in \mathbb{N}}$ is a subsequence of $(a_n)$.

## Remarks

Equivalently, a subsequence is the composite $a \circ \varphi$ of the sequence $a \colon \mathbb{N} \to X$ with a strictly increasing map $\varphi \colon \mathbb{N} \to \mathbb{N}$.
By induction, $n_k \ge k$ for each $k$.
The even terms $a_0, a_2, a_4, \dots$ form a subsequence, with $n_k = 2k$.

## Explanations

### L1 human

You get a subsequence when you delete some terms of a sequence and keep infinitely many terms in their old order.
From $1, 2, 3, 4, \dots$ you can keep the even numbers $2, 4, 6, \dots$.
