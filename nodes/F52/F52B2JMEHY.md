---
tag: F52B2JMEHY
kind: statement
role: lemma
name: Fitting's lemma
msc: [16D70, 16S50]
uses: [09VDS2W1E8, 0RGZ10DFPG, V6JBKT168T, AWSBZWWMG9, E2P29GCD9T]
about: [AWSBZWWMG9]
sources:
  - url: https://en.wikipedia.org/wiki/Fitting_lemma
same_as:
  wikidata: Q3229338
  wikipedia: Fitting lemma
---

## Statement

Let $R$ be a ring, let $M$ be a left [[$R$-module|09VDS2W1E8]] of [[finite length|V6JBKT168T]], and let $f \in \End_R(M)$ be an element of its [[endomorphism ring|AWSBZWWMG9]].
Then there is an integer $n \ge 1$ such that:

1. $M = \im f^n \oplus \ker f^n$, a direct sum of [[submodules|0RGZ10DFPG]];
2. the restriction of $f$ to $\im f^n$ is an automorphism of $\im f^n$;
3. the restriction of $f$ to $\ker f^n$ is nilpotent.

In particular, if $M$ is [[indecomposable|E2P29GCD9T]], then every endomorphism of $M$ is either an automorphism or nilpotent.

## Remarks

A module of finite length is both Noetherian and Artinian.
So the chain $\ker f \subseteq \ker f^2 \subseteq \cdots$ and the chain $\im f \supseteq \im f^2 \supseteq \cdots$ both become constant, say from step $n$ on.
If $x \in \im f^n \cap \ker f^n$, then $x = f^n(y)$ with $f^{2n}(y) = 0$, so $y \in \ker f^{2n} = \ker f^n$ and $x = 0$.
For $x \in M$, pick $z$ with $f^n(x) = f^{2n}(z)$; then $x = f^n(z) + (x - f^n(z))$ splits $x$ into the two parts.
For an indecomposable $M$ the corollary shows that the non-invertible endomorphisms form an ideal, so $\End_R(M)$ is a local ring.
Finite length is needed: multiplication by $2$ on the indecomposable $\Z$-module $\Z$ is neither an automorphism nor nilpotent.

## Explanations

### L1 human

Repeat a self-map of a module of finite length many times.
Eventually the module splits into two parts: on one part the map keeps shuffling elements bijectively, and on the other it pushes everything to zero.
If the module cannot be split at all, only one of these behaviours can occur.

### L2 human

Fitting's lemma is the module version of the splitting of a linear map of a finite-dimensional space into an invertible part and a nilpotent part.
Its main use is the corollary that the endomorphism ring of an indecomposable module of finite length is local.
This locality is exactly what the proof of the [[Krull–Schmidt theorem|94M0BPV1W4]] needs.
