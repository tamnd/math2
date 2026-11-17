---
tag: FPDDSFR941
kind: example
name: Peirce's law by the assume-false method
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [05RSK4Q657]
uses: [05RSK4Q657, 0ZNX6DQ3EJ, 05006AJ7DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Peirce%27s_law
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Truth_table
    locator: lead section
---

## Example

The assume-false method is a short cut of the [[truth table|05RSK4Q657]] method.
To test a formula, we assume that some row makes it false, and we work out the values that this forces.
We apply it to Peirce's law
$$((p \to q) \to p) \to p.$$

1. Assume a row makes the formula false.
2. An implication is false only when its antecedent is $\mathsf{T}$ and its consequent is $\mathsf{F}$, by the table of [[material implication|0ZNX6DQ3EJ]]. So $(p \to q) \to p$ is $\mathsf{T}$ and $p$ is $\mathsf{F}$.
3. Since $p$ is $\mathsf{F}$, the implication $p \to q$ is $\mathsf{T}$, whatever $q$ is.
4. Then $(p \to q) \to p$ is $\mathsf{T} \to \mathsf{F}$, which is $\mathsf{F}$.
5. Step 4 contradicts step 2, which says that $(p \to q) \to p$ is $\mathsf{T}$.
6. So no row makes the formula false, and Peirce's law is a [[tautology|05006AJ7DZ]].

Next we apply the method to $((p \to q) \to q) \to q$.

7. Assume a row makes it false. Then $(p \to q) \to q$ is $\mathsf{T}$ and $q$ is $\mathsf{F}$.
8. Since $q$ is $\mathsf{F}$ and $(p \to q) \to q$ is $\mathsf{T}$, the antecedent $p \to q$ must be $\mathsf{F}$.
9. Since $p \to q$ is $\mathsf{F}$, we get $p = \mathsf{T}$ and $q = \mathsf{F}$.
10. Check the row $p = \mathsf{T}$, $q = \mathsf{F}$: $p \to q = \mathsf{F}$, $(p \to q) \to q = \mathsf{F} \to \mathsf{F} = \mathsf{T}$, and the whole formula is $\mathsf{T} \to \mathsf{F} = \mathsf{F}$.
11. So the forced values are consistent, and this row shows that the formula is not a tautology.

## Remarks

The example shows both outcomes of the method: a contradiction proves a tautology, and a consistent set of forced values gives a falsifying row.
The method used $2$ cases of reasoning instead of the $4$ rows of a full table; for formulas with many variables the saving is large.
The full table of Peirce's law has the last column $\mathsf{T}, \mathsf{T}, \mathsf{T}, \mathsf{T}$, which confirms step 6.

When a forced value does not determine a variable, as $q$ in step 3, the method must hold for both values, or it must split into cases.
In step 3 both values of $q$ give the same result, so no split is needed.

Peirce's law is a tautology of classical logic, but it is not valid in [[intuitionistic logic|Q11N8X99FK]].
The truth table method and its short cuts are classical: they assume that each variable is $\mathsf{T}$ or $\mathsf{F}$.

## Explanations

### L1 human

To show that a statement can never be false, we pretend that it is false and look for trouble.
For Peirce's law, pretending it is false forces $p$ to be false.
Then a middle part must be both true and false at once.
That is impossible, so the statement can never be false.
For the second formula, the pretending leads to no trouble, and it gives a case where the formula really is false.

### L2 human

We prove by the assume-false method that $(p \to (q \to r)) \to ((p \to q) \to (p \to r))$ is a tautology.

1. Assume it is false. Then $p \to (q \to r)$ is $\mathsf{T}$, and $(p \to q) \to (p \to r)$ is $\mathsf{F}$.
2. From the second part: $p \to q$ is $\mathsf{T}$ and $p \to r$ is $\mathsf{F}$.
3. From $p \to r$ false: $p = \mathsf{T}$ and $r = \mathsf{F}$.
4. From $p \to q$ true and $p = \mathsf{T}$: $q = \mathsf{T}$.
5. Then $q \to r = \mathsf{T} \to \mathsf{F} = \mathsf{F}$, so $p \to (q \to r) = \mathsf{T} \to \mathsf{F} = \mathsf{F}$, which contradicts step 1.
6. So the formula is a tautology.

The typical use of the method is for long implications, where the false case forces many values at once.
A trap: the method needs care with $\lor$ and $\leftrightarrow$.
There a value of the whole formula does not force the values of the parts, and a split into cases is needed.
