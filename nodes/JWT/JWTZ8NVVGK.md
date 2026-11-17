---
tag: JWTZ8NVVGK
kind: concept
name: Indicators
aliases: [kirby-paris-indicators, indicator-function-for-initial-segments]
msc: ["03C62", "03F30"]
topics: [T6FK1E7GJ1]
audience: research
uses: [1QWN5CV4CG, MPSCREYC3M, 1NR3HAWG9D]
sources:
  - url: https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic
    locator: Structure of countable non-standard models
  - url: https://en.wikipedia.org/wiki/Paris–Harrington_theorem
    locator: lead section
---

## Summary

An *indicator* is a definable function $Y(a, b)$ on a [[non-standard model|1QWN5CV4CG]] $M$ of [[Peano arithmetic|MPSCREYC3M]] that detects initial segments of a given kind.
The value $Y(a, b)$ is non-standard exactly when some such segment contains $a$ and does not contain $b$.
Indicators turn questions about models of a theory into the growth of a definable function, and they give a template for proofs of unprovability.

## Motivation

To show that $\mathsf{PA}$ does not prove a sentence, one can build a model of $\mathsf{PA}$ in which the sentence fails.
In a non-standard model $M$, a natural source of such models is the initial segments $I$ of $M$ with $I \models \mathsf{PA}$.
These segments are not definable in $M$, so $M$ cannot talk about them directly.
An indicator is a definable function that measures them, through the size of its values.

## Notation

Let $M$ be a countable non-standard model of $\mathsf{PA}$, and write $\N$ for its standard part.

- A *cut* of $M$ is a set $I \subseteq M$ with $\N \subseteq I \ne M$ that is closed downward and under $x \mapsto x + 1$.
- For $a \in M$ and $I \subseteq M$, write $a \in I < b$ if $a \in I$ and $b \notin I$. Then $b$ is above every element of $I$.
- Let $\mathcal{K}$ be a class of cuts of $M$, for example the cuts $I$ with $I \models \mathsf{PA}$.

A function $Y : M^2 \to M$ is an *indicator for $\mathcal{K}$* if the following hold.

1. $Y$ is definable in $M$ by a formula of arithmetic without parameters.
2. $Y(a, b) \le b$, and $Y(a, b) \le Y(a', b')$ whenever $a' \le a \le b \le b'$.
3. For all $a \le b$ in $M$, $Y(a, b)$ is non-standard if and only if some $I \in \mathcal{K}$ has $a \in I < b$.

## Remarks

### Examples

- The [[difference indicator|1T6K132VVA]] $Y(a, b) = b - a$ is an indicator for the class of all cuts.
- The [[doubling indicator|K470Y7R628]] $Y(a, b) = \max\set{c : a \cdot 2^c \le b}$ is an indicator for the cuts closed under $x \mapsto 2x$.
- The function of the [[Paris-Harrington proof|D0Q498H0R5]], defined from the strengthened finite Ramsey theorem on $[a, b]$, is an indicator for the cuts that are models of $\mathsf{PA}$. This is the cited indicator lemma.

### Non-examples

- The [[doubling indicator is not an indicator for models of PA|Q1WSA5TPC2]]: for non-standard $c$ the value $Y(c, c^2)$ is non-standard, but no model of $\mathsf{PA}$ contains $c$ and omits $c^2$.
- A constant function is not an indicator for a nonempty class $\mathcal{K}$. No cut has $a \in I < a$, so $Y(a, a)$ is standard, but $Y(a, b)$ is non-standard when a cut in $\mathcal{K}$ separates $a$ from $b$.

### Basic properties

The template for unprovability, for a theory $T \supseteq \mathsf{PA}$ and an indicator $Y$ for the cuts that are models of $T$.

1. Suppose that $Y(a, b) \ge c$ has a formula with bounded quantifiers, so that it has the same truth value in $M$ and in each cut that is a model of $\mathsf{PA}$.
2. Suppose that $T$ proves $\forall a\, \exists b\; Y(a, b) \ge a$. Take a non-standard $a \in M$, for a model $M$ of $T$.
3. Let $b$ be the least element with $Y(a, b) \ge a$. Then $Y(a, b)$ is non-standard, so a cut $I \models T$ has $a \in I < b$.
4. In $I$ some $b' < b$ has $Y(a, b') \ge a$, by step 2 inside $I$ and step 1. This contradicts the choice of $b$.
5. So $T$ does not prove $\forall a\, \exists b\; Y(a, b) \ge a$.

The truth of this sentence in $\N$ is proved separately in each application, for example by compactness for the Paris-Harrington principle.

### History

Laurence Kirby and Jeff Paris developed indicators in the late 1970s, in work on initial segments of models of $\mathsf{PA}$.
The model-theoretic proof of the [[Paris-Harrington theorem|509ZWA0R26]] uses this method.

### Common errors

- An indicator is defined on one model $M$, but the useful indicators work in every countable non-standard model. Each application states which.
- Non-standard values of $Y$ say that a cut exists, but the cut is not definable in $M$. Arguments inside $M$ cannot name it.
- The class $\mathcal{K}$ is part of the definition. The same function can be an indicator for one class of cuts and not for a smaller class.

## Explanations

### L1 human

A non-standard model of arithmetic has the ordinary numbers at the bottom and infinite numbers above them.
Between two infinite numbers $a$ and $b$ there may be a gap in which a whole smaller model of arithmetic lives.
An indicator is a formula that measures the distance from $a$ to $b$, so that the distance is infinite exactly when such a gap exists.
This lets one prove that a statement about growth is unprovable by finding such gaps.

### L2 human

The first example in steps.

1. Let $Y(a, b) = b - a$ for $a \le b$.
2. If $b - a$ is non-standard, let $I$ be the set of the $x \le a + k$ for some standard $k$. This is a cut with $a \in I < b$.
3. If a cut $I$ has $a \in I < b$, then $a + k \in I$ for each standard $k$, so $b - a > k$ for each standard $k$.
4. So $b - a$ is non-standard exactly when a cut separates $a$ from $b$.

The typical use is the template in the Basic properties section, with an indicator for the cuts that are models of $\mathsf{PA}$.
The trap: an indicator for a larger class of cuts, such as the doubling-closed ones, is not an indicator for the models of $\mathsf{PA}$.

### L3 human

An indicator for the models of $\mathsf{PA}$ in $M$ gives a function $x \mapsto \min\set{b : Y(x, b) \ge x}$ that is total in $\N$ but not provably total in $\mathsf{PA}$.
So indicators connect the model theory of $\mathsf{PA}$ with [[provably total functions|Z742YPHPNS]] and with the [[fast-growing hierarchy|R6ZC4BJGXV]].
Suppose $Y$ is an indicator for the models of $\mathsf{PA}$ in every countable non-standard model, and the function $g(x) = \min\set{b : Y(x, b) \ge x}$ is total.
For a provably total $f$ and a non-standard $x$, the cut $I$ for $x$ and $g(x)$ contains $f(x)$, so $f(x) < g(x)$.
A [[compactness|1NR3HAWG9D]] argument then shows that $g$ eventually dominates $f$ in $\N$.
This gives the lower bound for the growth of the Paris-Harrington function.
