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

*Claim.* The set $S$ of real $2 \times 2$ matrices with [[determinant|00KDZRW4C0]] $0$ is a [[linear subspace|00YC1D652K]] of the vector space $M_2(\mathbb{R})$ of all real $2 \times 2$ matrices.

*Text as written.*
The zero matrix has determinant $0$, so $S$ is not empty.
The closure of $S$ under addition and under multiplication by scalars is a routine check, which we leave to the reader.
$\square$

A subspace must contain the zero matrix and be closed under addition and under multiplication by scalars.
We do the routine check.

1. The zero matrix: $\det \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = 0 \cdot 0 - 0 \cdot 0 = 0$. This condition holds.
2. Multiplication by scalars: for $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ and a real $t$, $\det(tA) = (ta)(td) - (tb)(tc) = t^2(ad - bc) = t^2 \det A$. So $\det A = 0$ gives $\det(tA) = 0$. This condition holds.
3. Addition: take $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$. Then $\det A = 1 \cdot 0 - 0 \cdot 0 = 0$ and $\det B = 0 \cdot 1 - 0 \cdot 0 = 0$, so $A, B \in S$.
4. But $A + B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, and $\det(A + B) = 1 \cdot 1 - 0 \cdot 0 = 1 \ne 0$. So $A + B \notin S$, and this condition fails.
5. So the claim is false, and the step that the text called routine is the false step.

## Remarks

1. The example shows a gap of the most dangerous kind for the [[level of detail in proofs|VYGBV5D8Y4]]: the omitted step is false. A reader who trusts the word "routine" accepts a false theorem.
2. The two closure conditions look alike, but they behave differently. The determinant is homogeneous of degree $2$, which gives closure under scalars, and it is not additive, which breaks closure under sums.
3. A writer can test a claimed routine step by writing it out. Here the first attempt at closure under addition shows that $\det(A + B)$ has no formula in terms of $\det A$ and $\det B$ alone.
4. A similar claim with trace in place of determinant is true, and there the check is routine. The trace satisfies $\operatorname{tr}(A + B) = \operatorname{tr} A + \operatorname{tr} B$ and $\operatorname{tr}(tA) = t \operatorname{tr} A$, so the matrices of trace $0$ form a subspace.
5. The words "routine" and "left to the reader" work like "trivial" and "obvious", as the page [[trivial, obvious and clearly|Y0HXCJRB9B]] explains.

## Explanations

### L1 human

A text says "this part is routine, check it yourself", and many readers skip it.
Here the skipped part is false.
Two special tables of numbers each have a certain value equal to $0$, but their sum has value $1$.
So the claim breaks exactly at the step that the text did not write.
This is why a writer should leave out only steps that the writer has checked.

### L2 human

We repeat the test with a second pair of matrices, to see that the failure is not an accident.

1. Take $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, with $\det A = 1 - 1 = 0$.
2. Take $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, with $\det B = 0$.
3. Then $A + B = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, with $\det(A + B) = 2 - 1 = 1$.
4. Again $A, B \in S$ and $A + B \notin S$.

The typical use of this test is to try a routine step on the simplest objects before omitting it.
A trap is to check only closure under scalars, which holds, and to assume that closure under addition is "similar".
