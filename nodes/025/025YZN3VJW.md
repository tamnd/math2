---
tag: 025YZN3VJW
kind: concept
name: Conjunction
aliases: [logical-and]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0ZGC7ZESYN, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_conjunction
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
  - book: isbn:9781108439534
    locator: Section 3.4
same_as:
  wikidata: Q191081
  wikipedia: Logical conjunction
---

## Summary

A claim joined by "and" makes two promises, and it is true only when both are kept.
"$6$ is even and $6$ is divisible by $3$" is true, while "$6$ is even and $6$ is divisible by $4$" is false because its second part fails.
The conjunction of two [[propositions|0ZGC7ZESYN]] $p$ and $q$ is the proposition $p \land q$, read "$p$ and $q$", which is true when $p$ and $q$ are both true and false in the other three cases.
The [[formal definition|0M28ASWG8T]] gives its truth table, and Lean's Mathlib calls it `And`.
To prove $p \land q$ you prove $p$ and you prove $q$, and from $p \land q$ you may use either part.

## Motivation

Most definitions ask for several conditions at once.
An integer $n$ is prime when $n > 1$ and its only positive divisors are $1$ and $n$.
A function is a bijection when it is injective and surjective.
A theorem with a list of hypotheses means that all of them hold.
To check such a definition or to use such a theorem, we need the rule that a list of conditions holds exactly when each one holds, and $\land$ states that rule for two conditions.
Longer lists are repeated conjunctions, and in the [[universal quantifier|0GHS47PDAQ]] the idea extends to infinitely many conditions.

## Notation

Most books write $p \land q$; others write $p \,\&\, q$, $p \cdot q$ or $pq$, and programmers write `p && q`.
With truth values $1$ and $0$, the value of $p \land q$ is the product $pq$, which is also $\min(p, q)$.
In English, "and", "but", "both ... and", "although" and the commas in a list of hypotheses all express conjunction.
The chain $a < b < c$ abbreviates $a < b \land b < c$, and "neither $p$ nor $q$" is $\neg p \land \neg q$.
In Lean, `a ∧ b` is notation for `And a b`.

## Remarks

### The truth table

Fix $n = 6$ and let $p$ be "$n$ is even".
For $q$ = "$n$ is divisible by $3$" both parts are T and the conjunction is T.
For $q$ = "$n$ is divisible by $4$" the second part is F and the conjunction is F.
Running through all four cases gives the table:

| $p$ | $q$ | $p \land q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

One false part is enough to make the whole false.
That is why the definition of a prime excludes $1$: the condition "$n > 1$" fails, so the conjunction fails.

### Chains, lists and "but"

[[The chain $1 < x < 4$|5R76S1NW39]] is the conjunction "$1 < x$ and $x < 4$".
At $x = 2$ both parts are T, at $x = 5$ the second part is F, and the chain holds exactly on the interval $(1, 4)$.
In the same way, $x \in A \cap B$ means $x \in A \land x \in B$, so conjunction is the logic of [[intersection|0ZNMMA9TF5]].
"But" is a conjunction with a hint of contrast: [["the absolute value is continuous but not differentiable at $0$"|HW5E2DSZH3]] makes two claims, and both must be checked.

### When "and" is not a conjunction

"The solutions of $x^2 = 4$ are $2$ and $-2$" does not mean "$x = 2$ and $x = -2$", since no number equals both.
[[The condition $x^2 = 4$|7HZCKQQNKD]] is the disjunction "$x = 2$ or $x = -2$".
In [["$2$ and $3$ are coprime"|R4D9KAT2QH]] the word "and" joins two numbers in one relation, not two propositions.
"Add $2$ and then multiply by $3$" is a command with an order of steps, and a conjunction has no order.

### Proving and using a conjunction

In [[natural deduction|6KT3BJZ7D1]], [[conjunction introduction|FJN3XDRXAR]] concludes $p \land q$ from $p$ and $q$, and the two elimination rules conclude $p$, or $q$, from $p \land q$.
In Mathlib these rules are `And.intro`, `And.left` and `And.right`.
[[A natural-deduction proof that $p \land q$ implies $q \land p$|26RCAE7TTT]] uses all three.
The rules hold in [[intuitionistic logic|Q11N8X99FK]] as well as in classical logic.
In practice, a proof of "$f$ is a bijection" has two parts, injectivity and surjectivity, and a hypothesis "$f$ is a bijection" gives you both facts to use.

### The rules you can use

Each law below can be checked on the four or eight rows of a truth table.
Conjunction is commutative, $p \land q \equiv q \land p$, because its table is symmetric in $p$ and $q$.
It is associative, $(p \land q) \land r \equiv p \land (q \land r)$, since both sides are T only in the row TTT, so we write $p \land q \land r$.
It is idempotent, $p \land p \equiv p$, and with a true proposition $\top$ and a false one $\bot$ we have $p \land \top \equiv p$ and $p \land \bot \equiv \bot$.
It distributes over [[disjunction|0F72FK8EKB]], $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$, and [[De Morgan's laws|09PKJKA6J0]] give $\neg(p \land q) \equiv \neg p \lor \neg q$.
The full list is in [[laws of propositional logic|A9CSGZNBV5]].

### Watch out

The negation of "$p$ and $q$" is "not $p$ or not $q$", not "not $p$ and not $q$".
For $n = 4$, "$n$ is even and $n > 10$" is F, so its negation must be T; "$n$ is odd or $n \le 10$" is T, but "$n$ is odd and $n \le 10$" is F.
Also, prove both parts: a proof that only shows injectivity has not shown that $f$ is a bijection.

### History

George Boole wrote the conjunction of two classes as a product $xy$ in his algebra of logic of 1847 and 1854.
Gottlob Frege's Begriffsschrift of 1879 used negation and the conditional as the only basic connectives and expressed "$p$ and $q$" as $\neg(p \to \neg q)$.
The introduction and elimination rules come from Gerhard Gentzen's natural deduction of the 1930s.

### Try it

For which integers $n$ with $-2 \le n < 3$ is $n^2 > 1$?
The first condition leaves $-2, -1, 0, 1, 2$, and the squares are $4, 1, 0, 1, 4$, so only $n = -2$ and $n = 2$ satisfy the whole conjunction.

Find the truth value of $(p \land q) \land \neg r$ when $p$ and $q$ are T and $r$ is F.
Here $p \land q$ is T and $\neg r$ is T, so the whole is T.

## Explanations

### L1 human

A claim with "and" is true only when both parts are true.
"$10$ is even and $10$ is bigger than $5$" is true, because both parts are true.
"$10$ is even and $10$ is bigger than $50$" is false, because the second part is false.
The order of the parts does not matter: "$10$ is bigger than $5$ and $10$ is even" says the same thing.

### L2 human

Prove that if an integer $n$ is divisible by $6$, then $n$ is even and $n$ is divisible by $3$.
Assume $6 \mid n$, so $n = 6k$ for an integer $k$.
The goal is a conjunction, so we prove its two parts separately.
First, $n = 2(3k)$, so $n$ is even.
Second, $n = 3(2k)$, so $n$ is divisible by $3$.
Conjunction introduction joins the two parts.

Splitting a goal this way, and splitting a hypothesis into its parts, is how conjunction appears in almost every proof.
Watch out: the converse is also true, but the rules of conjunction do not prove it.
From $n = 2a$ and $3 \mid 2a$, the arithmetic fact that the prime $3$ does not divide $2$ gives $3 \mid a$, so $6 \mid n$; the logic only splits and joins the parts.

### L3 human

With truth values $0$ and $1$, conjunction is the minimum, and also the product, of its inputs.
In a lattice or a [[Boolean algebra|0XADJKM699]] it is the meet, the greatest lower bound, and in hardware it is the AND [[logic gate|AMH914MF2A]].
Over a finite domain $\{a_1, \ldots, a_n\}$, the statement "for every $x$, $P(x)$" is $P(a_1) \land \cdots \land P(a_n)$, so the universal quantifier generalizes conjunction.
In type theory a proof of $p \land q$ is a pair of proofs; Mathlib's `And` is a structure with fields `left` and `right`, a product type.
In the poset of propositions ordered by implication, $p \land q$ is the categorical product of $p$ and $q$.
