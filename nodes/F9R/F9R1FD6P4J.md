---
tag: F9R1FD6P4J
kind: example
name: "The Brouwerian axiom in dual form: ◇□p → p"
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [2QPT4KCM0Q]
uses: [2QPT4KCM0Q, JS8W7PA6JK, E87G6ZTMTN, 061J5VGSPT, FDFQFWPM4X]
sources:
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Example

On two worlds where $1$ sees $2$ and $2$ sees only itself, with $p$ true at $2$ only, the formula $\lozenge\square p$ is true at $1$ while $p$ is false there.
The arrow from $1$ to $2$ has no arrow back, and that is what lets $\lozenge\square p \to p$ fail.
We derive this formula, the dual form of axiom $\mathrm{B}$ of the [[Brouwerian modal logic|2QPT4KCM0Q]], in $\mathsf{KB} = \mathsf{K} + \mathrm{B}$, without axiom $\mathrm{T}$:
$$\mathsf{KB} \vdash \lozenge\square p \to p.$$
Then we show that $\mathsf{T}$ does not prove it.

1. The instance of $\mathrm{B}$ for $\neg p$ is $\neg p \to \square\lozenge\neg p$.
2. The tautology $\neg\neg p \leftrightarrow p$ and RE of [[normal modal logic K|JS8W7PA6JK]] give $\lozenge\neg p \leftrightarrow \neg\square p$.
3. RE again gives $\square\lozenge\neg p \leftrightarrow \square\neg\square p$.
   So step 1 becomes $\neg p \to \square\neg\square p$.
4. Contraposition gives $\neg\square\neg\square p \to \neg\neg p$, and $\neg\square\neg\square p$ is $\lozenge\square p$.
5. With $\neg\neg p \to p$, we get $\lozenge\square p \to p$.
   No step used $\mathrm{T}$.
6. For $\mathsf{T} \nvdash \lozenge\square p \to p$, take $W = \{ 1, 2 \}$, $R = \{ (1, 1), (2, 2), (1, 2) \}$ and $V(p) = \{ 2 \}$.
7. The frame is reflexive, so it validates $\mathsf{T}$, by [[common modal axiom schemata|FDFQFWPM4X]] and [[soundness|E87G6ZTMTN]].
8. $\square p$ is true at $2$, since $2$ sees only $2$, so $\lozenge\square p$ is true at $1$.
9. $p$ is false at $1$, so $\lozenge\square p \to p$ fails at $1$.

## Remarks

The example shows that $\mathrm{B}$ and $\lozenge\square p \to p$ are interderivable in $\mathsf{K}$.
The same steps, read backwards with $\neg p$ again, give $\mathrm{B}$ back.

On a [[symmetric|061J5VGSPT]] frame the dual form reads as follows.
If $w$ has a successor $v$ at which $\square p$ holds, then $p$ holds at every successor of $v$.
By symmetry, $w$ is a successor of $v$, so $p$ holds at $w$.
The countermodel of step 6 fails exactly here: $1$ sees $2$, but $2$ does not see $1$.

What if you add the pair $(2, 1)$?
The relation becomes $W \times W$, and $\square p$ becomes false at $2$, so step 8 breaks.

## Explanations

### L1 human

The Brouwerian rule says: if $p$ is true at a world, then from every world it sees, one can look back to a $p$-world.
The dual form says: if a world sees some world from which only $p$-worlds are visible, then $p$ is true at the first world.
The reason is the same in both forms: in a symmetric picture, each world sees back every world that sees it.
For example, if town A sees town B, and from town B only sunny towns are visible, then town A is sunny.

### L2 human

We test the dual form on a frame of $\mathsf{KB}$.

1. Take $W = \{ 1, 2 \}$ with $R = W \times W$, and $V(p) = \{ 2 \}$.
2. $\square p$ is false at both worlds, since $1$ lacks $p$.
3. So $\lozenge\square p$ is false at both worlds, and $\lozenge\square p \to p$ holds everywhere.
4. This agrees with the derivation, since this frame validates $\mathsf{KB}$.

You use the dual form in proofs about symmetric frames, where it is often shorter than $\mathrm{B}$.
Watch out: the dual of $\mathrm{B}$ is $\lozenge\square p \to p$, not $\square\lozenge p \to p$, and the second formula is not valid on symmetric frames.
