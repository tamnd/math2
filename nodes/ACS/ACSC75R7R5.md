---
tag: ACSC75R7R5
kind: concept
name: Existence and uniqueness statements
msc: ["97E40", "03B10"]
topics: [WMY13MXY3W]
audience: ug1
uses: [EGTZPA6QH3, 12QQ51VK01, 0QAJHFGZZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Uniqueness_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.6
---

## Summary

Every time a book says "the" about a mathematical object, it relies on a statement that exactly one such object exists.
"The remainder of $17$ on division by $5$" makes sense because there is exactly one integer $r$ with $0 \le r < 5$ and $17 - r$ a multiple of $5$, namely $r = 2$.

An *existence and uniqueness statement* says that exactly one object has a given property $P$.
In symbols it is $\exists! x \, P(x)$, read "there is a unique $x$ such that $P(x)$".
It is the conjunction of two separate claims.
*Existence* says that at least one $x$ has $P(x)$.
*Uniqueness* says that at most one $x$ has $P(x)$: for all $x$ and $y$, if $P(x)$ and $P(y)$, then $x = y$.
A proof treats the two claims one at a time, and each needs its own argument.

## Motivation

Many objects are named with "the": the identity element of a group, the quotient and the remainder of a division, the limit of a convergent sequence, the solution of a linear system with an invertible matrix.
Each of these names rests on a theorem of existence and uniqueness.
Without existence, the name refers to nothing.
Without uniqueness, the name does not say which object is meant, and two parts of one proof could use two different objects.
So a definition of the form "the $x$ such that $P(x)$" is legitimate only after a proof of $\exists! x \, P(x)$.
This is a stronger form of the [[quantifiers|EGTZPA6QH3]] "there is" and "for all", built from them with "and".

## Notation

The [[uniqueness quantifier|0QAJHFGZZJ]] is $\exists!$, and some books write $\exists_1$.
It is short for either of two equivalent formulas:
$$\exists! x \, P(x) \iff \exists x \, \big( P(x) \land \forall y \, ( P(y) \Rightarrow y = x ) \big),$$
$$\exists! x \, P(x) \iff \exists x \, P(x) \land \forall x \, \forall y \, \big( P(x) \land P(y) \Rightarrow x = y \big).$$
In words, "exactly one" means "at least one and at most one".
The claim "at most one" has no standard symbol, and authors write it out as in the second part of the second formula.
In the Lean library Mathlib, $\exists! x, \, P(x)$ is notation for `ExistsUnique`, defined by the first formula.

## Remarks

### Taking a statement apart

The division theorem says: for all integers $a$ and $b$ with $b > 0$, there are unique integers $q$ and $r$ with $a = bq + r$ and $0 \le r < b$.
The word "unique" hides a second claim, so the theorem says two things.
First, some pair $(q, r)$ has the property.
Second, if two pairs $(q, r)$ and $(q', r')$ both have it, then $q = q'$ and $r = r'$.
[[The quotient and remainder of $17$ by $5$|JZ9PKJAMFN]] proves both claims for one case.

A second standard case is the group identity.
[[A group has exactly one identity element|A5YGEC10HD]]: the axiom gives existence, and for two identities $e$ and $e'$, the product $e e'$ equals both $e'$ and $e$.
For a real number $a > 0$, there is exactly one real $x > 0$ with $x^2 = a$, and that number is the [[square root|0F7FQS6XY6]] $\sqrt{a}$.
A convergent sequence has exactly one limit: existence is the hypothesis "convergent", and uniqueness is the theorem on the [[uniqueness of limits|0ZXJ2455NJ]].

### At least one and at most one

The two halves are independent, so each can fail alone.
[[The equation $x^2 = 4$ has a solution but not exactly one|A82V4N0G1P]]: existence holds, and uniqueness fails because of $2$ and $-2$.
The equation $x^2 = -1$ has at most one real solution, because it has none.
So "there is a unique real $x$ with $x^2 = -1$" is false, and the part that fails is existence.

"At most one" is often the useful claim by itself.
A [[strictly monotone|011EJQWWJS]] function $f \colon \mathbb{R} \to \mathbb{R}$ has at most one zero, because $x < y$ gives $f(x) \neq f(y)$.
The [[exponential function|0J0FCWV32D]] is strictly increasing and has no zero at all, so "at most one" holds here with none.
A claim such as "a polynomial of degree $2$ has at most two real roots" is a bound, not a uniqueness claim: $x^2 - 1$ has the two roots $1$ and $-1$.

### Rules you can use

The statement $\exists! x \, P(x)$ implies $\exists x \, P(x)$, and the converse fails, as $x^2 = 4$ shows.
The statement $\exists! x \, P(x)$ holds exactly when the set $\{ x : P(x) \}$ has one element.
The negation of $\exists! x \, P(x)$ is "no $x$ has $P(x)$, or there are $x \neq y$ with $P(x)$ and $P(y)$".
So to refute a uniqueness claim, you show either no object or two different objects.

Two uniqueness quantifiers in a row do not count pairs.
On the domain $\{0, 1\}$, let $P(x, y)$ be "$x = 1$ or $y = 0$".
For $x = 0$ only $y = 0$ works, and for $x = 1$ both values of $y$ work.
So exactly one $x$ has exactly one $y$, and $\exists! x \, \exists! y \, P(x, y)$ is true.
Check: the pairs $(0, 0)$, $(1, 0)$ and $(1, 1)$ all satisfy $P$, so there are three pairs, not one.

### Watch out

The first error is to prove existence, forget uniqueness, and then write "the" for the object.
The second error is to prove uniqueness by showing one object with the property.
Uniqueness needs two arbitrary objects $x$ and $y$ with the property, and a proof that $x = y$.
The third error is a proof of uniqueness from "suppose $x \neq y$" that never uses $P(x)$ or $P(y)$.
Such an argument cannot be right, because uniqueness depends on the property.
The fourth error is to read $\exists! x \, \exists! y$ as "exactly one pair", which the example on $\{0, 1\}$ refutes.

### History

Bertrand Russell's theory of [[definite descriptions|PD2R4XT79Q]] of 1905 analyzed "the $x$ such that $P(x)$" through existence and uniqueness.
Whitehead and Russell's Principia Mathematica (1910 to 1913) wrote such a description with an inverted Greek letter iota.

### Try it

First, decide whether exactly one real $x$ has $x^3 = -8$.
Yes: $x = -2$ works, and $x^3$ is strictly increasing, so no second value works.

Second, decide whether exactly one integer $n$ has $n^2 = n$.
No: both $n = 0$ and $n = 1$ work, so uniqueness fails.

## Explanations

### L1 human

"There is exactly one even prime" makes two claims.
First, some prime is even, and $2$ is one.
Second, no other prime is even, because every even number greater than $2$ has the divisor $2$ and so is not prime.
The first claim is "there is one".
The second claim is "there is no other one".
Together they say "exactly one".

### L2 human

Prove that the equation $3x + 5 = 11$ has exactly one real solution.

1. Existence: take $x = 2$.
   Then $3 \cdot 2 + 5 = 11$, so a solution exists.
2. Uniqueness: let $x$ and $y$ be real numbers with $3x + 5 = 11$ and $3y + 5 = 11$.
3. Subtract the two equations: $3x - 3y = 0$, so $3(x - y) = 0$.
4. Since $3 \neq 0$, we get $x - y = 0$, so $x = y$.
5. Step 1 proves existence, and steps 2 to 4 prove uniqueness.
   So $x = 2$ is the unique solution.

The proof has the standard two parts: one object for existence, and two arbitrary objects for uniqueness.
Watch out: in step 2 you must not take $y = 2$.
Uniqueness compares two arbitrary solutions, and neither may be fixed in advance.

### L3 human

In first-order logic with equality, $\exists!$ is a defined quantifier, and the uniqueness part needs the [[equality|E918704SKV]] symbol.
For each fixed $n$, the quantifier "there are exactly $n$" is definable in the same way, but "there are infinitely many" is not first-order definable.
A proof of $\exists! x \, P(x)$ justifies a definite description, and Lean, Isabelle and other proof assistants turn such a proof into a term with a choice or a description operator.
In constructive mathematics, the axiom of unique choice says that $\forall x \, \exists! y \, R(x, y)$ gives a function $f$ with $R(x, f(x))$ for all $x$.
It holds in many settings where full choice fails.
Universal properties in category theory are existence and uniqueness statements about morphisms: the morphism is unique, and the object is unique up to a unique isomorphism.
