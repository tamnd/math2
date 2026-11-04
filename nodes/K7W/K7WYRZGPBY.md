---
tag: K7WYRZGPBY
kind: statement
role: proposition
name: Linear combinations and consistency of a linear system
msc: [15A06]
uses: [0V8F3E48E6, 0T6MWGZSXA, 0X6V9B1V10, 0GT4WWGWH2]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-1.xml#L920
    locator: src/section2-1.xml:920
---

## Statement

Let $\mathbf v_1, \dots, \mathbf v_n$ and $\mathbf b$ be vectors in $\mathbb R^m$.
Form the [[augmented matrix|0T6MWGZSXA]] whose columns are $\mathbf v_1, \dots, \mathbf v_n$ followed by $\mathbf b$.
Then $\mathbf b$ is a [[linear combination|0V8F3E48E6]] of $\mathbf v_1, \dots, \mathbf v_n$ if and only if the [[linear system|0GT4WWGWH2]] with this augmented matrix is [[consistent|0X6V9B1V10]].

Moreover, each solution $(c_1, \dots, c_n)$ of the system gives weights with $c_1\mathbf v_1 + \dots + c_n\mathbf v_n = \mathbf b$.

## Remarks

The unknowns of the system are the weights $c_1, \dots, c_n$.
Each row of the system is one coordinate of the vector equation $c_1\mathbf v_1 + \dots + c_n\mathbf v_n = \mathbf b$.
