---
tag: MHYEJ83H2K
kind: example
name: K4 proves ◇◇p → ◇p
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [XVYMEZKH7R]
uses: [XVYMEZKH7R, JS8W7PA6JK, E87G6ZTMTN, 0GJZW9JFZQ, FDFQFWPM4X]
sources:
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Example

Axiom $\mathrm{4}$ talks about boxes, and its diamond form says that a world reached in two steps is reached in one.
We derive this form in $\mathsf{K4}$, one of the [[modal logics T, D and K4|XVYMEZKH7R]], and then show that the reverse box law is not a theorem:
$$\mathsf{K4} \vdash \lozenge\lozenge p \to \lozenge p, \qquad \mathsf{K4} \nvdash \square\square p \to \square p.$$

The derivation has six steps.

1. Substitute $\neg p$ for $p$ in axiom $\mathrm{4}$, which gives $\square\neg p \to \square\square\neg p$.
2. Contrapose, which gives $\neg\square\square\neg p \to \neg\square\neg p$.
   The right side is $\lozenge p$ by the definition of the diamond.
3. Unfold the definition twice: $\lozenge\lozenge p$ is $\neg\square\neg\neg\square\neg p$.
4. The tautology $\neg\neg\square\neg p \leftrightarrow \square\neg p$ and the rule RE of [[normal modal logic K|JS8W7PA6JK]] give $\square\neg\neg\square\neg p \leftrightarrow \square\square\neg p$.
5. Negate both sides of step 4, which gives $\lozenge\lozenge p \leftrightarrow \neg\square\square\neg p$.
6. Steps 2 and 5 together give $\lozenge\lozenge p \to \lozenge p$.

For the non-theorem we use a frame of $\mathsf{K4}$.

7. The frame $(\mathbb{N}, <)$ is [[transitive|0GJZW9JFZQ]], so it validates $\mathsf{K4}$ by the [[common modal axiom schemata|FDFQFWPM4X]].
8. Put $V(p) = \{ n : n \geq 2 \}$.
   Each $m \geq 1$ has only successors $n > m \geq 1$, so $n \geq 2$, and $\square p$ is true at $m$.
9. Every successor of $0$ is at least $1$, so $\square p$ holds at all of them, and $\square\square p$ is true at $0$.
10. The successor $1$ of $0$ lacks $p$, so $\square p$ is false at $0$.
    By [[soundness|E87G6ZTMTN]], $\square\square p \to \square p$ is not a theorem of $\mathsf{K4}$.

## Remarks

The derivation is the standard move from a box axiom to its diamond dual: substitute $\neg p$, contrapose, and remove the double negation with RE.
On frames the dual reads: if $w$ reaches a $p$-world in two steps, it reaches a $p$-world in one step.
That is transitivity again, seen from the diamond side.

Two uses of axiom $\mathrm{4}$ also give $\square p \to \square\square\square p$: chain $\square p \to \square\square p$ with the instance $\square\square p \to \square\square\square p$.
By induction, $\mathsf{K4} \vdash \square p \to \square^n p$ for every $n \geq 1$.

The reverse law $\square\square p \to \square p$ matches density: whenever $w R v$, there is a $u$ with $w R u$ and $u R v$.
The frame $(\mathbb{N}, <)$ is not dense, since nothing lies between $0$ and $1$, and step 10 uses exactly that gap.
On $(\mathbb{Q}, <)$, which is transitive and dense, $\square\square p \to \square p$ is valid.

## Explanations

### L1 human

In a transitive picture, a trip from $a$ to $b$ and a trip from $b$ to $c$ give a direct trip from $a$ to $c$.
"Diamond diamond $p$" says that a $p$-world can be reached in two steps.
Transitivity turns two steps into one, so "diamond $p$" follows.
The box form of the reverse can fail on the numbers $0, 1, 2, \dots$ with "smaller than".
If $p$ holds from $2$ on, then from $0$ every two-step trip ends in $p$, but the one-step trip from $0$ to $1$ does not.

### L2 human

We check that the dual really needs transitivity.
Take $W = \{ 1, 2, 3 \}$ with the arrows $1 R 2$ and $2 R 3$ only, and put $V(p) = \{ 3 \}$.
At $2$ the successor $3$ has $p$, so $\lozenge p$ is true at $2$, and then $\lozenge\lozenge p$ is true at $1$.
But $1$ sees only $2$, and $2$ lacks $p$, so $\lozenge p$ is false at $1$.
The frame is not transitive, as the [[common modal axiom schemata|FDFQFWPM4X]] predict.
If you add the arrow $1 R 3$, the frame becomes transitive and $\lozenge p$ becomes true at $1$.
The dual form is the one you use in work on the [[canonical model|TVE4F04KME]], where diamonds are easier to handle than boxes.
Watch out: the dual of $\square p \to \square\square p$ is $\lozenge\lozenge p \to \lozenge p$, with the arrow from the longer string to the shorter one.
