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

Let $\sigma = \{ < \}$ be the signature of orders, with one binary relation symbol.
We show that the string
$$\varphi = \forall x \, \exists y \, (x < y \land \neg y = x)$$
is a [[well-formed formula|HYJ10AF6RT]] over $\sigma$.
A formation sequence is a finite list of strings in which each entry is atomic or comes from earlier entries by one clause of the [[definition|2CHENV4DCC]].
Here is one that ends with $\varphi$.

1. $\varphi_1 = x < y$ is an [[atomic formula|MCZRXR3SVB]] by clause 2, because $<$ has arity $2$ and $x$, $y$ are terms.
2. $\varphi_2 = y = x$ is an atomic formula by clause 1.
3. $\varphi_3 = \neg y = x$ comes from $\varphi_2$ by clause 3.
4. $\varphi_4 = (x < y \land \neg y = x)$ comes from $\varphi_1$ and $\varphi_3$ by clause 4.
5. $\varphi_5 = \exists y \, (x < y \land \neg y = x)$ comes from $\varphi_4$ by clause 5 with the variable $y$.
6. $\varphi_6 = \forall x \, \exists y \, (x < y \land \neg y = x)$ comes from $\varphi_5$ by clause 5 with the variable $x$.

The last entry is $\varphi$, so $\varphi$ is a formula.
The complexities of the six entries are $0, 0, 1, 2, 3, 4$, since each step after the atomic ones adds one connective or one quantifier.

## Remarks

A formation sequence is not unique.
We can list $\varphi_2$ before $\varphi_1$, or insert extra formulas that we never use.
What is unique is the set of subformulas $\{ \varphi_1, \ldots, \varphi_6 \}$, because each formula has only one reading by the [[unique readability theorem|3QPV4XW8MC]].

Reading the sequence backward is a parsing algorithm.
The first symbol of $\varphi$ is $\forall$, so the last step was clause 5 with $x$, and the rest is $\varphi_5$.
In the same way $\varphi_5$ came from $\varphi_4$ by clause 5 with $y$.
The string $\varphi_4$ starts with a bracket, so it came from clause 4, and the connective that splits it is the $\land$ at bracket depth $1$.
Watch out: you must split at the connective of depth $1$, not at the first connective you meet.

If we change $\land$ to $\to$, the same sequence works with clause 4 for $\to$.
If we drop the brackets in step 4, clause 4 no longer produces the string, because clause 4 itself adds the brackets.
In ordinary text we still drop brackets when the binding order makes the reading clear.

In the natural numbers with the usual order, $\varphi$ is true, because $y = x + 1$ satisfies $x < y$ and $y \neq x$.
In the order $\{ 0, 1, 2 \}$ it is false, because no $y$ satisfies $2 < y$.

## Explanations

### L1 human

We build the formula like a tower, one block at a time.
First come the two simple claims "$x$ is less than $y$" and "$y$ equals $x$".
Then we add "not", then "and", then "there is a $y$", and last "for every $x$".
Each new block rests only on blocks already built.
The finished tower says that every element has some different element above it.

### L2 human

The formation sequence is also a way to compute by recursion.
Let $c(\psi)$ be the number of quantifiers in $\psi$.
Atomic entries get $c = 0$, so $c(\varphi_1) = c(\varphi_2) = 0$.
Negation and conjunction add no quantifier, so $c(\varphi_3) = 0$ and $c(\varphi_4) = 0 + 0 = 0$.
Each quantifier step adds $1$, so $c(\varphi_5) = 1$ and $c(\varphi_6) = 2$.
Check: $\varphi$ contains exactly the two quantifiers $\forall x$ and $\exists y$.
