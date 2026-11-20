---
tag: N3AC6Y96RZ
kind: example
name: Even cardinality is not first-order definable
aliases: [parity-is-not-first-order-definable, even-size-is-not-first-order]
msc: ["03C13", "03C07"]
topics: [N64R1MGDBN]
audience: grad
instance_of: [VT2PSXKM50]
uses: [VT2PSXKM50, X98C7KEQRV, ZZPXVVZARC, 72BMYXGFA8, 070R982G4B, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrenfeucht%E2%80%93Fra%C3%AFss%C3%A9_game
    locator: Equivalence and inexpressibility
  - url: https://en.wikipedia.org/wiki/Finite_model_theory
    locator: Characterisation of a class of structures
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Example

We show that no first-order sentence holds in exactly the [[finite|070R982G4B]] structures of even size, in two classes.

1. *Finite sets.* Let $L$ be empty, and suppose $\sigma$ has quantifier rank $n$ and holds in exactly the finite sets of even size.
2. Sets with $2n$ and $2n + 1$ elements both have at least $n$ elements. By [[the game on finite sets|X98C7KEQRV]] Duplicator wins $G_n$ on them.
3. By the [[Ehrenfeucht-Fraïssé theorem|72BMYXGFA8]] they agree on $\sigma$, but one has even and one odd size. This is a contradiction.
4. *Finite linear orders.* Let $L = \set{<}$, and suppose $\sigma$ has rank $n$ and holds in exactly the finite [[linear orders|0FRXBVVR03]] of even size.
5. The orders $L_{2^n}$ and $L_{2^n + 1}$ both have at least $2^n - 1$ elements. By the [[games on linear orders|ZZPXVVZARC]] Duplicator wins $G_n$ on them.
6. As in step 3, they agree on $\sigma$, and this is a contradiction.

So even size is not first-order definable on finite sets, and the order does not help.
This is an instance of the [[method of games|VT2PSXKM50]].

## Remarks

For finite sets, compactness gives a second proof.
If $\sigma$ held in exactly the even finite sets, $\sigma$ and $\neg\sigma$ would each hold in arbitrarily large finite sets, so each would have an infinite model.
The theory of infinite sets is complete, so this is impossible.
For finite linear orders this argument fails, since the infinite linear orders have many complete theories; the game argument does not need any infinite structure.

With the order, the sentences of rank $n$ count up to $2^n - 1$ instead of $n$, as in [[the counting sentences|7EPP1D7MGF]].
Counting further than any fixed bound is impossible in both cases.

## Explanations

### L1 human

A first-order sentence can count only up to a fixed number, set by how deeply its quantifiers are nested.
Beyond that number, it cannot tell one size from the next, so it cannot tell even from odd.
Putting the elements in a line helps the sentence count further, but still only up to a fixed number.

### L2 human

We follow Duplicator in $G_2(L_4, L_5)$, with virtual endpoints $0$ and $5$ in $L_4$, and $0$ and $6$ in $L_5$.

1. Round 1, with $r = 1$ round left after it: Spoiler picks $3 \in L_5$, at distance $3$ from both virtual ends. Duplicator picks $2 \in L_4$, at distance $2$ from $0$ and $3$ from $5$.
2. All distances are equal or both at least $2$.
3. Round 2: Spoiler picks $1 \in L_4$, below $2$. Duplicator picks $1 \in L_5$, below $3$. The pairs are ordered the same way, and Duplicator wins.

So $L_4 \equiv_2 L_5$, although $4$ is even and $5$ is odd.
A trap is to conclude that even size is undefinable in every logic; monadic second-order logic with order defines it, by guessing every second element.
