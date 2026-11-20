---
tag: KFJ7M9FRXV
kind: example
name: A family that is independent over R and dependent over F_2
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [0CRMGPAH83]
uses: [0EVHJFTG9Z, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_independence
    locator: Definition
---

## Example

Let $v_1 = (1, 0, 1)$, $v_2 = (0, 1, 1)$ and $v_3 = (1, 1, 0)$.
The entries are $0$ and $1$, so these vectors lie in $\R^3$ and also in $\mathbb{F}_2^3$.

Over $\R$, the family is [[linearly independent|0EVHJFTG9Z]].

1. Assume $a v_1 + b v_2 + c v_3 = (a + c, b + c, a + b) = (0, 0, 0)$.
2. The first two entries give $a = -c$ and $b = -c$.
3. The third entry gives $a + b = -2c = 0$, so $c = 0$, because $2 \ne 0$ in $\R$.
4. Then $a = b = 0$.

Over $\mathbb{F}_2$, the family is linearly dependent.

5. Compute $v_1 + v_2 + v_3 = (2, 2, 2)$.
6. In $\mathbb{F}_2$, $2 = 0$, so $v_1 + v_2 + v_3 = (0, 0, 0)$.
7. The coefficients $1, 1, 1$ are not all $0$, so this is a nontrivial relation.

## Remarks

The [[determinant|0C3CFHDN6R]] of the matrix with columns $v_1, v_2, v_3$ is $1 \cdot (0 - 1) - 0 + 1 \cdot (0 - 1) = -2$.
This is nonzero in $\R$ and in each field of characteristic other than $2$, and it is $0$ in $\mathbb{F}_2$.
So the family is independent over a field $F$ exactly when the characteristic of $F$ is not $2$.
Independence is a property of the family together with the field of scalars.

## Explanations

### L1 human

The same three lists of numbers can be independent or not, depending on which numbers we may use as coefficients.
In $\mathbb{F}_2$, we have $1 + 1 = 0$, and this creates a new relation.

### L2 human

Step 3 is where the field enters: we divide $-2c = 0$ by $-2$.
In $\mathbb{F}_2$, this division is not possible, and $c = 1$ also solves $-2c = 0$.
