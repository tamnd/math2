---
tag: QKEX4PD029
kind: concept
name: Mathematical notation
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
uses: [0BSJ7RQ9BW, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_notation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/ISO/IEC_80000
    locator: "Part 2: Mathematics"
---

## Summary

Mathematical notation is the written shorthand of mathematics, and it lets a reader check an argument line by line.
Read the sentence "for every $\varepsilon > 0$ there is $N$ such that $|a_n| < \varepsilon$ for all $n \ge N$".
Before any definition, the letters already tell you a lot: $\varepsilon$ is a small positive real number, $N$ and $n$ are whole numbers, and $a_n$ is the term number $n$ of a sequence.

Mathematical notation is a system of written symbols together with rules that say how the symbols combine and what each combination denotes.
It fixes three things: the symbols (letters, digits, signs of operations and relations, brackets), the layout rules (precedence, subscripts, superscripts, fraction bars), and the habits about which letters stand for which kinds of object.
A notation works when it is unambiguous, so that each well-formed expression has exactly one meaning.

## Motivation

Take the sentence "the square of the sum of two numbers is the sum of their squares plus twice their product".
In notation the same claim is
$$(a + b)^2 = a^2 + 2ab + b^2.$$
The formula is shorter, and you can check it by expanding $(a + b)(a + b)$ term by term.
It also shows a pattern that the sentence hides: put $-b$ in place of $b$ and you get $(a - b)^2 = a^2 - 2ab + b^2$ at once.

Mathematics needs notation because its arguments are long chains of such steps, and each step must be checkable.
The rest of the topic builds on this idea.
[[Conflicting conventions|CSFEP56A7D]] treats the symbols that two groups of authors read in two ways, [[abuse of notation|JV68YRB5YZ]] treats the shortcuts that everyone accepts, and [[equality, definition and equivalence signs|BCGR3NPPXC]] sorts out the family of signs that look like $=$.

## Notation

Letters have habits, and a reader who knows them reads faster.
The letters $n$, $m$ and $k$ are usually integers, often counts, and $i$, $j$ and $k$ are usually indices, though $i$ is also the imaginary unit.
The letters $x$, $y$ and $z$ are real variables or unknowns, $a$, $b$ and $c$ are constants or coefficients, and $\varepsilon$ and $\delta$ are small positive numbers.
Functions are $f$, $g$ and $h$, primes in number theory are $p$ and $q$, and complex numbers are $z$ and $w$.
Capital letters name larger objects: $A$ and $X$ for sets or matrices, $G$ and $H$ for groups, and $V$ and $W$ for vector spaces.
None of these is a rule, and a sentence such as "let $x$ be an integer" overrides each one.

The international standard ISO 80000-2 lists recommended signs and their readings.
It sets variables in italic type and sets the constants $\mathrm{e}$, $\mathrm{i}$ and $\pi$, the differential $\mathrm{d}$ and function names such as $\sin$ in upright type.
Most mathematics books follow it only in part, and they write italic $e$ and $i$.
The [[glossary of mathematical symbols|2PTCAGCWZE]] lists the shared symbols with their readings.

## Remarks

### Subscripts, superscripts and primes

A subscript picks one member of a family.
In a sequence, $a_n$ is the term number $n$, and in a [[matrix|0VD9ZSWWJG]], $a_{ij}$ is the entry in row $i$ and column $j$.
[[The entries of a matrix with two subscripts|D5H0JWNHNP]] works this out on the rule $a_{ij} = 10i + j$, where $a_{12} = 12$ but $a_{21} = 21$, so the order of the subscripts matters.

A superscript usually means a power, as in $x^2$.
It can also mark a derivative, as in $f^{(3)}$ for the third derivative, or an index in physics, where $x^2$ can be the second coordinate of a point.
A prime gives either a new name or a derivative: $x'$ is often a second variable, and $f'$ is the derivative of $f$.
The context decides, and a careful author says which reading holds when both are possible.

### The ellipsis and the sigma sign

Compare two ways to write the sum of the first $n$ positive integers:
$$1 + 2 + \cdots + n \qquad \text{and} \qquad \sum_{k=1}^{n} k.$$
The first form shows a few terms and asks you to guess the rule.
The second form states the rule: the index $k$ runs from $1$ to $n$, and the term for each $k$ is $k$.
For $n = 4$ both give $1 + 2 + 3 + 4 = 10$.
[[The sum 1 + 2 + ... + n in sigma notation|MBPSRTCW23]] shows that the sigma form also handles $n = 1$ and $n = 0$, where the dots read badly.

An ellipsis is safe only when the pattern is unique.
[[The list 1, 2, 4, ... does not determine its next term|1TDTSKQQX9]]: doubling gives $8$ next, and the rule $\frac{n^2 + n + 2}{2}$ gives $7$, so the display has no single meaning until the author adds the rule.
By habit, low dots stand between commas, as in $1, 2, \ldots, n$, and centered dots stand between operation signs, as in $1 + 2 + \cdots + n$.

### Bound and free letters

In $\sum_{k=1}^{n} k$ the two letters do different jobs.
The index $k$ is bound by the sum, so you can rename it: $\sum_{k=1}^{n} k = \sum_{j=1}^{n} j$.
The letter $n$ is free, and the value of the sum depends on it.
The same holds for the variable of an integral, $\int_0^1 x^2 \, dx = \int_0^1 t^2 \, dt = \tfrac{1}{3}$, and for the variable of a set-builder expression.
A letter must never be bound and free in one expression, so $\sum_{n=1}^{n} n$ is not well-formed.

### Layout in two dimensions

Notation uses the page in two directions.
Fractions, exponents, the limits of sums and integrals, and matrices all depend on the height of a symbol.
So $\frac{a}{b + c}$ is clear on the page, while the typed string `a/b+c` means $\frac{a}{b} + c$ by the precedence rules and needs brackets, `a/(b+c)`, to mean the fraction.

Precedence is part of the layout.
In $2 + 3 \cdot 4$ multiplication binds first, so the value is $2 + 12 = 14$, and every standard source agrees.
An exponent binds before a minus sign:
$$-3^2 = -(3^2) = -9, \qquad (-3)^2 = 9.$$
Watch out for software: some spreadsheet programs read `-3^2` as $(-3)^2 = 9$, so type the brackets you mean.

### Notation is not the object

One number has many names.
The expressions $\tfrac{1}{2}$, $0.5$, $2^{-1}$ and $\tfrac{3}{6}$ all denote the same number, and a theorem about the number does not care which name you use.
So a notation is good when it makes the facts you need easy to see.
The decimal $0.5$ is best for comparing sizes, and the fraction $\tfrac{3}{6}$ shows a common factor.
Leibniz's $\frac{dy}{dx}$ suggests the chain rule $\frac{dy}{dx} = \frac{dy}{du} \frac{du}{dx}$, though a derivative is not a fraction.

### Watch out

The first trap is a dropped bracket.
A student writes $-3^2 = 9$, but the exponent binds first, so $-3^2 = -9$.
The second trap is an ambiguous typed string.
Some readers take `8/2*4` as $(8/2) \cdot 4 = 16$, and others take it as $8 / (2 \cdot 4) = 1$, so write a fraction bar or brackets.
The third trap is to treat an ellipsis as a proof.
The display $1, 2, 4, \ldots$ suggests a rule, but only a formula fixes the terms after the dots.

### History

François Viète wrote both known and unknown quantities with letters in the late sixteenth century.
René Descartes, in La Géométrie (1637), used $x$, $y$ and $z$ for unknowns and $a$, $b$ and $c$ for known quantities, a habit that survives.
Robert Recorde introduced the equals sign in 1557.
Leonhard Euler introduced or spread the notations $f(x)$, $e$, $i$ and $\Sigma$ for a sum.
The international standard ISO 80000-2 first appeared in 2009, and a revised edition appeared in 2019.

### Try it

First, rename the bound letter in $\sum_{i=1}^{3} i^2$ and compute the sum.
It equals $\sum_{k=1}^{3} k^2 = 1 + 4 + 9 = 14$, and the renaming changes nothing.

Second, compute $-2^4$ and $(-2)^4$.
The exponent binds first, so $-2^4 = -16$, while $(-2)^4 = 16$.

## Explanations

### L1 human

Mathematical notation is the shorthand that mathematicians write.
Instead of "three times a number, plus two", we write $3x + 2$.
Each symbol has a fixed job: $x$ stands for the number, $3x$ means three times it, and $+$ means add.
Because the jobs are fixed, everyone reads $3x + 2$ in the same way.
For $x = 4$ the expression gives $3 \cdot 4 + 2 = 14$.
Some letters also have habits, so $n$ is usually a whole number and $x$ is usually an unknown.

### L2 human

Read $\sum_{i=1}^{3} (2i - 1)$ one symbol at a time.
The sign $\Sigma$ says that we add terms.
The text $i = 1$ below it says that the index $i$ starts at $1$, and the $3$ above it says that $i$ stops at $3$.
The term $2i - 1$ gives $1$, $3$ and $5$ for $i = 1, 2, 3$, so
$$\sum_{i=1}^{3} (2i - 1) = 1 + 3 + 5 = 9 = 3^2.$$
Check: with $n = 3$ the rule $n^2$ gives $9$ as well.

The value of the notation is that it states the pattern for all $n$ at once:
$$\sum_{i=1}^{n} (2i - 1) = n^2,$$
and a proof by [[mathematical induction|0ASJVEFA9J]] can then establish it.
Watch out: the index $i$ here is not the imaginary unit.
When both meanings could occur, as in complex analysis, authors use $k$ or $j$ for the index.

### L3 human

A notation is a formal language with a meaning attached: a grammar of well-formed expressions and a map that sends each expression to an object.
Programming languages and proof assistants make this exact, and in Lean each expression has a type and one parse.
Ordinary mathematical notation is not fully formal.
It relies on context, on symbols with several meanings, and on the [[abuse of notation|JV68YRB5YZ]] that a reader resolves silently, and these gaps become visible when someone formalizes a textbook proof.
Good notation also carries structure: index notation for matrices encodes the product rule $c_{ij} = \sum_k a_{ik} b_{kj}$, and the Einstein summation convention drops the $\Sigma$ altogether.
The other pages of the topic treat [[mathematical abbreviations|4ZNYMYRRY3]] and the informal [[mathematical jargon|4M1FGQ0HNZ]] that surround the symbols.
