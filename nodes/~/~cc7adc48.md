---
tag: ~cc7adc48
kind: concept
name: First-order logic with equality
aliases: [first-order-logic-with-identity, equality-axioms]
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
uses: [086QKPF0A6, ~de213704, 983GZBQYT4, E918704SKV]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Equality and its axioms
  - book: isbn:9780122384523
    locator: Section 2.1
  - book: isbn:9781482237726
    locator: Chapter 2
---

## Summary

First-order logic with equality has the binary symbol $=$ as a logical symbol, so that $t_1 = t_2$ is an [[atomic formula|~de213704]] in every language.
In every [[structure|983GZBQYT4]] the symbol $=$ means identity of elements: $t_1 = t_2$ is true when the two terms have the same value.
In a deductive calculus, the equality axioms of reflexivity and substitution govern $=$.
This is the standard form of first-order logic, and most mathematical theories need it.

## Motivation

Mathematics states equations all the time: $x \cdot e = x$, $f(x) = 0$, "there is exactly one".
Each of these needs a symbol for [[equality|E918704SKV]] with a fixed meaning.
One could add $=$ as an ordinary relation symbol with axioms, but then a structure may interpret it as an equivalence relation that is not identity.
Treating $=$ as logical fixes its meaning in all structures, and the equality axioms make the deductive calculus complete for this meaning.

## Notation

1. Logic with equality is also called logic with identity. Logic without equality is sometimes called pure first-order logic.
2. The formula $\neg (t_1 = t_2)$ is written $t_1 \neq t_2$.
3. A structure in which a binary relation symbol $\approx$ is interpreted as identity is a *normal* model, in the terms of Mendelson.
4. In Mathlib equality is built into `FirstOrder.Language.BoundedFormula` by the constructor `equal`, and it is not a relation symbol of the language.

## Remarks

### Examples

1. [[Counting sentences|~5d920f8d]] such as "there are at least two elements" and "there is exactly one $x$ with $\varphi$" are written with $=$.
2. [[The equality axioms for groups|~2958cf80]] are reflexivity and one substitution axiom for each symbol of $\set{\cdot, e, {}^{-1}}$ and for $=$ itself.
3. The axioms of a field include $\neg (0 = 1)$ and $\forall x \, (\neg (x = 0) \to \exists y \, (x \cdot y = 1))$, both with $=$.
4. A [[first-order theory with identity|9T8WK38ZK8]] contains the symbol $=$ with the reflexivity and substitution schemes.

### Non-examples

1. [[Congruence modulo 2 on the integers|~c9d88de6]] satisfies all the equality axioms in the signature of rings, but it is not identity. A structure that interprets $=$ in this way is not a structure of logic with equality.
2. [[Logic without equality|~d0c83280]] cannot say "there are at least two elements": every sentence without $=$ has the same truth value in a one-element structure and in a two-element copy of it.

### Basic properties

1. The equality axioms for a signature $\sigma$ are $\forall x \, (x = x)$, and for each function symbol $f$ and each relation symbol $R$ of arity $n$, including $=$ itself:
   - $\forall \bar{x} \, \forall \bar{y} \, ((x_1 = y_1 \land \dots \land x_n = y_n) \to f(\bar{x}) = f(\bar{y}))$;
   - $\forall \bar{x} \, \forall \bar{y} \, ((x_1 = y_1 \land \dots \land x_n = y_n) \to (R(\bar{x}) \to R(\bar{y})))$.
2. From these axioms, symmetry and transitivity of $=$ follow, by the axiom for $R$ equal to $=$.
3. If a structure interprets $=$ as a relation $E$ that satisfies the equality axioms, then $E$ is a [[congruence|DCSXXT4SER]], and the [[quotient|0011MTQMR6]] by $E$ is a normal model with the same true sentences. See the [[example of congruence modulo 2|~c9d88de6]].
4. So completeness for logic with equality follows from completeness for logic without equality, with the equality axioms added to the theory.
5. Equality is not definable from the other symbols in general: by non-example 2, the sentence $\exists x \, \exists y \, \neg (x = y)$ has no equivalent without $=$.

### History

Leibniz stated that things are identical when each can replace the other without change of truth.
Whitehead and Russell's Principia Mathematica defined identity by this law in higher-order logic.
Gödel's completeness paper of 1930 extended the result to the calculus with identity, by adding the equality axioms and passing to the quotient.

### Common errors

1. A student treats $=$ as one more relation symbol of the signature. In logic with equality its meaning is fixed in every structure.
2. A student proves symmetry of $=$ with an axiom that is not in the list. Symmetry follows from reflexivity and substitution into $x = x$.
3. A student thinks that the equality axioms force identity. They only force a congruence, and only the semantics of logic with equality forces identity.

## Explanations

### L1 human

In mathematics one writes $2 + 3 = 5$ to say that two expressions name the same number.
First-order logic with equality has the symbol $=$ for this, with its usual meaning in every structure.
Its rules say that equal things can replace each other: if $x = y$, then $x + 1 = y + 1$.
With $=$ one can count, for example "there are at least two elements": $\exists x \, \exists y \, \neg (x = y)$.

### L2 human

We derive symmetry of $=$ from the equality axioms.

1. Take the substitution axiom for $R$ equal to $=$, with $n = 2$: $(x_1 = y_1 \land x_2 = y_2) \to (x_1 = x_2 \to y_1 = y_2)$.
2. Put $x_1 := x$, $y_1 := y$, $x_2 := x$, $y_2 := x$. This gives $(x = y \land x = x) \to (x = x \to y = x)$.
3. Reflexivity gives $x = x$.
4. So $x = y$ implies $y = x$.
5. For transitivity, put $x_1 := x$, $y_1 := x$, $x_2 := y$, $y_2 := z$. This gives $(x = x \land y = z) \to (x = y \to x = z)$.

The typical use of the equality axioms is as part of a Hilbert system or of resolution with paramodulation.
A trap: with only reflexivity and the substitution axioms for $f$ and $R$, but not for $=$ itself, symmetry is not provable.

### L3 human

The semantics of logic with equality fixes $=$ as identity, while the axioms only fix it up to congruence.
The quotient construction closes this gap, so completeness, compactness and the Löwenheim-Skolem theorem hold with equality.
One change is that a model of size $\kappa$ can no longer be inflated freely: the sentences $\lambda_n$ with $=$ bound the size from below.
In logic without equality, every structure is elementarily equivalent to all its inflations, in which each element is copied many times.
In a finite relational signature, a formula without $=$ says that $x$ and $y$ can replace each other in each argument place of each relation symbol.
It defines the largest congruence, so equality is definable up to congruence.
In second-order logic equality is definable outright, by $\forall P \, (P(x) \leftrightarrow P(y))$, which is Leibniz's law.
