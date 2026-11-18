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

We show in the [[modal logic S4|N60RVXSA5W]], $\mathsf{S4} = \mathsf{KT4}$, that
$$\mathsf{S4} \vdash \square\lozenge\square\lozenge p \leftrightarrow \square\lozenge p.$$
We use RM and RE of [[normal modal logic K|JS8W7PA6JK]], and the diamond form of RM: from $\vdash \alpha \to \beta$ infer $\vdash \lozenge\alpha \to \lozenge\beta$.

1. The instance of $\mathrm{4}$ for $\lozenge p$ is $\square\lozenge p \to \square\square\lozenge p$.
2. The dual of $\mathrm{T}$ for $\square\lozenge p$ is $\square\lozenge p \to \lozenge\square\lozenge p$.
3. RM applied to step 2 gives $\square\square\lozenge p \to \square\lozenge\square\lozenge p$.
4. Steps 1 and 3 give $\square\lozenge p \to \square\lozenge\square\lozenge p$.
5. The instance of $\mathrm{T}$ for $\lozenge p$ is $\square\lozenge p \to \lozenge p$.
6. The diamond form of RM applied to step 5 gives $\lozenge\square\lozenge p \to \lozenge\lozenge p$.
7. The dual of $\mathrm{4}$, from [[K4 proves ◇◇p → ◇p|MHYEJ83H2K]], gives $\lozenge\lozenge p \to \lozenge p$.
8. Steps 6 and 7 give $\lozenge\square\lozenge p \to \lozenge p$, and RM gives $\square\lozenge\square\lozenge p \to \square\lozenge p$.
9. Steps 4 and 8 give the equivalence.
10. The dual equivalence $\lozenge\square\lozenge\square p \leftrightarrow \lozenge\square p$ follows: substitute $\neg p$, negate both sides, and move the negations inward with RE.

## Remarks

The example is the main step in the count of modalities of $\mathsf{S4}$.
A modality is a finite string of boxes and diamonds in front of $p$.
$\mathsf{S4}$ proves $\square\square p \leftrightarrow \square p$, by $\mathrm{4}$ and the instance of $\mathrm{T}$ for $\square p$, and dually $\lozenge\lozenge p \leftrightarrow \lozenge p$.
With RE, each block of equal symbols in a string can be shortened to one symbol, so every string is equivalent to an alternating string.
An alternating string of length at least 4 contains $\square\lozenge\square\lozenge$ or $\lozenge\square\lozenge\square$, and the example shortens it by 2.
So every modality is $\mathsf{S4}$-equivalent to one of the seven: $p$, $\square p$, $\lozenge p$, $\square\lozenge p$, $\lozenge\square p$, $\square\lozenge\square p$, $\lozenge\square\lozenge p$.
These seven are pairwise non-equivalent, as finite countermodels on preorders show.
In $\mathsf{S5}$ the list collapses further to $p$, $\square p$ and $\lozenge p$; in $\mathsf{K4}$ the list is infinite.

## Explanations

### L1 human

In S4, "box" can be read as "it is settled that" and "diamond" as "it is still possible that".
Two boxes in a row say the same as one box, and two diamonds say the same as one diamond.
The example shows that "settled that it is possible that it is settled that it is possible" means "settled that it is possible".
So long chains of these words shrink to short ones.
In the end only seven different chains remain.

### L2 human

1. Reduce the modality $\square\square\lozenge\lozenge\square\lozenge p$.
2. Shorten the blocks: $\square\square \mapsto \square$ and $\lozenge\lozenge \mapsto \lozenge$, which gives $\square\lozenge\square\lozenge p$.
3. The example gives $\square\lozenge\square\lozenge p \leftrightarrow \square\lozenge p$.
4. So the original modality is $\mathsf{S4}$-equivalent to $\square\lozenge p$.

The typical use of this reduction is to simplify formulas in $\mathsf{S4}$ before a search for a countermodel.
A trap: the reduction needs both $\mathrm{T}$ and $\mathrm{4}$, so in $\mathsf{K4}$ or $\mathsf{T}$ the seven classes are not the full answer.
