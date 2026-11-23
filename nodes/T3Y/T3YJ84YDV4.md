---
tag: T3YJ84YDV4
kind: example
name: The successor chain maps onto a reflexive point
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: grad
instance_of: [X27BR4YP2Y]
uses: [7T740SFHHV, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Model constructions
---

## Example

An infinite staircase and a single point with a loop look the same from inside, and a bounded morphism proves it.
Let $\mathfrak{N} = (\mathbb{N}, S, V)$ with $S = \{(n, n+1) : n \in \mathbb{N}\}$ and $V(p) = \emptyset$ for every variable $p$.
Let $\mathfrak{M}' = (\{a\}, \{(a, a)\}, V')$ with $V'(p) = \emptyset$ for every $p$.
Let $f \colon \mathbb{N} \to \{a\}$ be the constant map.
We check that $f$ is a bounded morphism, so that its graph $Z = \{(n, a) : n \in \mathbb{N}\}$ is a [[bisimulation|7T740SFHHV]].

1. Atoms: every variable is false at each $n$ and at $a = f(n)$.
2. Forth: if $n S m$, then $f(n) = a$, $f(m) = a$, and $a R' a$ holds.
3. Back: if $f(n) R' v'$, then $v' = a$.
   The world $n + 1$ satisfies $n S (n+1)$ and $f(n+1) = a$, so it is the required witness.

Read as a bisimulation, step 2 is zig at each pair $(n, a)$, since the only move $n S (n+1)$ is answered by $a R' a$ and $(n+1, a) \in Z$.
Step 3 is zag, since the only move $a R' a$ is answered by $n S (n+1)$.
So every $n$ is bisimilar to $a$.

## Remarks

The example shows that bisimulation is blind to well-foundedness and to size.
The relation $S$ has no cycles at all, and $\mathfrak{M}'$ is one point with a loop, yet no modal formula separates $0$ from $a$.
In fact $(\mathbb{N}, S)$ from $0$ is the tree unraveling of $\mathfrak{M}'$ from $a$: the paths from $a$ are $a$, $aa$, $aaa$, and so on.

The frame version is the useful one.
Validity on frames passes to bounded morphic images, so every formula valid on $(\mathbb{N}, S)$ is valid on the reflexive point.
Since $(\mathbb{N}, S)$ is irreflexive and the point is reflexive, no modal formula defines irreflexivity.

Change one thing and the morphism breaks.
If $S$ is cut down to the finite chain $0 S 1 S \cdots S k$, the back condition fails at $k$, because $a R' a$ has no answer from $k$.
Then $\square \bot$ is true at $k$ and false at $a$.

## Explanations

### L1 human

Number the steps of an endless staircase $0, 1, 2, \ldots$, and from each step allow one move up.
A single room with a door into itself offers the same choice: you can always go on.
Send every step to that one room, and every move on the staircase becomes a move through the door.
So an observer who only walks and looks cannot tell the staircase from the room.

### L2 human

Let us test the formula $\square \lozenge \top$, "every successor has a successor", on both sides.
At each $n$, the only successor is $n+1$, and $n+1$ has the successor $n+2$, so $\square \lozenge \top$ is true at $n$.
At $a$, the only successor is $a$ itself, which has a successor, so $\square \lozenge \top$ is true at $a$.
By induction on $k$, the formula $\square^k \lozenge \top$ is true at every $n$ and at $a$.
The invariance theorem predicts exactly this agreement, for every formula.
Watch out: a bounded morphism need not be injective or onto, but the back condition makes its image closed under $R'$.
