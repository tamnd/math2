---
tag: KN9PFGCGJ1
kind: statement
role: proposition
name: Macdonald's formula for symmetric products
sources:
  - wikipedia: en:68437256@r1360133546
    locator: Plethystic exponential, section Macdonald's formula for symmetric products
    note: adopted
    mention: wikipedia://en/68437256#KM8F
    sections: [Statement]
inventory: [CQJF8158W1]
---

## Statement

Let *X* be a finite CW complex, of dimension *d*, with Poincaré polynomial

$$P_X (t) = \sum_{k=0}^d b_k(X) \, t^k$$

where $b_k(X)$ is its *k*th Betti number. Then the Poincaré polynomial of the *n*th symmetric product of *X*, denoted $\operatorname{Sym}^n (X)$, is obtained from the series expansion:

$$\operatorname{PE}[P_X(-t)\,x] = \prod_{k=0}^d (1-t^k x)^{(-1)^{k+1}b_k(X)} = \sum_{n\geq 0} P_{\operatorname{Sym}^n(X)}(-t) \, x^n$$
