---
tag: G2X3PKG55F
kind: example
name: A neighborhood model in which axiom K fails
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [CN7HK9K1B6]
not_instance_of:
  - target: NGHWZ9Y7ZV
    note: N(a) neither contains W nor is closed under intersections, so no relation gives this frame
  - target: XBCYFDPS2F
    note: the box is read by a set of neighborhoods, and no accessibility relation gives the same truth sets
  - target: D1TJYZZDCY
    note: axiom K and necessitation fail on the frame, so its logic is not normal
uses: [CN7HK9K1B6, NGHWZ9Y7ZV, XBCYFDPS2F, D1TJYZZDCY, G989VP2NGP]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: lead section
---

## Example

At world $a$, both "$p$" and "if $p$ then $q$" count as necessary, and still "$q$" does not.
A neighborhood frame makes this possible.
It is a pair $(W, N)$ where $N$ assigns to each world $w$ a set $N(w)$ of subsets of $W$.
In [[neighborhood semantics|CN7HK9K1B6]], $\square\varphi$ is true at $w$ when $[\![ \varphi ]\!] \in N(w)$.
Take this model:
$$W = \{ a, b \}, \quad N(a) = \{ \{ a \}, \{ b \} \}, \quad N(b) = \varnothing, \quad V(p) = \{ a \}, \quad V(q) = \varnothing.$$

1. $[\![ p ]\!] = \{ a \}$ and $[\![ q ]\!] = \varnothing$, by the valuation.
2. $[\![ p \to q ]\!] = (W \setminus \{ a \}) \cup \varnothing = \{ b \}$.
3. $\square p$ is true at $a$, since $\{ a \} \in N(a)$.
4. $\square(p \to q)$ is true at $a$, since $\{ b \} \in N(a)$.
5. $\square q$ is false at $a$, since $\varnothing \notin N(a)$.
6. So axiom $\mathrm{K}$, $\square(p \to q) \to (\square p \to \square q)$, fails at $a$.
7. $\square\top$ is false at $a$, since $[\![ \top ]\!] = W \notin N(a)$.
   The formula $\top$ is valid, so [[necessitation|G989VP2NGP]] fails on this frame.
8. The rule RE holds.
   If $\varphi \leftrightarrow \psi$ is true at every world, then $[\![ \varphi ]\!] = [\![ \psi ]\!]$, so $\square\varphi$ and $\square\psi$ have the same truth value at each world.
9. No relation gives $N(a)$.
   A [[Kripke frame|NGHWZ9Y7ZV]] corresponds to $N(a) = \{ X : R[a] \subseteq X \}$, and this family contains $W$ and is closed under intersection.
10. Here $W \notin N(a)$, and $\{ a \} \cap \{ b \} = \varnothing \notin N(a)$, so both properties fail.

## Remarks

The example shows that neighborhood semantics validates fewer formulas than Kripke semantics.
Each failure matches a missing closure property of $N(a)$.
Closure under intersections and supersets would give $\mathrm{K}$, and $W \in N(a)$ would give necessitation.
The formulas valid on all neighborhood frames form the smallest classical modal logic $\mathsf{E}$.
This logic is closed under RE but is not a [[normal modal logic|D1TJYZZDCY]].

What if $N(a)$ and $N(b)$ are both the family of all subsets of $W$?
Then every $\square\varphi$ is true everywhere.
This is the model of the empty [[accessibility relation|XBCYFDPS2F]], so $\mathrm{K}$ and necessitation hold again.
What if you only add $\varnothing$ and $W$ to $N(a)$?
Then $\mathrm{K}$ holds at $a$, but $\square\top$ still fails at $b$, since $N(b)$ is empty.

## Explanations

### L1 human

In neighborhood semantics, each world keeps a list of "necessary" sets of worlds.
A statement is necessary at a world when the set of worlds where it holds is on the list.
At world $a$ the list has the sets $\{ a \}$ and $\{ b \}$, but not the empty set.
So "$p$" and "if $p$ then $q$" are both necessary at $a$, while "$q$" is not.
The usual rule "necessary premises give a necessary conclusion" breaks.

### L2 human

We find a second failure of normality on the same frame.

1. Take the formula $\square p \wedge \square\neg p$.
2. $[\![ \neg p ]\!] = \{ b \} \in N(a)$, and $[\![ p ]\!] = \{ a \} \in N(a)$.
3. So $\square p \wedge \square\neg p$ is true at $a$, while $\square\bot$ is false at $a$, since $\varnothing \notin N(a)$.
4. In $\mathsf{K}$, $\square p \wedge \square\neg p \to \square\bot$ is a theorem, so this is another failure of normality.

You use neighborhood models for logics where the box is not normal, for example logics of ability or of agency.
Watch out: neighborhood semantics still validates RE, so $\square\varphi$ and $\square\psi$ always agree when $\varphi$ and $\psi$ are classically equivalent.
