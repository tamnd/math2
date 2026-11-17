---
tag: PSACC4KCBN
kind: example
name: Kleene's quantifier gives arithmetical comprehension
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: research
instance_of: [NPDRXTBW5W]
uses: [NPDRXTBW5W, NAASTN80QN, XQENB067R3, CV2E6JZHVP, 330YAP9Y4Q]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Use of higher-order arithmetic
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
    locator: lead section
---

## Example

We show that $\mathsf{RCA}_0^\omega + (\exists^2)$ proves arithmetical comprehension, the axiom scheme of [[ACA0|NAASTN80QN]].
In $\mathsf{RCA}_0^\omega$ a set $X$ is a function of type $1$ with values in $\set{0, 1}$, and $n \in X$ means $X(n) = 1$.
We use a property of the base system, built on [[primitive recursive arithmetic|330YAP9Y4Q]] in all finite types: every quantifier-free formula $A(\vec{v})$ is provably equivalent to $t(\vec{v}) = 0$ for some term $t$ with the same free variables.
We fix $\varphi$ with $\varphi(g) = 0 \leftrightarrow \exists m\, g(m) = 0$ for all $g$ of type $1$.
Write $1 \mathbin{\dot-} k$ for the term that is $1$ when $k = 0$ and $0$ otherwise.

1. Claim: for every [[arithmetical|CV2E6JZHVP]] formula $A(\vec{v})$, with number variables and set parameters, there is a term $t$ that may use $\varphi$ such that $A(\vec{v}) \leftrightarrow t(\vec{v}) = 0$. We prove it by induction on the construction of $A$, outside the system: for each $A$ we give $t$ and a proof.
2. If $A$ is quantifier-free, the property of the base system gives $t$.
3. If $A \leftrightarrow t = 0$, then $\neg A \leftrightarrow (1 \mathbin{\dot-} t) = 0$.
4. If $A \leftrightarrow t = 0$ and $B \leftrightarrow s = 0$, then $A \wedge B \leftrightarrow t + s = 0$, since a sum of two natural numbers is $0$ only when both are $0$.
5. Let $A(\vec{v}) = \exists m\, B(\vec{v}, m)$ with $B(\vec{v}, m) \leftrightarrow s(\vec{v}, m) = 0$. Then $A(\vec{v}) \leftrightarrow \exists m\, (\lambda m.\, s(\vec{v}, m))(m) = 0 \leftrightarrow \varphi(\lambda m.\, s(\vec{v}, m)) = 0$. So $t(\vec{v}) = \varphi(\lambda m.\, s(\vec{v}, m))$ works.
6. A universal quantifier $\forall m\, B$ is $\neg \exists m\, \neg B$, so it is handled by steps 3 and 5. The other connectives are built from $\neg$ and $\wedge$. This proves the claim.
7. Now let $A(n)$ be arithmetical, with $n$ a number variable and possibly other parameters, and take $t$ from the claim.
8. Put $X = \lambda n.\, (1 \mathbin{\dot-} t(n))$. The base system has $\lambda$-abstraction, so $X$ is an object of type $1$.
9. $X(n) \in \set{0, 1}$, and $X(n) = 1 \leftrightarrow t(n) = 0 \leftrightarrow A(n)$. So $X = \set{n : A(n)}$.
10. This is the instance of arithmetical comprehension for $A$. So every axiom of $\mathsf{ACA}_0$ holds in $\mathsf{RCA}_0^\omega + (\exists^2)$.

## Remarks

The converse fails in the higher-order setting: $\mathsf{RCA}_0^\omega$ together with the scheme of arithmetical comprehension does not prove $(\exists^2)$.
The reason is that the model of the continuous functionals contains all functions $\N \to \N$, so it satisfies the scheme, but it contains no discontinuous functional.
For sentences of second-order arithmetic the two systems agree, since $\mathsf{RCA}_0^\omega + (\exists^2)$ is conservative over $\mathsf{ACA}_0$.
Step 5 is the only step that uses $\varphi$, and it removes one number quantifier at a time.

## Explanations

### L1 human

Arithmetical comprehension says: for any property of numbers that can be written with "for all numbers" and "there is a number", the set of numbers with the property exists.
Kleene's quantifier is a single machine that answers every question of the form "is there a number $m$ with $g(m) = 0$".
Each "there is a number" in a property becomes one call to the machine.
After all quantifiers are replaced, the property becomes a computation, and its set exists.

### L2 human

Take the property $A(n)$: "$n$ is in the range of $f$", that is $\exists m\, f(m) = n$, for a fixed one-to-one function $f$.

1. The inner formula $f(m) = n$ is equivalent to $s(n, m) = 0$ with $s(n, m) = \abs{f(m) - n}$, a primitive recursive term.
2. Step 5 gives $t(n) = \varphi(\lambda m.\, \abs{f(m) - n})$.
3. Step 8 gives the range as $X = \lambda n.\, (1 \mathbin{\dot-} \varphi(\lambda m.\, \abs{f(m) - n}))$.

Over $\mathsf{RCA}_0$, the existence of ranges of one-to-one functions already gives $\mathsf{ACA}_0$, so these instances, one for each one-to-one $f$, carry the whole axiom.
The typical use: this argument shows that $(\exists^2)$ is at least as strong as $\mathsf{ACA}_0$ whenever a higher-order theorem gives $(\exists^2)$.
The trap: step 1 is an induction in the metatheory, so the result is a scheme with one proof for each formula, not a single theorem about all formulas.

### L3 human

The term $t$ in the claim has nested calls to $\varphi$, one for each quantifier of $A$.
In this sense $\exists^2$ is a uniform version of the Turing jump: it computes the jump of any function in one step.
The same scheme, with the Suslin functional in place of $\varphi$, gives $\Pi^1_1$ comprehension, and the functionals of $\mathsf{Z}_2^\omega$ continue the pattern up the analytical hierarchy.
