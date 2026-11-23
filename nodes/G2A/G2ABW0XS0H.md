---
tag: G2ABW0XS0H
kind: example
name: In S4 the modality □◇□◇ reduces to □◇
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [N60RVXSA5W]
uses: [N60RVXSA5W, JS8W7PA6JK, MHYEJ83H2K, FDFQFWPM4X]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
---

## Example

Long strings of boxes and diamonds collapse in the [[modal logic S4|N60RVXSA5W]], $\mathsf{S4} = \mathsf{KT4}$, and the one step that does the work beyond $\square\square = \square$ is this equivalence:
$$\mathsf{S4} \vdash \square\lozenge\square\lozenge p \leftrightarrow \square\lozenge p.$$
We use the rules RM and RE of [[normal modal logic K|JS8W7PA6JK]].
RM has a diamond form: from $\vdash \alpha \to \beta$ infer $\vdash \lozenge\alpha \to \lozenge\beta$.

First we prove the direction from right to left.

1. The instance of $\mathrm{4}$ for $\lozenge p$ is $\square\lozenge p \to \square\square\lozenge p$.
2. The dual of $\mathrm{T}$, applied to $\square\lozenge p$, is $\square\lozenge p \to \lozenge\square\lozenge p$.
3. RM applied to step 2 gives $\square\square\lozenge p \to \square\lozenge\square\lozenge p$.
4. Steps 1 and 3 give $\square\lozenge p \to \square\lozenge\square\lozenge p$.

Then the direction from left to right.

5. The instance of $\mathrm{T}$ for $\lozenge p$ is $\square\lozenge p \to \lozenge p$.
6. The diamond form of RM applied to step 5 gives $\lozenge\square\lozenge p \to \lozenge\lozenge p$.
7. The dual of $\mathrm{4}$, from [[K4 proves ◇◇p → ◇p|MHYEJ83H2K]], gives $\lozenge\lozenge p \to \lozenge p$.
8. Steps 6 and 7 give $\lozenge\square\lozenge p \to \lozenge p$, and RM turns this into $\square\lozenge\square\lozenge p \to \square\lozenge p$.
9. Steps 4 and 8 give the equivalence.

The dual equivalence $\lozenge\square\lozenge\square p \leftrightarrow \lozenge\square p$ follows: substitute $\neg p$, negate both sides, and move the negations inward with RE.

## Remarks

The example is the main step in the count of the modalities of $\mathsf{S4}$.
$\mathsf{S4}$ proves $\square\square p \leftrightarrow \square p$, by $\mathrm{4}$ and the instance of $\mathrm{T}$ for $\square p$, and dually $\lozenge\lozenge p \leftrightarrow \lozenge p$.
With RE, each block of equal symbols shrinks to one symbol, so every string is equivalent to an alternating string.
An alternating string of length at least four contains $\square\lozenge\square\lozenge$ or $\lozenge\square\lozenge\square$, and the example shortens it by two.
So every modality is equivalent to one of $p$, $\square p$, $\lozenge p$, $\square\lozenge p$, $\lozenge\square p$, $\square\lozenge\square p$ and $\lozenge\square\lozenge p$.

Both axioms are used.
Step 2 needs $\mathrm{T}$ and step 1 needs $\mathrm{4}$, so in $\mathsf{T}$ or in $\mathsf{K4}$ the reduction is not available, and $\mathsf{K4}$ in fact has infinitely many distinct modalities.
In the stronger logic $\mathsf{S5}$ the list collapses further to $p$, $\square p$ and $\lozenge p$, by [[the reduction of iterated modalities in S5|GHPPQ19J6B]].

## Explanations

### L1 human

In $\mathsf{S4}$, "box" can be read as "it is settled that" and "diamond" as "it is still possible that".
Two boxes in a row say the same as one box, and two diamonds say the same as one diamond.
The example shows that "settled that it is possible that it is settled that it is possible" says the same as "settled that it is possible".
So long chains of these words shrink to short ones, and in the end only seven different chains remain.

### L2 human

We reduce the modality $\square\square\lozenge\lozenge\square\lozenge p$.
First shrink the blocks, $\square\square$ to $\square$ and $\lozenge\lozenge$ to $\lozenge$, which gives this string:
$$\square\lozenge\square\lozenge p.$$
The example then gives $\square\lozenge\square\lozenge p \leftrightarrow \square\lozenge p$.
So the original modality is $\mathsf{S4}$-equivalent to $\square\lozenge p$.
You use this reduction to simplify a formula before you search for a countermodel, since fewer nested modalities mean fewer worlds to draw.
Watch out: the shortening of blocks happens inside the string, so you need RE to replace a subformula by an equivalent one, not only modus ponens.
