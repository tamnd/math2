---
tag: E7SAHXQEVC
kind: statement
role: proposition
name: Matrix equation, linear combination of columns and linear system
msc: [15A06]
uses: [0PDVQEP0ZC, 0V8F3E48E6, 0T6MWGZSXA, 0GT4WWGWH2]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-2.xml#L901
    locator: src/section2-2.xml:901
---

## Statement

Let $A$ be an $m \times n$ matrix with columns $v_1, \dots, v_n$. Let $x = (x_1, \dots, x_n)^T$ be a column vector with $n$ entries, and let $b$ be a column vector with $m$ entries.

Then the following three statements are equivalent.

1. The vector $x$ satisfies the equation $Ax = b$, using the [[matrix-vector product|0PDVQEP0ZC]].
2. The vector $b$ is the [[linear combination|0V8F3E48E6]] $x_1 v_1 + \dots + x_n v_n$ of the columns of $A$, with the entries of $x$ as weights.
3. The entries $x_1, \dots, x_n$ form a solution of the [[linear system|0GT4WWGWH2]] whose [[augmented matrix|0T6MWGZSXA]] is $[v_1 \; \dots \; v_n \mid b]$.

## Remarks

The product $Ax$ is defined as the combination of the columns of $A$ weighted by the entries of $x$. This gives the link between the first two statements. The third statement reads the same equation one row at a time.
