---
tag: SX9CD5NEPD
kind: statement
role: proposition
name: Alternating and skew-symmetric bilinear forms
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
about: [0DGDS5XY84, 0PBY4E9GQF]
uses: [08ZQAKBKHF, 0P24YW565F, 1ZB13N78XW]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Symmetric, skew-symmetric, and alternating forms
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: Skew-symmetric and alternating forms
---

## Statement

Let $B$ be a [[bilinear form|0P799D6AMN]] on a vector space $V$ over a field $F$.

1. If $B$ is [[alternating|08ZQAKBKHF]], then $B$ is skew-symmetric.
2. If the [[characteristic|1ZB13N78XW]] of $F$ is not $2$ and $B$ is skew-symmetric, then $B$ is alternating.
3. If the characteristic of $F$ is $2$, then $B$ is skew-symmetric exactly when $B$ is symmetric.
4. Let $V$ have a basis $(e_1, \dots, e_n)$, and let $A$ be the [[matrix|0P24YW565F]] of $B$. Then $B$ is alternating exactly when $A^T = -A$ and $A_{ii} = 0$ for $i = 1, \dots, n$.

The [[proof|MA5AD01GHA]] expands $B(u + v, u + v)$.

## Remarks

### Why each hypothesis is needed

- Part 2 needs $\operatorname{char} F \neq 2$. Over $\mathbb{F}_2$, the [[identity form $x_1 y_1 + x_2 y_2$|1V7NMPCSK9]] is skew-symmetric, but $B(e_1, e_1) = 1$.
- Part 4 needs both conditions. Over $\mathbb{F}_2$, $A = I_2$ satisfies $A^T = -A$ but has a nonzero diagonal.

### Consequences

- Outside characteristic $2$, a form is alternating exactly when its matrix is [[skew-symmetric|0PBY4E9GQF]].
- In characteristic $2$, the alternating forms are the symmetric forms with $B(v, v) = 0$ for all $v$, and they form a proper subspace of the symmetric forms when $V \neq 0$.
- For any characteristic, the alternating forms on a space of dimension $n$ form a subspace of dimension $n(n - 1)/2$, since the entries above the diagonal fix $A$.

### Converse

Part 1 has the converse part 2 when $\operatorname{char} F \neq 2$, and no converse in characteristic $2$.
The one-dimensional [[form $f(x, y) = xy$ on $\mathbb{F}_2$|QFAWSF1A04]] is a smaller counterexample.

### Generalizations

The same statement holds for [[alternating multilinear maps|0K6CH0MT0F]] of any number of arguments, by the [[antisymmetry statement|VJZVSTWYYW]].

## Explanations

### L1 human

There are two ways to say that a form is like a signed area.
One way: a vector paired with itself gives $0$.
The other way: swapping the two vectors changes the sign.
The first way always gives the second.
The second way gives the first, except over number systems in which $1 + 1 = 0$.

### L2 human

We see the role of the characteristic in the proof of part 2.

1. Skew-symmetry with $u = v$ gives $B(v, v) = -B(v, v)$.
2. So $2B(v, v) = 0$.
3. If $2 \neq 0$ in $F$, we divide by $2$ and get $B(v, v) = 0$.
4. If $2 = 0$ in $F$, step 2 says nothing, and indeed $B(e_1, e_1) = 1$ is possible.

The typical use is the matrix test of part 4.
A trap: in characteristic $2$, "skew-symmetric" gives no information beyond "symmetric".

### L3 human

Part 4 says that the alternating forms are the image of the map $C \mapsto C - C^T$ from all matrices, since $A = U - U^T$ for the strictly upper triangular part $U$ of an alternating $A$.
In terms of tensors, alternating forms are $(\Lambda^2 V)^*$, while skew-symmetric forms are the forms that are odd under the swap of factors.
These agree exactly when $2$ is invertible, and this is the reason why quadratic and symplectic geometry in characteristic $2$ need separate treatment.
