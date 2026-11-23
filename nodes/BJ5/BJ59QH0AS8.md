---
tag: BJ59QH0AS8
kind: example
name: A Kripke frame as a neighborhood frame
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [CN7HK9K1B6]
uses: [CN7HK9K1B6, RT7QEGZSTQ, NGHWZ9Y7ZV, XBCYFDPS2F, 00E0YZCERH]
sources:
  - url: https://en.wikipedia.org/wiki/Neighborhood_semantics
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Semantics of modal logic
---

## Example

Take the [[Kripke frame|NGHWZ9Y7ZV]] with $W = \{ a, b \}$ and $R = \{ (a, b), (b, a), (b, b) \}$.
Its successor sets are $R[a] = \{ b \}$ and $R[b] = \{ a, b \}$.
We define a [[neighborhood frame|RT7QEGZSTQ]] on $W$ by $N(w) = \{ X \subseteq W : R[w] \subseteq X \}$.

1. The subsets of $W$ are $\varnothing$, $\{ a \}$, $\{ b \}$ and $W$, the four members of the [[power set|00E0YZCERH]].
2. $N(a)$ contains the subsets that contain $b$, so $N(a) = \{ \{ b \}, W \}$.
3. $N(b)$ contains the subsets that contain $a$ and $b$, so $N(b) = \{ W \}$.
4. Both $N(a)$ and $N(b)$ contain $W$.
5. For supersets, the only superset of $\{ b \}$ other than itself is $W$, which is in $N(a)$, and the only superset of $W$ is $W$.
6. For intersections, $\{ b \} \cap W = \{ b \}$ is in $N(a)$, and in $N(b)$ we have $W \cap W = W$.
7. So each $N(w)$ contains $W$ and is closed under supersets and intersections.

Now compare the two truth conditions for $\square p$.
In Kripke semantics, $w \models \square p$ exactly when $R[w] \subseteq V(p)$.
In neighborhood semantics, $w \models \square p$ exactly when $V(p) \in N(w)$.

8. For $V(p) = \varnothing$, neither $\{ b \}$ nor $W$ is a subset of $\varnothing$, so $\square p$ fails at $a$ and $b$ in Kripke semantics.
   In neighborhood semantics, $\varnothing$ is in neither $N(a)$ nor $N(b)$.
9. For $V(p) = \{ a \}$, neither $\{ b \}$ nor $W$ is a subset of $\{ a \}$, so $\square p$ fails at both worlds.
   In neighborhood semantics, $\{ a \}$ is in neither set.
10. For $V(p) = \{ b \}$, $\{ b \} \subseteq \{ b \}$ but $W \not\subseteq \{ b \}$, so $\square p$ holds at $a$ only.
    In neighborhood semantics, $\{ b \} \in N(a)$ and $\{ b \} \notin N(b)$.
11. For $V(p) = W$, $\square p$ holds at both worlds in Kripke semantics, and $W$ is in both sets.
12. So the two semantics agree on $\square p$ for all four valuations.

## Remarks

The agreement is general: $R[w] \subseteq [\![ \varphi ]\!]$ holds exactly when $[\![ \varphi ]\!] \in N(w)$, by the definition of $N$.
So an induction on formulas shows that the two semantics give the same truth sets for every formula.

Conversely, take a finite set and a neighborhood function that contains $W$ and is closed under supersets and intersections.
It comes from the relation with $R[w] = \bigcap N(w)$.
Here $\bigcap N(a) = \{ b \}$ and $\bigcap N(b) = W$, which gives back $R$.
So [[neighborhood semantics|CN7HK9K1B6]] extends Kripke semantics, and the extra frames are the ones that fail one of the closure conditions.

What if you drop the pair $(b, a)$?
Then $R[b] = \{ b \}$, and $N(b)$ grows to $\{ \{ b \}, W \}$.

## Explanations

### L1 human

In a Kripke frame, a world sees some worlds, and "necessarily $p$" means $p$ holds at all of them.
In a neighborhood frame, a world has a list of "necessary" sets of worlds.
From a Kripke frame we can make this list: all sets that contain everything the world sees.
Then both readings give the same answer, as we checked for each of the four choices of where $p$ holds.

### L2 human

The computation takes three steps.
First compute the successor sets $R[a] = \{ b \}$ and $R[b] = W$.
Then list their supersets, which gives $N(a) = \{ \{ b \}, W \}$ and $N(b) = \{ W \}$.
Finally, for $V(p) = \{ b \}$, $\square p$ holds at $a$ and fails at $b$ in both semantics.

You use this construction to see that every Kripke frame is a special neighborhood frame.
Watch out: on an infinite set, closure under finite intersections is not enough, and the neighborhoods must contain the intersection of all of them.

### L3 human

A neighborhood frame that is closed under supersets and under arbitrary intersections, and contains $W$, is augmented.
Augmented neighborhood frames are exactly the frames of the form $N(w) = \{ X : R[w] \subseteq X \}$.
The frames with (m), (c) and (n), which are closed only under finite intersections, validate $\mathsf{K}$ but include frames that are not Kripke frames.
