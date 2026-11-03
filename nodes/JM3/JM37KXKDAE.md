---
tag: JM37KXKDAE
kind: statement
role: theorem
name: Griesmer bound
msc: [94B65, 94B05]
uses: [E85KREWV60, M2X88AXM17, K8ZHAQAK2B]
about: [E85KREWV60]
sources:
  - url: https://en.wikipedia.org/wiki/Griesmer_bound
same_as:
  wikidata: Q5608716
  wikipedia: Griesmer bound
---

## Statement

Let $q$ be a prime power, and let $C$ be a [[linear code|E85KREWV60]] over $\F_q$ with length $n$, dimension $k \ge 1$ and [[minimum distance|M2X88AXM17]] $d$.
Then
$$n \ge \sum_{i=0}^{k-1} \ceil{\frac{d}{q^i}}.$$

## Remarks

The proof is by induction on $k$.
Take a codeword $c$ of [[Hamming weight|K8ZHAQAK2B]] $d$ and delete the $d$ positions where $c$ is nonzero from all codewords.
The result is a linear code of length $n - d$ and dimension $k - 1$, the residual code, and a counting argument shows that its minimum distance is at least $\ceil{d/q}$.
The induction hypothesis then gives $n - d \ge \sum_{i=0}^{k-2} \ceil{d/q^{i+1}}$, which is the claim.
Since each term is at least $1$, the bound implies $n \ge d + k - 1$, the Singleton bound for linear codes.
Example: the binary $[7, 4, 3]$ Hamming code gives $3 + 2 + 1 + 1 = 7 = n$, and the binary simplex code $[2^k - 1, k, 2^{k-1}]$ gives $2^{k-1} + 2^{k-2} + \cdots + 1 = 2^k - 1 = n$; both meet the bound.
The statement is about linear codes: the proof uses the residual code, which is built with the linear structure.

## Explanations

### L1 human

The Griesmer bound tells how long a linear code must be to have a given dimension and a given minimum distance.
Each extra dimension costs a number of positions that shrinks geometrically, $d$, then $d/q$, then $d/q^2$, and so on.
Codes that meet it are as short as possible.

### L2 human

The Griesmer bound is a strengthening of the Singleton bound for linear codes, sharp for many small parameters.
Codes meeting it are called Griesmer codes; the simplex codes and many codes from projective geometry, such as those built from minihypers, are examples.
The question of which parameters admit Griesmer codes is studied with geometric methods in finite projective spaces.
