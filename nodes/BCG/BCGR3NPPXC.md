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

Mathematics has a family of signs that look like the equals sign, and each one makes a different claim.
Read two lines of a typical proof: "let $s_n := 1 + 2 + \cdots + n$" and "then $s_n = \frac{n(n+1)}{2}$".
The first line gives a name and claims nothing, and the second line is a theorem that needs a proof.

The sign $=$ says that two expressions denote the same object, and the sign $:=$ gives a name to an object.
The signs $\equiv$, $\approx$, $\cong$, $\sim$ and $\simeq$ state weaker relations: congruence or identity, closeness, isomorphism, and various kinds of equivalence.
Only $=$ lets you replace one side by the other in every context.
So you must know which sign is in use, because a step that is valid for $=$ can be invalid for $\approx$ or for the one-way $=$ of big O notation.

## Motivation

A school student writes $\pi = 3.14$, and after a long computation the last digits of the answer are wrong.
The error is in the sign.
The numbers $\pi$ and $3.14$ are different, and the true claim is $\pi \approx 3.14$, or more exactly $3.14 < \pi < 3.15$.

Even $=$ makes two kinds of claim.
The line $x^2 - 1 = (x - 1)(x + 1)$ holds for every $x$, while the line $x^2 - 1 = 3$ holds only for $x = 2$ and $x = -2$.
The first is an identity and the second is an equation to solve, and some authors write $\equiv$ for the first kind to mark the difference.
Precise signs let a reader see which steps of a computation are exact, which ones are only approximate, and which ones are definitions.
[[Mathematical notation|QKEX4PD029]] introduced the symbols in general, and the equality family causes many of the errors in early proofs.

## Notation

The pages of this site write $:=$ for a definition and $=$ for a claim of [[equality|E918704SKV]].
They write $\equiv$ only for [[congruence modulo n|0WAY5WX8NY]], always with the modulus, and they write identities with $=$ and the words "for all $x$".
They use $\approx$ only between numbers, with the precision clear from the digits, and $\cong$ for isomorphism.
They keep the standard form $f = O(g)$ and read it as $f \in O(g)$.
Some books write $\stackrel{\text{def}}{=}$, $\triangleq$ or $:\Leftrightarrow$ for a definition, and some write $=:$ when the new name is on the right.

## Remarks

### Equals and "is defined as"

After "let $f(x) := x^2 - 4x + 5$", the line $f(x) = (x - 2)^2 + 1$ is a claim, and you check it by expanding:
$$(x - 2)^2 + 1 = x^2 - 4x + 4 + 1 = x^2 - 4x + 5.$$
A definition needs no proof and can never be false, because it fixes the meaning of a new symbol from that point on.

In school, $=$ often means "and the result is", as on a calculator.
In mathematics it is a relation: each $=$ claims that the expressions on its two sides have the same value.
[[The chain 3 + 4 = 7 · 2 = 14 misuses the equals sign|6C5J53X2AE]] shows the difference.
The student means "$3 + 4$ is $7$, and times $2$ that is $14$", but the middle sign claims $3 + 4 = 7 \cdot 2$, that is, $7 = 14$.
The correct chain is $(3 + 4) \cdot 2 = 7 \cdot 2 = 14$, where every expression has the value $14$.

### The triple bar

The sign $\equiv$ has two common readings, and the context tells them apart.
In number theory it is congruence: $17 \equiv 2 \pmod 5$, because $5$ divides $17 - 2 = 15$.
In algebra and analysis it can mean "equal for every value of the variable", as in $(x + 1)^2 \equiv x^2 + 2x + 1$ or "$f \equiv 0$" for the zero function.
A "$\pmod n$" nearby means congruence, and a function or polynomial on both sides means an identity.
In logic books $\equiv$ sometimes means logical equivalence, the relation that this site writes $\iff$.

Congruence allows less substitution than equality.
It respects $+$ and $\cdot$, but not exponents: $2 \equiv 7 \pmod 5$, and yet
$$2^2 = 4, \qquad 2^7 = 128 = 25 \cdot 5 + 3 \equiv 3 \pmod 5.$$

### Close, but not equal

The sign $\approx$ says that two numbers are close, with a precision that the context gives.
[[22/7 approximates π but does not equal it|7RFX1ACMJ2]]: the fraction is $3.142857\ldots$ and $\pi$ is $3.141592\ldots$, so $\frac{22}{7} - \pi \approx 0.00126$.
Since $\pi$ is irrational, no fraction equals it, and the sign $=$ would be false.

The relation $\approx$ is not transitive.
With the precision "differ by less than $0.5$", we have $0 \approx 0.4$ and $0.4 \approx 0.8$, but $0$ and $0.8$ differ by $0.8$.
So a chain of $\approx$ signs can drift far from its start, and an exact statement uses inequalities instead.

### Isomorphic, similar, equivalent

The sign $\cong$ usually says that an [[isomorphism|PZMGQMDN25]] exists, as in $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z} \cong \mathbb{Z}/6\mathbb{Z}$.
In school geometry it says that two figures are congruent, as for [[congruent triangles|093EDENVA1]].
The subject of the text tells you which reading holds.

The sign $\sim$ has the most readings.
It can be an [[equivalence relation|0G8VEZ3WTK]] named in the text, the relation of [[similar triangles|0YF6QXXWB5]], or [[asymptotic equivalence|0QR92XBV6H]] of functions, where $f \sim g$ means $f(n)/g(n) \to 1$.
For example, $n^2 + n \sim n^2$, since $\frac{n^2 + n}{n^2} = 1 + \frac{1}{n} \to 1$.
The sign $\simeq$ often means homotopy equivalence in topology, and some books use it for isomorphism instead.
Each text that uses $\sim$ or $\simeq$ defines it, so look for the definition before you use a rule.

### The one-way equals of big O

In [[big O notation|0TGV80E6A4]], $f = O(g)$ means that $|f(n)| \le C |g(n)|$ for some constant $C$ and all large $n$.
[[The one-way equals sign in n² + 3n = O(n²)|KVKC5MZ0CP]] proves both $n = O(n^2)$ and $n^2 + 3n = O(n^2)$.
If these were equalities, symmetry and transitivity would give $n = n^2 + 3n$, which at $n = 1$ says $1 = 4$.
So $O(n^2)$ is a class of functions, and $f = O(g)$ means $f \in O(g)$.
The sign is not symmetric: $n = O(n^2)$ is true, but $n^2 = O(n)$ is false.

### Watch out

The first trap is $\pi = 3.14$ or $\sqrt{2} = 1.414$.
Write $\approx$, and once a line uses $\approx$, every later line that depends on it is approximate too.

The second trap is to treat other signs as equality.
The arrow $\Rightarrow$ is not an equality sign: $x = 2 \Rightarrow x^2 = 4$ is true, but the converse fails at $x = -2$.
The sign $\le$ is not an equivalence, because it is not symmetric: $2 \le 3$ but $3 \not\le 2$.

The third trap is a chain of $\Rightarrow$ signs when solving an equation.
From $2x + 1 = 7 \Rightarrow 2x = 6 \Rightarrow x = 3$ you learn only that a solution must be $3$.
To claim that $3$ is a solution, each step must be reversible, which $\iff$ says, or you substitute: $2 \cdot 3 + 1 = 7$.

### History

Robert Recorde introduced the sign $=$ in The Whetstone of Witte in 1557, as two parallel lines of one length, because no two things can be more equal.
Carl Friedrich Gauss introduced $\equiv$ for congruence in his Disquisitiones Arithmeticae of 1801.
Paul Bachmann introduced the symbol $O$ in 1894, and Edmund Landau spread it and added the little $o$ in 1909.
Donald Knuth called statements such as $f = O(g)$ "one-way equalities".

### Try it

First, choose the sign to put between $g(t)$ and $3t^2 + 1$ in a definition of $g$, and the sign to put between $g(2)$ and $13$.
The first is $g(t) := 3t^2 + 1$, and the second is the claim $g(2) = 3 \cdot 4 + 1 = 13$.

Second, is $2^{10} \equiv 2^{0} \pmod{11}$, given that $10 \equiv 0 \pmod{10}$?
Yes, $2^{10} = 1024 = 93 \cdot 11 + 1$, so $2^{10} \equiv 1 = 2^0$; this follows from Fermat's little theorem, not from substituting congruent exponents.

## Explanations

### L1 human

The sign $=$ says "these two things are the same number".
For example, $3 + 4 = 7$, because both sides are seven.
The sign $\approx$ says "these are close, but not the same", as in $\pi \approx 3.14$.
The sign $:=$ says "from now on, this letter means that", as in $a := 5$.
Each sign makes a different claim, so we pick the sign that says exactly what we mean.

### L2 human

Here is a short computation in which each line needs a different sign.
Define $f(x) := x^2 - 4x + 5$, which is a definition and so uses $:=$.
Then $f(x) = (x - 2)^2 + 1$ for every $x$, an identity that the expansion above checks.
So $f(x) \ge 1$ for every $x$, with $f(2) = 1$, and these are exact claims.
At $x = \sqrt{5}$ the value is exact too, but its decimal form is rounded:
$$f(\sqrt{5}) = 5 - 4\sqrt{5} + 5 = 10 - 4\sqrt{5} \approx 1.0557.$$
For large $x$ the function behaves like $x^2$:
$$\frac{f(x)}{x^2} = 1 - \frac{4}{x} + \frac{5}{x^2} \to 1, \qquad \text{so } f(x) \sim x^2.$$
Check: $4\sqrt{5} \approx 8.9443$, and $10 - 8.9443 = 1.0557$.
The signs keep exact steps, rounded steps and limits apart, so a reader knows how far to trust each line.
Watch out: $f(x) \sim x^2$ does not mean that $f(x) - x^2$ is small, since $f(x) - x^2 = -4x + 5$ grows without bound.

### L3 human

In first-order logic, $a = b$ is the identity relation, governed by reflexivity and the substitution rule of the equality axioms.
The other signs name relations defined inside a theory: $a \equiv b \pmod n$ abbreviates $n \mid a - b$, and $A \cong B$ abbreviates the existence of an isomorphism.
The sign $:=$ belongs to the metalanguage, because it extends the language by a new symbol, and such an extension proves no new facts about the old symbols.
In Lean the distinction is explicit: `def` with `:=` introduces a definition, `=` is propositional equality, and definitional equality is a third notion that the type checker decides.
Mathlib writes big O as `f =O[l] g`, with the filter `l` stated, which removes the one-way equals sign.
In homotopy type theory the univalence axiom identifies equivalence of types with equality of types, so the gap between $\simeq$ and $=$ closes there.
