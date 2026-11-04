---
tag: BM6P0C2AC2
kind: statement
role: lemma
name: Gödel's β-function lemma
sources:
  - wikipedia: en:8371092@r1355768245
    locator: Gödel numbering for sequences, section Accessing members > Gödel's β-function lemma
    note: adopted
    mention: wikipedia://en/8371092#TT9T
    sections: [Statement]
inventory: [2MKMSGKP7Z]
---

## Statement

By an ingenious use of the [[Chinese remainder theorem|0FNN9B4W64]], we can constructively define such a recursive function $\beta$ (using simple number-theoretical functions, all of which can be defined in a total recursive way) fulfilling the specifications given above. Gödel defined the $\beta$ function using the Chinese remainder theorem in his article written in 1931. This is a primitive recursive function.

Thus, for all *n* and for any *n*-length sequence of natural numbers $\langle a_0,\dots a_{n-1} \rangle$, there exists an appropriate natural number *a*, called the Gödel number of the sequence such that $\beta(a,i) = a_i$.

Our specific solution will depend on a pairing function—there are several ways to implement the pairing function, so one method must be selected. Now, we can abstract from the details of the implementation of the pairing function. We need only to know its "interface": let $\pi$, *K*, and *L* denote the pairing function and its two projection functions, respectively, satisfying specification:

$$K\left(\pi\left(x,y\right)\right) = x$$

$$L\left(\pi\left(x,y\right)\right) = y$$

We shall use another auxiliary function that will compute the remainder for natural numbers. Examples:

- $$\mathrm{rem}(5, 3) = 2$$
- $$\mathrm{rem}(7, 2) = 1$$

It can be proven that this function can be implemented as a recursive function.
