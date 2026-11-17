---
tag: 1NNYWRN6B8
kind: concept
name: Sheffer stroke
aliases: [alternative-denial, inclusive-nand, logical-nand, nand-operator, scheffers-stroke, sheffer-connective, sheffers-stroke]
msc: ["03B05", "06E30"]
topics: [PM1AYWABA7]
audience: ug1
uses: [QS0XVAN9BG, 029JBBF693, 025YZN3VJW, 0F72FK8EKB, TDZVCWYJ9F]
sources:
  - wikipedia: en:29388@r1375830657
    locator: Sheffer stroke
    note: adopted
    mention: wikipedia://en/29388
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Sheffer_stroke
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Logical_NOR
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 1
same_as:
  wikidata: Q3874243
  wikipedia: Sheffer stroke
inventory: [37N3PZJH03]
---

## Summary

The Sheffer stroke is the binary [[logical connective|QS0XVAN9BG]] $p \uparrow q$, read "not both $p$ and $q$".
It is false when $p$ and $q$ are both true, and true in the three other cases.
It has the same truth table as $\neg(p \land q)$, so it is also called NAND ("not and") or alternative denial.
Its dual is the Peirce arrow $p \downarrow q$, read "neither $p$ nor $q$", which is true only when $p$ and $q$ are both false; it is also called NOR.
Each of the two connectives is [[functionally complete|TDZVCWYJ9F]] by itself: [[negation|029JBBF693]], [[conjunction|025YZN3VJW]], [[disjunction|0F72FK8EKB]] and every other truth function can be written with it alone.
This is why a single kind of gate suffices to build every digital circuit.

## Motivation

The usual connectives $\neg$, $\land$, $\lor$, $\to$ and $\leftrightarrow$ overlap: each can be expressed by others.
For example, $\set{\neg, \land}$ is already functionally complete.
So it is natural to ask for the smallest set of connectives that expresses everything.
A single binary connective is the smallest possible answer.
The connective must turn the all-true input into false, or $\neg p$ cannot be built, and it must turn the all-false input into true, for the same reason.
Among the $16$ binary connectives, exactly two do both and also express the rest: NAND and NOR.

## Notation

This topic writes $p \uparrow q$ for NAND and $p \downarrow q$ for NOR.
Many books write the Sheffer stroke as $p \mid q$, and some write it $p \,\overline{\land}\, q$.
In Polish notation the Sheffer stroke is $Dpq$.
The vertical bar $\mid$ also means "divides" in number theory, so the arrow $\uparrow$ is safer in mixed texts.
The truth tables, in the standard row order, are as follows.

| $p$ | $q$ | $p \uparrow q$ | $p \downarrow q$ |
|---|---|---|---|
| T | T | F | F |
| T | F | T | F |
| F | T | T | F |
| F | F | T | T |

## Remarks

### Examples

1. [[Negation, conjunction and disjunction from the Sheffer stroke|S3KJ52G2SF]]: $\neg p \equiv p \uparrow p$, $p \land q \equiv (p \uparrow q) \uparrow (p \uparrow q)$ and $p \lor q \equiv (p \uparrow p) \uparrow (q \uparrow q)$, checked row by row.
2. [[Negation, disjunction and conjunction from the Peirce arrow|WH9JHEB1K3]]: $\neg p \equiv p \downarrow p$, $p \lor q \equiv (p \downarrow q) \downarrow (p \downarrow q)$ and $p \land q \equiv (p \downarrow p) \downarrow (q \downarrow q)$.
3. Material implication from the stroke: $p \to q \equiv p \uparrow (q \uparrow q)$. Indeed $q \uparrow q \equiv \neg q$, and $p \uparrow \neg q \equiv \neg(p \land \neg q) \equiv p \to q$.
4. "It is not the case that $6$ is prime and $6$ is even" is the stroke of two statements. It is true, because "$6$ is prime" is false.

### Non-examples

1. [[Exclusive or alone is not functionally complete|KBG5Y5K65F]]: every formula built from variables with $\oplus$ alone is false when all variables are false, so $\neg p$ cannot be built.
2. Conjunction alone is not functionally complete. Every formula built with $\land$ alone is true when all variables are true, so $\neg p$ cannot be built. The same holds for $\lor$, $\to$ and $\leftrightarrow$.
3. Implication with the constant $\bot$ is functionally complete, but this uses two symbols. Implication alone is not, by non-example 2.

### Basic properties

1. $p \uparrow q \equiv \neg(p \land q) \equiv \neg p \lor \neg q$, by one of [[De Morgan's laws|09PKJKA6J0]].
2. $p \downarrow q \equiv \neg(p \lor q) \equiv \neg p \land \neg q$, by the other law.
3. Both connectives are commutative: $p \uparrow q \equiv q \uparrow p$ and $p \downarrow q \equiv q \downarrow p$.
4. Neither is associative. At $p = \mathsf{T}$, $q = \mathsf{T}$, $r = \mathsf{F}$, the formula $(p \uparrow q) \uparrow r$ is $\mathsf{F} \uparrow \mathsf{F} = \mathsf{T}$, and $p \uparrow (q \uparrow r)$ is $\mathsf{T} \uparrow \mathsf{T} = \mathsf{F}$.
5. Each alone is functionally complete, because it expresses $\neg$ and $\land$ (examples 1 and 2), and $\set{\neg, \land}$ is functionally complete.
6. Among the $16$ binary connectives, NAND and NOR are the only ones that are functionally complete alone. This follows from [[Post's functional completeness theorem|WGBR7JHBV4]], and it can be checked by a direct computation over the $16$ truth tables.

### Nicod's single axiom

In 1917 Jean Nicod gave a [[Hilbert system|1MGMQX43B8]] for classical propositional logic with the stroke as its only connective, one axiom scheme and one rule.
The axiom scheme is
$$(\varphi \uparrow (\chi \uparrow \psi)) \uparrow \big((\tau \uparrow (\tau \uparrow \tau)) \uparrow ((\theta \uparrow \chi) \uparrow ((\varphi \uparrow \theta) \uparrow (\varphi \uparrow \theta)))\big).$$
The rule infers $\psi$ from $\varphi$ and $\varphi \uparrow (\chi \uparrow \psi)$.
The rule is sound, because $\varphi \uparrow (\chi \uparrow \psi) \equiv \varphi \to (\chi \land \psi)$, so it is a form of [[modus ponens|0Y0MQYST0M]].
The axiom is a tautology: a computation over all $2^5 = 32$ assignments to $\varphi, \chi, \psi, \tau, \theta$ gives $\mathsf{T}$ in each.
Nicod's result is that every tautology written with the stroke is derivable in this system.

### History

Charles Sanders Peirce found, in unpublished work of about 1880, that NAND alone and NOR alone can express all truth functions.
Henry Maurice Sheffer published in 1913 an axiom system for Boolean algebra with a single operation, written with a stroke, and the connective carries his name.
Jean Nicod used the stroke in 1917 for his single axiom of propositional logic.
The name "Peirce arrow" for NOR honours Peirce's discovery.

### Common errors

1. A student writes $\neg p$ as $p \uparrow \bot$. This is $\neg(p \land \bot)$, which is always true; the correct form is $p \uparrow p$.
2. A student drops the brackets in $p \uparrow q \uparrow r$. The stroke is not associative, so the brackets are needed (basic property 4).
3. A student confuses the stroke $p \mid q$ with the divisibility relation $p \mid q$ or with "or". The stroke means "not both".

## Explanations

### L1 human

The Sheffer stroke says "not both".
"Not both: the shop is open and the shop is closed" is always true, because a shop cannot be both.
"Not both: $2$ is even and $3$ is odd" is false, because both parts are true.
The surprise is that this one rule is enough to build "not", "and", "or" and every other way to join statements.
For example, "not both $p$ and $p$" says the same as "not $p$".

### L2 human

We express $p \leftrightarrow q$ with the Sheffer stroke alone.

1. Write $p \leftrightarrow q \equiv (p \land q) \lor (\neg p \land \neg q)$.
2. Let $A = p \land q$ and $B = \neg p \land \neg q$. By example 1, $A \lor B \equiv (A \uparrow A) \uparrow (B \uparrow B) \equiv \neg A \uparrow \neg B$.
3. Here $\neg A = \neg(p \land q) \equiv p \uparrow q$, and $\neg B = \neg(\neg p \land \neg q) \equiv \neg p \uparrow \neg q \equiv (p \uparrow p) \uparrow (q \uparrow q)$.
4. So $p \leftrightarrow q \equiv (p \uparrow q) \uparrow \big((p \uparrow p) \uparrow (q \uparrow q)\big)$.
5. Check one row: at $p = \mathsf{T}$, $q = \mathsf{F}$, we get $p \uparrow q = \mathsf{T}$, $(p \uparrow p) \uparrow (q \uparrow q) = \mathsf{F} \uparrow \mathsf{T} = \mathsf{T}$, and $\mathsf{T} \uparrow \mathsf{T} = \mathsf{F}$, as $p \leftrightarrow q$ requires.

The typical use of such translations is in circuit design, where a chip of NAND gates is cheaper than a mix of gates.
A trap: formulas with the stroke alone grow long fast, so we translate in steps and check each step with a truth table.

### L3 human

Functional completeness of a set of connectives means that the set generates the clone of all operations on $\set{\mathsf{T}, \mathsf{F}}$.
[[Post's functional completeness theorem|WGBR7JHBV4]] names five properties: preserving $\mathsf{T}$, preserving $\mathsf{F}$, being monotone, being self-dual and being affine.
A set is complete exactly when, for each property, some member of the set fails it.
NAND and NOR fail all five, and they are the only binary connectives that do.
On a finite set with more than two elements, a single operation that generates all operations is called a [[Sheffer function|1K829SJG3K]].

In circuit design the same facts say that NAND gates alone, or NOR gates alone, can build every [[logic gate|AMH914MF2A]]; the stub page [[Nand|VJMV4X7PWH]] records this use.
In proof theory, Nicod's system shows that a complete Hilbert system can have one connective, one axiom scheme and one rule.
