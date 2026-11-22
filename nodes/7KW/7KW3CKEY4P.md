---
tag: 7KW3CKEY4P
kind: example
name: The phrase "let x = 3" does not quantify x
msc: ["97E40"]
topics: [WMY13MXY3W]
audience: school
not_instance_of:
  - target: EGTZPA6QH3
    note: the phrase gives the variable one fixed value, so it does not range over a domain
uses: [EGTZPA6QH3, 0GHS47PDAQ, 0MSRQHCNN9]
sources:
  - url: https://en.wikipedia.org/wiki/Free_variables_and_bound_variables
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
---

## Example

A worked exercise starts: "let $x = 3$; then $x^2 - 9 = 0$".
The same word "let" also starts general arguments, as in "let $x$ be a real number".
We show that "let $x = 3$" is not a [[quantifier|EGTZPA6QH3]].

1. A quantifier says for how many objects of a domain an open sentence is true, so it needs a variable that ranges over a domain.
2. The phrase "let $x = 3$" gives $x$ one value.
   From then on, $x$ is a name for the number $3$.
3. So "let $x = 3$; then $x^2 - 9 = 0$" says the same as "$3^2 - 9 = 0$", a statement about one number.
4. A [[universal quantifier|0GHS47PDAQ]] would claim $x^2 - 9 = 0$ for every $x$ in a domain.
   Over $\mathbb{R}$ that is false, since $x = 0$ gives $-9$.
5. An [[existential quantifier|0MSRQHCNN9]] would claim $x^2 - 9 = 0$ for some $x$, which is true.
   The phrase "let $x = 3$" makes neither claim; it only fixes a value.

## Remarks

The two uses of "let" differ in what follows the variable.
"Let $x$ be a real number" introduces an arbitrary element, and the argument that follows proves a universal statement.
"Let $x = 3$" introduces a specific element, and the argument proves a fact about $3$.

A specific value can still prove an existential statement.
The text "let $x = 3$; then $x^2 = 9$" proves "there is a real $x$ with $x^2 = 9$", and the existential quantifier sits in the claim, not in the word "let".
It cannot prove a universal statement.
A proof that starts with "let $x = 3$" and ends with "so $P(x)$ holds for all $x$" has checked one case.

## Explanations

### L1 human

"Let $x = 3$" means that from now on, $x$ is the number $3$.
So "$x + 1 = 4$" just says "$3 + 1 = 4$".
This is different from "for every number $x$, $x + 0 = x$", which is about all numbers at once.
The first sentence is about one number, and the second is about every number.

### L2 human

Sort three openings of a proof by what they allow the proof to claim.
"Let $n$ be an integer" makes $n$ arbitrary, so a proof of $P(n)$ from here proves "for every integer $n$, $P(n)$".
"Let $n = 7$" makes $n$ a name for one number, so a proof of $P(n)$ proves $P(7)$, and with it "there is an integer $n$ with $P(n)$".
"Let $n$ be an integer with $n^2 = 16$" makes $n$ arbitrary among the solutions $4$ and $-4$, so a proof of $P(n)$ proves "for every integer $n$ with $n^2 = 16$, $P(n)$".

When you check a proof, match its opening line against the quantifier of the claim.
Watch out: in the third opening the condition $n^2 = 16$ looks like a value, but it allows two values, so the opening is universal.
