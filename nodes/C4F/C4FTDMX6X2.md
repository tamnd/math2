---
tag: C4FTDMX6X2
kind: proof
name: Proof of the Gershgorin circle theorem by a largest coordinate
msc: [15A42, 15A18]
proves: 0ETGP0XVCJ
uses: [0ZND7NQ970, 076JGP6R3T, 03HF5PMY5T, 0GMV7GP8W0, 00S7C68D51]
sources:
  - url: https://en.wikipedia.org/wiki/Gershgorin_circle_theorem
    locator: Statement and proof
---

## Proof

We look at the row of $A x = \lambda x$ where the eigenvector $x$ has its largest coordinate.

1. Let $\lambda$ be an [[eigenvalue|0ZND7NQ970]] of $A$. By definition, there is $x = (x_1, \dots, x_n) \in \C^n$ with $x \ne 0$ and $A x = \lambda x$.
2. Choose an index $i$ with $\abs{x_i} \ge \abs{x_j}$ for all $j$. Since $x \ne 0$, some $x_j \ne 0$, so $\abs{x_i} > 0$.
3. By the definition of the [[matrix product|076JGP6R3T]], coordinate $i$ of $A x = \lambda x$ reads $\sum_{j=1}^{n} a_{ij} x_j = \lambda x_i$.
4. Subtract $a_{ii} x_i$ from both sides. This gives $(\lambda - a_{ii}) x_i = \sum_{j \ne i} a_{ij} x_j$.
5. Take [[absolute values|00S7C68D51]]. By the [[multiplicativity of the absolute value|0GMV7GP8W0]] and the [[triangle inequality|03HF5PMY5T]], $\abs{\lambda - a_{ii}} \abs{x_i} \le \sum_{j \ne i} \abs{a_{ij}} \abs{x_j}$.
6. By the choice of $i$ in step 2, $\abs{x_j} \le \abs{x_i}$ for all $j$. So the right side of step 5 is at most $\sum_{j \ne i} \abs{a_{ij}} \abs{x_i} = R_i \abs{x_i}$.
7. Divide by $\abs{x_i} > 0$. This gives $\abs{\lambda - a_{ii}} \le R_i$.
8. So $\lambda \in D_i$. Since $\lambda$ was any eigenvalue, each eigenvalue of $A$ lies in at least one of the discs $D_1, \dots, D_n$.

## Idea

Take an eigenvector and its coordinate of largest size. In that row, the diagonal term must balance the other terms of the row. These other terms are at most $R_i$ times the largest coordinate, so $\lambda$ is within $R_i$ of $a_{ii}$.
