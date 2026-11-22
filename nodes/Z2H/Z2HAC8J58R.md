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

1. `NTS` means "need to show".
   We write: `NTS` $(a + b)^2 - (a - b)^2 = 4ab$ for all [[real numbers|08J2M1JYAG]] $a$ and $b$.
2. `LHS` means "left-hand side", and here the `LHS` is $(a + b)^2 - (a - b)^2$.
3. `RHS` means "right-hand side", and here the `RHS` is $4ab$.
4. Expand the first square:
   $$(a + b)^2 = a^2 + 2ab + b^2.$$
5. Expand the second square:
   $$(a - b)^2 = a^2 - 2ab + b^2.$$
6. Subtract, and the squares cancel:
   $$\text{LHS} = (a^2 + 2ab + b^2) - (a^2 - 2ab + b^2) = 4ab = \text{RHS}.$$
7. So the `LHS` equals the `RHS` for all $a$ and $b$, which is what we needed to show.

Check: for $a = 3$ and $b = 1$, the `LHS` is $16 - 4 = 12$ and the `RHS` is $4 \cdot 3 \cdot 1 = 12$.

## Remarks

The proof follows the usual pattern for an identity: start from one side, change it step by step, and arrive at the other side.
The names `LHS` and `RHS` let each step say which side it changes, and `NTS` puts the goal in writing before the work starts.

The same proof works in every commutative ring, because steps 4 to 6 use only the laws of a commutative ring.
It fails when $ab \neq ba$.
Then step 4 gives $(a + b)^2 = a^2 + ab + ba + b^2$, the `LHS` becomes $2ab + 2ba$, and this need not equal $4ab$.
For the matrices $a = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $b = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ we get $ab = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $ba = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, so $2ab + 2ba = 2I$ while $4ab \neq 2I$.

## Explanations

### L1 human

In an equation, the part before the equals sign is the left-hand side, written `LHS`, and the part after it is the right-hand side, written `RHS`.
To check an equation, you work on one side until it looks like the other side.
For $a = 3$ and $b = 1$, the left side is $4^2 - 2^2 = 16 - 4 = 12$, and the right side is $4 \cdot 3 \cdot 1 = 12$.
Both sides agree, as the general proof says they must.

### L2 human

Use the same pattern for $(a + b)(a - b) = a^2 - b^2$.
Write the goal first: `NTS` $(a + b)(a - b) = a^2 - b^2$ for all real $a$ and $b$.
Then expand the `LHS`:
$$(a + b)(a - b) = a^2 - ab + ba - b^2.$$
For real numbers $ab = ba$, so the middle terms cancel and the `LHS` equals $a^2 - b^2$, the `RHS`.
Watch out: a proof must not start from the identity it wants and change both sides until it reaches $0 = 0$.
That argument shows only that the identity implies $0 = 0$, which is the wrong direction.
It becomes a proof only if every step can be reversed, and then it is clearer to write the steps from one side to the other.
