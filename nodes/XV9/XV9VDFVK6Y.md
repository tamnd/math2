---
tag: XV9VDFVK6Y
kind: definition
name: P
msc: [68Q15]
defines: GVT2NKN37K
uses: [ESPYW94XGR, YK3HD56R3G, T00W8RQT8E, 5MFZ4VNY6D]
sources:
  - url: https://en.wikipedia.org/wiki/P_(complexity)
---

## Definition

Let $\Sigma$ be a finite alphabet.
Let $t \colon \N \to \N$ be a function.
The class $\mathrm{DTIME}(t)$ is the set of [[languages|5MFZ4VNY6D]] $L \subseteq \Sigma^*$ decided by some deterministic [[multitape Turing machine|YK3HD56R3G]] $M$ as follows.
On every input of length $n$, the machine $M$ halts within $O(t(n))$ steps.
The [[complexity class|ESPYW94XGR]] *P* is
$$\mathrm{P} = \bigcup_{k \in \N} \mathrm{DTIME}(n^k).$$
So $L \in \mathrm{P}$ when some deterministic Turing machine decides $L$ with [[time complexity|T00W8RQT8E]] $O(n^k)$ for some $k$.

## Remarks

Example: the language of binary palindromes belongs to the class P, as follows.
A two-tape machine copies the input to its work tape, moves the input head back to the start, and compares the input read forward with the copy read backward.
This takes $O(n)$ steps.

Non-example: a machine that solves a problem by testing all $2^n$ subsets of an $n$-element set uses about $2^n$ steps, and $2^n$ is not $O(n^k)$ for any $k$.
Such a machine does not show that its problem is in P, though a faster algorithm might exist.

The class is the same for one-tape and multitape machines, since a one-tape machine simulates $t$ steps of a multitape machine in $O(t^2)$ steps.
P is closed under union, intersection, complement and concatenation of languages.
