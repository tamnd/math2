---
tag: 0F72FK8EKB
kind: concept
name: Disjunction
aliases: [logical-or, inclusive-or]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0ZGC7ZESYN, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_disjunction
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
  - book: isbn:9781108439534
    locator: Section 3.5
same_as:
  wikidata: Q1651704
  wikipedia: Logical disjunction
---

## Summary

A claim joined by "or" offers alternatives, and it is true when at least one of them holds.
"$7$ is even or $7$ is odd" is true because its second part is true, and "$7$ is even or $7 > 10$" is false because both parts fail.
The disjunction of two [[propositions|0ZGC7ZESYN]] $p$ and $q$ is the proposition $p \lor q$, read "$p$ or $q$", which is false when both parts are false and true otherwise.
In mathematics this "or" is inclusive: $p \lor q$ is true also when both parts are true.
The [[formal definition|0H5GKDTB01]] gives its truth table, and Lean's Mathlib calls it `Or`.
To prove $p \lor q$ it is enough to prove one part, and to use $p \lor q$ you argue by cases.

## Motivation

Many facts of mathematics offer alternatives without saying which one holds.
Every integer is even or odd.
If $ab = 0$ for real numbers $a$ and $b$, then $a = 0$ or $b = 0$.
Every real number $x$ satisfies $x \ge 0$ or $x \le 0$, and $x = 0$ satisfies both.
That last fact shows why mathematics chose the inclusive reading: alternatives that overlap are common, and an exclusive "or" would make such statements false.
The elimination rule of $\lor$ is the method of [[proof by cases|0WCP0PVET6]], which runs through all of mathematics.

## Notation

Most books write $p \lor q$; some books on Boolean algebra write $p + q$, and programmers write `p || q`.
We avoid $+$, because $p + q$ modulo $2$ is the [[exclusive or|PTMR3P9J6C]].
With truth values $1$ and $0$, the value of $p \lor q$ is $\max(p, q)$, which also equals $p + q - pq$.
In English, "or", "either ... or" and often "unless" express disjunction, as [[translating statements into logical form|WGZX7GV3PP]] shows.
In Lean, `a ∨ b` is notation for `Or a b`.

## Remarks

### The truth table

Fix $n = 12$ and let $p$ be "$n$ is even".
For $q$ = "$n > 10$" both parts are T, and the inclusive "or" makes $p \lor q$ T.
For $n = 7$ and the same $q$, both parts are F, and only then is $p \lor q$ F.
The four cases give the table:

| $p$ | $q$ | $p \lor q$ |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

A single true part decides a disjunction, however many parts it has.
[["$x \le 3$ or $x \ge 2$"|BX9T7YS4B8]] is true for every real $x$, since the row FF would need $x > 3$ and $x < 2$ at once.

### Inclusive and exclusive "or"

In daily speech "or" is often exclusive: [["the meal comes with soup or salad"|XBS0DS337X]] promises one of the two, not both.
That claim is false in the row TT, so it is the exclusive or $p \oplus q$, not $p \lor q$.
In mathematics "or" is inclusive unless the text says "but not both" or "exactly one of".
The two readings differ only in the row where both parts are true, so when the parts cannot both hold, as in "$x < 0$ or $x \ge 0$", the choice does not matter.
[[Connectives in mathematical language|12QQ51VK01]] treats the reading of "or" in mathematical English.

### Proving and using a disjunction

In [[natural deduction|6KT3BJZ7D1]], the two introduction rules conclude $p \lor q$ from $p$, or from $q$; in Mathlib they are `Or.inl` and `Or.inr`.
[[Disjunction elimination|FTH70E7K1D]] says: if $p \lor q$ holds, and $r$ follows from $p$, and $r$ follows from $q$, then $r$ holds; in Mathlib it is `Or.elim`.
[[The proof that $n^2$ leaves remainder $0$ or $1$ on division by $4$|T6KQTVF2Q8]] uses both: the cases come from "$n$ is even or odd", and each case ends with an introduction rule.
The [[disjunctive syllogism|6EFJF9NAYX]] is a derived rule: from $p \lor q$ and $\neg p$, conclude $q$.

### What intuitionistic logic asks

Classical mathematicians often prove $p \lor q$ by assuming $\neg p$ and deriving $q$.
That step uses $(\neg p \to q) \to (p \lor q)$, which is not valid in [[intuitionistic logic|Q11N8X99FK]].
There a proof of $p \lor q$ must prove one of the parts and say which one.
For the same reason $p \lor \neg p$, the [[law of excluded middle|0RYYK8PG4S]], is not an intuitionistic law.

### The rules you can use

Disjunction is commutative and associative, so a disjunction of many parts is true exactly when at least one part is true.
It is idempotent, $p \lor p \equiv p$, and with a true proposition $\top$ and a false one $\bot$ we have $p \lor \bot \equiv p$ and $p \lor \top \equiv \top$.
It distributes over conjunction, $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$, and [[De Morgan's laws|09PKJKA6J0]] give $\neg(p \lor q) \equiv \neg p \land \neg q$, which Mathlib states as `not_or`.
In classical logic $p \to q \equiv \neg p \lor q$, as the page on [[material implication|0NMG7W7Q11]] shows.
In set language, $x \in A \cup B$ means $x \in A \lor x \in B$, so disjunction is the logic of [[union|0X1GSWNBN1]].
The full list is in [[laws of propositional logic|A9CSGZNBV5]].

### Watch out

A proof by cases must cover every possibility.
To prove $|x| \ge x$, the split "$x > 0$ or $x < 0$" misses $x = 0$, since that disjunction is F at $0$; the split "$x \ge 0$ or $x < 0$" is complete.
Also, the negation of "$p$ or $q$" is "not $p$ and not $q$", not "not $p$ or not $q$".
At $x = 5$ the claim "$x > 0$ or $x < 0$" is T, so its negation must be F.
The correct negation "$x \le 0$ and $x \ge 0$" is F there, but the wrong form "$x \le 0$ or $x \ge 0$" is T.

### History

Chrysippus and the Stoic logicians listed the disjunctive syllogism among their basic forms of argument.
George Boole, in his book of 1854, added two classes only when they had no common member, so his "or" behaved like the exclusive "or".
William Stanley Jevons argued in 1864 for the inclusive reading, and later logic and mathematics followed him.

### Try it

Is "$2$ is even or $2$ is prime" true?
Yes: both parts are true, and the inclusive "or" accepts that.

For which real $x$ is "$x^2 < 1$ or $x > 0$" true?
The first part holds on $(-1, 1)$ and the second on $(0, \infty)$, so the disjunction holds on their union $(-1, \infty)$.

## Explanations

### L1 human

A claim with "or" is true when at least one part is true.
"$7$ is even or $7$ is odd" is true, because the second part is true.
"$7$ is even or $7$ is bigger than $10$" is false, because both parts are false.
In mathematics "or" also allows both parts to be true, so "$12$ is even or $12$ is bigger than $10$" is true.
On a menu, "soup or salad" usually means only one, and that is a different "or".

### L2 human

Prove that $|x| \ge x$ for every real $x$, where $|x| = x$ for $x \ge 0$ and $|x| = -x$ for $x < 0$.
The order of the real numbers gives the disjunction "$x \ge 0$ or $x < 0$", and we use it by cases.
If $x \ge 0$, then $|x| = x$, so $|x| \ge x$.
If $x < 0$, then
$$|x| = -x > 0 > x,$$
so again $|x| \ge x$.
The goal holds in both cases, so disjunction elimination gives it for every $x$.
A known disjunction, such as "even or odd" or "$\ge 0$ or $< 0$", is the usual source of the cases in such a proof.

### L3 human

With truth values $0$ and $1$, disjunction is the maximum of its inputs; in a lattice or a [[Boolean algebra|0XADJKM699]] it is the join, and in hardware the OR [[logic gate|AMH914MF2A]].
Over a finite domain $\{a_1, \ldots, a_n\}$, "there is an $x$ with $P(x)$" is $P(a_1) \lor \cdots \lor P(a_n)$, so the [[existential quantifier|0MSRQHCNN9]] generalizes disjunction.
In type theory a proof of $p \lor q$ is a proof of one part with a tag that says which; Mathlib's `Or` is this sum type, with constructors `Or.inl` and `Or.inr`.
The rule `Or.elim` is the universal property of the coproduct.
Intuitionistic logic has the disjunction property: if $p \lor q$ is provable from no assumptions, then $p$ or $q$ is provable.
Classical logic lacks it, as $p \lor \neg p$ shows for a variable $p$.
