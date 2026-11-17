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

A definite description is a phrase of the form "the $x$ such that $\varphi(x)$", meant to pick out exactly one object.
Logic writes it $\iota x \, \varphi(x)$, with the iota operator.
First-order syntax has no such terms, and Russell's analysis of 1905 removes them: "the $\varphi$ is $\psi$" becomes $\exists x \, (\varphi(x) \land \forall y \, (\varphi(y) \to y = x) \land \psi(x))$.
In mathematics a description is safe after a proof of $\exists! x \, \varphi(x)$, with the [[uniqueness quantifier|0QAJHFGZZJ]].

## Motivation

Mathematics names objects by descriptions all the time: the identity of a group, the limit of a sequence, the greatest common divisor.
A description is a [[term|6D3WA7N2W4]] in effect, but its condition is a [[formula|HYJ10AF6RT]], and the condition may fail.
"The largest prime" and "the square root of $4$ in $\mathbb{Z}$" do not name one object.
A logic must decide what such phrases mean, or forbid them.
Russell's analysis keeps the first-order syntax and turns each description into quantifiers, so no new terms are needed.

## Notation

1. Russell and Whitehead write $(\iota x)(\varphi x)$, with an inverted iota. Modern texts write $\iota x \, \varphi(x)$ or $\iota x . \varphi$.
2. The analysis of "the $\varphi$ is $\psi$" is written $\psi(\iota x \, \varphi)$ and abbreviates $\exists x \, (\varphi(x) \land \forall y \, (\varphi(y) \to y = x) \land \psi(x))$.
3. A scope marker, as $[\iota x \, \varphi]\, \neg \psi(\iota x \, \varphi)$, says where the description is eliminated.
4. In Isabelle/HOL the operator is $\mathrm{THE}\ x.\ \varphi\, x$.

## Remarks

### Examples

1. [[The present King of France|~568c1e56]]: "the King of France is not bald" has two readings, with the description inside or outside the negation.
2. [[The predecessor as a description|~80f366d0]]: in $\mathbb{N}$, $\iota y \, (S(y) = x)$ denotes $x - 1$ for $x \neq 0$, and fails for $x = 0$.
3. In a group, the identity is $\iota e \, \forall g \, (e \cdot g = g \land g \cdot e = g)$. Existence and uniqueness are proved first, as on the page about [[definite descriptions in definitions|5P955TVSS2]].

### Non-examples

1. [[The square root of 4 in the integers|~35dca08a]]: two integers satisfy $x \cdot x = 4$, so "the integer with $x \cdot x = 4$" picks no single object.
2. The [[indefinite description|DTKQ9G0CKS]] "a prime number" does not claim uniqueness. Its logical form is $\exists x \, (P(x) \land \psi(x))$.
3. Hilbert's [[epsilon term|~41c81e04]] $\varepsilon x \, \varphi$ is not a description. It denotes some object with $\varphi$, and it needs no uniqueness.

### Basic properties

1. Russell's analysis makes "the $\varphi$ is $\psi$" false when no object or more than one object satisfies $\varphi$.
2. If $\exists! x \, \varphi(x)$ holds, then $\psi(\iota x \, \varphi)$ holds exactly when $\forall x \, (\varphi(x) \to \psi(x))$ holds. The scope then does not matter.
3. With a negation, scope matters: $\neg \psi(\iota x \, \varphi)$ and $[\iota x \, \varphi] \, \neg \psi$ differ when $\varphi$ has no unique witness.
4. If a theory $T$ proves $\forall \bar{u} \, \exists! x \, \varphi(\bar{u}, x)$, a new function symbol $f$ with $\varphi(\bar{u}, f(\bar{u}))$ gives a conservative [[extension by definition|GCK0NN60E4]]. Then $f(\bar{u})$ is $\iota x \, \varphi$.

### History

Frege treated descriptions as names in his Grundgesetze of 1893, with a default value when uniqueness fails.
Russell's paper "On Denoting" of 1905 analysed them away by quantifiers, and Principia Mathematica made this analysis part of its formal system.
Strawson objected in 1950 that a failed description makes a statement neither true nor false, which led to presupposition and to free logics.

### Common errors

1. A student uses "the $x$ with $\varphi$" before proving uniqueness. The phrase has no referent until $\exists! x \, \varphi$ is proved.
2. A student forgets the uniqueness clause and writes $\exists x \, (\varphi(x) \land \psi(x))$. That is the analysis of "a $\varphi$ is $\psi$".
3. A student negates "the $\varphi$ is $\psi$" as "the $\varphi$ is not $\psi$". The negation also holds when nothing or several things satisfy $\varphi$.

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
3. In a group, $\exists! e \, \varphi(e)$ holds. So the sentence is equivalent to $\forall e \, (\varphi(e) \to \psi(e))$, by property 2.
4. That is true, because $e \cdot a = a = a \cdot e$.

The typical use is to justify notation such as $e$, $\gcd(a, b)$ or $\lim a_n$, introduced by a description.
A trap: in a structure where $\varphi$ fails, such as a semigroup without identity, the sentence is false, not meaningless.

### L3 human

There are three standard treatments of descriptions.
Russell eliminates them contextually, so first-order syntax stays as it is, at the price of scope distinctions.
Frege and Carnap give every description a value, with a chosen default when uniqueness fails; the $\varepsilon$-operator is a relative of this approach.
Free logics allow terms that denote nothing, so $\iota x \, \varphi$ is a term that may lack a referent, with rules for $E!$ that say when a term denotes.
These logics are treated in the topic [[non-classical logics|NJB94B39QK]].
In a theory with $\forall \bar{u} \, \exists! x \, \varphi$, all three agree, and the description is a defined function symbol.
