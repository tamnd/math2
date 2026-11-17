---
tag: BCGR3NPPXC
kind: concept
name: Equality, definition and equivalence signs
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
uses: [QKEX4PD029, E918704SKV, 0G8VEZ3WTK, 0WAY5WX8NY, 0TGV80E6A4]
sources:
  - url: https://en.wikipedia.org/wiki/Equals_sign
    locator: History
  - url: https://en.wikipedia.org/wiki/Triple_bar
    locator: Mathematics and philosophy
  - url: https://en.wikipedia.org/wiki/Big_O_notation
    locator: lead section
---

## Summary

Mathematics uses a family of signs that look like the equals sign, and each sign makes a different claim.
The sign $=$ says that two expressions denote the same object, the sign $:=$ gives a name to an object, and the signs $\equiv$, $\approx$, $\cong$, $\sim$ and $\simeq$ state weaker relations such as congruence, closeness, isomorphism or equivalence.
Only $=$ allows a reader to replace one side by the other in every context.
A reader must know which sign is in use, because a step that is valid for $=$ can be invalid for $\approx$ or for the $=$ of big O notation.

## Motivation

A school student writes $\pi = 3.14$ and later gets a wrong final digit after a long computation.
The error comes from the sign: $\pi$ and $3.14$ are different numbers, and the true claim is $\pi \approx 3.14$.
In the same way, a sentence such as "$x^2 - 1 = (x - 1)(x + 1)$" holds for every $x$, while "$x^2 - 1 = 3$" holds only for $x = \pm 2$.
The same sign $=$ makes two kinds of claims here, and some authors write $\equiv$ for the first kind.
Precise signs let a reader see which steps of a computation are exact and which ones lose information.

## Notation

| Sign | Read as | Meaning | Example |
|---|---|---|---|
| $=$ | equals | both sides denote the same object; see [[equality|E918704SKV]] | $2 + 3 = 5$ |
| $\ne$ | is not equal to | the two sides denote different objects | $2 + 3 \ne 6$ |
| $:=$ | is defined as | the left side is a new name for the right side | $f(x) := x^2 + 1$ |
| $\equiv$ | is congruent to, or is identically equal to | [[congruence modulo n|0WAY5WX8NY]], or an equality that holds for every value of the variables | $17 \equiv 2 \pmod 5$ |
| $\approx$ | is approximately equal to | the two numbers are close, to a precision given by context | $\sqrt{2} \approx 1.414$ |
| $\cong$ | is isomorphic to, or is congruent to | an [[isomorphism|PZMGQMDN25]] exists; for figures, [[congruent triangles|093EDENVA1]] | $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z} \cong \mathbb{Z}/6\mathbb{Z}$ |
| $\sim$ | is equivalent to, or is similar to | an [[equivalence relation|0G8VEZ3WTK]] named in context; [[asymptotic equivalence|0QR92XBV6H]] of functions; [[similar triangles|0YF6QXXWB5]] | $n^2 + n \sim n^2$ as $n \to \infty$ |
| $\simeq$ | is equivalent to | homotopy equivalence, or another weak equivalence named in context | a disc $\simeq$ a point |
| $f = O(g)$ | $f$ is big O of $g$ | a one-way statement: $f$ lies in the class $O(g)$ of [[big O notation|0TGV80E6A4]] | $3n + 5 = O(n)$ |
| $\iff$ | if and only if | the two statements are [[logically equivalent|0JMR2HM2N2]] | $x^2 = 4 \iff x = \pm 2$ |

This site writes $:=$ for definitions, $\equiv$ only for congruences with the modulus stated, and $\approx$ only for numbers, with the precision clear from the digits.
It writes $\cong$ for isomorphism and $\iff$ between statements, never between numbers.
It keeps the standard form $f = O(g)$ and reads it as $f \in O(g)$.

## Remarks

### Examples

1. [[The one-way equals sign in n² + 3n = O(n²)|KVKC5MZ0CP]]. The statements $n = O(n^2)$ and $n^2 + 3n = O(n^2)$ are both true, but $n \ne n^2 + 3n$.
2. [[22/7 approximates π but does not equal it|7RFX1ACMJ2]]. The correct sign is $\approx$, since $\frac{22}{7} - \pi \approx 0.00126$.
3. An identity and an equation. The identity $(x + 1)^2 \equiv x^2 + 2x + 1$ holds for every $x$, while the equation $(x + 1)^2 = 4$ holds only for $x = 1$ and $x = -3$.
4. A definition. After "$s_n := 1 + 2 + \cdots + n$", the sentence "$s_n = \frac{n(n+1)}{2}$" is a theorem to prove, not part of the definition.

### Non-examples

1. [[The chain 3 + 4 = 7 · 2 = 14 misuses the equals sign|6C5J53X2AE]]. Each sign $=$ in a chain must relate the expressions on its two sides, and here the middle sign claims $7 = 14$.
2. The sign $\Rightarrow$ is not a sign of equality or equivalence. The statement $x = 2 \Rightarrow x^2 = 4$ is true, but its converse fails at $x = -2$.
3. The sign $\le$ is not an equivalence sign, because it is not symmetric: $2 \le 3$ but $3 \not\le 2$.

### Basic properties

1. Equality is reflexive, symmetric and transitive, and it allows substitution: if $a = b$, then $f(a) = f(b)$ for every function $f$.
2. Congruence modulo $n$ is an equivalence relation, and it is compatible with $+$ and $\cdot$. It does not allow every substitution: $2 \equiv 7 \pmod 5$, but $2^2 = 4$ and $2^7 = 128 \equiv 3 \pmod 5$.
3. The relation $\approx$ is not transitive. With the precision "differ by less than $0.5$", we have $0 \approx 0.4$ and $0.4 \approx 0.8$, but $0$ and $0.8$ differ by $0.8$.
4. The big O sign is not symmetric: $n = O(n^2)$ is true, but $n^2 = O(n)$ is false.
5. A definition $a := b$ is not a claim and needs no proof. It fixes the meaning of the new symbol $a$ from that point on.

### History

Robert Recorde introduced the sign $=$ in The Whetstone of Witte in 1557, as a pair of parallel lines of one length, because, in his words, no two things can be more equal.
The sign did not appear in print again until 1618.
Carl Friedrich Gauss first used $\equiv$ for congruence in 1801, in the Disquisitiones Arithmeticae.
Paul Bachmann introduced the symbol $O$ in 1894, and Edmund Landau extended the notation in 1909.
Donald Knuth calls statements such as $f = O(g)$ "one-way equalities".

### Common errors

1. A student writes $\pi = 3.14$. The correct statement is $\pi \approx 3.14$, and a precise version is $3.14 < \pi < 3.15$.
2. A student writes a chain such as $3 + 4 = 7 \cdot 2 = 14$, where the middle sign is false. Each step needs its own line or its own complete expression.
3. A student reverses a big O statement and concludes $O(n^2) = n$. The right side of $f = O(g)$ is a class of functions, not a function.
4. A student writes $\Rightarrow$ between the steps of a computation, as in $2x + 1 = 7 \Rightarrow 2x = 6 \Rightarrow x = 3$. This is correct, but $\iff$ is needed to claim that $x = 3$ is also a solution.

## Explanations

### L1 human

The sign $=$ says "these two things are the same number".
For example, $3 + 4 = 7$, because both sides are seven.
The sign $\approx$ says "these are close, but not the same", as in $\pi \approx 3.14$.
The sign $:=$ says "from now on, this letter means that", as in $a := 5$.
Each sign makes a different claim, so we pick the sign that says exactly what we mean.

### L2 human

We check which sign fits each line of a short computation.

1. Define $f(x) := x^2 - 4x + 5$. This line is a definition, so it uses $:=$.
2. For every $x$, $f(x) = (x - 2)^2 + 1$. This is an identity, and expanding gives $x^2 - 4x + 4 + 1$, which is the definition again.
3. So $f(x) \ge 1$ for every $x$, and $f(2) = 1$. These are exact claims, so they use $=$ and $\ge$.
4. At $x = 2.1$, $f(2.1) = 0.01 + 1 = 1.01$, an exact value.
5. At $x = \sqrt{5}$, $f(\sqrt{5}) = 10 - 4\sqrt{5} \approx 1.0557$, a rounded value, so the line uses $\approx$.
6. As $x \to \infty$, $f(x) \sim x^2$, since $\frac{f(x)}{x^2} = 1 - \frac{4}{x} + \frac{5}{x^2} \to 1$.

The typical use of these signs is to keep exact and approximate steps apart in a computation.
A trap: once a line uses $\approx$, every later line that depends on it is approximate too.

### L3 human

Formally, the claim $a = b$ in first-order logic is the identity relation, governed by reflexivity and the substitution rule of the equality axioms.
The other signs name relations defined inside the theory: $a \equiv b \pmod n$ abbreviates $n \mid a - b$, and $A \cong B$ abbreviates the existence of an isomorphism.
The sign $:=$ belongs to the metalanguage, because it extends the language by a new constant or function symbol, and the extension is conservative.
In Lean the distinction is explicit: `def` and `:=` introduce definitions, `=` is the propositional equality type, and definitional equality is a third notion that the type checker decides.
Mathlib writes big O as `f =O[l] g`, with the filter `l` stated, which removes the one-way equals sign.
In homotopy type theory the univalence axiom identifies equivalence of types with equality of types, so the gap between $\simeq$ and $=$ closes there.
