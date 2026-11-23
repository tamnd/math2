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
To test a formula, we assume that some row makes it false and work out the values that this forces.
We apply it to Peirce's law,
$$((p \to q) \to p) \to p.$$

1. Assume a row makes the formula F.
2. An implication is F only when its antecedent is T and its consequent is F, by the table of [[material implication|0ZNX6DQ3EJ]].
   So $(p \to q) \to p$ is T and $p$ is F.
3. Since $p$ is F, the implication $p \to q$ is T, whatever $q$ is.
4. Then $(p \to q) \to p$ is $\mathrm{T} \to \mathrm{F}$, which is F.
5. Step 4 contradicts step 2, which says that $(p \to q) \to p$ is T.
6. So no row makes the formula F, and Peirce's law is a [[tautology|05006AJ7DZ]].

Next we apply the method to $((p \to q) \to q) \to q$.

7. Assume a row makes it F.
   Then $(p \to q) \to q$ is T and $q$ is F.
8. Since $q$ is F and $(p \to q) \to q$ is T, the antecedent $p \to q$ must be F.
9. Since $p \to q$ is F, we get $p$ = T and $q$ = F.
10. Check the row TF: $p \to q$ is F, $(p \to q) \to q$ is $\mathrm{F} \to \mathrm{F} = \mathrm{T}$, and the whole formula is $\mathrm{T} \to \mathrm{F} = \mathrm{F}$.
11. So the forced values are consistent, and this row shows that the formula is not a tautology.

## Remarks

### Two outcomes

A contradiction among the forced values proves a tautology, and a consistent set of forced values gives a falsifying row.
The full table of Peirce's law has the last column T, T, T, T, which confirms step 6.
For formulas with many variables, the method saves much work compared with a table of $2^n$ rows.

### Values that are not forced

When a forced value does not fix a variable, as $q$ in step 3, the argument must hold for both values, or it must split into cases.
In step 3 both values of $q$ give the same result, so no split is needed.

### A classical law

Peirce's law is a tautology of classical logic, but it is not valid in [[intuitionistic logic|Q11N8X99FK]].
The truth table method and its short cuts are classical, since they assume that each variable is T or F.

## Explanations

### L1 human

To show that a statement can never be false, we pretend that it is false and look for trouble.
For Peirce's law, pretending it is false forces $p$ to be false.
Then a middle part must be both true and false at once.
That is impossible, so the statement can never be false.
For the second formula, the pretending leads to no trouble, and it gives a case where the formula really is false.

### L2 human

Prove by the assume-false method that $(p \to (q \to r)) \to ((p \to q) \to (p \to r))$ is a tautology.

1. Assume it is F.
   Then $p \to (q \to r)$ is T, and $(p \to q) \to (p \to r)$ is F.
2. From the second part, $p \to q$ is T and $p \to r$ is F.
3. From $p \to r$ false, $p$ is T and $r$ is F.
4. From $p \to q$ true and $p$ true, $q$ is T.
5. Then $q \to r$ is $\mathrm{T} \to \mathrm{F} = \mathrm{F}$, so $p \to (q \to r)$ is $\mathrm{T} \to \mathrm{F} = \mathrm{F}$, which contradicts step 1.
6. So the formula is a tautology.

The method suits long implications, where the false case forces many values at once.
Watch out: the method needs care with $\lor$ and $\leftrightarrow$.
There a value of the whole formula does not force the values of the parts, and a split into cases is needed.
