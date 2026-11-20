---
tag: X98C7KEQRV
kind: example
name: The Ehrenfeucht-Fraïssé game on two finite sets
aliases: [ehrenfeucht-fraisse-game-on-pure-sets]
msc: ["03C07", "03C13"]
topics: [N64R1MGDBN]
audience: ug2
instance_of: [2RE7YAZK8R]
uses: [2RE7YAZK8R, 1DVRN1T2Z0, 070R982G4B, FVEVRE5XNZ]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrenfeucht%E2%80%93Fra%C3%AFss%C3%A9_game
    locator: Definition
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Example

Let $L$ be the empty signature, so a structure is a nonempty set, and the only atomic formulas are equations $x = y$.
Let $A$ and $B$ be sets with $m$ and $k$ elements, where $m$ or $k$ may be infinite, and let $n \ge 1$.
We show that Duplicator wins the [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]] $G_n(A, B)$ if and only if $m = k$, or $m \ge n$ and $k \ge n$.

1. A play is won by Duplicator when $a_i = a_j \iff b_i = b_j$ for all rounds $i, j$, since equality is the only relation.
2. If $m = k$, Duplicator fixes a bijection $f \colon A \to B$, answers $a$ by $f(a)$ and $b$ by $f^{-1}(b)$. Every play satisfies step 1.
3. Let $m, k \ge n$. In a round, if Spoiler picks an element chosen before, Duplicator answers with its partner from that earlier round.
4. Otherwise Duplicator answers with an element not chosen before on the other side. Before round $i \le n$ at most $i - 1 < n$ elements are chosen on each side, so one is free. The equalities then match.
5. Let $m < k$ and $m < n$. Spoiler picks $m + 1$ distinct elements of $B$, in rounds $1$ to $m + 1 \le n$. Duplicator must answer with $m + 1$ distinct elements of $A$, and $A$ has only $m$. So Spoiler wins.

## Remarks

By the [[Ehrenfeucht-Fraïssé theorem|72BMYXGFA8]], sets with $m$ and $k$ elements satisfy the same sentences of [[quantifier rank|FVEVRE5XNZ]] at most $n$ if and only if $m = k$ or both are at least $n$.
So no first-order sentence in the empty signature separates all even sizes from all odd sizes; see [[this example|N3AC6Y96RZ]].
Step 5 is the game form of the [[counting sentence|7EPP1D7MGF]] $\sigma_{\ge m+1}$, which has rank $m + 1$.

## Explanations

### L1 human

When the sets carry no structure, the only thing Duplicator must keep straight is which chosen elements are the same.
Duplicator copies a repeat with a repeat and a new element with a new element.
This works as long as neither set runs out of new elements.
A set with $m$ elements runs out after $m$ rounds, and Spoiler wins once there are more rounds than that and the other set is larger.

### L2 human

We play $G_3$ on $A = \set{1, 2}$ and $B = \set{1, 2, 3}$.

1. Here $m = 2 < 3 = n$ and $m < k$, so Spoiler should win.
2. Round 1: Spoiler picks $1 \in B$, and Duplicator answers $1 \in A$.
3. Round 2: Spoiler picks $2 \in B$. Duplicator must answer a new element, $2 \in A$.
4. Round 3: Spoiler picks $3 \in B$. Both elements of $A$ are used, and any answer repeats one, so Spoiler wins.

With only $2$ rounds Duplicator wins, by step 3 and step 4, since both sets have at least $2$ elements.
A trap is to think that Duplicator needs a bijection; for $n \le \min(m, k)$ fresh answers suffice.
