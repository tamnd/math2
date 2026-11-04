---
tag: V282NG3QJR
kind: proof
name: Proof of Labelled enumeration theorem
proves: XNX30CK7S5
sources:
  - wikipedia: en:34871920@r1195473520
    locator: Labelled enumeration theorem, section Proof of the theorem
    note: adopted
    mention: wikipedia://en/34871920#MA1C
    sections: [Proof]
---

## Proof

It follows from the re-labelling construction that there are

$$\frac{1}{|G|} \sum_{r_1 + r_2 + \cdots + r_n = k} {k \choose r_1, r_2, \ldots, r_n} \; r_1! [z^{r_1}] g(z) \; r_2! [z^{r_2}] g(z) \; \cdots \; r_n! [z^{r_n}] g(z)$$

or

$$\frac{k!}{|G|} \sum_{r_1 + r_2 + \cdots + r_n = k} [z^{r_1}] g(z) [z^{r_2}] g(z) \cdots [z^{r_n}] g(z) \; = \; \frac{k!}{|G|} [z^k] g(z)^n$$

different configurations of total size *k*. The formula evaluates to an integer because $[z^k] g(z)^n$ is zero for *k* \< *n* (remember that *g* does not include objects of size zero) and when $k \ge n$ we have $n!|k!$ and the order $|G|$ of *G* divides the order of $S_n$, which is $n!$, by [[Lagrange's theorem|3C53TD]]. The conclusion is that the EGF of the labelled configurations is given by

$$f_n(z) = \sum_{k \ge 0} \left( \frac{k!}{|G|} [z^k] g(z)^n \right) \frac{z^k}{k!} = \frac{1}{|G|} \sum_{k \ge 0} z^k [z^k] g(z)^n = \frac{g(z)^n}{|G|}.$$

This formula could also be obtained by enumerating sequences, i.e. the case when the slots are not being permuted, and by using the above argument without the $1/|G|$-factor to show that their generating function under re-labelling is given by $g(z)^n$. Finally note that every sequence belongs to an orbit of size $|G|$, hence the generating function of the orbits is given by $g(z)^n/|G|.$
