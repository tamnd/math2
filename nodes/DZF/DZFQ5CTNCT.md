---
tag: DZFQ5CTNCT
kind: definition
name: Raptor code
msc: [94B60, 68P30]
defines: W1MPPTS4ED
uses: [6G24FVAKZX, E85KREWV60, ESYMTB37YG]
sources:
  - url: https://en.wikipedia.org/wiki/Raptor_code
---

## Definition

Let $1 \le k \le n$, and let $\mathcal{C}$ be a binary [[linear code|E85KREWV60]] of length $n$ and dimension $k$, the precode.
Let $E \colon \F_2^k \to \F_2^n$ be an encoding map of $\mathcal{C}$, and let $\Omega$ be a probability distribution on $\set{1, \dots, n}$.
Symbols are elements of $\F_2^{\ell}$, and $E$ acts on lists of $k$ symbols coordinate by coordinate.
The *Raptor code* with parameters $(k, \mathcal{C}, \Omega)$ encodes input symbols $x_1, \dots, x_k$ as follows.

1. Compute the intermediate symbols $(z_1, \dots, z_n) = E(x_1, \dots, x_k)$.
2. Apply the [[LT code|6G24FVAKZX]] with degree distribution $\Omega$ to $z_1, \dots, z_n$ to produce the output stream.

## Remarks

Decoding first runs LT peeling on the received symbols to recover part of the intermediate symbols.
Then it decodes the precode, treating the unknown intermediate symbols as erasures on an [[erasure channel|ESYMTB37YG]].
Shokrollahi showed that suitable precodes and degree distributions of constant average degree work well.
The receiver then recovers the input from slightly more than $k$ output symbols with high probability.
The cost is a constant number of operations per symbol for each fixed overhead.

Example: with the trivial precode $n = k$ and $E = \id$, a Raptor code is just the LT code with distribution $\Omega$; the LT codes are the special case without precode.

Non-example: applying an LT code first and an erasure code to its output second does not give a Raptor code.
The order of the layers matters: the precode acts on the input before the LT layer.
