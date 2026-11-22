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

A definition that makes a choice along the way is *well defined* when the result does not depend on the choice.
"Let $f(\tfrac{a}{b}) = a + b$" looks like a function on the rationals, but $\tfrac{1}{2} = \tfrac{2}{4}$ while $1 + 2 = 3$ and $2 + 4 = 6$, so it gives two values for one input and defines nothing.

The main case is a [[function|0EPAT51DXQ]] on a [[quotient set|0011MTQMR6]].
Let $\sim$ be an [[equivalence relation|0G8VEZ3WTK]] on a set $X$, and let $g \colon X \to Y$ be a function.
The rule $f([x]) := g(x)$ is well defined exactly when
$$x \sim x' \implies g(x) = g(x') \qquad \text{for all } x, x' \in X,$$
and then $f$ is a function on $X/{\sim}$.
Until this condition is proved, the rule is a claim, not a definition.

## Motivation

Many objects of mathematics are classes: residues modulo $n$, rational numbers as classes of fractions, cosets of a subgroup, vectors as classes of arrows.
We name a class by one of its members, and we want to compute with classes by computing with members.
That is safe only when every member gives the same answer, and well-definedness is the proof that it does.
The obligation appears in every [[definition by abstraction|B60DBNF77S]], and it returns in group theory as the reason that a quotient group needs a normal subgroup.

## Notation

Authors write "the map is well defined" after a noun and "a well-defined map" before it, with the same meaning, and a rule that fails is sometimes called ill-defined.
In Lean and Mathlib, a function on a quotient is built as `Quotient.lift f h`.
Here `f : α → β` is the rule on representatives, and `h` is a proof of `∀ a b, a ≈ b → f a = f b`, so the system does not accept the function until the well-definedness proof is given.
For operations of two arguments there is `Quotient.lift₂`, which asks for the condition in both arguments at once.

## Remarks

### A rule that fails

Take a [[rational number|KF8H084HDE]] and propose "the numerator of $\tfrac{a}{b}$".
To use the rule, we must pick a fraction for the number, and the number $\tfrac{1}{2}$ has the fractions $\tfrac{1}{2}$, $\tfrac{2}{4}$ and $\tfrac{-3}{-6}$:
$$\text{numerator}\left(\tfrac{1}{2}\right) = 1, \qquad \text{numerator}\left(\tfrac{2}{4}\right) = 2.$$
One input gives two outputs, so the rule is not a function on $\mathbb{Q}$.
The rule $f(\tfrac{a}{b}) = a + b$ fails in the same way, with $3$ and $6$.

A subtler failure is the rule that adds tops and bottoms, $\tfrac{a}{b} \oplus \tfrac{c}{d} := \tfrac{a + c}{b + d}$.
It gives $\tfrac{1}{2} \oplus \tfrac{1}{3} = \tfrac{2}{5}$ but $\tfrac{2}{4} \oplus \tfrac{1}{3} = \tfrac{3}{7}$, and $\tfrac{2}{5} \neq \tfrac{3}{7}$ since $2 \cdot 7 \neq 5 \cdot 3$.
[[Adding numerators and denominators|C3Z6VNAXSG]] works through it.
You can repair the numerator rule by fixing the representative, for example the fraction in lowest terms with $b > 0$, and then it is a function.

### A rule that works

Now add residues modulo $5$ by the rule $[a] + [b] := [a + b]$.
The class $[3]$ also has the members $8$ and $-2$, and $[4]$ also has $-1$ and $9$.
Try three choices of members:
$$3 + 4 = 7, \qquad 8 + (-1) = 7, \qquad -2 + 9 = 7.$$
All three sums lie in $[2]$.
Three choices are not a proof, so we argue in general.
If $a' = a + 5s$ and $b' = b + 5t$, then $a' + b' = (a + b) + 5(s + t)$, so $[a' + b'] = [a + b]$.
The same argument works for every $n$, and [[addition of residues modulo $n$|Y03QSFQCCH]] writes it out.

Addition of fractions passes the test too.
If $ab' = a'b$ and $cd' = c'd$, then
$$(ad + bc) \, b'd' = a'b \, dd' + c'd \, bb' = (a'd' + b'c') \, bd,$$
so $\tfrac{ad + bc}{bd} = \tfrac{a'd' + b'c'}{b'd'}$.
Check: $\tfrac{1}{2} + \tfrac{1}{3} = \tfrac{5}{6}$, and $\tfrac{2}{4} + \tfrac{1}{3} = \tfrac{10}{12} = \tfrac{5}{6}$.

### The test in general

Let $\pi \colon X \to X/{\sim}$ send $x$ to its class $[x]$, and let $g \colon X \to Y$.
There is a function $f \colon X/{\sim} \to Y$ with $f([x]) = g(x)$ for all $x$ exactly when $g$ is constant on each class, and then $f$ is unique.
The proof has four steps.

1. Suppose $f$ exists, and let $x \sim x'$.
   Related elements have the same [[equivalence class|0W95W33CMP]], so $[x] = [x']$ and $g(x) = f([x]) = f([x']) = g(x')$.
2. Conversely, suppose $g$ is constant on classes.
   For a class $c$, choose any $x$ with $[x] = c$, and set $f(c) = g(x)$.
3. Another choice $x'$ with $[x'] = c$ satisfies $x' \sim x$, so $g(x') = g(x)$.
   So $f(c)$ does not depend on the choice, and $f$ is a function.
4. Every class is $[x]$ for some $x$, so the values $g(x)$ fix $f$ on every class, which gives uniqueness.

In symbols, $f \circ \pi = g$, and $f$ is the only function with this property.

### What the test gives you

Reduction from residues modulo $6$ to residues modulo $3$ passes the test, because $6 \mid a' - a$ implies $3 \mid a' - a$, as [[the reduction from $\mathbb{Z}/6\mathbb{Z}$ to $\mathbb{Z}/3\mathbb{Z}$|55FJH3WXE9]] shows.
The reverse rule $[a]_3 \mapsto [a]_6$ fails, because $[0]_3 = [3]_3$ but $[0]_6 \neq [3]_6$.
The map $[k] \mapsto e^{2\pi i k / n}$ from $\mathbb{Z}/n\mathbb{Z}$ to $\mathbb{C}$ passes, because $e^{2\pi i (k + mn)/n} = e^{2\pi i k/n} (e^{2\pi i})^m = e^{2\pi i k/n}$.

Well-definedness and injectivity are the two directions of one equivalence.
Well-definedness of $f$ says that $x \sim x'$ implies $g(x) = g(x')$.
Injectivity of $f$ says the converse, that $g(x) = g(x')$ implies $x \sim x'$.
And every function $h$ on $X/{\sim}$ arises from the test, with $g = h \circ \pi$.

### Operations and congruences

An operation $[a] \ast [b] := [a \cdot b]$ is well defined exactly when $a \sim a'$ and $b \sim b'$ imply $a \cdot b \sim a' \cdot b'$.
An equivalence relation with this property is a [[congruence relation|DCSXXT4SER]].
For left cosets of a subgroup $N$ of a group, the product $(aN)(bN) := abN$ is well defined exactly when $N$ is a [[normal subgroup|0CB0DX5BVV]], which is why a [[quotient group|0KYX2N69J0]] needs normality.

Here is the failure in the [[symmetric group|0515A6D2Y1]] $S_3$.
Let $H = \{ e, (1\,2) \}$, which is not normal.
We have $eH = (1\,2)H$, so the rule must give $e(1\,3)H = (1\,2)(1\,3)H$.
These cosets are equal only if $(1\,3)^{-1}(1\,2)(1\,3) \in H$, but that conjugate is $(2\,3)$, which is not in $H$.

Gauss introduced the notation $a \equiv b \pmod{n}$ in his *Disquisitiones Arithmeticae* of 1801, and his rules for adding and multiplying congruences say exactly that the operations on residues are well defined.

### Other uses of the word

The word also covers values that need no classes.
The expression $\tfrac{1}{0}$ is not well defined, because no $x$ satisfies $0 \cdot x = 1$.
The expression $a + b + c$ is well defined, because the associative law makes both readings equal.
The rule $f(n) = n - 1$ is not well defined as a map $\mathbb{N} \to \mathbb{N}$ when $0 \in \mathbb{N}$, because $f(0) = -1$ is outside the codomain.

A definition with "the" is well defined when exactly one object fits, as [[definitions that use "the"|5P955TVSS2]] explains.
A recursion is well defined when exactly one function obeys it.
An invariant computed from a choice, such as the dimension of a vector space computed from a basis, is well defined when every choice gives the same number.

### Watch out

The first error is to check one representative of each class.
A computation with $3$ and $4$ says nothing about $8$ and $-1$, so the proof must start from arbitrary $a \sim a'$ and $b \sim b'$.

The second error is to vary only one argument of an operation.
For $\oplus$ above, varying $\tfrac{1}{2}$ alone already shows the failure, but to prove that an operation works, both arguments must vary.

The third error is to confuse the two directions.
To prove that $f$ is well defined you show that related inputs give equal outputs, not that equal outputs come from related inputs.

### Try it

First, is $[a]_4 \mapsto [a]_2$ from $\mathbb{Z}/4\mathbb{Z}$ to $\mathbb{Z}/2\mathbb{Z}$ well defined?
Yes: $4 \mid a' - a$ gives $2 \mid a' - a$, so $[a']_2 = [a]_2$.

Second, is $\tfrac{a}{b} \mapsto \tfrac{a^2}{b^2}$ well defined on $\mathbb{Q}$?
Yes: $ab' = a'b$ gives $a^2 b'^2 = a'^2 b^2$ by squaring, and $b^2 \neq 0$.

Third, is $\tfrac{a}{b} \mapsto \tfrac{a + 1}{b}$ well defined?
No: $\tfrac{1}{2} \mapsto \tfrac{2}{2} = 1$, but $\tfrac{2}{4} \mapsto \tfrac{3}{4}$.

## Explanations

### L1 human

Sometimes a rule asks you to choose something before it gives an answer.
The rule is well defined if every choice leads to the same answer.
Suppose the rule for a fraction is "take the top number".
One half can be written $\tfrac12$, giving $1$, or $\tfrac24$, giving $2$.
The two answers differ although the number is the same, so the rule is not well defined.
The rule "divide the top by the bottom" gives one half both times, so it is fine.

### L2 human

We prove that multiplication of residues modulo $n$, $[a] \cdot [b] := [ab]$, is well defined.

1. Let $[a] = [a']$ and $[b] = [b']$.
   By the definition of [[congruence modulo $n$|0TPW25CBN6]], there are integers $s$ and $t$ with $a' = a + sn$ and $b' = b + tn$.
2. Multiply out:
   $$a'b' = ab + atn + bsn + stn^2 = ab + n(at + bs + stn).$$
3. So $a'b' - ab$ is a multiple of $n$, and $[a'b'] = [ab]$.
4. The class of the product does not depend on the representatives.

Check with $n = 5$: $[3] \cdot [4] = [12] = [2]$, and the representatives $8$ and $-1$ give $[-8] = [2]$.
The proof shows the usual pattern: whenever a construction says "choose a representative", vary the choice and show that the result stays the same.
Watch out: the same idea fails for exponents, since modulo $5$ the exponents $1$ and $6$ give $2^1 = 2$ but $2^6 = 64 \equiv 4$.

### L3 human

The test is the universal property of the quotient set.
The map $\pi \colon X \to X/{\sim}$ is the coequalizer of the two projections from the relation $\{ (x, x') : x \sim x' \}$ to $X$.
The same pattern gives the [[universal property of the quotient group|0GJ83E78A5]], and those of the quotient ring and the quotient topology.
In type theory a quotient type comes with an eliminator, which in Lean is `Quotient.lift`, so the well-definedness proof is a part of the term itself.

Many theorems are well-definedness results in disguise.
The dimension of a vector space does not depend on the basis.
The degree of a map of circles does not depend on the map chosen in its homotopy class, and a cohomology class does not depend on the chosen cocycle.
In each case, a number or class computed from a choice turns out to be a function on the set of classes.
