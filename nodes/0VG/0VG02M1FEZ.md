---
tag: 0VG02M1FEZ
kind: statement
role: theorem
name: Every polynomial has a root in some extension field
msc: [12F05]
uses: [0M893X7YY7, 0AWMPX35CW, 00X2A9G9W3, 0D6KH8Y59N]
sources:
  - url: https://en.wikipedia.org/wiki/Splitting_field
    locator: Constructing splitting fields
---

## Statement

Let $K$ be a [[field|0QA8CHH8MG]] and let $f \in K[x]$ with $\deg f \ge 1$.
Then there is a [[field extension|0WQ1A8SHTZ]] $L/K$ with $[L : K] \le \deg f$ such that $f$ has a [[root|00EHX6FWC0]] in $L$.

## Remarks

The proof: let $g$ be an irreducible factor of $f$ in $K[x]$. [[Adjoining a root of $g$|0M893X7YY7]] gives the field $L = K[x]/(g)$ of degree $\deg g$ over $K$.
The class of $x$ in $L$ is a root of $g$, and so of $f$.
The irreducible factor $g$ exists because $K[x]$ is a [[unique factorisation domain|0D6KH8Y59N]].
Repeating the step gives a [[splitting field|02NZZ1J0FH]] of $f$.

## Explanations

### L1 human

A polynomial with no root in a field gets a root in a bigger field.
The bigger field is built from the polynomial itself, without any reference to the complex numbers.
