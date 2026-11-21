---
tag: T9VZWHERBR
kind: example
name: Amalgamation of finite linear orders
aliases: [amalgamation-of-finite-linear-orders]
msc: ["03C15", "06A05"]
topics: [ZS8X8KS54R]
audience: grad
instance_of: [XSCSX39GEZ]
uses: [XSCSX39GEZ, 2KBFZ1MPMW, 0FRXBVVR03, K4D3S1MBZH, SCRB74SWQN]
sources:
  - url: https://en.wikipedia.org/wiki/Fraïssé_limit
    locator: Examples
  - book: isbn:9780521587136
---

## Example

Let $\mathcal{L}$ be the class of finite [[linear orders|0FRXBVVR03]], in the signature $\set{<}$.
We show that $\mathcal{L}$ has the [[amalgamation property|XSCSX39GEZ]].

1. Let $f \colon A \to B$ and $g \colon A \to C$ be [[embeddings|SCRB74SWQN]], and list $A$ as $a_1 < \dots < a_k$.
2. Send $a_i$ to the rational number $i$; this gives the same values on $A$ for both maps below.
3. Each element of $B \setminus f(A)$ lies in one of the $k + 1$ open intervals cut out by $f(A)$.
4. Send the elements of $B$ in each interval to rationals in the matching interval of $\Q$, in increasing order. This uses that $\Q$ is [[dense|K4D3S1MBZH]] and has no endpoints.
5. Do the same for $C$, choosing rationals not already used for $B$.
6. Let $D$ be the union of the two images with the order of $\Q$. Both maps are embeddings and agree on $A$, so $D$ is an amalgam.

## Remarks

The images of $B$ and $C$ meet only in the image of $A$, so the amalgamation is strong.
It is not free: two new points $b \in B$ and $c \in C$ must be compared in $D$, so the amalgam adds a relation that neither $B$ nor $C$ contains.
Amalgams are not unique, since new points in the same interval can be interleaved in many ways.
The class $\mathcal{L}$ is the age of $(\Q, <)$, and $(\Q, <)$ is its Fraïssé limit.

## Explanations

### L1 human

Two finite chains share a common part.
Put the shared points on a line first.
Then slot the other points of each chain into the gaps where they belong.
Where both chains put points into the same gap, choose any interleaving; the result is still a chain.

### L2 human

We amalgamate over $A = \set{a}$.

1. Let $B = \set{a < b}$ and $C = \set{c < a}$.
2. Send $a \mapsto 0$, $b \mapsto 1$, $c \mapsto -1$.
3. The chain $-1 < 0 < 1$ contains $B$ and $C$, and both copies of $a$ go to $0$.

The typical use is to build $(\Q, <)$ as a Fraïssé limit.
A trap is to call the amalgamation free; the order between new points is extra information.
