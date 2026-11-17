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

Let $D$ be a [[set|0BSJ7RQ9BW]], the domain of discourse, and let $n \ge 1$.
An $n$-ary predicate on $D$ is an expression $P(x_1, \dots, x_n)$ whose free variables are $x_1, \dots, x_n$, such that for each [[tuple|9HFER6N708]] $(a_1, \dots, a_n)$ of elements of $D$, the expression $P(a_1, \dots, a_n)$ obtained by substituting $a_i$ for $x_i$ is a [[proposition|0ZGC7ZESYN]].
A predicate is an open sentence: it has no truth value of its own, and it becomes a proposition when each free variable gets a value or is bound by a quantifier.
The truth set of $P$ is the set of the tuples that make it true, $\{(a_1, \dots, a_n) \in D^n \mid P(a_1, \dots, a_n) \text{ is true}\}$, and it is an $n$-ary relation on $D$.
Predicates are the language of mathematical definitions and theorems, because the quantifiers $\forall$ and $\exists$ act on them.
The precise definition is on the page [[predicate (definition)|0T3DPBG981]].

## Motivation

In propositional logic, "$7$ is prime" and "$8$ is prime" are two unrelated propositional variables $p$ and $q$.
The logic cannot see that both sentences say the same thing about two different numbers.
So it cannot express "every prime number greater than $2$ is odd", and it cannot check the argument "every prime number greater than $2$ is odd; $7$ is a prime number greater than $2$; so $7$ is odd".

The fix is to separate the property from the object.
The open sentence "$x$ is prime" is a predicate, and "$7$ is prime" is the result of substituting $7$ for $x$.
A predicate with two variables, such as "$x$ divides $y$", expresses a relation between two objects.
With predicates and quantifiers, the statements of mathematics get a precise logical form.

## Notation

A predicate is written $P(x)$, $Q(x, y)$ or $R(x_1, \dots, x_n)$; many logic books drop the brackets and write $Px$ or $Rxy$.
A binary predicate is often written between its variables, as in $x < y$, $x \mid y$ or $x \in A$.
The truth set of a unary predicate is written $\{x \in D \mid P(x)\}$ or $\{x \in D : P(x)\}$, in [[set-builder notation|0TMZ89Q5KA]]; other names are the extension of $P$ and, for an equation, its solution set.
The domain of discourse $D$ is also called the universe of discourse or the domain.
Unary predicates are also called [[monadic predicates|156GNVG2DT]], and the letters $P$, $Q$, $R$ that stand for arbitrary predicates are [[predicate variables|Q8ZEXA1KE6]].
In Lean, a predicate on a type is a function from the type to propositions.

## Remarks

### Examples

1. [[The predicate "$n$ is prime" on $\{1, \dots, 10\}$|~ca2f4ff4]]: a unary predicate with the truth set $\{2, 3, 5, 7\}$.
2. [[The predicate "$x$ divides $y$" on $\{1, 2, 3, 4\}$|~1724b473]]: a binary predicate whose truth set has $8$ pairs.
3. The predicate $x^2 < 4$ has the truth set $(-2, 2)$ on $D = \mathbb{R}$ and the truth set $\{-1, 0, 1\}$ on $D = \mathbb{Z}$. The truth set depends on the domain.
4. The ternary predicate $x + y = z$ on $\mathbb{N}$ has as truth set the set of triples $(a, b, a + b)$, the graph of addition.
5. The formula $\exists y \in \mathbb{Z} \; (x = 2y)$ contains two variables, but only $x$ is free, so it is a unary predicate on $\mathbb{Z}$. Its truth set is the set of even integers.
6. The page [[the open sentence $x > 3$ is not a statement|1812QVCW76]] shows a unary predicate on $\mathbb{R}$ that has no truth value until $x$ gets a value.

### Non-examples

1. [[The expression $x^2 + 1$ is not a predicate|~06064548]]: a substitution gives a number, not a proposition.
2. "$7$ is prime" is not a predicate with a variable: it has no free variable, so it is already a proposition. Some books call a proposition a $0$-ary predicate.
3. $\forall x \in \mathbb{R} \; (x^2 \ge 0)$ is not a predicate: its only variable is bound, so it is a proposition, and it is true.
4. "$x$ is a large number" is not a predicate in mathematics: for $x = 1000$ it has no definite truth value, because "large" has no exact meaning.

### Basic properties

1. Connectives on predicates match operations on truth sets. For unary predicates on $D$, the truth set of $P(x) \land Q(x)$ is the [[intersection|0ZNMMA9TF5]] of the truth sets, the truth set of $P(x) \lor Q(x)$ is the [[union|0X1GSWNBN1]], and the truth set of $\neg P(x)$ is the [[complement|0RKF1ZT5JJ]] in $D$.
2. The statement $\forall x \in D \; (P(x) \to Q(x))$ is true exactly when the truth set of $P$ is a [[subset|0BJR9QR08E]] of the truth set of $Q$.
3. The statement $\forall x \in D \; P(x)$ is true exactly when the truth set of $P$ is $D$, and $\exists x \in D \; P(x)$ is true exactly when the truth set is nonempty. See the [[universal quantifier|0GHS47PDAQ]] and the [[existential quantifier|0MSRQHCNN9]].
4. Fixing one variable of an $n$-ary predicate gives an $(n - 1)$-ary predicate. Fixing $x = 2$ in "$x \mid y$" gives the unary predicate "$2 \mid y$", "$y$ is even".
5. Two predicates on $D$ are equivalent when they have the same truth set, and this depends on $D$. The predicates $x^2 = 1$ and $x = 1$ are equivalent on $\mathbb{N}$ and not equivalent on $\mathbb{Z}$, because $x = -1$ separates them.
6. A binary predicate on $D$ and its truth set, a [[binary relation|05AVARPXA2]] on $D$, carry the same information: $P(a, b)$ is true exactly when $(a, b)$ is in the relation.

### History

Aristotle analysed a sentence into a subject and a predicate, as in "Socrates is mortal".
In his Begriffsschrift of 1879, Gottlob Frege replaced this analysis with function and argument: a predicate behaves like a function whose values are truth values.
Frege introduced the quantifiers in the same work, and Charles Sanders Peirce introduced them independently in the 1880s.

### Common errors

1. A student calls an open sentence true or false, as in "$x > 3$ is false". The sentence has a truth value only after $x$ gets a value or is quantified.
2. A student forgets the domain. "$x^2 = 2$ has a solution" is false on $\mathbb{Q}$ and true on $\mathbb{R}$.
3. A student calls an expression with a variable a predicate when its values are numbers, as in "$f(x) = x^2$ is a predicate". The expression $x^2$ is a term; the equation $f(x) = 4$ is a predicate.

## Explanations

### L1 human

A predicate is a sentence with a blank, such as "___ is prime".
It is not true or false yet, because we do not know what is in the blank.
When we fill the blank with $7$, we get "$7$ is prime", which is true.
When we fill it with $8$, we get "$8$ is prime", which is false.
The set of all fillings that make the sentence true is the truth set: for the numbers $1$ to $10$ it is $\{2, 3, 5, 7\}$.
A sentence with two blanks, such as "___ is smaller than ___", compares two things.

### L2 human

We find the truth set of the predicate $P(x)$: "$x^2 - 3x + 2 \le 0$" on $D = \mathbb{Z}$.

1. Factor: $x^2 - 3x + 2 = (x - 1)(x - 2)$.
2. A product of two real numbers is at most $0$ when the factors have opposite signs or one factor is $0$. Here this means $1 \le x \le 2$.
3. The integers in $[1, 2]$ are $1$ and $2$. So the truth set is $\{1, 2\}$.
4. Check: $P(1)$ says $0 \le 0$, true; $P(2)$ says $0 \le 0$, true; $P(3)$ says $2 \le 0$, false; $P(0)$ says $2 \le 0$, false.
5. So $\exists x \in \mathbb{Z} \; P(x)$ is true and $\forall x \in \mathbb{Z} \; P(x)$ is false.

The typical use of a predicate is in a definition: "an integer $n$ is even when $\exists k \in \mathbb{Z} \; (n = 2k)$" defines the predicate "$n$ is even" and, with it, the set of even integers.
A trap is to change the domain silently: on $D = \mathbb{R}$ the same predicate has the truth set $[1, 2]$, an infinite set.

### L3 human

In [[first-order logic|086QKPF0A6]], a predicate symbol $R$ of arity $n$ is interpreted in a structure with domain $M$ as a subset $R^M \subseteq M^n$, and a formula $\varphi(x_1, \dots, x_n)$ with free variables $x_1, \dots, x_n$ defines the relation $\{\bar a \in M^n \mid M \models \varphi[\bar a]\}$.
The relations obtained in this way are the definable sets of the structure, and the [[satisfaction|2RBQPV02AS]] relation gives the exact meaning of "$P(\bar a)$ is true".
A predicate is the same as its characteristic function $D^n \to \{\mathrm{T}, \mathrm{F}\}$, so predicates on $D$ correspond to subsets of $D^n$, and the connectives correspond to the Boolean operations on the power set.

In set theory, the axiom schema of separation turns a predicate $P$ and a set $A$ into the set $\{x \in A \mid P(x)\}$.
A predicate on the universe of all sets need not define a set: the predicate $x \notin x$ gives Russell's paradox.
In type theory, a predicate on a type is a function into a type of propositions, and second-order logic quantifies over the predicates themselves.
The quantifier pages of this sub-area, [[universal quantifier|0GHS47PDAQ]] and [[existential quantifier|0MSRQHCNN9]], build propositions from predicates.
