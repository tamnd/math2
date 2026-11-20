---
tag: NY42G4JYKY
kind: example
name: A ternary structure whose star is not an involution
msc: ["03B47"]
topics: [98QF5J4W16]
audience: research
not_instance_of:
  - target: H4Z8J0KMAY
    note: the star of this structure is not an involution, so it is not a Routley-Meyer frame and refutes not not p implies p
uses: [XHN0G5FFR5, GP56NBN9RY]
sources:
  - url: https://en.wikipedia.org/wiki/Relevance_logic
    locator: Axioms; Models, Routley-Meyer models
---

## Example

Let $W = \set{0, 1}$, let $Rabc$ hold if and only if $b = c$, and let $0^* = 1$ and $1^* = 1$.
This structure meets every condition of a [[Routley-Meyer frame|XHN0G5FFR5]] except $a^{**} = a$, and the axiom $\neg\neg A \rightarrow A$ of $\mathbf{B}$ fails in it.

1. $a \leq b$ means $R0ab$, which holds if and only if $a = b$.
2. So $\leq$ is equality, and conditions 1, 2, 3 and 5 hold.
3. $0^{**} = 1^* = 1 \neq 0$, so ${}^*$ is not an [[involution|GP56NBN9RY]] and condition 4 fails.
4. Every set is hereditary, since $\leq$ is equality.
   Put $p$ true at $1$ only.
5. $0^* = 1$ and $1 \Vdash p$, so $0 \nVdash \neg p$.
   $1^* = 1$ and $1 \Vdash p$, so $1 \nVdash \neg p$.
6. So $\neg p$ is true nowhere, and $\neg\neg p$ is true at $0$ and at $1$.
7. $R000$ holds, $0 \Vdash \neg\neg p$ and $0 \nVdash p$, so $\neg\neg p \rightarrow p$ fails at $0$.

## Remarks

The Wikipedia article lists $\neg\neg A \rightarrow A$ among the axioms of $\mathbf{B}$, the weakest logic that it gives for Routley-Meyer frames.
So condition 4 is needed: without it, the semantics does not validate the double negation axiom.
The converse direction $p \rightarrow \neg\neg p$ is true at $0$ here, since $\neg\neg p$ is true everywhere.

## Explanations

### L1 human

The star of a point is the point that negation looks at.
If the star of the star of $a$ is not $a$ itself, two negations do not cancel.

### L2 human

We check condition 3 of the definition for this structure.

1. Condition 3 says: if $d \leq a$ and $Rabc$, then $Rdbc$.
2. $d \leq a$ means $d = a$, by step 1 of the example.
3. So $Rdbc$ is $Rabc$, and the condition holds.

The typical use of this structure is to show which frame condition makes a given axiom valid.
A trap: the formula $\neg\neg p \rightarrow p$ fails here at $0$, but a structure that fails a frame condition can still make some instances of the axiom true.
