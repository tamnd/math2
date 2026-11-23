---
tag: PD2R4XT79Q
kind: concept
name: Definite description
aliases: [russells-theory-of-descriptions, iota-operator]
msc: ["03B10", "03A05"]
topics: [PSRDJXRW53]
audience: grad
uses: [HYJ10AF6RT, 6D3WA7N2W4, 0QAJHFGZZJ]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section D
    note: adapted
    mention: wikipedia://en/76765067#V32V
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Definite_description
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Definite_description
    locator: Mathematical logic
  - url: https://en.wikipedia.org/wiki/On_Denoting
    locator: lead section
inventory: [S08JM76X82]
---

## Summary

"The identity element of $G$" names one object, because a group has exactly one identity.
A phrase of the form "the $x$ such that $\varphi(x)$", meant to pick out exactly one object, is a definite description.
Logic writes it $\iota x \, \varphi(x)$, with the iota operator.

First-order syntax has no such terms, and Russell's analysis of 1905 removes them.
On this analysis "the $\varphi$ is $\psi$" becomes
$$\exists x \, \big( \varphi(x) \land \forall y \, (\varphi(y) \to y = x) \land \psi(x) \big),$$
which says that exactly one object is $\varphi$ and that it is $\psi$.
In mathematics a description is safe to use after a proof of $\exists! x \, \varphi(x)$, with the [[uniqueness quantifier|0QAJHFGZZJ]].

## Motivation

Mathematics names objects by descriptions all the time: the identity of a group, the limit of a sequence, the greatest common divisor.
A description works like a [[term|6D3WA7N2W4]], but its condition is a [[formula|HYJ10AF6RT]], and the condition may fail.
"The largest prime" and "the integer whose square is $4$" do not name one object.
A logic must decide what such phrases mean, or forbid them.
Russell's analysis keeps first-order syntax as it is and turns each description into quantifiers, so no new terms are needed.

## Notation

Whitehead and Russell write $(\iota x)(\varphi x)$, with an inverted iota, and modern texts write $\iota x \, \varphi(x)$ or $\iota x . \varphi$.
The expression $\psi(\iota x \, \varphi)$ stands for "the $\varphi$ is $\psi$" and abbreviates Russell's formula above.
A scope marker, as in $[\iota x \, \varphi] \, \neg \psi(\iota x \, \varphi)$, says where the description is eliminated.
In Isabelle/HOL the operator is written $\mathrm{THE}\ x.\ \varphi\, x$.

## Remarks

### Examples and non-examples

In [[the present King of France|KETATPMAWN]], the sentence "the King of France is not bald" has two readings, with the description inside or outside the negation.
In [[the predecessor as a description|KZEDH1C6M6]], the term $\iota y \, (S(y) = x)$ over $\mathbb{N}$ denotes $x - 1$ for $x \neq 0$, and has no referent for $x = 0$.
In a group, the identity is $\iota e \, \forall g \, (e \cdot g = g \land g \cdot e = g)$, and its existence and uniqueness are proved first, as in [[definite descriptions in definitions|5P955TVSS2]].

On the other side, [[the square root of 4 in the integers|NPMNGQXA04]] is not a description, since two integers satisfy $x \cdot x = 4$.
The [[indefinite description|DTKQ9G0CKS]] "a prime number" does not claim uniqueness, and its logical form is $\exists x \, (P(x) \land \psi(x))$.
Hilbert's [[epsilon term|TH5ZKCKN3W]] $\varepsilon x \, \varphi$ is not a description either: it denotes some object with $\varphi$, and it needs no uniqueness.

### Basic properties

Russell's analysis makes "the $\varphi$ is $\psi$" false when no object, or more than one object, satisfies $\varphi$.
If $\exists! x \, \varphi(x)$ holds, then $\psi(\iota x \, \varphi)$ holds exactly when $\forall x \, (\varphi(x) \to \psi(x))$ holds, and the scope does not matter.
With a negation and no unique witness, scope matters: $\neg \psi(\iota x \, \varphi)$ with narrow scope is false, while the wide-scope negation is true.

Suppose a theory $T$ proves $\forall \bar{u} \, \exists! x \, \varphi(\bar{u}, x)$.
Then a new function symbol $f$ with the axiom $\forall \bar{u} \, \varphi(\bar{u}, f(\bar{u}))$ gives a conservative [[extension by definition|GCK0NN60E4]], and $f(\bar{u})$ plays the role of $\iota x \, \varphi$.

### Watch out

The phrase "the $x$ with $\varphi$" has no referent until $\exists! x \, \varphi$ is proved, so do not use it before.
Forgetting the uniqueness clause gives $\exists x \, (\varphi(x) \land \psi(x))$, which is the analysis of "a $\varphi$ is $\psi$", not of "the $\varphi$ is $\psi$".
The negation of "the $\varphi$ is $\psi$" is not "the $\varphi$ is not $\psi$": the negation also holds when nothing, or several things, satisfy $\varphi$.

### History

Frege treated descriptions as names in his Grundgesetze of 1893, with a fixed value when uniqueness fails.
Russell's paper "On Denoting" of 1905 analyzed them away by quantifiers, and Principia Mathematica made this analysis part of its formal system.
Strawson objected in 1950 that a failed description makes a statement neither true nor false, which led to work on presupposition and to free logics.

### Try it

Eliminate the description in "the even prime is odd", and decide its truth.
The sentence is $\exists x \, (E(x) \land P(x) \land \forall y \, (E(y) \land P(y) \to y = x) \land \neg E(x))$, and it is false, because the one even prime $2$ is even.

## Explanations

### L1 human

A definite description is a phrase like "the tallest student" or "the identity element".
It only makes sense when exactly one object fits.
Russell's idea: "the tallest student is happy" means "there is a tallest student, there is only one, and that one is happy".
If there is no tallest student, the sentence is simply false.

### L2 human

We eliminate the description in "the identity element of $G$ commutes with $a$".

1. Let $\varphi(e)$ be $\forall g \, (e \cdot g = g \land g \cdot e = g)$, and let $\psi(e)$ be $e \cdot a = a \cdot e$.
2. By Russell's analysis, the sentence is $\exists e \, (\varphi(e) \land \forall y \, (\varphi(y) \to y = e) \land \psi(e))$.
3. In a group $\exists! e \, \varphi(e)$ holds, so by the basic properties the sentence is equivalent to $\forall e \, (\varphi(e) \to \psi(e))$.
4. That is true, because $\varphi(e)$ gives $e \cdot a = a = a \cdot e$.

The typical use is to justify notation such as $e$, $\gcd(a, b)$ or $\lim a_n$, introduced by a description.
Watch out: in a structure where $\varphi$ fails, such as a semigroup without identity, the sentence is false, not meaningless.

### L3 human

There are three standard treatments of descriptions.
Russell eliminates them in context, so first-order syntax stays as it is, at the price of scope distinctions.
Frege and Carnap give every description a value, with a chosen default when uniqueness fails; the $\varepsilon$-operator is a relative of this approach.
Free logics allow terms that denote nothing, so $\iota x \, \varphi$ is a term that may lack a referent, with an existence predicate $E!$ that says when a term denotes.
These logics are treated in the topic [[non-classical logics|NJB94B39QK]].
In a theory that proves $\forall \bar{u} \, \exists! x \, \varphi$, all three agree, and the description is a defined function symbol.
