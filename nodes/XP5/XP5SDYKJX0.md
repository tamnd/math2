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

To prove an identity, start from one side and change it, one justified step at a time, until it becomes the other side.
Every link in the chain is an equality, so the chain carries the value from the start to the end, and it never assumes what you want to prove.

Here is the pattern on a real goal: for every positive integer $n$,
$$\frac1n - \frac{1}{n + 1} = \frac{1}{n(n + 1)}.$$
Start from the left side and put it over the common denominator $n(n + 1)$, which is not $0$:
$$\frac1n - \frac{1}{n + 1} = \frac{n + 1}{n(n + 1)} - \frac{n}{n(n + 1)} = \frac{(n + 1) - n}{n(n + 1)} = \frac{1}{n(n + 1)}.$$
Check: for $n = 2$, $\tfrac12 - \tfrac13 = \tfrac16$.

In general, an identity is an equation $E_1 = E_2$ between two expressions that holds for every value of its variables in a stated domain.
A proof fixes arbitrary values in the domain and builds a chain $E_1 = F_1 = \dots = F_k = E_2$, each link justified by a definition, an algebraic law or an identity proved before.

## Motivation

You first meet identities as rules, such as $(a + b)^2 = a^2 + 2ab + b^2$.
Later you have to prove new ones, and the habits of solving equations get in the way.
To solve an equation, you change both sides until the unknown stands alone, and you are allowed to assume that the equation holds.
To prove an identity, you may not assume it, because it is the claim.
A chain of equalities that starts at one known expression avoids the problem, since it never uses the claim as a step.

Identities are the tools of every computation, from factoring in school algebra to trigonometry, telescoping sums and the manipulation of series.
The chain of equalities is the simplest [[direct proof|0NTF6DMVAP]].
Equalities that no chain reaches, such as the value of a supremum, need [[equality by two inequalities|S3QADD13E9]] instead.

## Notation

An identity is usually written with the plain sign $=$ and a hidden "for all", as in $\sin^2 x + \cos^2 x = 1$; the [[implicit universal quantifier in an algebraic identity|N3FERWCTTJ]] makes that [[quantifier|EGTZPA6QH3]] visible.
Some books write $E_1 \equiv E_2$ to mark an identity, and the same sign means congruence or definition elsewhere, as [[equality, definition and equivalence signs|BCGR3NPPXC]] explains.
"LHS" and "RHS" abbreviate the left-hand side and the right-hand side, as in [[the abbreviations LHS, RHS and NTS|Z2HAC8J58R]].
The domain is part of the identity: $\frac{x^2 - 1}{x - 1} = x + 1$ holds on $\mathbb{R} \setminus \{1\}$ and not on $\mathbb{R}$, where the left side is undefined at $1$.

## Remarks

### Three shapes of chain

The first shape turns one side into the other.
Start from the side with more structure, because expanding is a step that a reader can check, while factoring needs an idea.
For the [[factorization of a^3 + b^3 + c^3 - 3abc|RVVKF9AC7N]], you expand the product on the right and watch twelve terms cancel.

The second shape turns both sides into one common form.
For the [[Brahmagupta-Fibonacci identity|0K2DMACEZ4]],
$$(a^2 + b^2)(c^2 + d^2) = (ac - bd)^2 + (ad + bc)^2,$$
both sides expand to $a^2c^2 + a^2d^2 + b^2c^2 + b^2d^2$, since the cross terms $-2abcd$ and $+2abcd$ cancel on the right.
This is legal because equality is symmetric and transitive.

The third shape shows that $E_1 - E_2$ simplifies to $0$.
It is the same as the first shape applied to the identity $E_1 - E_2 = 0$.

### Reversible steps and the domain

Some proofs run as a chain of equations, from the claim down to a true equation such as $1 = 1$.
Such a chain proves the claim only when every step is an equivalence, so that you can read it upward.
Adding a term to both sides and multiplying by a non-zero number are reversible.
Squaring and multiplying by an expression that can be $0$ are not.
[[Squaring both sides does not prove an identity|FGS7ZJJYRK]]: from $\sqrt{x^2} = x$ you reach $x^2 = x^2$, yet the claim fails at $x = -1$.

Division needs the same care.
The [[half-angle identity|6YT3DTAXKJ]] $\frac{1 - \cos x}{\sin x} = \frac{\sin x}{1 + \cos x}$ multiplies by $\frac{1 + \cos x}{1 + \cos x}$ and cancels $\sin x$, so the proof first checks that both are non-zero off the multiples of $\pi$.

### Checking values is not proving

Testing an identity at a few values is a good check, but not a proof.
The equation $x^3 = 3x^2 - 2x$ holds at $x = 0$, $1$ and $2$, and fails at $x = 3$, where the sides are $27$ and $27 - 6 = 21$.
For polynomials there is an exact version of the method of values.
If two polynomials of degree at most $d$ agree at $d + 1$ distinct points, they are equal, because their difference has more roots than [[its degree allows|0KJVQV3E0F]].
In the example, $x^3$ and $3x^2 - 2x$ have degree at most $3$, so they would need to agree at $4$ points, and three points were not enough.

Identities with a variable number of terms, such as $1 + 2 + \dots + n = \frac{n(n + 1)}{2}$, need [[induction|0ASJVEFA9J]] or the pairing trick, as in [[two proofs of that formula|D6G69GNKPC]].

### Watch out

The classic slip starts from the claim, does the same thing to both sides, reaches $0 = 0$, and stops.
A false claim can lead to a true equation: from $-1 = 1$, squaring gives $1 = 1$.
So either write the chain forward, from one side to the other, or state that each step is reversible and check it.
A second slip divides by $\sin x$ or by $x - 1$ and forgets to record where the identity fails or is undefined.

### History

Algebraic identities are much older than our symbols for them.
The Brahmagupta-Fibonacci identity appears, stated in words, in the *Arithmetica* of Diophantus.

### Try it

Prove $(a + b)^2 - (a - b)^2 = 4ab$.
Expand the left side: $(a^2 + 2ab + b^2) - (a^2 - 2ab + b^2) = 4ab$.

Is $\frac{x^2 - 4}{x - 2} = x + 2$ an identity on $\mathbb{R}$?
No, because the left side is undefined at $x = 2$; it is an identity on $\mathbb{R} \setminus \{2\}$, by factoring $x^2 - 4 = (x - 2)(x + 2)$ and cancelling the non-zero factor $x - 2$.

## Explanations

### L1 human

An identity is an equation that is true for every number you put in.
For example, $(a + b)^2 = a^2 + 2ab + b^2$ holds for all numbers $a$ and $b$.
With $a = 3$ and $b = 4$, the left side is $49$ and the right side is $9 + 24 + 16 = 49$.
A check with a few numbers does not prove that it always works.
To prove it, start with one side and change it, one allowed step at a time, until you reach the other side.

### L2 human

We prove $\frac{1}{1 - x} - \frac{1}{1 + x} = \frac{2x}{1 - x^2}$ for every real $x \ne \pm 1$.

1. Let $x$ be real with $x \ne \pm 1$, so $1 - x \ne 0$ and $1 + x \ne 0$.
2. Write both fractions over the common denominator $(1 - x)(1 + x)$, which is not $0$:
   $$\frac{1}{1 - x} - \frac{1}{1 + x} = \frac{(1 + x) - (1 - x)}{(1 - x)(1 + x)}.$$
3. The numerator is $2x$, and the denominator is $1 - x^2$, so the left side equals $\frac{2x}{1 - x^2}$.
4. Since $x$ was arbitrary, the identity holds on $\mathbb{R} \setminus \{1, -1\}$.

Check: at $x = 3$, the left side is $-\tfrac12 - \tfrac14 = -\tfrac34$, and the right side is $\tfrac{6}{-8} = -\tfrac34$.
Identities like this simplify an expression before an integral or a limit.
Watch out: multiplying the claimed identity by $1 - x^2$ and checking the result is reversible only where $1 - x^2 \ne 0$, so state the domain first.

### L3 human

An identity in $x_1, \dots, x_n$ is a statement in a ring of functions or of formal expressions.
Over an infinite field, a polynomial identity of functions is the same as an equality of formal polynomials, so comparing coefficients proves it.
Over a finite field this fails: $x^p = x$ for every element of $\mathbb{F}_p$, yet $x^p$ and $x$ are different polynomials.
In universal algebra, identities are the laws that define a variety, such as the group laws.
Sums with a variable number of terms need induction, telescoping or [[double counting|0F8YBHF2W3]], and the algorithms of Gosper and Zeilberger prove many hypergeometric summation identities by machine.
