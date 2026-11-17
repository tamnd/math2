---
tag: R99VNXVM8P
kind: example
name: A formation sequence for a formula of orders
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [HYJ10AF6RT]
uses: [HYJ10AF6RT, 2CHENV4DCC, MCZRXR3SVB]
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Example

Let $\sigma = \set{<}$ be the signature of orders, with one binary relation symbol.
We show that the string
$$\varphi = \forall x \, \exists y \, (x < y \land \neg y = x)$$
is a [[well-formed formula|HYJ10AF6RT]] over $\sigma$.
We give a formation sequence: a finite list of strings in which each entry is atomic or comes from earlier entries by one clause of the [[definition|2CHENV4DCC]].

1. $\varphi_1 = x < y$. It is an [[atomic formula|MCZRXR3SVB]], by clause 2, because $<$ has arity $2$ and $x$, $y$ are terms.
2. $\varphi_2 = y = x$. It is an atomic formula, by clause 1, because $y$ and $x$ are terms.
3. $\varphi_3 = \neg y = x$. It comes from $\varphi_2$ by clause 3.
4. $\varphi_4 = (x < y \land \neg y = x)$. It comes from $\varphi_1$ and $\varphi_3$ by clause 4.
5. $\varphi_5 = \exists y \, (x < y \land \neg y = x)$. It comes from $\varphi_4$ by clause 5, with the variable $y$.
6. $\varphi_6 = \forall x \, \exists y \, (x < y \land \neg y = x)$. It comes from $\varphi_5$ by clause 5, with the variable $x$.

The last entry is $\varphi$, so $\varphi$ is a formula.
The complexities of the six entries are $0, 0, 1, 2, 3, 4$, because each step after the atomic ones adds one connective or one quantifier.

## Remarks

The formation sequence is not unique.
We can list $\varphi_2$ before $\varphi_1$, or insert extra formulas that we never use.
The set $\set{\varphi_1, \ldots, \varphi_6}$ of subformulas is unique, because each formula has only one reading, by the [[unique readability theorem|3QPV4XW8MC]].
If we change $\land$ to $\to$, the same sequence works with clause 4 for $\to$.
If we drop the brackets in step 4, the string $\exists y \, x < y \land \neg y = x$ is no longer produced by clause 4, because clause 4 adds the brackets.
In the text we still write it without brackets only when the binding order makes the reading clear.

## Explanations

### L1 human

We build the formula like a tower, one block at a time.
First come the two simple claims "$x$ is less than $y$" and "$y$ equals $x$".
Then we add "not", then "and", then "there is a $y$", and last "for every $x$".
Each block uses only blocks that are already built.
The finished tower says: below every element there is no top, because each $x$ has a different $y$ above it.

### L2 human

We read the formula from the outside in, which reverses the formation sequence.

1. The first symbol is $\forall$, so $\varphi$ came from clause 5 with the variable $x$, and the rest is $\varphi_5$.
2. The first symbol of $\varphi_5$ is $\exists$, so $\varphi_5$ came from clause 5 with the variable $y$, and the rest is $\varphi_4$.
3. The string $\varphi_4$ starts with a bracket, so it came from clause 4. The connective $\land$ is the one at bracket depth $1$, and it splits $\varphi_4$ into $\varphi_1$ and $\varphi_3$.
4. The string $\varphi_3$ starts with $\neg$, so it came from clause 3, and the rest $\varphi_2$ is atomic.

The typical use is a parser: this outside-in reading is the algorithm of the unique readability theorem.
The trap is step 3: we must split at the connective of depth $1$, not at the first connective that we see.
