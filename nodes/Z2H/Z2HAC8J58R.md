---
tag: Z2HAC8J58R
kind: example
name: The abbreviations LHS, RHS and NTS in the proof of an identity
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
instance_of: [4ZNYMYRRY3]
uses: [4ZNYMYRRY3, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_mathematical_abbreviations
    locator: lead section
---

## Example

We prove the identity
$$(a + b)^2 - (a - b)^2 = 4ab \quad \text{for all } a, b \in \mathbb{R},$$
and we write the proof with the [[abbreviations|4ZNYMYRRY3]] `NTS`, `LHS` and `RHS`.

1. `NTS` means "need to show". We write: `NTS` $(a + b)^2 - (a - b)^2 = 4ab$ for all [[real numbers|08J2M1JYAG]] $a$ and $b$.
2. `LHS` means "left-hand side". Here the `LHS` is $(a + b)^2 - (a - b)^2$.
3. `RHS` means "right-hand side". Here the `RHS` is $4ab$.
4. We expand the first square: $(a + b)^2 = a^2 + 2ab + b^2$.
5. We expand the second square: $(a - b)^2 = a^2 - 2ab + b^2$.
6. We subtract: the `LHS` equals $(a^2 + 2ab + b^2) - (a^2 - 2ab + b^2) = 4ab$.
7. So the `LHS` equals the `RHS` for all $a$ and $b$, which is what we needed to show.

A check with numbers: for $a = 3$ and $b = 1$, the `LHS` is $16 - 4 = 12$ and the `RHS` is $4 \cdot 3 \cdot 1 = 12$.

## Remarks

The example shows the usual pattern for an identity: start from one side, transform it step by step, and reach the other side.
The words `LHS` and `RHS` name the two sides, so each step can say which side it changes.
The pattern does not change when we replace $\mathbb{R}$ by any commutative ring, because steps 4 to 6 use only the laws of a commutative ring.
In a ring where $ab \neq ba$, step 4 gives $a^2 + ab + ba + b^2$, and the `LHS` becomes $2ab + 2ba$, which need not equal $4ab$.

## Explanations

### L1 human

In an equation, the part before the equals sign is the left-hand side, written `LHS`, and the part after it is the right-hand side, written `RHS`.
To check an equation, we work on one side until it looks like the other side.
For $a = 3$ and $b = 1$, the left side is $4^2 - 2^2 = 16 - 4 = 12$, and the right side is $4 \cdot 3 \cdot 1 = 12$.
Both sides agree, as the general proof says they must.

### L2 human

We use the same pattern for $(a + b)(a - b) = a^2 - b^2$.

1. `NTS`: $(a + b)(a - b) = a^2 - b^2$ for all real $a$ and $b$.
2. Expand the `LHS`: $(a + b)(a - b) = a^2 - ab + ba - b^2$.
3. Since $ab = ba$ for real numbers, the middle terms cancel, and the `LHS` equals $a^2 - b^2$, which is the `RHS`.

The typical use of `LHS` and `RHS` is in a chain of equalities, where each line changes one side.
A trap: a proof must not start from the identity to be proved and work on both sides at once until it reaches a true statement such as $0 = 0$.
That argument proves the converse direction, and it is valid only when every step can be reversed.
