---
tag: KV7FHJCE14
kind: example
name: K1 of a field
msc: [19B99]
instance_of: [SXVNJY4XFY]
uses: [04C5ZBG1WT, E5JXB0E324, 00KDZRW4C0, AAB05HS00Y]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
    locator: K1
---

## Example

Let $F$ be a [[field|04C5ZBG1WT]] and $F^\times$ its multiplicative group.
Then the [[determinant|00KDZRW4C0]] induces an isomorphism
$$\det \colon K_1(F) \xrightarrow{\ \cong\ } F^\times.$$
Check of surjectivity: for $u \in F^\times$, the matrix $\mathrm{diag}(u, 1, \dots, 1)$ has determinant $u$.
Check of injectivity: let $A \in GL_n(F)$ have determinant $1$.
Gaussian elimination using only the operations "add a multiple of one row to another" brings $A$ to $\mathrm{diag}(1, \dots, 1, d)$.
A zero pivot is avoided by first adding another row with a nonzero entry in that column.
Then $d = \det A = 1$, so $A$ is a product of elementary matrices and lies in the [[elementary subgroup|E5JXB0E324]] $E_n(F)$.
Hence the kernel of $\det$ on $K_1(F) = GL(F)/E(F)$ is trivial, that is, [[SK1|AAB05HS00Y]] of a field is $0$.
For example, $K_1(\Q) \cong \Q^\times$ and $K_1(\F_q) \cong \F_q^\times$, cyclic of order $q - 1$.

## Explanations

### L1 human

Over a field, row operations can simplify any invertible matrix down to a diagonal matrix with a single interesting entry.
That entry is the determinant, and nothing else survives.
So for a field, $K_1$ is just the group of nonzero numbers under multiplication.
