---
tag: 6JXBZ2C9B4
kind: example
name: Truth sets in a three-world Kripke model
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [NGHWZ9Y7ZV]
uses: [NGHWZ9Y7ZV, XBCYFDPS2F, G8VGTW9P4F]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: lead section
---

## Example

Take the [[Kripke model|NGHWZ9Y7ZV]] $\mathfrak{M} = (W, R, V)$ with
$$W = \set{1, 2, 3}, \quad R = \set{(1, 2), (1, 3), (2, 2)}, \quad V(p) = \set{2}, \quad V(q) = \set{1, 3}.$$
The successor sets of the [[accessibility relation|XBCYFDPS2F]] are $R[1] = \set{2, 3}$, $R[2] = \set{2}$ and $R[3] = \varnothing$.
A world is in $[\![ \square\varphi ]\!]$ when its successor set lies inside $[\![ \varphi ]\!]$, and in $[\![ \lozenge\varphi ]\!]$ when its successor set meets $[\![ \varphi ]\!]$.

1. $[\![ \square p ]\!] = \set{2, 3}$. $R[1] \not\subseteq \set{2}$ since $3 \notin V(p)$, $R[2] = \set{2} \subseteq \set{2}$, and $R[3] = \varnothing$.
2. $[\![ \lozenge p ]\!] = \set{1, 2}$. Both $R[1]$ and $R[2]$ contain $2$, and $R[3]$ is empty.
3. $[\![ \lozenge q ]\!] = \set{1}$. $R[1]$ contains $3 \in V(q)$, while $R[2] = \set{2}$ misses $V(q)$.
4. $[\![ \square\lozenge p ]\!] = \set{2, 3}$. $R[1]$ contains $3 \notin [\![ \lozenge p ]\!]$, and $R[2] = \set{2} \subseteq \set{1, 2}$.
5. $[\![ \lozenge\square p ]\!] = \set{1, 2}$. $R[1]$ and $R[2]$ both meet $\set{2, 3}$, and $R[3]$ is empty.
6. $[\![ \square q ]\!] = \set{3}$. $R[1]$ and $R[2]$ contain $2 \notin V(q)$, and $R[3]$ is empty.
7. $[\![ p \vee q ]\!] = \set{2} \cup \set{1, 3} = W$.
8. $[\![ \square(p \vee q) ]\!] = W$, since every successor set lies inside $W$.
9. $[\![ \square p \vee \square q ]\!] = \set{2, 3} \cup \set{3} = \set{2, 3}$.
10. So $\square(p \vee q) \to (\square p \vee \square q)$ fails at $1$: the box of a disjunction does not split into a disjunction of boxes.

## Remarks

The example shows how truth sets are computed from the inside out, one subformula at a time.
World $3$ has no successors, so every formula $\square\varphi$ is true at $3$ and every formula $\lozenge\varphi$ is false at $3$.
The formulas $p \vee q$ and $\square(p \vee q)$ are true in the model, that is at every world.
They are not valid on the frame: with $V(p) = V(q) = \varnothing$, both are false at $1$.
If we add the pair $(1, 1)$, then $\square q$ is still false at $1$, since $2 \in R[1]$ and $2 \notin V(q)$.
If we put $3$ into $V(p)$, then $1 \in [\![ \square p ]\!]$, and the failure in step 10 disappears.

## Explanations

### L1 human

Think of three rooms with one-way doors: room 1 opens to rooms 2 and 3, and room 2 opens to itself.
A lamp $p$ is on in room 2 only.
"Box $p$" in a room means the lamp is on in every room behind its doors.
In room 1 this fails, since room 3 is dark.
Room 3 has no doors, so "box" statements hold there for free.

### L2 human

1. Compute $[\![ \lozenge q \to \square p ]\!]$.
2. From step 3, $[\![ \lozenge q ]\!] = \set{1}$, and from step 1, $[\![ \square p ]\!] = \set{2, 3}$.
3. The implication fails exactly where $\lozenge q$ holds and $\square p$ fails, that is at $1$.
4. So $[\![ \lozenge q \to \square p ]\!] = \set{2, 3}$.

The typical use of such a table is to find a countermodel for a formula that is not a theorem.
A trap: a formula true at every world of one model need not be valid on the frame, since validity quantifies over all valuations.
