---
tag: V0J3A9Q4SY
kind: example
name: The smallest filtration of a transitive model need not be transitive
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [6ZZSHAKG5F]
uses: [6ZZSHAKG5F, T99DK51S0W, NGHWZ9Y7ZV, 0GJZW9JFZQ]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Take the [[Kripke model|NGHWZ9Y7ZV]] with these parts:
$$W = \{ a, b, b', c \}, \quad R = \{ (a, b), (b', c) \}, \quad V(p) = \{ b, b' \}, \quad V(q) = \{ c \}.$$
Let $\Sigma = \{ p, q, \square q \}$.
We compare the smallest [[filtration|6ZZSHAKG5F]] with the transitive filtration.

### The classes

$R$ is [[transitive|0GJZW9JFZQ]], since $b$ and $c$ have no successors, so there is no chain $x R y R z$ at all.
$\square q$ is false at $a$, since its successor $b$ lacks $q$.
$\square q$ is true at $b$ and at $c$, which have no successors, and at $b'$, since its successor $c$ has $q$.
So the values of $(p, q, \square q)$ are $(0, 0, 0)$ at $a$, $(1, 0, 1)$ at $b$ and at $b'$, and $(0, 1, 1)$ at $c$.
So the classes are $A = \{ a \}$, $B = \{ b, b' \}$ and $C = \{ c \}$.

### The smallest filtration

The smallest filtration takes the images of the arrows, so $R^s = \{ (A, B), (B, C) \}$.
It is not transitive: $A R^s B$ and $B R^s C$ hold, and $A R^s C$ fails.
The merge of $b$ and $b'$ created the path $A, B, C$, and nothing in $R$ supplies the shortcut.

### The transitive filtration

The transitive filtration has $[w] R^t [v]$ when every $\square\varphi \in \Sigma$ true at $w$ has both $\square\varphi$ and $\varphi$ true at $v$.
$A$ makes $\square q$ false, so the condition is empty, and $A$ sees $A$, $B$ and $C$.
$B$ makes $\square q$ true, so $B$ sees only classes with $q$ and $\square q$, and only $C$ qualifies.
$C$ makes $\square q$ true, so in the same way $C$ sees only $C$.
So $R^t = \{ (A, A), (A, B), (A, C), (B, C), (C, C) \}$.

### Check

$R^t$ is transitive.
A two-step path from $A$ ends somewhere, and $A$ sees every class.
A two-step path from $B$ or $C$ goes through $C$ and ends at $C$, and $(B, C)$ and $(C, C)$ are in $R^t$.
$R^t$ contains $R^s$, so it satisfies (min), and its definition gives (max), so it is a filtration.
At $A$ the successor $A$ lacks $q$, so $\square q$ is false, and at $B$ and $C$ the only successor $C$ has $q$, so $\square q$ is true, as in the original model.

## Remarks

### Why the transitive filtration works

Logics of transitive frames, such as $\mathsf{K4}$ and $\mathsf{S4} = \mathsf{KT4}$, need the transitive filtration.
It is transitive for every transitive model, and it satisfies the [[filtration theorem|T99DK51S0W]].
Its proof of (min) uses the transitivity of $R$: if $w R v$ and $\square\varphi$ holds at $w$, then $\square\varphi$ holds at $v$ as well.

### A variant

If we give $b$ the successor $c$ as well, then transitivity forces $a R c$, and the smallest filtration contains $(A, C)$.

### Watch out

The smallest filtration of a model of a logic need not lie on a frame of that logic.
Take the frame $(\{ A, B, C \}, R^s)$ with $q$ true only at $B$.
Then $\square q$ is true at $A$ and false at $B$, so the instance $\square q \to \square\square q$ of axiom $\mathrm{4}$ fails at $A$.
So the finite model property of $\mathsf{K4}$ needs the right filtration.

## Explanations

### L1 human

Two people, $b$ and $b'$, look the same to us, so we merge them into one person $B$.
Person $a$ points to $b$, and $b'$ points to $c$.
After the merge, $A$ points to $B$, and $B$ points to $C$.
But nobody pointed from $a$ to $c$, so the merged picture has a two-step path without a direct step.
The fix is to add the missing arrows in a careful way.

### L2 human

Take the instance $\square q \to \square\square q$ of axiom $\mathrm{4}$ in the model with $R^s$.
At $A$, $\square q$ is false, so the instance holds.
At $B$, $\square q$ is true, and $\square\square q$ needs $\square q$ at $C$, which is true, so the instance holds.
So the model with $R^s$ makes this instance true, but its frame does not validate axiom $\mathrm{4}$, as the Watch out shows.
The typical use of the transitive filtration is the proof of the finite model property of $\mathsf{K4}$ and $\mathsf{S4}$.
