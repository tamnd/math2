---
tag: PTMR3P9J6C
kind: concept
name: Exclusive or
aliases: [xor, exclusive-disjunction]
msc: ["03B05", "06E30"]
topics: [PM1AYWABA7]
audience: school
uses: [0ZGC7ZESYN, 029JBBF693, 025YZN3VJW, 0F72FK8EKB, 0S6GMNJ62Y]
sources:
  - url: https://en.wikipedia.org/wiki/Exclusive_or
    locator: lead section
  - url: https://en.wikipedia.org/wiki/GF(2)
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
same_as:
  wikipedia: Exclusive or
---

## Summary

Exclusive or is the "one or the other, but not both" of daily speech, and it is also the addition of bits.
A staircase lamp with a switch at the bottom and a switch at the top is on when exactly one switch is flipped, and off again when both are.
For [[propositions|0ZGC7ZESYN]] $p$ and $q$, the exclusive or $p \oplus q$ is true when exactly one of $p$ and $q$ is true, that is, when they have different truth values.
So $p \oplus q \equiv \neg(p \leftrightarrow q)$, the [[negation|029JBBF693]] of the [[biconditional|0S6GMNJ62Y]].
With $1$ for T and $0$ for F, the value of $p \oplus q$ is $p + q$ modulo $2$, and the [[formal definition|K1V1KVEAHN]] gives the table.

## Motivation

The mathematical "or" is inclusive, but some alternatives exclude each other, and a connective that is false when both parts hold describes them exactly.
A second source is arithmetic with bits: the last bit of $a + b$ for two bits is $1$ exactly when one of $a$, $b$ is $1$.
A third source is parity: a lamp wired to several switches is on when an odd number of them has been flipped.
These are one connective, $\oplus$, and it returns in error-detecting codes, in ciphers, in circuits that add numbers, and in the algebra of [[Boolean rings|0RCV1ZFP8G]].

## Notation

We write $p \oplus q$.
Other notations are $p \mathbin{\underline{\vee}} q$, $p \not\leftrightarrow q$, $p \not\equiv q$, XOR and EOR, and many programming languages write `p ^ q`.
In a Boolean ring the exclusive or is written $p + q$, while some books on Boolean algebra use $+$ for the inclusive "or", so check the convention of each book.
In Lean's Mathlib, the exclusive or of two propositions is `Xor' a b`, defined as $(a \land \neg b) \lor (b \land \neg a)$.

## Remarks

### The truth table

Take $n = 9$, $p$ = "$n$ is odd" and $q$ = "$n$ is prime".
Here $p$ is T and $q$ is F, so exactly one part holds and $p \oplus q$ is T.
For $n = 7$ both parts are T, and $p \oplus q$ is F.
The four rows are:

| $p$ | $q$ | $p \oplus q$ | $p \leftrightarrow q$ |
|---|---|---|---|
| T | T | F | T |
| T | F | T | F |
| F | T | T | F |
| F | F | F | T |

The table of $\oplus$ agrees with the inclusive [[disjunction|0F72FK8EKB]] except in the row TT.
The last column shows that $\oplus$ and $\leftrightarrow$ disagree in every row, which proves $p \oplus q \equiv \neg(p \leftrightarrow q)$.
Moving the negation inside gives two more forms, $\neg p \leftrightarrow q$ and $p \leftrightarrow \neg q$.
"At least one but not both" gives $(p \lor q) \land \neg(p \land q)$, and listing the two true rows gives $(p \land \neg q) \lor (\neg p \land q)$.

### Addition modulo 2

With $1$ for T and $0$ for F, the table is the addition table of the [[integers modulo 2|03VFZ2WETT]]: $0 + 0 = 0$, $0 + 1 = 1 + 0 = 1$, and $1 + 1 = 0$.
So every law of $\oplus$ is a law of addition in the field [[GF(2)|C2TYYZEY7F]].
F is the zero, $p \oplus \mathrm{F} \equiv p$, and every proposition is its own inverse, $p \oplus p \equiv \mathrm{F}$.
Adding T is negation, $p \oplus \mathrm{T} \equiv \neg p$.
Conjunction is multiplication modulo $2$, and it distributes: $p \land (q \oplus r) \equiv (p \land q) \oplus (p \land r)$.
The inclusive "or" becomes $p \lor q \equiv p \oplus q \oplus (p \land q)$, which is $p + q - pq$ read modulo $2$.

### Associativity and parity

Exclusive or is commutative and associative, $(p \oplus q) \oplus r \equiv p \oplus (q \oplus r)$, because addition modulo $2$ is.
[[The truth table of $p \oplus q \oplus r$|DB2NK7HWFQ]] checks all $8$ rows and finds T exactly in the rows with $1$ or $3$ true inputs.
In general $p_1 \oplus \cdots \oplus p_n$ is T exactly when an odd number of the $p_i$ is T, since the sum of $n$ bits modulo $2$ is the parity of the number of $1$s.
That is the [[parity bit|D0E6Y0P30Q]] of a block of data.
[[On bit strings|PZZV5DGWKZ]] the same laws make $(m \oplus k) \oplus k = m$, so one key both encrypts and decrypts a one-time pad.

### What it is not

[["Exactly one of $p$, $q$, $r$"|ZV2QXSKFRG]] is not $p \oplus q \oplus r$: when all three are T, the first is F and the second is T, because $3$ is odd.
The menu claim [["soup or salad"|XBS0DS337X]] is an exclusive or, so it is not the inclusive $p \lor q$.
And disjunction does not distribute over $\oplus$: with $p$, $q$, $r$ all T, $p \lor (q \oplus r)$ is T, but $(p \lor q) \oplus (p \lor r)$ is $\mathrm{T} \oplus \mathrm{T}$, which is F.

### Watch out

Do not write $p + q$ for $p \lor q$ and then compute $1 + 1 = 0$.
Modulo $2$, $+$ is $\oplus$, and $p \lor q$ has the value $1$ when $p = q = 1$.
Also, $\neg(p \leftrightarrow q)$ is not $\neg p \leftrightarrow \neg q$: in the row TF the second compares F with T, so it is F, while $\neg(p \leftrightarrow q)$ is T.
In fact $\neg p \leftrightarrow \neg q$ is equivalent to $p \leftrightarrow q$ itself.

### History

In The Laws of Thought of 1854, George Boole added two classes only when they had no common member, so his "or" behaved like the exclusive "or".
Later logic chose the inclusive "or" as the basic connective.
Marshall Stone showed in 1936 that Boolean algebras and Boolean rings are the same structures, with the exclusive or as the addition of the ring.

### Try it

Compute $1 \oplus 1 \oplus 0 \oplus 1 \oplus 1 \oplus 0$.
There are four $1$s, an even number, so the result is $0$.

For which real $x$ is "$x < 0$ xor $x > 0$" true?
For every $x \ne 0$ exactly one part holds, and at $x = 0$ both parts are F, so it is true exactly for $x \ne 0$.

## Explanations

### L1 human

"Exclusive or" means "one or the other, but not both".
Think of a staircase lamp with a switch at the bottom and a switch at the top.
Flipping one switch changes the lamp, and flipping both puts it back as it was.
So the lamp is on exactly when one switch is flipped.
In numbers, $1 + 0$ is $1$, but $1 + 1$ wraps around to $0$ when we keep only "even" or "odd".

### L2 human

Show that $p \oplus q \equiv (p \lor q) \land \neg(p \land q)$ by a truth table.

| $p$ | $q$ | $p \lor q$ | $\neg(p \land q)$ | $(p \lor q) \land \neg(p \land q)$ | $p \oplus q$ |
|---|---|---|---|---|---|
| T | T | T | F | F | F |
| T | F | T | T | T | T |
| F | T | T | T | T | T |
| F | F | F | T | F | F |

The last two columns agree in every row, so the formulas are equivalent.
This form is how a circuit builds XOR from OR, AND and NOT gates.
Watch out: the second factor matters, since $p \lor q$ alone is T in the row TT.

### L3 human

The bit strings $\{0, 1\}^n$ with bitwise $\oplus$ form the vector space $\mathrm{GF}(2)^n$.
Linear codes are subspaces of it, and the [[Hamming distance|EP5HNGSXFA]] of two strings is the number of $1$s in their exclusive or.
In [[Nim|HYQPVQF509]], a position is lost for the player to move exactly when the bitwise exclusive or of the heap sizes is $0$.
The power set of a set, with [[symmetric difference|0ME21QN125]] as addition and intersection as multiplication, is a Boolean ring.
Over $\mathrm{GF}(2)$ every [[Boolean function|0X05GS525E]] has a unique expression as an exclusive or of conjunctions of variables.
In complexity theory, [[parity is not in AC0|W6T7X0QCFH]]: circuits of bounded depth and polynomial size cannot compute it.
