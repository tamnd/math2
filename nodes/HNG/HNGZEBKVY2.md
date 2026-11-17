---
tag: HNGZEBKVY2
kind: concept
name: Well-defined
aliases: [well-definedness, well-defined-function]
msc: ["00A35"]
topics: [BP0WAF23HB]
audience: ug1
uses: [8ZCZ3HW91Z, 0G8VEZ3WTK, 0W95W33CMP, 0011MTQMR6, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Well-defined_expression
    locator: Independence of representative
  - url: https://en.wikipedia.org/wiki/Well-defined_expression
    locator: Functions with one argument
  - url: https://en.wikipedia.org/wiki/Well-defined_expression
    locator: Operations
  - book: isbn:9781108439534
    locator: Chapter 4
---

## Summary

A definition is well defined when it gives exactly one result, and this result does not depend on any choice that the definition makes.
The main case is a [[function|0EPAT51DXQ]] on a [[quotient set|0011MTQMR6]].
Let $\sim$ be an [[equivalence relation|0G8VEZ3WTK]] on a set $X$, and let $g \colon X \to Y$ be a function.
The rule $f([x]) := g(x)$ is well defined exactly when $x \sim x'$ implies $g(x) = g(x')$ for all $x, x' \in X$.
Then $f$ is a function on $X/{\sim}$.
Until this condition is proved, the rule names a value that may depend on the representative $x$ of the class, and it is not yet a function.
Well-definedness is the proof obligation of each definition by representatives, and it appears in every construction with classes, cosets or residues.

## Motivation

We want to add residues modulo $5$.
A residue is a class, such as $[3] = \{\ldots, -7, -2, 3, 8, 13, \ldots\}$.
The natural rule is "pick a number from each class, add the numbers, and take the class of the sum".
But a class has many members, and different picks might give different classes.
For $[3] + [4]$, the picks $3$ and $4$ give $[7]$, and the picks $8$ and $-1$ give $[7]$ again.
To trust the rule, we need a proof that every pick gives the same class.
That proof is the proof that the addition is well defined, and it is on the page of the [[addition of residues|Y03QSFQCCH]].

## Notation

1. Authors write "well defined" after a noun ("the map is well defined") and "well-defined" before a noun ("a well-defined map"). Both mean the same.
2. A rule that is not well defined is sometimes called "ill-defined".
3. In Lean and Mathlib, a function on a quotient is made with `Quotient.lift f h`. Here `f : α → β` is the rule on representatives, and `h` is a proof of `∀ a b, a ≈ b → f a = f b`. The system does not accept the function without `h`.
4. For operations with two arguments, Lean has `Quotient.lift₂`, which asks for the same condition in both arguments.

## Remarks

### The criterion for functions on classes

Let $\sim$ be an equivalence relation on $X$, let $\pi \colon X \to X/{\sim}$ be the map $\pi(x) = [x]$, and let $g \colon X \to Y$.
Then the following are equivalent.

1. There is a function $f \colon X/{\sim} \to Y$ with $f([x]) = g(x)$ for each $x \in X$.
2. For all $x, x' \in X$, if $x \sim x'$, then $g(x) = g(x')$.

When they hold, $f$ is unique.
The proof has four steps.

1. Suppose 1 holds, and let $x \sim x'$. Then $[x] = [x']$, because two related elements have the same [[equivalence class|0W95W33CMP]]. So $g(x) = f([x]) = f([x']) = g(x')$.
2. Suppose 2 holds. For a class $c$, choose any $x$ with $[x] = c$, and set $f(c) = g(x)$.
3. Another choice $x'$ with $[x'] = c$ satisfies $x' \sim x$, so $g(x') = g(x)$ by 2. So $f(c)$ does not depend on the choice, and $f$ is a function.
4. Each class is $[x]$ for some $x$, so the values $f([x]) = g(x)$ fix $f$ on every class. This gives uniqueness.

### Operations on classes

An operation $[a] \ast [b] := [a \cdot b]$ is well defined exactly when $a \sim a'$ and $b \sim b'$ imply $a \cdot b \sim a' \cdot b'$.
An equivalence relation with this property for an operation is called a [[congruence relation|DCSXXT4SER]].
For cosets of a subgroup $N$ of a group, the product $(aN)(bN) := abN$ is well defined exactly when $N$ is a [[normal subgroup|0CB0DX5BVV]].
This is why the [[quotient group|0KYX2N69J0]] needs normality.

### Other uses of the word

1. A value. The expression $\tfrac{1}{0}$ is not well defined, because no number $x$ satisfies $0 \cdot x = 1$. The expression $a + b + c$ is well defined, because the associative law makes both readings equal.
2. A codomain. The rule $f(n) = n - 1$ does not define a function $\mathbb{N} \to \mathbb{N}$, because $f(0) = -1$ is not in $\mathbb{N}$.
3. "The". A definition "the $x$ such that $C(x)$" is well defined when exactly one $x$ satisfies $C$, see [[definitions that use "the"|5P955TVSS2]].
4. A recursion. A recursive definition is well defined when exactly one function satisfies it, see [[kinds of definitions|B60DBNF77S]].
5. An invariant. A number that is computed from a choice, such as the dimension of a vector space from a basis, is well defined when each choice gives the same number.

### Examples

1. The [[addition of residues modulo $n$|Y03QSFQCCH]], $[a] + [b] := [a + b]$, is well defined, because $n \mid a - a'$ and $n \mid b - b'$ give $n \mid (a + b) - (a' + b')$.
2. The [[reduction from $\mathbb{Z}/6\mathbb{Z}$ to $\mathbb{Z}/3\mathbb{Z}$|55FJH3WXE9]], $[a]_6 \mapsto [a]_3$, is well defined, because $3 \mid 6$.
3. The addition of [[rational numbers|KF8H084HDE]], $\tfrac{a}{b} + \tfrac{c}{d} := \tfrac{ad + bc}{bd}$, is well defined. If $ab' = a'b$ and $cd' = c'd$, then $(ad + bc)b'd' = a'b\,dd' + c'd\,bb' = (a'd' + b'c')bd$.
4. The map $\mathbb{Z}/n\mathbb{Z} \to \mathbb{C}$, $[k] \mapsto e^{2\pi i k/n}$, is well defined, because $e^{2\pi i (k + mn)/n} = e^{2\pi i k/n} \cdot (e^{2\pi i})^m = e^{2\pi i k/n}$.
5. The product of cosets $(aN)(bN) := abN$ is well defined for a normal subgroup $N$.

### Non-examples

1. [[Adding numerators and denominators|C3Z6VNAXSG]], $\tfrac{a}{b} \oplus \tfrac{c}{d} := \tfrac{a + c}{b + d}$, is not well defined: $\tfrac12 \oplus \tfrac13 = \tfrac25$, but $\tfrac24 \oplus \tfrac13 = \tfrac37 \neq \tfrac25$.
2. The rule $[a]_3 \mapsto [a]_6$ from $\mathbb{Z}/3\mathbb{Z}$ to $\mathbb{Z}/6\mathbb{Z}$ is not well defined: $[0]_3 = [3]_3$, but $[0]_6 \neq [3]_6$.
3. The rule $\tfrac{a}{b} \mapsto a$ from $\mathbb{Q}$ to $\mathbb{Z}$ is not well defined: $\tfrac12 = \tfrac24$, but $1 \neq 2$.
4. In the [[symmetric group|0515A6D2Y1]] $S_3$, let $H = \{e, (1\,2)\}$, and try $(aH)(bH) := abH$. We have $eH = (1\,2)H$, but $(1\,3)H \neq (1\,2)(1\,3)H$, because $(1\,3)^{-1}(1\,2)(1\,3) = (2\,3) \notin H$.

### Basic properties

1. The criterion above: a rule on representatives defines a function on classes exactly when it is constant on each class.
2. The function $f$ satisfies $f \circ \pi = g$, and it is the only function with this property. This is the universal property of the quotient set.
3. The function $f$ is injective exactly when $g(x) = g(x')$ implies $x \sim x'$. So for $f$ we check one direction for well-definedness and the other direction for injectivity.
4. Each function $h \colon X/{\sim} \to Y$ arises in this way, from $g = h \circ \pi$.

### History

Gauss introduced the congruence notation $a \equiv b \pmod n$ in *Disquisitiones Arithmeticae* (1801).
His rules for adding and multiplying congruences are the statement that the operations on residues are well defined.

### Common errors

1. A student checks the rule on one representative of each class only. A check of $g(x)$ for one $x$ proves nothing about the other members of the class.
2. A student confuses well-definedness with injectivity. Well-definedness says $x \sim x' \Rightarrow g(x) = g(x')$. Injectivity of $f$ says the converse.
3. A student forgets to check that the values lie in the stated codomain.

## Explanations

### L1 human

Sometimes a rule asks us to choose something, and then it gives an answer.
The rule is well defined if every choice leads to the same answer.
For example, suppose that the rule for a fraction is "take its numerator".
For one half we could write $\tfrac12$ and answer $1$, or write $\tfrac24$ and answer $2$.
The two answers differ, although the number is the same, so this rule is not well defined.
The rule "take the numerator divided by the denominator" gives one half for both, so it is fine.

### L2 human

We prove that multiplication of residues modulo $n$ is well defined: $[a] \cdot [b] := [ab]$.

1. Let $[a] = [a']$ and $[b] = [b']$. By the definition of [[congruence modulo $n$|0TPW25CBN6]], there are integers $s$ and $t$ with $a' = a + sn$ and $b' = b + tn$.
2. Then $a'b' = ab + atn + bsn + stn^2 = ab + n(at + bs + stn)$.
3. So $a'b' - ab$ is a multiple of $n$, and $[a'b'] = [ab]$.
4. So the class of the product does not depend on the representatives.

Check with $n = 5$: $[3] \cdot [4] = [12] = [2]$, and with the representatives $8$ and $-1$, $[8 \cdot (-1)] = [-8] = [2]$.
The typical use: each time a construction says "choose a representative", the proof must vary the choice and show that the result stays the same.
A trap is to vary only one argument: an operation with two arguments needs the check in both.

### L3 human

The criterion is the universal property of the quotient set: $\pi \colon X \to X/{\sim}$ is the coequalizer of the two projections from the relation $\{(x, x') : x \sim x'\}$ to $X$.
The same pattern gives the [[universal property of the quotient group|0GJ83E78A5]], of the quotient ring and of the quotient topology.
In type theory, a quotient type comes with an eliminator that is exactly `Quotient.lift`, so a well-definedness proof is a part of the term itself.
Many invariants are well-definedness results.
The dimension of a vector space does not depend on the basis.
The degree of a map does not depend on the representative of its homotopy class.
A cohomology class does not depend on the chosen cocycle.
In each case, the main theorem says that a number or class computed from a choice is in fact a function on the set of classes.
