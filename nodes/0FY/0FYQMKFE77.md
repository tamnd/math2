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

Let $P(x, y)$ be a [[predicate|0QHEWQD30B]] with two free variables on a domain $D$.
The order of quantifiers is the order in which the [[universal quantifier|0GHS47PDAQ]] and the [[existential quantifier|0MSRQHCNN9]] bind the variables, read from left to right.
Two quantifiers of the same kind can be exchanged: $\forall x \, \forall y \, P(x, y) \equiv \forall y \, \forall x \, P(x, y)$ and $\exists x \, \exists y \, P(x, y) \equiv \exists y \, \exists x \, P(x, y)$.
Two quantifiers of different kinds cannot be exchanged in general.
The statement $\exists y \, \forall x \, P(x, y)$ implies $\forall x \, \exists y \, P(x, y)$, but the converse implication fails.
In $\forall x \, \exists y \, P(x, y)$, the witness $y$ may depend on $x$; in $\exists y \, \forall x \, P(x, y)$, one $y$ must work for every $x$.
The order matters because many definitions of analysis and algebra differ only in the order of their quantifiers.

## Motivation

The definitions of [[continuity|0X3WGX95FE]] and of [[uniform continuity|0M4JJT780X]] of a function $f \colon A \to \mathbb{R}$ use the same symbols in a different order.
$$\text{continuous:} \quad \forall a \in A \;\, \forall \varepsilon > 0 \;\, \exists \delta > 0 \;\, \forall x \in A \;\, \bigl( |x - a| < \delta \to |f(x) - f(a)| < \varepsilon \bigr)$$
$$\text{uniformly continuous:} \quad \forall \varepsilon > 0 \;\, \exists \delta > 0 \;\, \forall a \in A \;\, \forall x \in A \;\, \bigl( |x - a| < \delta \to |f(x) - f(a)| < \varepsilon \bigr)$$
The only change is the position of $\forall a$.
In the first line, $\delta$ comes after $a$ and $\varepsilon$, so $\delta$ may depend on both.
In the second line, $\delta$ comes after $\varepsilon$ only, so one $\delta$ must serve every point $a$.
The function $x^2$ on $\mathbb{R}$ satisfies the first definition and not the second, so the two orders give different notions.
A precise rule for the order is needed to state such definitions and to use them correctly.

## Notation

A string of quantifiers is read from left to right, and each quantifier has the rest of the formula as its scope.
So $\forall x \, \exists y \, P(x, y)$ means $\forall x \, \bigl( \exists y \, P(x, y) \bigr)$.
Quantifiers of the same kind are often grouped: $\forall x, y \in \mathbb{R}$ means $\forall x \in \mathbb{R} \; \forall y \in \mathbb{R}$.
To show the dependence of a witness, authors write $y = y(x)$ or $\delta = \delta(\varepsilon, a)$.
In English, a quantifier placed at the end of a sentence, as in "$|f(x) - f(a)| < \varepsilon$ for all $x$", has a scope that a reader must find; symbols remove the doubt.

## Remarks

### Examples

1. [[Identity and inverse axioms of a group differ in the order of quantifiers|~a42ae4f3]]: the identity axiom has the form $\exists e \, \forall x$, and the inverse axiom has the form $\forall x \, \exists y$.
2. [[The square function is continuous but not uniformly continuous on R|~08964e2f]]: the order $\forall a \, \forall \varepsilon \, \exists \delta$ holds and the order $\forall \varepsilon \, \exists \delta \, \forall a$ fails.
3. On $D = \{1, 2, 3\}$, let $P(x, y)$ mean $x + y = 4$. Then $\forall x \, \exists y \, P(x, y)$ is true with $y = 4 - x$. But $\exists y \, \forall x \, P(x, y)$ is false: $P(1, y)$ forces $y = 3$, and $P(3, 3)$ is false.
4. Over $\mathbb{Z}$, $\forall x \, \exists y \, (y > x)$ is true and $\exists y \, \forall x \, (y > x)$ is false. The page [[every number has a larger one, but no number is larger than all|F1GYSA9TW0]] checks both.
5. For a real sequence $(a_n)$ and $L \in \mathbb{R}$, $\forall \varepsilon > 0 \; \exists N \; \forall n \geq N \; |a_n - L| < \varepsilon$ says that $a_n \to L$. The order $\exists N \; \forall \varepsilon > 0 \; \forall n \geq N \; |a_n - L| < \varepsilon$ says that $a_n = L$ for all $n \geq N$, because a number $|a_n - L| \geq 0$ below every $\varepsilon > 0$ is $0$.

### Non-examples

1. [[Two existential quantifiers can be exchanged|~25ac0d7f]]: in $\exists x \, \exists y$ the order does not change the meaning.
2. If the predicate does not depend on $x$, the order does not matter on a non-empty domain: $\forall x \, \exists y \, Q(y) \equiv \exists y \, Q(y) \equiv \exists y \, \forall x \, Q(y)$.
3. $\forall x \in \mathbb{R} \; \forall y \in \mathbb{R} \; (x + y = y + x)$ is a statement with two universal quantifiers, and writing $\forall y \, \forall x$ gives the same statement.

### Basic properties

1. $\exists y \, \forall x \, P(x, y)$ implies $\forall x \, \exists y \, P(x, y)$. The proof has four steps.
    1. Assume $\exists y \, \forall x \, P(x, y)$, and choose $y_0 \in D$ with $\forall x \, P(x, y_0)$. Reason: elimination of $\exists$.
    2. Let $x_0 \in D$ be arbitrary. Then $P(x_0, y_0)$. Reason: elimination of $\forall$ in step 1, applied to $x_0$.
    3. So $\exists y \, P(x_0, y)$, with witness $y_0$. Reason: introduction of $\exists$.
    4. Since $x_0$ was arbitrary, $\forall x \, \exists y \, P(x, y)$. Reason: introduction of $\forall$. No step uses excluded middle, so the implication is valid in [[intuitionistic logic|Q11N8X99FK]] as well.
2. The converse implication fails: example 3 has a true $\forall x \, \exists y$ and a false $\exists y \, \forall x$. The invalid step from $\forall \exists$ to $\exists \forall$ is the [[quantifier shift fallacy|CRW82NARQV]].
3. Quantifiers of the same kind commute. For $\forall$: if $P(x, y)$ holds for all $x$ and all $y$, then for each $y$ it holds for all $x$, and conversely. For $\exists$, a pair $(a, b)$ with $P(a, b)$ is a witness for both orders.
4. Dependence of witnesses: in $\forall x \, \exists y \, P(x, y)$, the witness $y$ is chosen after $x$, so it may be a function $g(x)$. The statement $\exists y \, \forall x \, P(x, y)$ asks for a witness that does not depend on $x$, a constant function. With the [[axiom of choice|0HTGB13FE2]], the first statement is equivalent to $\exists g \, \forall x \, P(x, g(x))$.
5. In a longer prefix, a witness may depend on the universally quantified variables to its left, and on no others. In $\forall \varepsilon \, \exists \delta \, \forall a$, the number $\delta$ depends on $\varepsilon$ only.
6. Negation keeps the order of the variables and changes each quantifier: $\neg \forall x \, \exists y \, P(x, y) \equiv \exists x \, \forall y \, \neg P(x, y)$. This uses the [[negation of a universal statement|0P3A06QNDP]] and the [[negation of an existential statement|05SZQKH75K]].

### History

Ordinary language often leaves the order of quantifiers to the context.
Gottlob Frege's Begriffsschrift of 1879 wrote each quantifier with a bound variable and a scope, so the order became part of the notation.
In analysis, the difference between pointwise and uniform statements was a source of errors in the 19th century; the page [[quantifier shift fallacy|CRW82NARQV]] describes Cauchy's sum theorem.

### Common errors

1. A student proves "for each $a$ there is a $\delta$" and concludes "there is a $\delta$ for all $a$". This is the quantifier shift fallacy.
2. In a proof of a $\forall x \, \exists y$ statement, a student chooses $y$ before $x$ is given, or chooses $y$ that depends on a variable introduced later.
3. A student negates $\forall x \, \exists y \, P$ as $\exists y \, \forall x \, \neg P$, changing the order of the variables. The correct negation keeps $x$ first: $\exists x \, \forall y \, \neg P$.

## Explanations

### L1 human

"Every class in the school has a teacher" is a claim about each class.
Class $1$ can have teacher Ana, class $2$ teacher Ben, and class $3$ teacher Cara.
"There is a teacher who teaches every class" is a much stronger claim.
It asks for one person, for example Ana, in all three classes.
The words are almost the same, but the order of "every" and "there is" changes the meaning.
The first sentence can be true while the second is false.

### L2 human

We compare two orders of the quantifiers for the sequence $a_n = \frac{1}{n}$ and $L = 0$.

1. Order A: $\forall \varepsilon > 0 \; \exists N \; \forall n \geq N \; |a_n| < \varepsilon$. Let $\varepsilon > 0$ be given.
2. Choose an integer $N > \frac{1}{\varepsilon}$. For $n \geq N$, $|a_n| = \frac{1}{n} \leq \frac{1}{N} < \varepsilon$. So order A is true, and $N$ depends on $\varepsilon$.
3. Order B: $\exists N \; \forall \varepsilon > 0 \; \forall n \geq N \; |a_n| < \varepsilon$. Suppose that some $N$ works.
4. Take $n = N$ and $\varepsilon = \frac{1}{N}$. Then $|a_N| = \frac{1}{N}$ is not less than $\varepsilon$, a contradiction. So order B is false.
5. Order B implies order A by basic property 1, so order B is the stronger statement. Here it fails and order A holds.

The typical use is in definitions: to read a definition, find for each existential quantifier the variables to its left, because the witness may depend on exactly these.
A trap is to choose $N$ at the start of a proof of order A, before $\varepsilon$ is given, and then to treat it as fixed for every $\varepsilon$.

### L3 human

The order of quantifiers has a game reading: in $\forall x \, \exists y \, P(x, y)$, an opponent chooses $x$, then we answer with $y$, and we win when $P(x, y)$ holds.
The statement is true exactly when we have a winning strategy, which is a function from $x$ to $y$.
In $\exists y \, \forall x$ we must move first, and our move cannot use $x$.
The functions that replace existential quantifiers are Skolem functions, and the [[Skolem normal form|GCPQGMJYEV]] is built from them.
The number of alternations between $\forall$ and $\exists$ in a prefix measures the logical complexity of a formula, as in the [[arithmetical hierarchy|7CVJCQKY41]].
In analysis, the pairs continuity and uniform continuity, [[pointwise convergence|0GFGK40582]] and [[uniform convergence|08VZ57PT26]] differ only in the order, and compactness is the usual tool that proves the stronger order.
