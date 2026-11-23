---
tag: 0QHEWQD30B
kind: concept
name: Predicate
aliases: [propositional-function]
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
uses: [0ZGC7ZESYN, 0BSJ7RQ9BW, 9HFER6N708]
sources:
  - url: https://en.wikipedia.org/wiki/Predicate_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Domain_of_discourse
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.1
same_as:
  wikidata: Q1144319
  wikipedia: Predicate (logic)
---

## Summary

A predicate is a sentence with a blank, such as "$n$ is prime", that becomes true or false once you fill the blank.
On the numbers $1$ to $10$, filling in $7$ gives the true [[proposition|0ZGC7ZESYN]] "$7$ is prime", filling in $8$ gives a false one, and the fillings that give true sentences form the truth set $\{2, 3, 5, 7\}$.
In general, let $D$ be a [[set|0BSJ7RQ9BW]], the domain of discourse, and let $n \ge 1$.
An $n$-ary predicate on $D$ is an expression $P(x_1, \dots, x_n)$ with free variables $x_1, \dots, x_n$, such that for each [[tuple|9HFER6N708]] $(a_1, \dots, a_n) \in D^n$ the substituted expression $P(a_1, \dots, a_n)$ is a proposition.
Its truth set is the $n$-ary relation
$$T_P = \{(a_1, \dots, a_n) \in D^n \mid P(a_1, \dots, a_n) \text{ is true}\}.$$
The [[formal definition|0T3DPBG981]] states this with each condition named.

## Motivation

In propositional logic, "$7$ is prime" and "$8$ is prime" are two unrelated variables $p$ and $q$.
The logic cannot see that both sentences say the same thing about two different numbers.
So it cannot express "every prime greater than $2$ is odd", and it cannot check the argument "every prime greater than $2$ is odd; $7$ is a prime greater than $2$; so $7$ is odd".

The fix is to separate the property from the object.
The open sentence "$x$ is prime" is a predicate, and "$7$ is prime" is what you get by putting $7$ in place of $x$.
A predicate with two variables, such as "$x$ divides $y$", expresses a relation between two objects.
Every definition in mathematics defines a predicate, and the quantifiers $\forall$ and $\exists$ of the next pages act on predicates to make statements.

## Notation

Books write $P(x)$, $Q(x, y)$ or $R(x_1, \dots, x_n)$, and many logic books drop the brackets and write $Px$ or $Rxy$.
A binary predicate is often written between its variables, as in $x < y$, $x \mid y$ or $x \in A$.
The truth set of a unary predicate is $\{x \in D \mid P(x)\}$ in [[set-builder notation|0TMZ89Q5KA]]; other names are the extension of $P$ and, for an equation, its solution set.
The domain of discourse is also called the universe of discourse.
Unary predicates are also called [[monadic predicates|156GNVG2DT]], and letters that stand for arbitrary predicates are [[predicate variables|Q8ZEXA1KE6]].
In Lean, a predicate on a type `α` is a function `α → Prop`.

## Remarks

### Filling the blanks

[[The predicate "$n$ is prime" on the numbers $1$ to $10$|AMYQ47TB3F]] is the first example to work through.
Check each number: $1$ is not prime by definition, $2$, $3$, $5$ and $7$ have no divisor strictly between $1$ and themselves, and $4$, $6$, $8$, $9$, $10$ all factor.
So the truth set is $\{2, 3, 5, 7\}$.

[[The predicate "$x$ divides $y$" on $\{1, 2, 3, 4\}$|3RMVHD47KR]] has two blanks, so you check all $16$ ordered pairs.
The pairs that make it true are $(1, 1)$, $(1, 2)$, $(1, 3)$, $(1, 4)$, $(2, 2)$, $(2, 4)$, $(3, 3)$ and $(4, 4)$, eight in all.
Order matters, since $2 \mid 4$ is true and $4 \mid 2$ is false.

The ternary predicate $x + y = z$ on $\mathbb{N}$ has as truth set all triples $(a, b, a + b)$, the graph of addition.

### The domain decides

The predicate $x^2 < 4$ has the truth set $(-2, 2)$ on $D = \mathbb{R}$ and the truth set $\{-1, 0, 1\}$ on $D = \mathbb{Z}$.
In the same way, "$x^2 = 2$ has a solution" is false on $\mathbb{Q}$ and true on $\mathbb{R}$.
Two predicates on $D$ are equivalent when they have the same truth set, and this also depends on $D$.
The predicates $x^2 = 1$ and $x = 1$ are equivalent on $\mathbb{N}$ but not on $\mathbb{Z}$, where $x = -1$ separates them.

### Free and bound variables

The formula $\exists y \in \mathbb{Z} \; (x = 2y)$ contains two variables, but the quantifier binds $y$, so only $x$ is free.
It is a unary predicate on $\mathbb{Z}$, and its truth set is the set of even integers.
Fixing one variable of an $n$-ary predicate gives an $(n - 1)$-ary predicate.
Fixing $x = 2$ in "$x \mid y$" gives "$2 \mid y$", that is, "$y$ is even".

### What is not a predicate

[[The expression $x^2 + 1$ is not a predicate|N3BWWPFE9K]]: putting $x = 2$ gives the number $5$, which is neither true nor false, so the expression is a term.
"$7$ is prime" has no free variable, so it is already a proposition; some books call it a $0$-ary predicate.
$\forall x \in \mathbb{R} \; (x^2 \ge 0)$ is also a proposition, because its only variable is bound.
"$x$ is a large number" is not a predicate of mathematics, because "large" has no exact meaning and $x = 1000$ gives no definite truth value.

### Truth sets and set operations

Connectives on unary predicates match operations on truth sets.
The truth set of $P(x) \land Q(x)$ is the [[intersection|0ZNMMA9TF5]] of the two truth sets, that of $P(x) \lor Q(x)$ is the [[union|0X1GSWNBN1]], and that of $\neg P(x)$ is the [[complement|0RKF1ZT5JJ]] in $D$.
The statement $\forall x \in D \; (P(x) \to Q(x))$ is true exactly when $T_P$ is a [[subset|0BJR9QR08E]] of $T_Q$.
The statement $\forall x \in D \; P(x)$ is true exactly when $T_P = D$, and $\exists x \in D \; P(x)$ is true exactly when $T_P$ is nonempty; the [[universal quantifier|0GHS47PDAQ]] and the [[existential quantifier|0MSRQHCNN9]] develop this.
A binary predicate and its truth set, a [[binary relation|05AVARPXA2]], carry the same information.

### Watch out

An open sentence has no truth value, so "$x > 3$ is false" makes no sense until $x$ has a value or is quantified, as [[the open sentence $x > 3$ is not a statement|1812QVCW76]] explains.
Do not call a formula for a number a predicate: $f(x) = x^2$ defines a term, while $f(x) = 4$ is a predicate.
And always say what the domain is, because the truth set changes with it.

### History

Aristotle analyzed a sentence into a subject and a predicate, as in "Socrates is mortal".
In his Begriffsschrift of 1879, Gottlob Frege replaced this with function and argument: a predicate behaves like a function whose values are truth values.
Frege introduced the quantifiers in the same work, and Charles Sanders Peirce introduced them independently in the 1880s.

### Try it

Find the truth set of "$x^2 - 3x + 2 \le 0$" on $\mathbb{Z}$.
The left side is $(x - 1)(x - 2)$, which is at most $0$ exactly for $1 \le x \le 2$, so the truth set is $\{1, 2\}$.

Is "$x + y$ is even" equivalent to "$x = y$" on $\{0, 1\}$?
Yes: both have the truth set $\{(0, 0), (1, 1)\}$, but on $\{0, 1, 2\}$ the pair $(0, 2)$ separates them.

## Explanations

### L1 human

A predicate is a sentence with a blank, such as "___ is prime".
It is not true or false yet, because the blank is empty.
Fill the blank with $7$ and you get "$7$ is prime", which is true.
Fill it with $8$ and you get "$8$ is prime", which is false.
The fillings that make the sentence true form the truth set, and for the numbers $1$ to $10$ it is $\{2, 3, 5, 7\}$.
A sentence with two blanks, such as "___ is smaller than ___", compares two things.

### L2 human

Find the truth set of $P(x)$: "$x^2 - 3x + 2 \le 0$" on $D = \mathbb{Z}$.
First factor:
$$x^2 - 3x + 2 = (x - 1)(x - 2).$$
A product of two real numbers is at most $0$ when one factor is $0$ or the factors have opposite signs, and here that means $1 \le x \le 2$.
The integers in $[1, 2]$ are $1$ and $2$, so the truth set is $\{1, 2\}$.
Check: $P(1)$ and $P(2)$ say $0 \le 0$, which is true, and $P(0)$ and $P(3)$ say $2 \le 0$, which is false.
So $\exists x \in \mathbb{Z} \; P(x)$ is true and $\forall x \in \mathbb{Z} \; P(x)$ is false.
A definition works the same way: "$n$ is even when $\exists k \in \mathbb{Z} \; (n = 2k)$" defines a predicate and, with it, the set of even integers.
Watch out: on $D = \mathbb{R}$ the same predicate has the truth set $[1, 2]$, an infinite set.

### L3 human

In [[first-order logic|086QKPF0A6]], a predicate symbol $R$ of arity $n$ is interpreted in a structure with domain $M$ as a subset $R^M \subseteq M^n$.
A formula $\varphi(x_1, \dots, x_n)$ defines the relation $\{\bar a \in M^n \mid M \models \varphi[\bar a]\}$, and the relations obtained in this way are the definable sets of the structure.
The [[satisfaction|2RBQPV02AS]] relation gives the exact meaning of "$P(\bar a)$ is true".
A predicate is the same as its characteristic function $D^n \to \{\mathrm{T}, \mathrm{F}\}$, so predicates on $D$ correspond to subsets of $D^n$, and the connectives correspond to the Boolean operations on the power set.

In set theory, the axiom schema of separation turns a predicate $P$ and a set $A$ into the set $\{x \in A \mid P(x)\}$.
A predicate on the universe of all sets need not define a set: the predicate $x \notin x$ gives Russell's paradox.
Second-order logic quantifies over predicates themselves.
