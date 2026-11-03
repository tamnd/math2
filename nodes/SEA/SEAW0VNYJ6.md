---
tag: SEAW0VNYJ6
kind: definition
name: Weyl's unitary trick
msc: ["22E46", 17B10]
defines: DDQ2WBQ9GB
uses: [9TFC6ADC1C, WYGRXCG2RN]
sources:
  - url: https://en.wikipedia.org/wiki/Unitarian_trick
---

## Definition

Let $\mathfrak{g}$ be a complex [[semisimple Lie algebra|EY9DN7QAX1]].
*Weyl's unitary trick* is the method of studying the finite-dimensional complex representations of $\mathfrak{g}$ through the following steps:

1. choose a compact real form $\mathfrak{k}$ of $\mathfrak{g}$, that is, a real Lie subalgebra with $\mathfrak{g} = \mathfrak{k} \oplus i\mathfrak{k}$ whose Killing form is negative definite;
2. restrict from $\mathfrak{g}$ to $\mathfrak{k}$, a bijection from complex representations of $\mathfrak{g}$ to representations of $\mathfrak{k}$ on complex spaces that keeps invariant subspaces;
3. pass to the simply connected Lie group $K$ with [[Lie algebra|WKVBS76432]] $\mathfrak{k}$, a [[compact Lie group|9TFC6ADC1C]] to whose [[representations|WYGRXCG2RN]] those of $\mathfrak{k}$ integrate;
4. prove the desired property for representations of the compact group $K$, for example by averaging over its Haar measure, and transfer it back to $\mathfrak{g}$.

## Remarks

Example: for $\mathfrak{g} = \mathfrak{sl}(2, \C)$, one takes $\mathfrak{k} = \mathfrak{su}(2)$ and $K = SU(2)$.
Complete reducibility of representations of $SU(2)$, proved by averaging an inner product, gives complete reducibility of finite-dimensional representations of $\mathfrak{sl}(2, \C)$.
Non-example: the real form $\mathfrak{sl}(2, \R)$ of $\mathfrak{sl}(2,\C)$ cannot replace $\mathfrak{k}$ in step 3, because every connected Lie group with Lie algebra $\mathfrak{sl}(2,\R)$, such as $SL(2,\R)$, is not compact.
The same method applies to a connected complex semisimple Lie group $G$ with a compact real form $K$, using holomorphic representations of $G$.
In step 3, the integrated representation of $K$ has the same invariant subspaces as the representation of $\mathfrak{k}$.
The compactness of $K$ in step 3 is a theorem of Weyl.
It says that a connected Lie group whose Lie algebra has a negative definite Killing form is compact, and so is its universal cover.
