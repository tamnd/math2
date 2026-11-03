---
tag: HSXZD57ABX
kind: example
name: Hadamard code
msc: [94B05, 94B25]
instance_of: [E85KREWV60]
uses: [K8ZHAQAK2B, M2X88AXM17, J0N4J606X0, K784BA2WHV, 0S52TNNTH9, KMTYBQK7V0]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_code
same_as:
  wikidata: Q1567339
  wikipedia: Hadamard code
---

## Example

Let $k \ge 1$ and let $y_1, \dots, y_{2^k}$ be the $2^k$ elements of $\F_2^k$ in some fixed order.
For $x \in \F_2^k$, let $c_x = (x \cdot y_1, \dots, x \cdot y_{2^k}) \in \F_2^{2^k}$, where $x \cdot y$ is the [[dot product|0S52TNNTH9]].
The *Hadamard code* is $C = \set{c_x : x \in \F_2^k}$.
The map $x \mapsto c_x$ is linear and injective, since $x \cdot e_i = x_i$ for the unit vectors $e_i$.
So $C$ is a [[linear code|E85KREWV60]] of length $2^k$ and dimension $k$.
For $x \ne 0$, the linear form $y \mapsto x \cdot y$ is onto $\F_2$, and its kernel has $2^{k-1}$ elements, so $c_x$ has [[Hamming weight|K8ZHAQAK2B]] exactly $2^{k-1}$.
Hence the [[minimum distance|M2X88AXM17]] is $2^{k-1}$, and $C$ is a $[2^k, k, 2^{k-1}]$ code.

## Remarks

Writing $(-1)^{x \cdot y}$ in place of $x \cdot y$ turns the codewords into the rows of the Sylvester [[Hadamard matrix|J0N4J606X0]] of order $2^k$.
Its relative distance is $1/2$, which is very large, but its rate $k / 2^k$ is very small.
By the [[Plotkin bound|KMTYBQK7V0]], a binary code of length $n$ with relative distance above $1/2$ has at most $2n$ codewords.
It can be decoded by computing the [[Walsh–Hadamard transform|K784BA2WHV]] of the received word.
Write $c_x(y)$ for the entry $x \cdot y$ of $c_x$; by linearity $c_x(y) = c_x(y + z) - c_x(z)$ for every $z$.
So each entry can be recovered from two other entries at random positions, which makes the code locally decodable and useful in complexity theory.
Deleting the position with $y = 0$, which is always $0$, gives the simplex code $[2^k - 1, k, 2^{k-1}]$, the dual of the binary Hamming code.

## Explanations

### L1 human

The Hadamard code writes down a message $x$ of $k$ bits by listing the parity of $x$ against every possible pattern $y$ of $k$ bits.
That is a very long list, $2^k$ bits, but any two different messages give lists that disagree in exactly half of the places.
So even if almost a quarter of the list is corrupted, the message can still be recovered.
It trades length for robustness in the most extreme way.
