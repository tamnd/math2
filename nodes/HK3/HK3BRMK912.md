---
tag: HK3BRMK912
kind: statement
role: theorem
name: Lie product formula
msc: [15A16, "22E15"]
uses: [020M04FN1H, 0JXZKX526R, 05M5SWSZZD]
about: [020M04FN1H]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_product_formula
same_as:
  wikidata: Q3077645
  wikipedia: Lie product formula
---

## Statement

Let $n \ge 1$ and let $A$ and $B$ be $n \times n$ complex [[matrices|0JXZKX526R]].
Then
$$e^{A + B} = \lim_{m \to \infty} \left( e^{A/m} e^{B/m} \right)^m,$$
where $e^X$ is the [[matrix exponential|020M04FN1H]] and the [[limit|05M5SWSZZD]] is taken entry by entry.

## Remarks

Let $X_m = e^{A/m} e^{B/m}$ and $Y_m = e^{(A + B)/m}$.
Both equal $I + (A + B)/m + O(1/m^2)$, so $\norm{X_m - Y_m} = O(1/m^2)$.
The identity $X^m - Y^m = \sum_{k=0}^{m-1} X^k (X - Y) Y^{m-1-k}$ and the bound $\norm{X_m}, \norm{Y_m} \le e^{(\norm{A} + \norm{B})/m}$ give $\norm{X_m^m - Y_m^m} = O(1/m)$, and $Y_m^m = e^{A + B}$.
If $AB = BA$, then $e^{A/m} e^{B/m} = e^{(A + B)/m}$ and the formula holds for every $m$.
In general $e^{A + B} \ne e^A e^B$: for $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, $e^A e^B = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, while $e^{A + B} = \begin{pmatrix} \cosh 1 & \sinh 1 \\ \sinh 1 & \cosh 1 \end{pmatrix}$.

## Explanations

### L1 human

For numbers, $e^{a + b} = e^a e^b$, but for matrices this fails when $A$ and $B$ do not commute.
The formula repairs this: alternate many tiny steps of $A$ and of $B$, and the result approaches $e^{A + B}$.
It is like walking diagonally by taking many small steps east and north in turn.

### L2 human

The formula is the basis of splitting methods: to solve $x' = (A + B)x$, one alternates the flows of $x' = Ax$ and $x' = Bx$, which may be easier to compute.
In a Lie group it shows that the sum in the Lie algebra corresponds to a limit of products in the group.
Trotter extended it to certain unbounded operators on Hilbert spaces, where it is called the Trotter product formula.
It is a key step in the proof of the [[Golden–Thompson inequality|Z7R754JC7N]].
