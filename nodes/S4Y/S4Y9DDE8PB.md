---
tag: S4Y9DDE8PB
kind: definition
name: Cryptographic hash function
msc: [94A60, 68P25]
defines: XJ8F3NQMGN
uses: [K99S0Q0814, RA37YDW2TY, 0KVGH0J5B3, 0HJHYMGN3C]
sources:
  - url: https://en.wikipedia.org/wiki/Cryptographic_hash_function
---

## Definition

Let $\lambda$ be the security parameter and let $\ell(\lambda)$ be a polynomial.
A *hash function family* is a pair $(\mathsf{Gen}, H)$ of algorithms that run in polynomial time, with the following properties.
The [[probabilistic algorithm|K99S0Q0814]] $\mathsf{Gen}(1^\lambda)$ outputs a key $s$.
For each key $s$, $H_s$ maps strings of some input domain to $\set{0,1}^{\ell(\lambda)}$, and the domain contains strings longer than $\ell(\lambda)$.
The family is a *cryptographic hash function*, or *collision resistant*, if the following holds.
For each probabilistic polynomial-time adversary $A$, the probability is negligible that $A(s)$ outputs $x \ne x'$ with $H_s(x) = H_s(x')$, where $s = \mathsf{Gen}(1^\lambda)$.
A function $\nu$ is negligible if $\nu(\lambda) < 1/p(\lambda)$ for every polynomial $p$ and all large $\lambda$.

## Remarks

Two weaker properties are also used.
Second-preimage resistance: given $s$ and a random $x$, it is hard to find $x' \ne x$ with $H_s(x') = H_s(x)$.
Preimage resistance: given $s$ and $H_s(x)$ for a random $x$, it is hard to find any preimage, so that $H_s$ is a [[one-way function|RA37YDW2TY]].
Collision resistance implies second-preimage resistance.

Example: let $G$ be a [[cyclic group|0KVGH0J5B3]] of prime order $q$ with generators $g$ and $h$ chosen by $\mathsf{Gen}$, and set $H(x_1, x_2) = g^{x_1} h^{x_2}$ for $x_1, x_2 \in \Z/q\Z$.
Its input is two elements of $\Z/q\Z$ and its output is one element of $G$, so with a compact encoding of $G$ it roughly halves the length.
A collision $g^{x_1} h^{x_2} = g^{x_1'} h^{x_2'}$ with $(x_1, x_2) \ne (x_1', x_2')$ forces $x_2 \ne x_2'$, and gives $\log_g h = (x_1 - x_1')/(x_2' - x_2)$ modulo $q$.
So the family is collision resistant if the [[discrete logarithm|0HJHYMGN3C]] in $G$ is hard.

Non-example: $H(x) = $ the last $\ell$ bits of $x$ is not collision resistant, since $0x$ and $1x$ collide for any $x$ of length $\ell$.
