---
tag: 8Q0HST6PC1
kind: example
name: Łukasiewicz implication is not a scalar projection
aliases: [lukasiewicz-implication-is-not-a-vector-logic-projection]
msc: ["03B50", "03B52"]
topics: [WZP584JQ06]
audience: grad
not_instance_of:
  - target: DJ41X602BJ
    note: the map (a, b) to min(1, 1 - a + b) is not of the form s^T G (u ⊗ v), because every such form is bilinear in a and b
uses: [DJ41X602BJ, 0N7ENQRCXN, JQ713VVD0G]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_logic
    locator: Many-valued two-dimensional logic; Scalar projections of vector outputs
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 3. Łukasiewicz logic
---

## Example

In [[vector logic|DJ41X602BJ]], let $u = \alpha s + (1 - \alpha) n$ and $v = \alpha' s + (1 - \alpha') n$ with $\alpha, \alpha' \in [0, 1]$.
We show that no matrix $G$ of size $q \times q^2$ gives $s^T G (u \otimes v) = \min(1, 1 - \alpha + \alpha')$ for all $\alpha, \alpha'$.
The right side is the [[Łukasiewicz implication|JQ713VVD0G]].

1. Assume that such a $G$ exists, and put $g(\alpha, \alpha') = s^T G (u \otimes v)$.
2. Write $c_{ab} = s^T G (a \otimes b)$ for $a, b \in \set{s, n}$.
3. By bilinearity of $\otimes$, $g(\alpha, \alpha') = \alpha \alpha' c_{ss} + \alpha (1 - \alpha') c_{sn} + (1 - \alpha) \alpha' c_{ns} + (1 - \alpha)(1 - \alpha') c_{nn}$.
4. At the corners, $g(1, 1) = c_{ss}$, $g(1, 0) = c_{sn}$, $g(0, 1) = c_{ns}$ and $g(0, 0) = c_{nn}$.
5. The Łukasiewicz implication has the corner values $1, 0, 1, 1$. So $c_{ss} = 1$, $c_{sn} = 0$, $c_{ns} = 1$ and $c_{nn} = 1$.
6. Then step 3 at $\alpha = \alpha' = \tfrac12$ gives $g(\tfrac12, \tfrac12) = \tfrac14 (1 + 0 + 1 + 1) = \tfrac34$.
7. But $\min(1, 1 - \tfrac12 + \tfrac12) = 1 \ne \tfrac34$. This contradicts the assumption.

So the Łukasiewicz implication is not a scalar projection of a matrix of vector logic.

## Remarks

The proof uses only the corner values and bilinearity.
So it works for any map on $[0, 1]^2$ that is not the bilinear extension of its values on $\set{0, 1}^2$.
For example, $\min(\alpha, \alpha')$ is not a projection either: the corners force $\alpha \alpha'$, which is $\tfrac14$ at $(\tfrac12, \tfrac12)$, and not $\tfrac12$.
The strong conjunction $\max(0, \alpha + \alpha' - 1)$ also fails, since it is $0$ at $(\tfrac12, \tfrac12)$.

The matrix $L$ of vector logic has the same corner values as the Łukasiewicz implication.
Its projection is $1 - \alpha (1 - \alpha')$, and the two maps agree exactly when $\alpha \in \set{0, 1}$ or $\alpha' \in \set{0, 1}$.

## Explanations

### L1 human

In vector logic, the value of an implication for uncertain inputs is a weighted average of its four classical values.
At "half true implies half true", that average is $\tfrac34$.
Łukasiewicz logic gives this implication the value $1$.
No choice of matrix can fix the gap, because the average is fixed by the four classical values.

### L2 human

1. Read off the four classical values of the connective.
2. Average them with the weights $\tfrac14$ each, which gives the projected value at $(\tfrac12, \tfrac12)$.
3. Compare with the value of the connective at $(\tfrac12, \tfrac12)$.

The typical use is to test whether a fuzzy connective can come from vector logic.
A trap: agreement on all classical inputs does not give agreement on the middle values.
