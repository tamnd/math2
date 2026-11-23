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

Take the [[Kripke model|NGHWZ9Y7ZV]] $\mathfrak{M} = (W, R, V)$ given by these data:
$$W = \{ 1, 2, 3 \}, \quad R = \{ (1, 2), (1, 3), (2, 2) \}, \quad V(p) = \{ 2 \}, \quad V(q) = \{ 1, 3 \}.$$
The successor sets of the [[accessibility relation|XBCYFDPS2F]] are $R[1] = \{ 2, 3 \}$, $R[2] = \{ 2 \}$ and $R[3] = \varnothing$.
A world is in $[\![ \square\varphi ]\!]$ when its successor set lies inside $[\![ \varphi ]\!]$, and in $[\![ \lozenge\varphi ]\!]$ when its successor set meets $[\![ \varphi ]\!]$.
We compute the truth sets from the inside out.

1. $[\![ \square p ]\!] = \{ 2, 3 \}$.
   World $1$ fails because $3 \in R[1]$ and $3 \notin V(p)$, world $2$ passes because $R[2] = \{ 2 \}$, and world $3$ passes because $R[3]$ is empty.
2. $[\![ \lozenge p ]\!] = \{ 1, 2 \}$.
   Both $R[1]$ and $R[2]$ contain $2$, and $R[3]$ is empty.
3. $[\![ \lozenge q ]\!] = \{ 1 \}$.
   $R[1]$ contains $3 \in V(q)$, while $R[2] = \{ 2 \}$ misses $V(q)$.
4. $[\![ \square\lozenge p ]\!] = \{ 2, 3 \}$.
   $R[1]$ contains $3 \notin [\![ \lozenge p ]\!]$, while $R[2] = \{ 2 \} \subseteq \{ 1, 2 \}$.
5. $[\![ \lozenge\square p ]\!] = \{ 1, 2 \}$.
   $R[1]$ and $R[2]$ both meet $\{ 2, 3 \}$, and $R[3]$ is empty.
6. $[\![ \square q ]\!] = \{ 3 \}$.
   $R[1]$ and $R[2]$ contain $2 \notin V(q)$, and $R[3]$ is empty.
7. $[\![ p \vee q ]\!] = \{ 2 \} \cup \{ 1, 3 \} = W$.
8. $[\![ \square(p \vee q) ]\!] = W$, since every successor set lies inside $W$.
9. $[\![ \square p \vee \square q ]\!] = \{ 2, 3 \} \cup \{ 3 \} = \{ 2, 3 \}$.
10. So $\square(p \vee q) \to (\square p \vee \square q)$ fails at $1$.

## Remarks

Step 10 shows that the box of a disjunction does not split into a disjunction of boxes.
At world $1$ every successor has $p$ or $q$, but neither variable holds at all successors: $2$ has only $p$ and $3$ has only $q$.

World $3$ has no successors, so every formula $\square\varphi$ is true at $3$ and every formula $\lozenge\varphi$ is false at $3$.
That is why $3$ is in $[\![ \square p ]\!]$ and in $[\![ \square q ]\!]$ at the same time.

The formulas $p \vee q$ and $\square(p \vee q)$ are true in the model, at every world.
They are not valid on the frame, since with $V(p) = V(q) = \varnothing$ both are false at $1$.

What changes if we change the data?
If we add the pair $(1, 1)$, then $\square q$ is still false at $1$, since $2 \in R[1]$ and $2 \notin V(q)$.
If we put $3$ into $V(p)$, then $R[1] = \{ 2, 3 \} \subseteq V(p)$, so $1 \in [\![ \square p ]\!]$, and the failure in step 10 disappears.

## Explanations

### L1 human

Think of three rooms with one-way doors: room 1 opens to rooms 2 and 3, and room 2 opens to itself.
A lamp $p$ is on in room 2 only.
"Box $p$" in a room means that the lamp is on in every room behind its doors.
In room 1 this fails, since room 3 is dark.
Room 3 has no doors, so every "box" statement holds there for free.

### L2 human

We compute the truth set of $\lozenge q \to \square p$.
From step 3, $[\![ \lozenge q ]\!] = \{ 1 \}$, and from step 1, $[\![ \square p ]\!] = \{ 2, 3 \}$.
The implication fails exactly where $\lozenge q$ holds and $\square p$ fails, and that happens only at $1$:
$$[\![ \lozenge q \to \square p ]\!] = W \setminus \{ 1 \} = \{ 2, 3 \}.$$
The typical use of such a table is to find a countermodel for a formula that is not a theorem.
Watch out: a formula true at every world of one model need not be valid on the frame, since validity on the frame quantifies over all valuations.
