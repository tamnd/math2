---
tag: XVYMEZKH7R
kind: concept
name: Modal logics T, D and K4
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, FDFQFWPM4X, E87G6ZTMTN]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Summary

Take two worlds $1$ and $2$, with one arrow from $1$ to $2$ and a loop at $2$, and make $p$ true at $2$ only.
At world $1$ every successor has $p$, so $\square p$ is true there, but $p$ itself is false.
So the law $\square p \to p$ fails at $1$, and the reason is that $1$ cannot see itself.
The logics $\mathsf{T}$, $\mathsf{D}$ and $\mathsf{K4}$ are what you get when you add one such law to the basic logic $\mathsf{K}$, and each law matches one property of the arrows.

Exactly, as in [[the definition|6M7Q6GFPK4]], each is the smallest [[normal modal logic|JS8W7PA6JK]] that contains one axiom:
$$\mathsf{T} = \mathsf{K} \oplus (\square p \to p), \qquad \mathsf{D} = \mathsf{K} \oplus (\square p \to \lozenge p), \qquad \mathsf{K4} = \mathsf{K} \oplus (\square p \to \square\square p).$$
Each is sound and complete for one class of frames.
$\mathsf{T}$ is the logic of reflexive frames, $\mathsf{D}$ of serial frames, and $\mathsf{K4}$ of transitive frames.

## Motivation

Each reading of the box accepts some laws and rejects others.
What is necessary is true, and what is known is true, so the alethic and the epistemic readings accept $\mathrm{T}$.
What is obligatory need not happen, so the deontic reading rejects $\mathrm{T}$.
But an obligation should at least be possible to meet, and that is $\mathrm{D}$.
For "at every later time", a later time of a later time is a later time, and that is $\mathrm{4}$.

The [[common modal axiom schemata|FDFQFWPM4X]] turn each of these laws into a condition on the accessibility relation.
So each logic comes with a clean class of frames, and you can test a formula by drawing a small frame of that class.
The three logics are the building blocks of the standard systems: [[S4|N60RVXSA5W]] is $\mathsf{T}$ plus $\mathrm{4}$, and the logic $\mathsf{KD45}$ of belief starts from $\mathsf{D}$ and $\mathsf{K4}$.

## Notation

Books name a logic by its axioms after $\mathsf{K}$, so $\mathsf{T}$ is also $\mathsf{KT}$ and $\mathsf{D}$ is also $\mathsf{KD}$, where D stands for "deontic".
Kripke's paper of 1963 calls $\mathsf{T}$ by the name $\mathsf{M}$, after the system of von Wright.
$\mathsf{K4}$ has no other common name, and adding $\mathrm{D}$ or $\mathrm{T}$ to it gives $\mathsf{KD4}$ and $\mathsf{S4} = \mathsf{KT4}$.
Watch the two uses of one letter: $\mathrm{T}$ in roman type is the axiom, and $\mathsf{T}$ in sans-serif type is the logic.

## Remarks

### How the three logics compare

The axiom $\mathrm{T}$ proves $\mathrm{D}$.
The instance $\square\neg p \to \neg p$ of $\mathrm{T}$ contraposes to $p \to \lozenge p$, and chaining with $\square p \to p$ gives $\square p \to \lozenge p$.
So $\mathsf{D} \subseteq \mathsf{T}$, and [[the comparison of K, D and T|P213018JH6]] shows that both inclusions in $\mathsf{K} \subsetneq \mathsf{D} \subsetneq \mathsf{T}$ are strict.
The logic $\mathsf{K4}$ lies on a different branch.
A reflexive frame need not be transitive, and a transitive frame need not be reflexive, so [[axiom 4 is not a theorem of T|EP284NG45P]] and $\mathrm{T}$ is not a theorem of $\mathsf{K4}$.
Both logics lie inside $\mathsf{S4}$.

### Derivations you can do

In $\mathsf{K4}$ the dual of axiom $\mathrm{4}$ holds, and [[the derivation of ◇◇p → ◇p in K4|MHYEJ83H2K]] gives it in six steps.
Two uses of $\mathrm{4}$ also give $\square p \to \square\square\square p$, and in general $\square p \to \square^n p$ for every $n \ge 1$.
In $\mathsf{T}$ you get $p \to \lozenge p$, as in the comparison above.
In $\mathsf{D}$ you get $\lozenge\top$ from $\square\top$, so every world has a successor, and in fact $\mathsf{D} = \mathsf{K} \oplus \lozenge\top$.

### Countermodels on small frames

To show that a logic does not prove a formula, you draw a frame of the right class where the formula fails.
For $\mathsf{K4} \nvdash \square p \to p$, take one world $w$ with no arrows and $V(p) = \varnothing$.
The empty relation is transitive, $\square p$ is true at $w$ because $w$ has no successors, and $p$ is false.
For $\mathsf{K4} \nvdash \square\square p \to \square p$, take the frame $(\mathbb{N}, <)$, which is serial and transitive, and make $p$ false at $1$ only.
At $0$, every world reached in two steps is at least $2$, so $\square\square p$ is true, but $\square p$ is false because of $1$.
The same model shows $\mathsf{D} \nvdash \square\square p \to \square p$.
The [[order on the natural numbers|2SVYW67C85]] is a frame of $\mathsf{D}$ and $\mathsf{K4}$, but not of $\mathsf{T}$.

### The rules you can use

The logics are sound and complete for their frames, by [[soundness|E87G6ZTMTN]] and [[the completeness theorem|FXTCKYR3AQ]].
Each has the [[finite model property|3NT8RCA6HE]], so each is decidable.
For $\mathsf{K4}$ the finite models come from a transitive filtration, because the smallest filtration may lose transitivity.
Satisfiability is PSPACE-complete for all three, by [[the complexity theorem|1P2B0C7CQ4]], since every logic between $\mathsf{K}$ and $\mathsf{S4}$ is PSPACE-hard.
$\mathsf{K4}$ has infinitely many distinct modalities: on a finite chain $0 < 1 < \dots < m$, the formulas $\square^n p$ and $\square^{m} p$ differ at $0$ when $p$ is false only at $m - 1 \ge n$.

### Watch out

Three slips are common.
First, $\mathsf{K4}$ does not contain $\mathsf{T}$, because a transitive frame need not be reflexive; the one-world frame without arrows is the witness.
Second, $\mathsf{D}$ does not prove $p \to \lozenge p$.
On the serial frame with $1 R 2$ and $2 R 2$ and $V(p) = \{ 1 \}$, the formula $p$ is true at $1$ and $\lozenge p$ is false.
Third, seriality is not reflexivity: $\mathrm{D}$ asks only that each world sees some world, not that it sees itself.

### History

Von Wright's system $\mathsf{M}$, from An Essay in Modal Logic of 1951, has the same theorems as $\mathsf{T}$.
Kripke's paper of 1963 on normal modal logics proved the completeness of $\mathsf{M}$ for reflexive frames.
The deontic reading goes back to von Wright's paper "Deontic logic" of 1951.

### Try it

First, is the frame with worlds $1, 2$ and arrows $1 R 2$ and $2 R 1$ a frame of $\mathsf{T}$, $\mathsf{D}$ or $\mathsf{K4}$?
It is serial, so it is a frame of $\mathsf{D}$; it is not reflexive, and it is not transitive because $1 R 2$ and $2 R 1$ but not $1 R 1$.

Second, show that $\square p \to p$ fails on that frame.
Put $V(p) = \{ 2 \}$; at $1$ the only successor $2$ has $p$, so $\square p$ is true, while $p$ is false.

## Explanations

### L1 human

These are three ways to make the basic logic of necessity a little stronger.
Picture worlds as rooms and arrows as doors.
In $\mathsf{T}$ every room has a door to itself, so what holds in every room you can enter holds in your own room.
In $\mathsf{D}$ every room has at least one door, so a duty can always be met somewhere.
In $\mathsf{K4}$ two doors in a row can be replaced by one door, as with times $0 < 1 < 2$, where a later time of a later time is a later time.

### L2 human

We show that $\mathsf{T}$ does not prove axiom $\mathrm{4}$.
Take three worlds with a loop at each, and the arrows $1 R 2$ and $2 R 3$, and put $V(p) = \{ 1, 2 \}$.
The frame is reflexive, so by soundness every theorem of $\mathsf{T}$ is true at every world.
Now read off the successors:
$$R[1] = \{ 1, 2 \}, \qquad R[2] = \{ 2, 3 \}, \qquad R[3] = \{ 3 \}.$$
Both successors of $1$ have $p$, so $\square p$ is true at $1$.
The successor $3$ of $2$ lacks $p$, so $\square p$ is false at $2$, and then $\square\square p$ is false at $1$.
So $\square p \to \square\square p$ fails at $1$, and it is not a theorem of $\mathsf{T}$.
This is the typical use of the frame classes: a derivation shows that a formula is in a logic, and one small frame of the right class shows that it is not.
The countermodel must lie in the class of the logic, or it shows nothing.

### L3 human

The axioms $\mathrm{T}$, $\mathrm{D}$ and $\mathrm{4}$ are Sahlqvist formulas, so their logics are canonical and their frame classes are first-order, by [[Sahlqvist's theorem|S4SSDMETJM]].
The logic $\mathsf{K4}$ is the base of a large theory of transitive logics, and the provability logic [[GL|WJK0YA4GP2]] is one of its extensions.
The logics $\mathsf{D}$ and $\mathsf{KD45}$ are the base of the logics of obligation and belief in [[applied modal logics|CQM9SRN8PM]].
The [[lattice of normal modal logics|EZ011FT3GT]] puts all of these systems into one ordered picture.
