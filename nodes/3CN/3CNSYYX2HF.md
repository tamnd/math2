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

An *ordinal notation system* is a pair $(A, \prec)$ of a set $A \subseteq \N$ and a relation ${\prec} \subseteq A \times A$ with three properties.

1. The set $A$ and the relation $\prec$ are [[computable|PPGD5KW8JC]]. In proof theory one asks more: they are [[primitive recursive|QQQRJA90EP]], and usually elementary.
2. The relation $\prec$ is a strict [[total order|0FRXBVVR03]] on $A$.
3. The relation $\prec$ is [[well-founded|0DQPNJNPYK]]: there is no infinite sequence $a_0 \succ a_1 \succ a_2 \succ \cdots$ in $A$.

By properties 2 and 3, $(A, \prec)$ is a [[well-order|01CGSJ0GNQ]].
So it is isomorphic to a unique [[ordinal|0YSCSX5YZC]] $\alpha$, its [[order type|FMFGTVVR4S]], and we call $(A, \prec)$ a notation system *for* $\alpha$.
The elements of $A$ are *notations*.
A notation $a$ *denotes* the ordinal $\abs{a}$, the order type of $\set{b \in A : b \prec a}$.
Then $a \mapsto \abs{a}$ is the isomorphism from $(A, \prec)$ onto $\alpha$.

In most systems, $A$ is the set of closed terms in normal form of a term language.
The language has symbols for ordinal functions, such as $0$, $+$, $\alpha \mapsto \omega^\alpha$ and the Veblen or collapsing functions.
The terms are coded by natural numbers, and the term functions are computable on codes.

## Notation

- One writes $\abs{a}$ or $o(a)$ for the ordinal denoted by $a$, and $\operatorname{otp}(\prec)$ or $\abs{\prec}$ for the order type.
- Many books use the same symbol for a notation and the ordinal that it denotes, for example $\omega^\omega$ for both the term and the ordinal. This is safe inside one fixed system.
- In computability theory, a "system of notation" in the sense of Kleene is a partial map from $\N$ onto an initial segment of the ordinals. It has codes for successors and limits. That sense does not ask that the set of notations is decidable; see [[Kleene's O|WHAP0K600D]].

## Remarks

- The order types of computable well-orders of $\N$ are exactly the ordinals below the Church-Kleene ordinal $\omega_1^{\mathrm{CK}}$. So every ordinal notation system is a system for a countable ordinal below $\omega_1^{\mathrm{CK}}$.
- Property 3 is not decidable from a program for $\prec$: the set of indices of computable well-orders is $\Pi^1_1$-complete in the [[analytical hierarchy|M6JGF4TPM6]]. Each notation system needs its own proof of well-foundedness.
- The examples and the problem of natural notation systems are on the concept page [[ordinal notation system|7MBX59Y7N9]].

## Explanations

### L1 human

An ordinal notation system is a way to write names for ordinals with finite symbols, so that a computer can compare any two names.
For example, $\omega \cdot 2 + 3$ and $\omega^2$ are names, and the rule says that the first is smaller.
The names must be listed in an order with no endless way down.
Then each name stands for exactly one ordinal.

### L2 human

We check the definition for the system $A = \N$ with $a \prec b$ if and only if $a < b$.

1. The set $\N$ and the relation $<$ are primitive recursive.
2. The relation $<$ is a strict total order.
3. Every nonempty set of natural numbers has a least element, so there is no infinite descending sequence.
4. The order type is $\omega$, and the notation $n$ denotes the ordinal $n$.

The typical use: a theory $T$ "proves the well-foundedness" of a notation system when it proves transfinite induction along $\prec$, and this measures the strength of $T$.
The trap: two notation systems for the same ordinal can behave very differently inside a weak theory, so a statement about provability must name the system.

### L3 human

A notation system turns an infinite object, a countable ordinal, into a computable relation on $\N$ that a theory of arithmetic can talk about.
The [[proof-theoretic ordinal|C72RBH0CDR]] of a theory is defined through such systems.
Every [[ordinal analysis|C5E5TG8PGP]] ends with a notation system and a proof of transfinite induction along its initial segments.
The strongest systems in use are built with collapsing functions from large cardinals.
Their well-foundedness proofs need strong set theory, even though the systems themselves are primitive recursive.
