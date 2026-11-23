---
tag: 0FYQMKFE77
kind: concept
name: Order of quantifiers
aliases: [quantifier-order]
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
uses: [0GHS47PDAQ, 0MSRQHCNN9, 0QHEWQD30B]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Uniform_continuity
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.2
same_as:
  wikidata: Q592911
  wikipedia: Quantifier (logic)
---

## Summary

"Every class in the school has a teacher" and "some teacher teaches every class" use the same words in a different order, and the second claim is much stronger.
In symbols, with $T(c, t)$ meaning "$t$ teaches $c$", the first is $\forall c \, \exists t \, T(c, t)$ and the second is $\exists t \, \forall c \, T(c, t)$.
In general, let $P(x, y)$ be a [[predicate|0QHEWQD30B]] with two free variables on a domain $D$.
The order of quantifiers is the order, read from left to right, in which the [[universal quantifier|0GHS47PDAQ]] and the [[existential quantifier|0MSRQHCNN9]] bind the variables.
Quantifiers of the same kind can be exchanged, but quantifiers of different kinds cannot.
The statement $\exists y \, \forall x \, P(x, y)$ implies $\forall x \, \exists y \, P(x, y)$, and the converse fails.
In $\forall x \, \exists y \, P(x, y)$ the witness $y$ may depend on $x$, while in $\exists y \, \forall x \, P(x, y)$ one $y$ must work for every $x$.

## Motivation

The definitions of [[continuity|0X3WGX95FE]] and of [[uniform continuity|0M4JJT780X]] of a function $f \colon A \to \mathbb{R}$ use the same symbols in a different order:
$$\text{continuous:} \quad \forall a \in A \;\, \forall \varepsilon > 0 \;\, \exists \delta > 0 \;\, \forall x \in A \;\, \bigl( |x - a| < \delta \to |f(x) - f(a)| < \varepsilon \bigr),$$
$$\text{uniformly continuous:} \quad \forall \varepsilon > 0 \;\, \exists \delta > 0 \;\, \forall a \in A \;\, \forall x \in A \;\, \bigl( |x - a| < \delta \to |f(x) - f(a)| < \varepsilon \bigr).$$
Only the position of $\forall a$ changes.
In the first line $\delta$ comes after $a$ and $\varepsilon$, so it may depend on both, and in the second line one $\delta$ must serve every point $a$.
The function $x^2$ on $\mathbb{R}$ satisfies the first definition and not the second, so the two orders give different notions.
Many definitions in analysis and algebra differ only in this way.

## Notation

A string of quantifiers is read from left to right, and each quantifier has the rest of the formula as its scope.
So $\forall x \, \exists y \, P(x, y)$ means $\forall x \, \bigl( \exists y \, P(x, y) \bigr)$.
Quantifiers of the same kind are often grouped: $\forall x, y \in \mathbb{R}$ means $\forall x \in \mathbb{R} \; \forall y \in \mathbb{R}$.
To show how a witness depends on earlier variables, authors write $y = y(x)$ or $\delta = \delta(\varepsilon, a)$.
In English, a quantifier at the end of a sentence, as in "$|f(x) - f(a)| < \varepsilon$ for all $x$", leaves the reader to find its scope, and symbols remove the doubt.

## Remarks

### A first check on a small domain

Let $D = \{1, 2, 3\}$ and let $P(x, y)$ mean $x + y = 4$.
The table lists the truth values of $P(x, y)$, with $x$ in the rows and $y$ in the columns.

| $P(x, y)$ | $y = 1$ | $y = 2$ | $y = 3$ |
|---|---|---|---|
| $x = 1$ | F | F | T |
| $x = 2$ | F | T | F |
| $x = 3$ | T | F | F |

Every row contains a T, so $\forall x \, \exists y \, P(x, y)$ is true, with $y = 4 - x$.
No column is all T, so $\exists y \, \forall x \, P(x, y)$ is false.
In general, $\forall x \, \exists y$ asks for a T in every row, and $\exists y \, \forall x$ asks for a column of T.

### Examples

[[The square function is continuous but not uniformly continuous on $\mathbb{R}$|D3GPZRVGDM]]: the order $\forall a \, \forall \varepsilon \, \exists \delta$ holds and the order $\forall \varepsilon \, \exists \delta \, \forall a$ fails.
[[The identity and inverse axioms of a group differ in the order of quantifiers|MX1W7T91RG]]: the identity axiom has the form $\exists e \, \forall x$, and the inverse axiom has the form $\forall x \, \exists y$.
Over $\mathbb{Z}$, $\forall x \, \exists y \, (y > x)$ is true and $\exists y \, \forall x \, (y > x)$ is false, as [[every number has a larger one, but no number is larger than all|F1GYSA9TW0]] checks.
For a real sequence, $\forall \varepsilon > 0 \; \exists N \; \forall n \geq N \; |a_n - L| < \varepsilon$ says that $a_n \to L$.
With $\exists N$ moved to the front, it says that $a_n = L$ for all $n \geq N$, since a number $|a_n - L| \ge 0$ below every $\varepsilon > 0$ is $0$.

### When the order does not matter

[[Two existential quantifiers can be exchanged|RKAJ2ZPA1T]], and two universal quantifiers can too.
For $\forall$, both orders say that every pair satisfies $P$, and for $\exists$, a pair $(a, b)$ with $P(a, b)$ is a witness for both orders.
If the predicate does not depend on $x$, the order does not matter on a nonempty domain: $\forall x \, \exists y \, Q(y) \equiv \exists y \, Q(y) \equiv \exists y \, \forall x \, Q(y)$.

### The rules you can use

To prove $\exists y \, \forall x \, P(x, y) \to \forall x \, \exists y \, P(x, y)$, choose $y_0$ with $\forall x \, P(x, y_0)$, let $x_0$ be arbitrary, and note $P(x_0, y_0)$, so $y_0$ is a witness for $\exists y \, P(x_0, y)$.
No step uses excluded middle, so the implication is valid in [[intuitionistic logic|Q11N8X99FK]] as well.
The converse fails, as the table shows, and the invalid step from $\forall \exists$ to $\exists \forall$ is the [[quantifier shift fallacy|CRW82NARQV]].
In a longer prefix, a witness may depend on the universally quantified variables to its left and on no others.
With the [[axiom of choice|0HTGB13FE2]], $\forall x \, \exists y \, P(x, y)$ is equivalent to $\exists g \, \forall x \, P(x, g(x))$, and $\exists y \, \forall x$ asks for a constant $g$.
Negation keeps the order of the variables and switches each quantifier: $\neg \forall x \, \exists y \, P(x, y) \equiv \exists x \, \forall y \, \neg P(x, y)$, by the [[negation of a universal statement|0P3A06QNDP]] and the [[negation of an existential statement|05SZQKH75K]].

### Watch out

A proof that gives "for each $a$ there is a $\delta$" does not give "there is a $\delta$ for all $a$".
In a proof of $\forall x \, \exists y$, the witness $y$ must be chosen after $x$ is given, and it may not depend on a variable introduced later.
Negating $\forall x \, \exists y \, P$ as $\exists y \, \forall x \, \neg P$ changes the order of the variables; the correct negation keeps $x$ first, $\exists x \, \forall y \, \neg P$.

### History

Ordinary language often leaves the order of quantifiers to the context.
Gottlob Frege's Begriffsschrift of 1879 wrote each quantifier with a bound variable and a scope, so the order became part of the notation.
In 19th-century analysis, the difference between pointwise and uniform statements was a source of errors, as the discussion of Cauchy's sum theorem in [[quantifier shift fallacy|CRW82NARQV]] describes.

### Try it

Over $\mathbb{N} = \{0, 1, 2, \dots\}$, is $\exists y \, \forall x \, (y \le x)$ true?
Yes: $y = 0$ satisfies $0 \le x$ for every natural number $x$.

Over $\mathbb{Z}$, is $\exists y \, \forall x \, (y \le x)$ true?
No: for any integer $y$, the integer $x = y - 1$ gives $y \not\le x$, although $\forall x \, \exists y \, (y \le x)$ is true with $y = x$.

## Explanations

### L1 human

"Every class in the school has a teacher" is a claim about each class.
Class $1$ can have teacher Ana, class $2$ teacher Ben, and class $3$ teacher Cara.
"There is a teacher who teaches every class" asks for one person, for example Ana, in all three classes.
The words are almost the same, but the order of "every" and "there is" changes the meaning.
The first sentence can be true while the second is false.

### L2 human

Compare two orders for the sequence $a_n = \frac{1}{n}$ and $L = 0$.
Order A is $\forall \varepsilon > 0 \; \exists N \; \forall n \geq N \; |a_n| < \varepsilon$.
Given $\varepsilon > 0$, choose an integer $N > \frac{1}{\varepsilon}$; for $n \geq N$, $|a_n| = \frac{1}{n} \leq \frac{1}{N} < \varepsilon$, so order A is true, and $N$ depends on $\varepsilon$.
Order B is $\exists N \; \forall \varepsilon > 0 \; \forall n \geq N \; |a_n| < \varepsilon$.
If some $N$ worked, then $n = N$ and $\varepsilon = \frac{1}{N}$ would give $\frac{1}{N} < \frac{1}{N}$, a contradiction, so order B is false.
To read a definition, find for each existential quantifier the variables to its left, because its witness may depend on exactly these.
Watch out: choosing $N$ at the start of a proof of order A, before $\varepsilon$ is given, proves nothing.

### L3 human

The order of quantifiers has a game reading: in $\forall x \, \exists y \, P(x, y)$, an opponent chooses $x$, we answer with $y$, and we win when $P(x, y)$ holds.
The statement is true exactly when we have a winning strategy, which is a function from $x$ to $y$, and in $\exists y \, \forall x$ we must move first, without seeing $x$.
The functions that replace existential quantifiers are Skolem functions, and the [[Skolem normal form|GCPQGMJYEV]] is built from them.
The number of alternations between $\forall$ and $\exists$ in a prefix measures the logical complexity of a formula, as in the [[arithmetical hierarchy|7CVJCQKY41]].
In analysis, continuity and uniform continuity, and [[pointwise convergence|0GFGK40582]] and [[uniform convergence|08VZ57PT26]], differ only in the order, and compactness is the usual tool that proves the stronger order.
