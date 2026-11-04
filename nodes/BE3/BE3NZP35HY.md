---
tag: BE3NZP35HY
kind: statement
role: proposition
name: Augmentation principle for reduced row echelon form
msc: [15A06]
uses: [0WF5AQYTW6, 0T6MWGZSXA]
about: [0WF5AQYTW6]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-3.xml#L683
    locator: src/section1-3.xml:683
---

## Statement

Let $A$ be a matrix. Say that a matrix $B$ is an augmentation of $A$ when $B$ is formed from $A$ by adjoining further columns to the right of $A$, so that the first columns of $B$ are the columns of $A$.

If $B$ is an augmentation of $A$, then the [[reduced row echelon form|0WF5AQYTW6]] of $B$ is an augmentation of the reduced row echelon form of $A$.

In other words, the leftmost columns of the reduced row echelon form of $B$ make up the reduced row echelon form of $A$.

## Remarks

This is why one may row reduce an [[augmented matrix|0T6MWGZSXA]] and read the reduced form of the coefficient matrix from its left part.
Row operations act on each column separately, so the added columns do not change the operations chosen for the first columns.
