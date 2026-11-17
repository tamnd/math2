---
tag: XP5SDYKJX0
kind: concept
name: Proving identities
aliases: [proving-identities, proof-of-an-identity]
msc: ["00A35", "97E50"]
topics: [MEKKHHQTKB, G9JFJGY4TQ]
audience: school
specializes: [0B94TKFQJX]
uses: [0B94TKFQJX, 0NTF6DMVAP, EGTZPA6QH3, BCGR3NPPXC]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/List_of_trigonometric_identities
    locator: lead section
  - book: isbn:9781108439534
    locator: Chapter 3
---

## Summary

An identity is an equation $E_1 = E_2$ between two expressions that holds for every value of its variables in a stated domain.
To prove an identity, we fix arbitrary values of the variables in the domain and build a chain of equalities $E_1 = F_1 = F_2 = \dots = E_2$.
Each link of the chain must have a reason: a definition, an algebraic law, or an identity that was proved before.
There are three standard shapes.
The proof transforms the left side into the right side, or both sides into one common expression, or the difference $E_1 - E_2$ into $0$.
A fourth shape, a chain of equivalent equations that ends in a true equation, is legal only when each step can be reversed.
The method matters because identities are the tools of every computation in algebra, trigonometry and analysis.

## Motivation

A school student first meets identities as rules, such as $(a + b)^2 = a^2 + 2ab + b^2$.
Later the student must prove new identities, and the habits of solving equations then cause errors.
To solve an equation, we change both sides until the unknown is alone.
To prove an identity, we may not assume the identity, because that is the claim.
The method of chains of equalities avoids this trap: it starts from one known expression and changes it, with a reason at each step, until it becomes the other expression.

## Notation

1. An identity is often written with the ordinary sign $=$ and an implicit "for all", as in $\sin^2 x + \cos^2 x = 1$. The page [[implicit universal quantifier in an algebraic identity|N3FERWCTTJ]] makes the hidden quantifier explicit.
2. Some books write $E_1 \equiv E_2$ to mark an identity. The sign $\equiv$ also means congruence and definition in other books, as the page on [[equality, definition and equivalence signs|BCGR3NPPXC]] explains.
3. "LHS" and "RHS" abbreviate the left-hand side and the right-hand side, as in the example [[the abbreviations LHS, RHS and NTS|Z2HAC8J58R]].
4. The domain is part of the identity. For example, $\frac{x^2 - 1}{x - 1} = x + 1$ is an identity on $\mathbb{R} \setminus \{1\}$, and it is false as an identity on $\mathbb{R}$, because the left side is not defined at $1$.

## Remarks

### Examples

1. [[The factorization of a^3 + b^3 + c^3 - 3abc|RVVKF9AC7N]]: we expand the right side and cancel terms until only the left side remains.
2. [[Two forms of the tangent of a half angle|6YT3DTAXKJ]]: we multiply by a well-chosen form of $1$ and use the [[Pythagorean trigonometric identity|03H7WZ4T3K]], with care for the domain.
3. The [[Brahmagupta-Fibonacci identity|0K2DMACEZ4]] $(a^2 + b^2)(c^2 + d^2) = (ac - bd)^2 + (ad + bc)^2$: we expand both sides and reach the same expression $a^2c^2 + a^2d^2 + b^2c^2 + b^2d^2$.
4. $\frac{1}{n} - \frac{1}{n + 1} = \frac{1}{n(n + 1)}$ for each positive integer $n$: we put the left side over the common denominator $n(n + 1)$.
5. $1 + 2 + \dots + n = \frac{n(n + 1)}{2}$: an identity with a variable number of terms. A chain of equalities does not apply directly, and [[mathematical induction|0ASJVEFA9J]] or the pairing trick proves it, as in [[two proofs of the formula|D6G69GNKPC]].

### Non-examples

1. [[Squaring both sides does not prove an identity|FGS7ZJJYRK]]: a student starts from $\sqrt{x^2} = x$, squares, gets $x^2 = x^2$, and concludes. The squaring step cannot be reversed, and the claimed identity is false at $x = -1$.
2. A check of an identity at several values, for example at $x = 0, 1, 2$, is not a proof for all real $x$. The equation $x^3 = 3x^2 - 2x$ holds at $x = 0$, $1$ and $2$, but it fails at $x = 3$, where the left side is $27$ and the right side is $27 - 6 = 21$.
3. A chain that divides by an expression that can be $0$ proves the identity only where the expression is not $0$. The domain of the result must say so.

### Basic properties

1. The relation "is identically equal to" is reflexive, symmetric and transitive. So a chain of equalities is legal, and we may work from either side.
2. If $E_1 = F$ and $E_2 = F$ are identities, then $E_1 = E_2$ is an identity. This justifies the shape "both sides to a common form".
3. $E_1 = E_2$ is an identity if and only if $E_1 - E_2 = 0$ is an identity. This justifies the shape "the difference is zero".
4. For polynomials in one variable over $\mathbb{R}$, the method of values works in a restricted form. If two polynomials of degree at most $d$ agree at $d + 1$ distinct points, then they are equal. Otherwise their difference has more roots than its degree allows, which contradicts the theorem that [[a polynomial has at most as many roots as its degree|0KJVQV3E0F]].
5. A chain of equivalences $E_1 = E_2 \iff \dots \iff T$, where $T$ is a true equation, proves the identity only if each step is an equivalence. Adding the same term to both sides, and multiplying by a non-zero number, are reversible. Squaring, and multiplying by an expression that can be $0$, are not reversible.

### History

The word "identity" for an equation that holds for all values of its variables is standard in algebra books.
Algebraic identities are much older than the symbols that we use for them.
The Brahmagupta-Fibonacci identity appears in the Arithmetica of Diophantus, written in words, as its page records.

### Common errors

1. A student starts from the identity to be proved and reaches $0 = 0$ or $1 = 1$. If any step is not reversible, the argument proves nothing about the identity.
2. A student cancels a factor that can be $0$, or divides by $\sin x$, and does not record the values where the identity fails or is undefined.
3. A student "works on both sides" at once, with steps such as "square both sides", and so turns the proof into a chain of equations whose direction is not clear. Each step of a proof must be an equality of two expressions, or a stated equivalence of two equations.

## Explanations

### L1 human

An identity is an equation that is true for every number that we put in.
For example, $(a + b)^2 = a^2 + 2ab + b^2$ is true for all numbers $a$ and $b$.
With $a = 3$ and $b = 4$, the left side is $49$ and the right side is $9 + 24 + 16 = 49$.
But a check with a few numbers does not prove that it is always true.
To prove it, we start with one side and change it, one allowed step at a time, until we get the other side.
Each step must keep the value the same for all numbers.

### L2 human

We prove that $\frac{1}{1 - x} - \frac{1}{1 + x} = \frac{2x}{1 - x^2}$ for every real $x$ with $x \neq 1$ and $x \neq -1$.

1. Let $x$ be an arbitrary real number with $x \neq \pm 1$. Then $1 - x \neq 0$ and $1 + x \neq 0$, so both fractions on the left are defined.
2. We write both fractions over the common denominator $(1 - x)(1 + x)$, which is not $0$ by step 1.
3. The left side becomes $\frac{(1 + x) - (1 - x)}{(1 - x)(1 + x)}$.
4. The numerator is $1 + x - 1 + x = 2x$.
5. The denominator is $(1 - x)(1 + x) = 1 - x^2$, by the product of a sum and a difference.
6. So the left side equals $\frac{2x}{1 - x^2}$, the right side.
7. Since $x$ was arbitrary with $x \neq \pm 1$, the identity holds on $\mathbb{R} \setminus \{1, -1\}$.

A check: at $x = 3$ the left side is $\frac{1}{-2} - \frac{1}{4} = -\frac34$, and the right side is $\frac{6}{-8} = -\frac34$.
The typical use of such an identity is to simplify an expression before an integral or a limit.
A trap is to multiply both sides of the claimed identity by $1 - x^2$ and to "check" the resulting equation.
This step can be reversed only where $1 - x^2 \neq 0$, so the domain must be stated before the step.

### L3 human

An identity in the variables $x_1, \dots, x_n$ is a statement about a ring of functions or of formal expressions.
For polynomials with coefficients in an infinite field, an identity of functions is the same as an equality of formal polynomials, and so it can be proved by comparing coefficients.
Over a finite field this fails: $x^p = x$ holds for every element of $\mathbb{F}_p$, but $x^p$ and $x$ are different polynomials.
The same distinction appears in algebra as the difference between a polynomial and a polynomial function, and in universal algebra as the laws of a variety.
Identities with a variable number of terms, such as sums over $k$ from $1$ to $n$, need [[mathematical induction|0ASJVEFA9J]], a telescoping argument, or a counting proof such as [[double counting|0F8YBHF2W3]].
Algorithms such as those of Zeilberger and Gosper prove many hypergeometric summation identities automatically, and computer algebra systems check polynomial identities by normal forms.
The proof of an identity is the simplest case of the [[direct proof|0NTF6DMVAP]].
Other patterns of this topic, such as [[equality by two inequalities|S3QADD13E9]], prove equalities that no chain of equalities reaches.
