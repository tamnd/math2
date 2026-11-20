---
tag: S563QJHDTK
kind: example
name: The formula algebra is not a Boolean algebra
msc: ["03G05", "08B20"]
topics: [QYA4H5Y7VR]
audience: grad
not_instance_of:
  - target: 0XADJKM699
    note: the terms p ∧ q and q ∧ p are distinct elements, so the meet is not commutative
  - target: QC9M3Q8B8Q
    note: the formula algebra is not a quotient by provable equivalence
uses: [MGCVQXXQJH, TT7WT5HPN9, GTS4DRRMZR]
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum–Tarski_algebra
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Term_algebra
    locator: lead section
---

## Example

Let $F$ be the set of [[formulas|TT7WT5HPN9]] over $P = \set{p, q}$ in $\neg$ and $\to$, with the operations that build formulas.
Define $\varphi \land \psi := \neg(\varphi \to \neg \psi)$ and $\varphi \lor \psi := \neg \varphi \to \psi$ as before.
We check that $\langle F, \land, \lor, \neg \rangle$ fails several Boolean laws.

1. Commutativity of $\land$ fails: $p \land q$ is the string $\neg(p \to \neg q)$, and $q \land p$ is $\neg(q \to \neg p)$.
   These strings are different, so $p \land q \ne q \land p$ in $F$.
2. Idempotence fails: $p \land p$ is $\neg(p \to \neg p)$, which is longer than $p$.
3. Double negation fails: $\neg \neg p$ has two more symbols than $p$.
4. There is no greatest element: a top $\varphi$ would satisfy $\varphi \land \varphi = \varphi$, and step 2 excludes this for every $\varphi$.

So $F$ is not a [[Boolean algebra|0XADJKM699]], and it is not a Lindenbaum-Tarski algebra.

## Remarks

1. $F$ is the absolutely [[free algebra|GTS4DRRMZR]] in the signature $\neg$, $\to$: no equation between distinct terms holds in it.
2. The [[Lindenbaum-Tarski algebra|MGCVQXXQJH]] is the quotient of $F$ by provable equivalence, and in the quotient all the laws of steps 1 to 4 hold.
3. Every congruence of $F$ that contains provable equivalence gives a Boolean algebra as quotient, since that quotient is a quotient of $\mathbf{L}_\emptyset$.

## Explanations

### L1 human

Before we group formulas into boxes, each formula is just a string of symbols.
The strings "$p$ and $q$" and "$q$ and $p$" are different strings.
So the strings themselves do not obey the rules of logic.
The rules hold only after we group equivalent strings together.

### L2 human

1. Count symbols: $p$ has one symbol, and $\neg \neg p$ has three.
2. So $\neg \neg p \ne p$ in $F$.
3. In the Lindenbaum-Tarski algebra, $[\neg \neg p] = [p]$ by T2 and T3 of L.
4. So the quotient map $F \to \mathbf{L}_\emptyset$ merges the two strings.

The typical use: the formula algebra is the starting point of every Lindenbaum-Tarski construction.
The trap: the operations of $F$ are well defined, but they satisfy no laws.
