---
tag: MYJDXMN68Q
kind: statement
role: theorem
name: Frege's theorem in propositional logic
sources:
  - wikipedia: en:4725226@r1364500909
    locator: Frege's theorem, section Frege's theorem in propositional logic
    note: adopted
    mention: wikipedia://en/4725226#775Z
    sections: [Statement]
inventory: [2H3EBWHKYJ]
---

## Statement

| ( | *P* | → | ( | *Q* | → | *R* | )) | → | (( | *P* | → | *Q* | ) | → | ( | *P* | → | *R* | )) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | 1 | **2** |  | 3 | 4 | 5 |  | **6** |  | 7 | 8 | 9 |  | **10** |  | 11 | 12 | 13 |  |

In propositional logic, Frege's theorem refers to this [[tautology|05006AJ7DZ]]:

$$\big(P\to(Q\to R)\big)\to\big((P\to Q)\to(P\to R)\big)$$

The theorem already holds in one of the weakest logics imaginable, the constructive implicational calculus. The proof under the Brouwer–Heyting–Kolmogorov interpretation reads $f \mapsto g\mapsto p\mapsto (f(p)\circ g)(p)$. In words: "Let *f* denote a reason that *P* implies that *Q* implies *R*. And let *g* denote a reason that *P* implies *Q*. Then given a *f*, then given a *g*, then given a reason *p* for *P*, we know both that *Q* holds by *g* and that *Q* implies *R* holds by *f*. So *R* holds."

The [[truth table|05RSK4Q657]] to the right gives a semantic proof. For all possible assignments of *false* () or *true* () to *P*, *Q*, and *R* (columns 1, 3, 5), each subformula is evaluated according to the rules for [[material conditional|0NMG7W7Q11]], the result being shown below its main operator. Column 6 shows that the whole formula evaluates to *true* in every case, i.e. that it is a tautology. In fact, its antecedent (column 2) and its consequent (column 10) are even equivalent.
