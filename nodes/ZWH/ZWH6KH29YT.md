---
tag: ZWH6KH29YT
kind: example
name: The standard translation of □◇p
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [YW6YGBMVQY]
uses: [YW6YGBMVQY, 1HQ1W36J4V, 086QKPF0A6, NGHWZ9Y7ZV, G8VGTW9P4F]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_translation
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Example

We compute the [[standard translation|YW6YGBMVQY]] $\mathrm{ST}_x(\square\lozenge p)$ and check it on a model.
The clauses we need are $\mathrm{ST}_x(p) = Px$, $\mathrm{ST}_x(\neg\psi) = \neg\mathrm{ST}_x(\psi)$ and $\mathrm{ST}_x(\square\psi) = \forall y\, (Rxy \to \mathrm{ST}_y(\psi))$, and for $\mathrm{ST}_y$ the roles of $x$ and $y$ are swapped.
We read $\lozenge p$ as $\neg\square\neg p$, as in [[the definition of modal formulas|G8VGTW9P4F]].

### The translation

The box clause at $x$ gives $\mathrm{ST}_x(\square\lozenge p) = \forall y\, (Rxy \to \mathrm{ST}_y(\lozenge p))$.
Next, $\mathrm{ST}_y(\lozenge p) = \mathrm{ST}_y(\neg\square\neg p) = \neg\mathrm{ST}_y(\square\neg p)$.
The box clause at $y$ gives $\mathrm{ST}_y(\square\neg p) = \forall x\, (Ryx \to \neg Px)$.
So $\mathrm{ST}_y(\lozenge p) = \neg\forall x\, (Ryx \to \neg Px)$, which is equivalent to $\exists x\, (Ryx \wedge Px)$.
Hence the translation is equivalent to this formula:
$$\forall y\, \big( Rxy \to \exists x\, (Ryx \wedge Px) \big).$$
The only free variable is the outer $x$, and the inner $\exists x$ binds a new occurrence.
The reuse is safe: inside $\exists x$ the formula speaks only about $y$ and its successors, and the old value of $x$ is no longer needed.

### The model

Take the [[Kripke model|NGHWZ9Y7ZV]] with $W = \{ 1, 2, 3 \}$, $R = \{ (1, 2), (1, 3), (2, 2), (3, 1) \}$ and $V(p) = \{ 2 \}$.

On the modal side, $\lozenge p$ is true at $1$ via the successor $2$, true at $2$ via the successor $2$, and false at $3$, whose only successor is $1$.
So $\square\lozenge p$ is false at $1$, since its successor $3$ fails $\lozenge p$.
It is true at $2$, whose only successor is $2$, and true at $3$, whose only successor is $1$.

On the first-order side at $x = 1$, the values $y = 2$ and $y = 3$ satisfy $R1y$.
For $y = 2$ the witness $x = 2$ gives $R22 \wedge P2$.
For $y = 3$ the only $x$ with $R3x$ is $1$, and $P1$ is false, so the translation is false at $x = 1$.
At $x = 2$ the only $y$ is $2$, with witness $2$, and at $x = 3$ the only $y$ is $1$, with witness $2$.

Check: the translation is true at $2$ and $3$ and false at $1$, exactly as on the modal side.

## Remarks

### Why the values agree

The agreement is an instance of [[the correctness of the standard translation|1HQ1W36J4V]].
Two variables suffice for every modal formula, by the same alternation of $x$ and $y$.

### Other ways to write it

A translation with a fresh variable at each box, $\forall y\, (Rxy \to \exists z\, (Ryz \wedge Pz))$, is equivalent but uses three variables.
In both versions the quantifiers are guarded: each one ranges over the successors of the current world only.

### Watch out

Reusing $x$ is safe only because the outer $x$ does not occur inside the scope of the inner $\exists x$.
If a formula needed the outer world again inside the inner quantifier, as $Rxx$ does, the reuse would change its meaning, and no modal formula can express such a formula anyway.

## Explanations

### L1 human

The modal formula says: "wherever you go in one step, you can go one more step and find $p$".
The translation says the same thing in the language of points and arrows.
The name $x$ is used again for the second step, because by then the starting point is no longer needed.
We checked on three points that both versions say yes or no at the same places.

### L2 human

The computation has three moves.
Translate the outer box as $\forall y\, (Rxy \to \dots)$.
Translate the inner diamond at $y$ as $\exists x\, (Ryx \wedge Px)$.
Then put the second into the gap of the first.
The typical use is to read a modal formula as a first-order property of a point.

### L3 human

The image of the translation lies in the two-variable fragment and in the guarded fragment of first-order logic.
Both fragments are decidable, which explains part of the good algorithmic behavior of modal logic.
