---
tag: 1ZK55FS2BF
kind: statement
role: proposition
name: Invertibility and the reduced row echelon form
msc: [15A09]
uses: [0EB9N0S33C, 0WF5AQYTW6, 0T6MWGZSXA, 098D6FQN3N]
about: [0EB9N0S33C, 0WF5AQYTW6]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-1.xml#L551
    locator: src/section3-1.xml:551
---

## Statement

Let $A$ be a square matrix.
Then $A$ is [[invertible|0EB9N0S33C]] if and only if its [[reduced row echelon form|0WF5AQYTW6]] is the identity matrix $I$, that is, $A \sim I$.

Moreover, when $A$ is invertible, row reduction finds the inverse.
Form the [[augmented matrix|0T6MWGZSXA]] $[A \mid I]$ and apply [[Gauss–Jordan elimination|098D6FQN3N]].
The result is
$$[A \mid I] \sim [I \mid A^{-1}].$$

## Remarks

Each row operation is left multiplication by an invertible matrix.
So reducing $A$ to $I$ gives a product $E$ of such matrices with $EA = I$.
Applying the same operations to $I$ gives $EI = E = A^{-1}$.
