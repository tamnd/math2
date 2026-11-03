---
tag: G4C8XDKQVY
kind: definition
name: List decoding
msc: [94B35, 94B65]
defines: T88M6XTTRP
uses: [EFGYF9P0PN, EP5HNGSXFA, M2X88AXM17]
sources:
  - url: https://en.wikipedia.org/wiki/List_decoding
---

## Definition

Let $\Sigma$ be a finite alphabet, let $n \ge 1$, and let $C \subseteq \Sigma^n$ be a [[block code|EFGYF9P0PN]].
Let $\Delta$ denote the [[Hamming distance|EP5HNGSXFA]] on $\Sigma^n$, let $0 \le \rho \le 1$ and let $L \ge 1$ be an integer.
The code $C$ is *$(\rho, L)$-list decodable* if for every $y \in \Sigma^n$,
$$\abs{\set{c \in C : \Delta(c, y) \le \rho n}} \le L.$$
A *list decoding algorithm* for $C$ at radius $\rho$ takes $y \in \Sigma^n$ and outputs all $c \in C$ with $\Delta(c, y) \le \rho n$.

## Remarks

Example: if $C$ has [[minimum distance|M2X88AXM17]] $d$ and $\rho n \le (d - 1)/2$, then $C$ is $(\rho, 1)$-list decodable.
Indeed two codewords in one ball of radius $\rho n$ would be at distance at most $2\rho n \le d - 1$ by the triangle inequality.
So unique decoding is the case $L = 1$.

Non-example: $C = \F_2^n$ with $n \ge 2$ and $\rho = 1/n$ is not $(\rho, L)$-list decodable for $L < n + 1$, since the ball of radius $1$ around any word contains $n + 1$ codewords.

A list decoding algorithm is useful when $L$ is small, for instance bounded by a polynomial in $n$, so that the output can be written down efficiently.
