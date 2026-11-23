---
tag: D8SD54M5PN
kind: concept
name: Language of arithmetic
aliases: [first-order-language-of-arithmetic, signature-of-arithmetic]
msc: ["03F30", "03B10"]
topics: [QHCRN4JVG0]
audience: ug2
uses: [086QKPF0A6, WDVVEYD6AT, 6D3WA7N2W4, HYJ10AF6RT, 983GZBQYT4, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: Peano arithmetic as first-order theory
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
    locator: lead section
  - book: isbn:9780521857840
  - book: isbn:9780521701464
  - url: https://builds.openlogicproject.org/
    locator: Arithmetization of Syntax
---

## Summary

How do you say "six is even" with no word for "six" and no word for "even"?
You write "six" as the term $SSSSSS0$, six steps of "next" after zero, and you write "even" as "is some number plus itself":
$$\exists y\, (y + y = SSSSSS0).$$
The language of arithmetic is the small alphabet that makes this possible, and every formal theory of the natural numbers is written in it.

Exactly, the language of arithmetic $L_A$ is the first-order [[signature|WDVVEYD6AT]] with a constant symbol $0$, a unary function symbol $S$, binary function symbols $+$ and $\cdot$, and a binary relation symbol $<$.
The equality symbol $=$ belongs to the logic.
Its [[terms|6D3WA7N2W4]] and [[formulas|HYJ10AF6RT]] are those of [[first-order logic|086QKPF0A6]] over this signature.
For each $n \in \mathbb{N}$, the numeral $\overline{n}$ is the term $S S \cdots S 0$ with $n$ copies of $S$.
The standard model $\mathfrak{N}$ is the [[structure|983GZBQYT4]] with domain $\mathbb{N}$ in which the five symbols mean zero, successor, addition, multiplication and the usual order.
The [[formal definition|329ZG1Z0G5]] gives the clauses one by one.

## Motivation

To study arithmetic as a formal system, we must first fix the symbols that its sentences may use.
The [[Peano axioms|0QFT7Z76N5]] of Dedekind and Peano quantify over sets of numbers, and first-order logic cannot do that.
So we choose a small first-order signature and ask what it can express.

The answer depends on the symbols in a sharp way.
Zero and successor alone can say very little beyond "this number is that numeral".
Adding $+$ gives the language of [[Presburger arithmetic|4W0E9G7PPV]], whose true sentences form a decidable set.
Adding $\cdot$ changes everything.
With $+$ and $\cdot$ you can code finite sequences by [[Gödel's β-function lemma|BM6P0C2AC2]], and then you can define exponentiation, every computable function and even the syntax of formulas.
So $L_A$ is the smallest natural language in which arithmetic can talk about computation and about its own proofs.
[[Robinson arithmetic|3K1AKGXF8A]], [[Peano arithmetic|HACXBCM7SS]] and the incompleteness theorems all live in it.

## Notation

Many books write $x'$ for $S x$, and some write $\mathsf{s}$ or $\operatorname{succ}$.
Some books add a constant $1$, and some leave out $<$ and define it.
Here $<$ is a symbol of $L_A$, and a theory that uses it contains the defining axiom $x < y \leftrightarrow \exists v\,(v + S x = y)$.
We write $x \le y$ for $x < y \lor x = y$, and $x \ne y$ for $\neg\, x = y$.
For a term $t$ in which $x$ does not occur, the bounded quantifiers are abbreviations:
$$\forall x < t\; \varphi \;:=\; \forall x\,(x < t \to \varphi), \qquad \exists x < t\; \varphi \;:=\; \exists x\,(x < t \land \varphi).$$
The forms $\forall x \le t$ and $\exists x \le t$ are defined in the same way with $\le$.
Other books write the numeral of $n$ as $\underline{n}$, $\mathbf{n}$ or $\ulcorner n \urcorner$, and [[the example on closed terms|VK6WWSDMXK]] writes $\underline{n}$.
The standard model is also written $\mathcal{N}$ or $(\mathbb{N}, 0, S, +, \cdot, <)$, and $0$ counts as a natural number.

## Remarks

### Terms, numerals and values

A closed term is built from $0$ with $S$, $+$ and $\cdot$, and it has a value in $\mathfrak{N}$.
Take the term $\overline{2} \cdot (\overline{1} + \overline{3})$.
Work from the inside out:
$$\overline{1} + \overline{3} \mapsto 1 + 3 = 4, \qquad \overline{2} \cdot (\overline{1} + \overline{3}) \mapsto 2 \cdot 4 = 8.$$
So the term has the value $8$, the same value as the numeral $\overline{8}$.
It is still not the numeral $\overline{8}$, which is the string $SSSSSSSS0$.
Every closed term $t$ has a value $t^{\mathfrak{N}}$, and the [[Σ1-completeness theorem|69234Z1V00]] shows that Robinson arithmetic proves $t = \overline{t^{\mathfrak{N}}}$.
In the other direction, each number $n$ is the value of $\overline{n}$, so each element of $\mathfrak{N}$ is defined by the formula $x = \overline{n}$.

### Saying more with defined notions

The language has no symbol for "divides" or "prime", but formulas can spell them out.
Divisibility is $\exists z \le y\, (z \cdot x = y)$, and primality says that $x > 1$ and every factorization of $x$ uses $1$.
[[Divisibility, evenness and primality as formulas|BD4PEHWBRX]] writes these formulas and checks them on small numbers.
With them, the [[infinitude of primes and Goldbach's conjecture|HTTAH8PY38]] become single sentences of $L_A$.

Defined notions can be stacked.
A number $x$ is a power of $2$ exactly when $x \ne 0$ and $2$ is its only prime factor:
$$x \ne 0 \land \forall y \le x\, \forall z \le x\, \bigl((y \cdot z = x \land \mathrm{Prime}(y)) \to y = \overline{2}\bigr).$$
The bounds lose nothing, because a factor of a positive number $x$ is at most $x$.
Check: at $x = 8$ the only prime factor is $2$, so the formula holds, and at $x = 12$ the factor $3$ makes it fail.

### What the language cannot say

The string $x^y = z$ is not a formula of $L_A$, because there is no symbol for exponentiation.
The relation $z = x^y$ is still definable in $\mathfrak{N}$ by a long formula, through the β-function.
The string $\exists X\, X(0)$ is not a formula either, because $X$ ranges over sets and $L_A$ has only variables for numbers.

A smaller signature can lose real power.
The signature $\{0, S, +, <\}$ of Presburger arithmetic is not $L_A$, and no formula over it defines multiplication in $\mathbb{N}$.
[[The language of Presburger arithmetic|TKDKW5MENB]] proves this with the squares, whose gaps grow without bound.
Dropping $<$, in contrast, loses nothing, since $\exists v\,(v + S x = y)$ defines it; adding $<$ is an [[extension by definitions|GCK0NN60E4]].

### Size and strength

The language has countably many symbols, so it has countably many terms and formulas.
By [[Gödel numbering|MFJXPAF0R0]], the set of codes of formulas is decidable.
The subsets of $\mathbb{N}^k$ that formulas define in $\mathfrak{N}$ are the arithmetical sets of the [[arithmetical hierarchy|7CVJCQKY41]].
The [[classes Δ0, Σn and Πn|GE43CSZTS9]] measure how complex such a formula is.
One set escapes every formula: the set of true sentences of $L_A$ is not definable in $\mathfrak{N}$, by [[Tarski's undefinability theorem|YRV6SYK2BY]].

### Watch out

Do not confuse the numeral $\overline{n}$, a term, with the number $n$, an element of $\mathbb{N}$.
A proof in a theory moves numerals around, and a model assigns them numbers.

Do not think that $L_A$ fixes the meaning of its symbols.
The language gives only the symbols, and [[non-standard models of arithmetic|1QWN5CV4CG]] read them in other ways.
For example, a structure may contain an element that is not the value of any numeral.

Do not treat $\mathrm{Prime}(x)$ or $x \mid y$ as symbols.
They are names for long formulas, and a formal proof must work with the formulas themselves.

### History

Dedekind in 1888 and Peano in 1889 gave axioms for the natural numbers with a first number and a successor operation, and they defined addition and multiplication by recursion.
Gödel's paper of 1931 worked in a higher-order system whose arithmetical primitives were zero and successor.
In that paper he used the Chinese remainder theorem to show that every primitive recursive relation is definable from addition and multiplication.
Robinson's theory, published in *Undecidable Theories* by Tarski, Mostowski and Robinson in 1953, uses the first-order signature $0$, $S$, $+$, $\cdot$.

### Try it

First, write "$x$ is odd" as a formula of $L_A$ with one bounded quantifier.
One answer is $\exists y \le x\, (S(y + y) = x)$, since $x = 2y + 1$ forces $y \le x$.

Second, find the value in $\mathfrak{N}$ of the term $S(\overline{2} \cdot \overline{3}) + \overline{1}$.
The product is $6$, the successor is $7$, and adding $1$ gives $8$.

## Explanations

### L1 human

The language of arithmetic is a small alphabet for writing facts about whole numbers.
It has a name for zero, a sign for "the next number", signs for plus and times, and a sign for "less than".
With these signs and the words "for all" and "there is", we can write sentences such as "every number has a larger number".
We write the number three as "next of next of next of zero".
Ideas such as "even" or "prime" are not signs of the alphabet, but we can spell them out.
For example, "$x$ is even" becomes "there is a $y$ with $y + y = x$".

### L2 human

Here is a typical task: express "$x$ is a prime number" in $L_A$ and test the formula at $x = 6$.
A prime is a number larger than $1$ whose only factorizations use $1$, so we write
$$\mathrm{Prime}(x) := \overline{1} < x \land \forall y \le x\, \forall z \le x\, \bigl(y \cdot z = x \to (y = \overline{1} \lor z = \overline{1})\bigr).$$
The bounds lose nothing: if $y \cdot z = x$ and $x \ge 1$, then $y \ge 1$ and $z \ge 1$, so both are at most $x$.
At $x = 6$ the first part $1 < 6$ holds.
The pair $y = 2$, $z = 3$ satisfies the bounds and $2 \cdot 3 = 6$, but neither factor is $1$.
So the formula is false at $6$, as it should be.

This is how number theory enters a formal theory: each statement becomes a sentence that [[Peano arithmetic|HACXBCM7SS]] may or may not prove.
Watch out in weak theories, though.
[[Robinson arithmetic|3K1AKGXF8A]] does not prove that multiplication is commutative, so $y \cdot z = x$ and $z \cdot y = x$ are different formulas there.

### L3 human

$L_A$ is one choice among many first-order signatures for arithmetic, and the choice matters less than it seems.
Two signatures whose operations are definable from each other in $\mathfrak{N}$ give the same definable sets, and so the same arithmetical hierarchy.
The choice does matter for weak theories.
[[Robinson arithmetic|3K1AKGXF8A]] and bounded arithmetic are sensitive to which functions are primitive, and bounded arithmetic adds symbols such as $\lfloor x/2 \rfloor$ and $|x|$.
[[Primitive recursive arithmetic|WCXH72T8D8]] takes the opposite route and adds a symbol for every primitive recursive function.
In model theory, $\mathfrak{N}$ is the prime model of [[true arithmetic|DX0KPMH4QZ]], and the countable models of [[Peano arithmetic|HACXBCM7SS]] form a large field of study.
The [[incompleteness theorems|HXHHWY3328]] turn the formulas of $L_A$ into numbers, so that $L_A$ can speak about itself.
