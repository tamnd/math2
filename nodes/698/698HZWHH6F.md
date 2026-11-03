---
tag: 698HZWHH6F
kind: statement
role: theorem
name: Luby–Rackoff theorem
msc: [94A60, 68P25, 68Q87]
uses: [JWVE27832R, K99S0Q0814, Z5CCVBME2V, 05RWFKVTJ7, MD9THSA21A]
about: [JWVE27832R]
sources:
  - url: https://en.wikipedia.org/wiki/Feistel_cipher
---

## Statement

Let $n$ be the security parameter.
A keyed family of functions $f_s \colon \set{0,1}^n \to \set{0,1}^n$, computable in polynomial time, is *pseudorandom* if the following holds.
For each [[probabilistic Turing machine|K99S0Q0814]] $A$ that runs in polynomial time with [[oracle|Z5CCVBME2V]] access, the advantage $\abs{\Pr[A^{f_s}(1^n) = 1] - \Pr[A^{g}(1^n) = 1]}$ is negligible in $n$.
Here $s$ is a uniform key and $g$ is a uniform random function.
A *negligible* function is one that is smaller than $1/p(n)$ for every polynomial $p$ and all large $n$.
A keyed family of [[permutations|05RWFKVTJ7]] is a pseudorandom permutation if the same holds with $g$ a uniform random permutation.
It is a strong pseudorandom permutation if this holds even when $A$ may also query the inverse permutation.

1. Let $F_1, F_2, F_3$ be drawn with independent keys from a pseudorandom function family. Then the three-round [[Feistel network|JWVE27832R]] with these round functions is a pseudorandom permutation of $\set{0,1}^{2n}$.
2. With four rounds and independent keys, the Feistel network is a strong pseudorandom permutation.

## Remarks

The core of the proof is the case of truly random round functions.
There, an adversary making $q$ queries distinguishes the network from a random permutation with advantage $O(q^2 / 2^n)$.
The adversary can only win if two queries collide in an internal half-block.
Replacing the random functions by pseudorandom ones changes the advantage only negligibly, by a hybrid argument.

Two rounds do not suffice.
For two inputs $(L, R)$ and $(L', R)$ with the same right half, the left halves of the outputs are $L \oplus F_1(R)$ and $L' \oplus F_1(R)$.
Their sum is $L \oplus L'$, which a random permutation gives only with probability about $2^{-n}$.
Three rounds are not a strong pseudorandom permutation: an attack that also queries the inverse breaks them.

## Explanations

### L1 human

A block cipher should look like a random shuffle of all possible blocks to anyone who cannot see the key.
Michael Luby and Charles Rackoff showed how to build such a shuffle from random-looking functions that need not be invertible.
Three Feistel rounds are enough against an attacker who only encrypts, and four are enough against one who may also decrypt.

### L2 human

The theorem justifies the Feistel design of ciphers such as DES in an idealized model.
It turns a pseudorandom function family, which exists if [[pseudorandom generators|MD9THSA21A]] exist, into a pseudorandom permutation family.
Together with the construction of pseudorandom functions from pseudorandom generators, it shows that block ciphers in this sense exist if one-way functions exist.
