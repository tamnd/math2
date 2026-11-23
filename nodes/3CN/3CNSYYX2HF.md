---
tag: 3CNSYYX2HF
kind: definition
name: Ordinal notation system
msc: ["03F15", "03D60"]
topics: [XTTKZTYDSD]
audience: grad
defines: 7MBX59Y7N9
uses: [01CGSJ0GNQ, 0FRXBVVR03, 0DQPNJNPYK, FMFGTVVR4S, PPGD5KW8JC, QQQRJA90EP, 0YSCSX5YZC]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_notation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Ordinal notations
---

## Definition

An ordinal notation system is a computable well-order on a set of natural numbers, whose elements serve as names of ordinals.

An *ordinal notation system* is a pair $(A, \prec)$ of a set $A \subseteq \mathbb{N}$ and a relation ${\prec} \subseteq A \times A$ with three properties.

1. The set $A$ and the relation $\prec$ are [[computable|PPGD5KW8JC]].
   In proof theory we ask more: they are [[primitive recursive|QQQRJA90EP]], and usually elementary.
2. The relation $\prec$ is a strict [[total order|0FRXBVVR03]] on $A$.
3. The relation $\prec$ is [[well-founded|0DQPNJNPYK]]: there is no infinite sequence $a_0 \succ a_1 \succ a_2 \succ \cdots$ in $A$.

By properties 2 and 3, $(A, \prec)$ is a [[well-order|01CGSJ0GNQ]].
So it is isomorphic to a unique [[ordinal|0YSCSX5YZC]] $\alpha$, its [[order type|FMFGTVVR4S]], and we call $(A, \prec)$ a notation system *for* $\alpha$.
The elements of $A$ are *notations*.
A notation $a$ *denotes* the ordinal $\lvert a \rvert$, the order type of $\{ b \in A : b \prec a \}$.
The map $a \mapsto \lvert a \rvert$ is then the isomorphism from $(A, \prec)$ onto $\alpha$.

In most systems, $A$ is the set of closed terms in normal form of a term language.
The language has symbols for ordinal functions, such as $0$, $+$, $\alpha \mapsto \omega^\alpha$ and the Veblen or collapsing functions.
The terms are coded by natural numbers, and the term functions are computable on codes.

## Notation

We write $\lvert a \rvert$ or $o(a)$ for the ordinal denoted by $a$, and $\operatorname{otp}(\prec)$ or $\lvert \prec \rvert$ for the order type.
Many books use one symbol for a notation and for the ordinal it denotes, such as $\omega^\omega$ for both, which is safe inside one fixed system.
In computability theory, a "system of notation" in Kleene's sense is a partial map from $\mathbb{N}$ onto an initial segment of the ordinals, with codes for successors and limits.
That sense does not ask that the set of notations be decidable; see [[Kleene's O|WHAP0K600D]].

## Remarks

Each condition has a job.
Computability lets a theory of arithmetic express $\prec$ by a formula, and primitive recursiveness lets even a weak theory prove the basic facts about it.
Totality makes every pair of names comparable, so that the names line up as a single ordinal and not as a tree.
Well-foundedness is what makes the order an ordinal at all.

For a small example, take $A = \mathbb{N}$ and $a \prec b$ if and only if $a < b$.
The relation is primitive recursive and a strict total order, and every nonempty set of natural numbers has a least element, so it is well-founded.
Its order type is $\omega$, and the notation $n$ denotes the ordinal $n$.
The integers with $<$, coded in $\mathbb{N}$, pass conditions 1 and 2 but fail condition 3, since $-1 > -2 > \cdots$ descends for ever.

Condition 3 is the hard one.
The set of indices of computable well-orders is $\Pi^1_1$-complete in the [[analytical hierarchy|M6JGF4TPM6]], so no algorithm decides it from a program for $\prec$, and each system needs its own proof.
The order types of computable well-orders are exactly the ordinals below the Church-Kleene ordinal $\omega_1^{\mathrm{CK}}$.
Examples and the problem of natural systems are on the concept page [[ordinal notation system|7MBX59Y7N9]].

## Explanations

### L1 human

An ordinal notation system is a way to write names for ordinals with finite symbols, so that a computer can compare any two names.
For example, $\omega \cdot 2 + 3$ and $\omega^2$ are names, and the rule says that the first is smaller.
The names must be listed in an order with no endless way down.
Then each name stands for exactly one ordinal.

### L2 human

What does it mean that a theory $T$ "proves the well-foundedness" of a notation system?
Since $\prec$ is primitive recursive, $T$ has a formula $x \prec y$ for it.
We say $T$ proves the well-foundedness when $T$ proves transfinite induction along $\prec$: for each formula $\varphi$, if $\varphi$ passes from all predecessors of $a$ to $a$, then $\varphi$ holds on all of $A$.
For the system of type $\omega$ above, this is ordinary induction, written with strong predecessors.
This is the typical use, and it measures the strength of $T$.
Watch out: two systems for the same ordinal can behave very differently inside a weak theory, so a statement about provability must name the system.

### L3 human

A notation system turns an infinite object, a countable ordinal, into a computable relation on $\mathbb{N}$ that a theory of arithmetic can talk about.
The [[proof-theoretic ordinal|C72RBH0CDR]] of a theory is defined through such relations.
Every [[ordinal analysis|C5E5TG8PGP]] ends with a notation system and a proof of transfinite induction along its initial segments.
The strongest systems in use are built with collapsing functions from names of large cardinals.
Their well-foundedness proofs need strong set theory, even though the systems themselves are primitive recursive.
