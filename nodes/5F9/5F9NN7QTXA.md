---
tag: 5F9NN7QTXA
kind: example
name: The trace is not multiplicative
msc: ["15A15"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: 0VTH8KPCG2
    note: "the trace M2(Q) → Q is not a ring homomorphism, because tr(I · I) = 2 but tr I · tr I = 4, and tr I = 2 is not 1"
uses: [07PTPSZPME]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a product
---

## Example

The trace respects addition but not multiplication, and the identity matrix already shows it.
Work in $M_2(\mathbb{Q})$.

1. By the [[definition|07PTPSZPME]], $\operatorname{tr} I_2 = 1 + 1 = 2$, while a [[ring homomorphism|0VTH8KPCG2]] must send the identity to $1$.
2. For products,
$$\operatorname{tr}(I_2 \cdot I_2) = \operatorname{tr} I_2 = 2, \qquad \operatorname{tr} I_2 \cdot \operatorname{tr} I_2 = 2 \cdot 2 = 4.$$
3. The failure is not special to the identity. For $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$,
$$AB = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad \operatorname{tr}(AB) = 1, \qquad \operatorname{tr} A \cdot \operatorname{tr} B = 0 \cdot 0 = 0.$$
4. So $\operatorname{tr}(XY) = \operatorname{tr} X \operatorname{tr} Y$ fails for some $X$ and $Y$, and the trace is not a ring homomorphism.

## Remarks

### No fix is possible

Scaling does not help.
If $\varphi = c \operatorname{tr}$ were multiplicative, then $\varphi(I_2) = \varphi(I_2)^2$ would force $2c = 4c^2$, so $c = 0$, which gives the zero map, or $c = 1/2$, which fails on step 3, since $\tfrac12 \cdot 1 \neq 0$.
In fact $M_n(F)$ has no ring homomorphism onto a field $F$ for $n \ge 2$.
Its kernel would be a proper two-sided ideal, and [[a matrix ring over a field has no nontrivial two-sided ideals|Z46WD9W1ZS]], so the kernel would be $0$, and $M_n(F)$, which is not commutative, would embed in the commutative ring $F$.

### Watch out

The determinant has the opposite behavior.
It is multiplicative, $\det(AB) = \det A \det B$, but it is not additive, since $\det(I_2 + I_2) = 4$ while $\det I_2 + \det I_2 = 2$.

## Explanations

### L1 human

The trace of a product is usually not the product of the traces.
Even for the identity matrix you get $2$ on one side and $4$ on the other.

### L2 human

The trace keeps the structure of addition but not of multiplication.
What survives of multiplication is the cyclic property $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.
Step 3 is consistent with it: $BA = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ also has trace $1$.
