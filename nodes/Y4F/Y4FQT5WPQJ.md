---
tag: Y4FQT5WPQJ
kind: statement
role: lemma
name: Sauer–Shelah lemma
msc: [05D05, 68Q32]
uses: [14HX3QF45H, 0C21Q694AG, 0GBZM0MT0F]
about: [KCFXR9K3GD]
sources:
  - url: https://en.wikipedia.org/wiki/Sauer–Shelah_lemma
same_as:
  wikidata: Q17156650
  wikipedia: Sauer–Shelah lemma
---

## Statement

Let $X$ be a finite set with $n$ elements, let $d \ge 0$ be an integer, and let $\mathcal{F}$ be a [[family|0C21Q694AG]] of subsets of $X$.
Suppose that $\mathcal{F}$ has [[VC dimension|14HX3QF45H]] at most $d$, that is, no subset of $X$ with $d + 1$ elements is shattered by $\mathcal{F}$.
Then
$$|\mathcal{F}| \le \sum_{i=0}^{d} \binom{n}{i}.$$

## Remarks

A stronger statement holds: every family $\mathcal{F}$ shatters at least $|\mathcal{F}|$ subsets of $X$, where the empty set counts and is shattered by every nonempty family.
It is proved by induction on $n$, splitting $\mathcal{F}$ according to a fixed element $x$.
If the VC dimension is at most $d$, all shattered sets have at most $d$ elements, which gives the lemma.

The bound is sharp: for $d \le n$, the family of all subsets of $X$ with at most $d$ elements has VC dimension $d$ and exactly $\sum_{i \le d} \binom{n}{i}$ members.
For fixed $d$ the bound is a polynomial of degree $d$ in $n$, while $X$ has $2^n$ subsets.

## Explanations

### L1 human

If a family of sets cannot realise every pattern on any $d + 1$ points, then it is small: its size grows only like $n^d$ instead of $2^n$.
So a single local obstruction forces a strong global limit.

### L2 human

In learning theory, the lemma bounds the number of ways a class of classifiers with finite [[VC dimension|KCFXR9K3GD]] can label $n$ points.
This polynomial growth is the key step in the proof that such classes are learnable from a number of samples that depends on the dimension.
In combinatorial geometry it bounds the complexity of set systems such as half-planes, which leads to the existence of small $\varepsilon$-nets.
