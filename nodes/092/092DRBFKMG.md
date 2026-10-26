---
tag: 092DRBFKMG
kind: definition
name: Catalan numbers
msc: [05A15]
defines: 0YWZJEABB2
sources:
  - url: https://en.wikipedia.org/wiki/Catalan_number
    locator: lead section
---

## Definition

The Catalan numbers $C_n$, for natural numbers $n$, are defined by the recursion
$$C_0 = 1, \qquad C_{n+1} = \sum_{i=0}^{n} C_i\, C_{n-i}.$$

## Remarks

The first values, for $n = 0, 1, \dots, 7$, are $1, 1, 2, 5, 14, 42, 132, 429$.
The [[closed formula|0NNDQVJ54Q]] is $C_n = \frac{1}{n+1} \binom{2n}{n}$.
$C_n$ counts [[Dyck words|0R9JR0465V]] of semilength $n$ and [[binary trees|02A8EMC83C]] with $n$ nodes, and many other families.

## Explanations

### L1 human

Catalan numbers count many structures that split into a left part and a right part.
For example, there are $C_3 = 5$ ways to put brackets on a product $abcd$ of four factors: $((ab)c)d$, $(a(bc))d$, $(ab)(cd)$, $a((bc)d)$ and $a(b(cd))$.
