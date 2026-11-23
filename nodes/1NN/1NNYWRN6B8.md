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

One connective is enough: "not both" can express "not", "and", "or" and every other truth function.
"Not both: $n$ is even and $n$ is prime" is false only for $n = 2$, where both parts hold.
For propositions $p$ and $q$, the Sheffer stroke $p \uparrow q$ is false when $p$ and $q$ are both true, and true in the three other cases.
It has the same table as $\neg(p \land q)$, so it is also called NAND or alternative denial.
Its dual is the Peirce arrow $p \downarrow q$, "neither $p$ nor $q$", also called NOR, which is true only when both parts are false.
Each of the two is [[functionally complete|TDZVCWYJ9F]] by itself, which is why one kind of gate suffices to build every digital circuit.

## Motivation

The usual connectives $\neg$, $\land$, $\lor$, $\to$ and $\leftrightarrow$ overlap, since each can be expressed by others, and $\{\neg, \land\}$ is already functionally complete.
So it is natural to ask for the smallest set of connectives that expresses everything.
A single binary connective is the smallest possible answer.
Such a connective must turn the input TT into F, or a formula built from it is T whenever its variables are T, and $\neg p$ is out of reach.
For the same reason it must turn FF into T.
Among the $16$ binary [[logical connectives|QS0XVAN9BG]], exactly two do both and also express the rest: NAND and NOR.

## Notation

We write $p \uparrow q$ for NAND and $p \downarrow q$ for NOR.
Many books write the Sheffer stroke as $p \mid q$, and some write $p \,\overline{\land}\, q$.
In Polish notation the Sheffer stroke is $Dpq$.
The bar $\mid$ also means "divides" in number theory, so the arrow $\uparrow$ is safer in mixed texts.

## Remarks

### The truth table

Take $p$ = "$n$ is even" and $q$ = "$n$ is prime", and test four numbers.

| $n$ | $p$ | $q$ | $p \uparrow q$ | $p \downarrow q$ |
|---|---|---|---|---|
| $2$ | T | T | F | F |
| $4$ | T | F | T | F |
| $3$ | F | T | T | F |
| $9$ | F | F | T | T |

"Not both even and prime" fails only at $n = 2$.
"Neither even nor prime" holds only at $n = 9$.
By [[De Morgan's laws|09PKJKA6J0]], $p \uparrow q \equiv \neg p \lor \neg q$ and $p \downarrow q \equiv \neg p \land \neg q$.
Both connectives are commutative.

### Building the other connectives

Applied to two copies of $p$, the stroke says "not both $p$ and $p$", so $p \uparrow p \equiv \neg p$ gives [[negation|029JBBF693]].
Negating the stroke gives back the [[conjunction|025YZN3VJW]], $p \land q \equiv (p \uparrow q) \uparrow (p \uparrow q)$.
And $p \lor q \equiv \neg p \uparrow \neg q \equiv (p \uparrow p) \uparrow (q \uparrow q)$.
[[The stroke example|S3KJ52G2SF]] checks these three in all four rows, and [[the Peirce arrow example|WH9JHEB1K3]] does the same for NOR.
Implication follows: $p \to q \equiv p \uparrow (q \uparrow q)$, because $q \uparrow q$ is $\neg q$ and $p \uparrow \neg q$ is $\neg(p \land \neg q)$.

### Why only these two

Since $\{\neg, \land\}$ is functionally complete and the stroke expresses both, the stroke alone is functionally complete, and the same argument works for NOR.
No other binary connective is complete alone.
This follows from [[Post's functional completeness theorem|WGBR7JHBV4]], and a direct check of the $16$ tables confirms it.
The connectives $\land$, $\lor$, $\to$ and $\leftrightarrow$ give T on the input TT, so they keep T and never build $\neg p$.
[[The exclusive or|KBG5Y5K65F]] gives F on the input FF, so it keeps F and fails in the same way.

### Nicod's single axiom

In 1917 Jean Nicod gave a [[Hilbert system|1MGMQX43B8]] for classical propositional logic with the stroke as its only connective, one axiom scheme and one rule.
The axiom scheme is
$$(\varphi \uparrow (\chi \uparrow \psi)) \uparrow \big((\tau \uparrow (\tau \uparrow \tau)) \uparrow ((\theta \uparrow \chi) \uparrow ((\varphi \uparrow \theta) \uparrow (\varphi \uparrow \theta)))\big).$$
The rule infers $\psi$ from $\varphi$ and $\varphi \uparrow (\chi \uparrow \psi)$.
The rule is sound, because $\varphi \uparrow (\chi \uparrow \psi) \equiv \varphi \to (\chi \land \psi)$, so it is a form of [[modus ponens|0Y0MQYST0M]].
The axiom is a tautology, as a computation over all $2^5 = 32$ assignments to $\varphi, \chi, \psi, \tau, \theta$ shows.
Nicod's result is that every tautology written with the stroke is derivable in this system.

### Watch out

The stroke is not associative, so $p \uparrow q \uparrow r$ needs brackets.
At $p$ T, $q$ T, $r$ F, the formula $(p \uparrow q) \uparrow r$ is $\mathrm{F} \uparrow \mathrm{F} = \mathrm{T}$, while $p \uparrow (q \uparrow r)$ is $\mathrm{T} \uparrow \mathrm{T} = \mathrm{F}$.
Also, $\neg p$ is $p \uparrow p$, not $p \uparrow \bot$, since $p \uparrow \bot$ is $\neg(p \land \bot)$, which is always T.
And the stroke $p \mid q$ means "not both", not "or" and not "divides".

### History

Charles Sanders Peirce found, in unpublished work of about 1880, that NAND alone and NOR alone can express all truth functions.
Henry Maurice Sheffer published in 1913 an axiom system for Boolean algebra with a single operation written with a stroke, and the connective carries his name.
Jean Nicod used the stroke in 1917 for his single axiom of propositional logic.
The name "Peirce arrow" for NOR honors Peirce's discovery.

### Try it

Compute $(\mathrm{T} \uparrow \mathrm{F}) \uparrow \mathrm{T}$.
First $\mathrm{T} \uparrow \mathrm{F} = \mathrm{T}$, then $\mathrm{T} \uparrow \mathrm{T} = \mathrm{F}$.

Write $\neg p$ with the Peirce arrow alone.
"Neither $p$ nor $p$" is $p \downarrow p$, which is T exactly when $p$ is F.

## Explanations

### L1 human

The Sheffer stroke says "not both".
"Not both: the shop is open and the shop is closed" is always true, because a shop cannot be both.
"Not both: $2$ is even and $3$ is odd" is false, because both parts are true.
The surprise is that this one rule is enough to build "not", "and", "or" and every other way to join statements.
For example, "not both $p$ and $p$" says the same as "not $p$".

### L2 human

Express $p \leftrightarrow q$ with the stroke alone.

1. Write $p \leftrightarrow q \equiv (p \land q) \lor (\neg p \land \neg q)$, and call the two disjuncts $A$ and $B$.
2. Since $A \lor B \equiv \neg A \uparrow \neg B$, we need $\neg A$ and $\neg B$.
3. Here $\neg A \equiv p \uparrow q$, and $\neg B \equiv \neg p \uparrow \neg q \equiv (p \uparrow p) \uparrow (q \uparrow q)$.
4. So $p \leftrightarrow q \equiv (p \uparrow q) \uparrow \big((p \uparrow p) \uparrow (q \uparrow q)\big)$.
5. Check the row TF: $p \uparrow q = \mathrm{T}$, and $(p \uparrow p) \uparrow (q \uparrow q) = \mathrm{F} \uparrow \mathrm{T} = \mathrm{T}$.
   So the formula is $\mathrm{T} \uparrow \mathrm{T} = \mathrm{F}$, as $p \leftrightarrow q$ requires.

Circuit designers make such translations, since a chip of NAND gates alone is cheaper than a mix of gates.
Watch out: formulas with the stroke alone grow long fast, so translate in steps and check each step with a truth table.

### L3 human

Functional completeness of a set of connectives means that the set generates the clone of all operations on $\{\mathrm{T}, \mathrm{F}\}$.
[[Post's functional completeness theorem|WGBR7JHBV4]] names five properties: preserving T, preserving F, being monotone, being self-dual and being affine.
A set is complete exactly when, for each property, some member of the set fails it.
NAND and NOR fail all five, and they are the only binary connectives that do.
On a finite set with more than two elements, a single operation that generates all operations is called a [[Sheffer function|1K829SJG3K]].
In circuit design, NAND gates alone, or NOR gates alone, can build every [[logic gate|AMH914MF2A]], and [[Nand|VJMV4X7PWH]] records this use.
In proof theory, Nicod's system shows that a complete Hilbert system can have one connective, one axiom scheme and one rule.
