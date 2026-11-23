---
tag: CG8FE46WJC
kind: example
name: Standard first-order languages
msc: ["03C07", "03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [WDVVEYD6AT]
uses: [WDVVEYD6AT, DKFGQTRYZE, 92SWXST1ZM, G5S1M9, 0B1261B5ED, 04C5ZBG1WT, 0FRXBVVR03, 00C0BR7D7H, 0HE5WDQ9FJ, 0QFT7Z76N5, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Signature_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Syntax
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Example

Each part of algebra and logic has its own small first-order language, and a few of them come up again and again.
Below are the standard [[signatures|WDVVEYD6AT]], each with its arities and one typical axiom.
For each one we check that every symbol has one arity and that the axiom is a [[sentence|DKFGQTRYZE]] over that signature.

1. Pure equality: the empty signature.
   A typical axiom is $\exists x \, \exists y \, \neg (x = y)$, "there are at least two elements", and it uses only variables and the logical symbol $=$.
2. Orders: $\{ < \}$, one binary relation symbol.
   [[Total orders|0FRXBVVR03]] satisfy $\forall x \, \forall y \, (x < y \lor x = y \lor y < x)$, where each atomic part applies $<$ or $=$ to two variables.
3. Graphs: $\{ E \}$, one binary relation symbol for adjacency.
   A [[graph|00C0BR7D7H]] satisfies $\forall x \, \neg E(x, x)$ and $\forall x \, \forall y \, (E(x, y) \to E(y, x))$.
4. Groups: $\{ \cdot, {}^{-1}, e \}$ with arities $2, 1, 0$.
   The inverse axiom of [[groups|G5S1M9]] is $\forall x \, (x \cdot x^{-1} = e \land x^{-1} \cdot x = e)$, where $x^{-1}$ is the usual way to write the term ${}^{-1}(x)$.
5. Rings: $\{ +, -, \cdot, 0, 1 \}$ with arities $2, 1, 2, 0, 0$.
   A [[ring|0B1261B5ED]] satisfies the distributive law $\forall x \, \forall y \, \forall z \, (x \cdot (y + z) = x \cdot y + x \cdot z)$.
6. Fields: the ring signature again, with no symbol for division.
   The axiom $\forall x \, (\neg (x = 0) \to \exists y \, (x \cdot y = 1))$ of [[fields|04C5ZBG1WT]] needs no new symbol, and ordered fields add $<$.
7. Arithmetic: $\{ 0, S, +, \cdot \}$ with arities $0, 1, 2, 2$, and some books add a binary relation symbol $<$.
   The [[Peano axioms|0QFT7Z76N5]] include $\forall x \, \neg (S(x) = 0)$.
8. Set theory: $\{ \in \}$, one binary relation symbol.
   The axiom of extensionality of [[ZF|0HE5WDQ9FJ]] is $\forall x \, \forall y \, (\forall z \, (z \in x \leftrightarrow z \in y) \to x = y)$.
9. Vector spaces over a fixed field $K$: $\{ +, -, 0 \}$ and one unary symbol $\lambda_k$ for each $k \in K$, read as "multiply by $k$".
   A [[vector space|000AYPA9AJ]] satisfies $\forall x \, \forall y \, (\lambda_k(x + y) = \lambda_k(x) + \lambda_k(y))$, one axiom for each $k$.

In each item every symbol has one arity, and each axiom has no free variables, so each is a sentence over its signature.

## Remarks

### Counting elements with equality alone

The empty signature can still count.
"There are at least $3$ elements" is the sentence
$$\lambda_{\ge 3} = \exists x \, \exists y \, \exists z \, \big(\neg (x = y) \land \neg (x = z) \land \neg (y = z)\big).$$
Check: the formula asks for three elements that differ in pairs, and three elements have $\binom{3}{2} = 3$ pairs, so there are three inequations.
In general $\lambda_{\ge n}$ uses $n$ quantifiers and $\binom{n}{2}$ inequations, and "at most $n$" is $\neg \lambda_{\ge n+1}$.
The infinite set $\{ \lambda_{\ge n} : n \ge 1 \}$ has exactly the infinite structures as models, so "infinite" is expressed by a set of sentences, though by no single one.

### How the choices matter

The signature changes the substructures: with the symbols of item 4, every substructure of a group is a subgroup, as [[groups in two signatures|CBKC2DMXEQ]] shows.
Item 9 has one symbol for each scalar, so for $K = \mathbb{R}$ the signature is uncountable; [[many-sorted logic|7TDHDN8P96]] can treat the scalars as a second sort instead.
Items 2, 3 and 8 are relational: they have no function symbols, so their only terms are variables.
A set of axioms over one of these signatures is a [[first-order theory|92SWXST1ZM]], such as the theory of groups or Peano arithmetic.

## Explanations

### L1 human

Each area of mathematics has its own small list of symbols.
Group theory uses multiplication, inverse and the identity.
Ring theory uses addition, negation, multiplication, $0$ and $1$.
Set theory uses only the membership symbol $\in$.
With these lists fixed, the axioms of each area can be written as first-order sentences.

### L2 human

We check one entry in detail, the field axiom of item 6.
The symbols $\cdot$, $0$ and $1$ are in the ring signature, with arities $2$, $0$ and $0$.
So $x$, $0$, $x \cdot y$ and $1$ are terms, and $x = 0$ and $x \cdot y = 1$ are atomic formulas.
The quantifier $\exists y$ binds $y$, and $\forall x$ binds $x$, so no variable is free and the axiom is a sentence.
The axiom is not universal, so a substructure of a field need not be a field.
For instance, $\mathbb{Z}$ is a substructure of $\mathbb{Q}$ in the ring signature, but $2$ has no inverse in $\mathbb{Z}$.
The typical use of the list is as a reference when an exercise says "in the language of rings" or "in the language of arithmetic".
Watch out: "the language of fields" has no symbol for division, because $x / 0$ has no value and every function symbol must name a total function.
