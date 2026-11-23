---
tag: PDNHFSACCV
kind: example
name: "A routine check that fails: singular matrices do not form a subspace"
msc: ["00A35", "15A03"]
topics: [STSM6PR7TX]
audience: ug2
not_instance_of:
  - target: VYGBV5D8Y4
    note: the step left to the reader as routine is false, so the omission is a gap and not an acceptable omission
uses: [VYGBV5D8Y4, 00YC1D652K, 00KDZRW4C0, Y0HXCJRB9B]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_subspace
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof terminology
---

## Example

The claim is that the set $S$ of real $2 \times 2$ matrices with [[determinant|00KDZRW4C0]] $0$ is a [[linear subspace|00YC1D652K]] of the space $M_2(\mathbb{R})$ of all real $2 \times 2$ matrices.
A text offers this proof, which is a flawed example.

> The zero matrix has determinant $0$, so $S$ is not empty.
> The closure of $S$ under addition and under multiplication by scalars is a routine check, which we leave to the reader.
> $\square$

A subspace must contain the zero matrix and be closed under addition and under multiplication by scalars, so we do the routine check.
The zero matrix has determinant $0 \cdot 0 - 0 \cdot 0 = 0$, so the first condition holds.
For $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ and a real $t$, we get $\det(tA) = (ta)(td) - (tb)(tc) = t^2 \det A$, so closure under scalars holds.

Closure under addition fails.
Take
$$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.$$
Both have determinant $0$, so $A, B \in S$.
But $A + B$ is the identity matrix, with determinant $1$, so $A + B \notin S$.
The claim is false, and the step the text called routine is exactly the false step.

## Remarks

This is the most dangerous kind of gap in the [[level of detail|VYGBV5D8Y4]] of a proof: the omitted step is false.
A reader who trusts the word "routine" accepts a false theorem.

The two closure conditions look alike but behave differently.
The determinant is homogeneous of degree $2$, which gives closure under scalars, and it is not additive, which breaks closure under sums.
Writing the step out exposes this at once, since $\det(A + B)$ has no formula in terms of $\det A$ and $\det B$ alone.

With the trace in place of the determinant the claim is true and the check really is routine.
The trace satisfies $\operatorname{tr}(A + B) = \operatorname{tr} A + \operatorname{tr} B$ and $\operatorname{tr}(tA) = t \operatorname{tr} A$, so the matrices of trace $0$ form a subspace.
The words "routine" and "left to the reader" work like [[trivial, obvious and clearly|Y0HXCJRB9B]]: they claim that a step is easy without showing it.

## Explanations

### L1 human

A text says "this part is routine, check it yourself", and many readers skip it.
Here the skipped part is false.
Two special tables of numbers each have a certain value equal to $0$, but their sum has value $1$.
So the claim breaks exactly at the step that the text did not write.
This is why a writer should leave out only steps that the writer has checked.

### L2 human

We repeat the test with a second pair of matrices, to see that the failure is not an accident.
The matrix $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ has $\det A = 1 - 1 = 0$, and $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ has $\det B = 0$.
Their sum $A + B = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ has $\det(A + B) = 2 - 1 = 1$.
Again $A, B \in S$ and $A + B \notin S$.

Before omitting a routine step, try it on the simplest objects.
Watch out: checking only closure under scalars, which holds, and calling closure under addition "similar" is how the false claim gets through.
