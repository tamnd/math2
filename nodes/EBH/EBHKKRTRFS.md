---
tag: EBHKKRTRFS
kind: example
name: Wilkie's identity
msc: [08B05, 03C05]
illustrates: [RCRD8CAVB4]
uses: [RCRD8CAVB4, PKD440G2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Tarski%27s_high_school_algebra_problem
    locator: Solution
---

## Example

Write $A = 1 + x$, $B = 1 + x + x^2$, $C = 1 + x^3$ and $D = 1 + x^2 + x^4$, where $x^2$ means $x \cdot x$ and so on.
*Wilkie's identity* is
$$(A^y + B^y)^x \cdot (C^x + D^x)^y = (A^x + B^x)^y \cdot (C^y + D^y)^x.$$
It is an [[identity|PKD440G2XW]] in the signature $1, +, \cdot$, exponentiation.

Check that it holds for all positive integers $x, y$.
Let $Q = 1 - x + x^2$, a positive integer for $x \ge 1$.
Then $C = A \cdot Q$ and $D = B \cdot Q$.
So $C^x + D^x = Q^x (A^x + B^x)$ and $C^y + D^y = Q^y (A^y + B^y)$.
Both sides become $(A^y + B^y)^x \cdot (A^x + B^x)^y \cdot Q^{xy}$.

Alex Wilkie showed that this identity cannot be derived from the eleven high school identities, which answers [[Tarski's high school algebra problem|RCRD8CAVB4]] negatively.
The check above uses the term $1 - x + x^2$, which needs subtraction and so is not a term of the signature.

## Explanations

### L1 human

Both sides of Wilkie's identity are built only from $1$, addition, multiplication and powers, and they are always equal for positive whole numbers.
The quick proof factors $1 + x^3$ and $1 + x^2 + x^4$ with the help of $1 - x + x^2$, which uses a minus sign.
School rules have no minus sign, and Wilkie proved that they cannot prove the identity in any other way.
