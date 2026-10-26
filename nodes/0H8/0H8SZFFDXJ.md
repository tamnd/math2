---
tag: 0H8SZFFDXJ
kind: statement
role: proposition
name: Rule of Sarrus
msc: [15A15]
uses: [0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Rule_of_Sarrus
    locator: lead section
same_as:
  wikidata: Q913837
  wikipedia: Rule of Sarrus
---

## Statement

Let $K$ be a commutative ring and let $a, b, c, d, e, f, g, h, i \in K$.
Then
$$\det \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} = aei + bfg + cdh - ceg - bdi - afh,$$
where $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

Copy the first two columns to the right of the matrix.
Then the three positive terms are the products along the diagonals that go down to the right.
The three negative terms are products along the diagonals that go up to the right in the same picture.
This rule is the [[Leibniz formula|016PE4VZ8Q]] for $n = 3$; it has no analogue with diagonals for $n \ge 4$.

## Explanations

### L1 human

The rule of Sarrus is a memory aid for $3 \times 3$ determinants.
Write the first two columns again to the right of the matrix.
Add the three products down to the right, and subtract the three products up to the right.
