---
tag: 8BMQTZZEWB
kind: example
name: Drinker paradox
aliases: [drinker-principle, drinking-principle]
msc: ["03B10", "03B20"]
topics: [NJDME6F845]
audience: ug2
instance_of: [5SDS9T8E7J]
uses: [5SDS9T8E7J, 1WTCZB4DVB, 0WCP0PVET6, YXYF6JQXBT, Q11N8X99FK, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Drinker_paradox
    locator: lead section
---

## Example

Let $D$ be a unary relation symbol, read "$x$ drinks".
The drinker principle is the sentence
$$\delta = \exists x \, (D(x) \to \forall y \, D(y)).$$
It says: in every pub with at least one person, there is someone such that, if that person drinks, then everyone drinks.
We show that $\delta$ is [[valid|5SDS9T8E7J]], by [[proof by cases|0WCP0PVET6]].

1. Let $\mathcal{M}$ be any structure for $D$. Its domain $M$ is nonempty, by the convention for structures.
2. Case 1: $\mathcal{M} \models \forall y \, D(y)$. Take any $a \in M$; it exists because $M$ is nonempty.
3. Then $D(a) \to \forall y \, D(y)$ holds in $\mathcal{M}$, because its consequent is true. So $a$ witnesses $\delta$.
4. Case 2: $\mathcal{M} \not\models \forall y \, D(y)$. Then some $a \in M$ has $a \notin D^{\mathcal{M}}$.
5. Then $D(a) \to \forall y \, D(y)$ holds in $\mathcal{M}$, because its antecedent is false. So $a$ witnesses $\delta$.
6. In both cases, $\mathcal{M} \models \delta$ by the clause for $\exists$ in [[satisfaction|1WTCZB4DVB]]. So $\delta$ is valid.

## Remarks

The sentence sounds false because "if that person drinks, then everyone drinks" suggests a cause.
In first-order logic, $\to$ is material implication, and the witness depends on the whole structure, not on a cause.

The principle needs a nonempty domain.
In the empty structure, allowed in [[inclusive first-order logic|YXYF6JQXBT]], every existential sentence is false, so $\delta$ fails.

The principle is not valid in [[intuitionistic logic|Q11N8X99FK]].
The proof above decides whether everyone drinks, and that step uses the law of excluded middle.
A [[Kripke countermodel|NGHWZ9Y7ZV]] has two worlds $w_0 \leq w_1$, with domains $\set{a} \subseteq \set{a, b}$.
In it, $D(a)$ is forced at both worlds, and $D(b)$ is never forced.

1. At $w_0$, the only candidate witness is $a$.
2. $D(a)$ is forced at $w_0$, but $\forall y \, D(y)$ is not, because of $b$ at $w_1$.
3. So $D(a) \to \forall y \, D(y)$ is not forced at $w_0$, and $\delta$ is not forced at $w_0$.

Raymond Smullyan made the principle popular in his puzzle book of 1978, "What Is the Name of This Book?".
The dual form $\exists x \, (\exists y \, D(y) \to D(x))$ is also valid, by the same case analysis.

## Explanations

### L1 human

Either everyone in the pub drinks, or someone does not.
If everyone drinks, pick anybody: "if this person drinks, everyone drinks" is true, because everyone drinks.
If someone does not drink, pick that person: the "if" part is false, so the whole "if, then" statement is true.

### L2 human

We find the witness in two small structures with domain $\set{1, 2, 3}$.

1. $D^{\mathcal{M}} = \set{1, 2, 3}$: everyone drinks, so every element is a witness.
2. $D^{\mathcal{M}} = \set{1, 2}$: the element $3$ does not drink, so $3$ is a witness. The elements $1$ and $2$ are not witnesses, because $D(1)$ holds and $\forall y \, D(y)$ fails.

The typical use is to show that a valid sentence can sound false in everyday language.
A trap is to look for a fixed witness that works in every structure; the witness depends on the structure.

### L3 human

The principle is a standard test for automated and interactive provers, because its classical proof needs case analysis and a witness that depends on the case.
The classical proof gives no method to find the witness: to decide which case holds, one must inspect the whole domain.
For a decidable predicate $D$ on $\N$, given by a program, no algorithm finds a witness from the program in all cases.
This matches the intuitionistic failure of $\delta$.
