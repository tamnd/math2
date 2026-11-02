---
tag: DD8SAAED09
kind: statement
role: lemma
name: Bailey's lemma
msc: [33D15, 11P84]
uses: [Y1X8ZZQ7VM]
about: [Y1X8ZZQ7VM]
sources:
  - url: https://en.wikipedia.org/wiki/Bailey_pair
---

## Statement

Let $q, a, \rho_1, \rho_2 \in \C \setminus \set{0}$ be such that no denominator below vanishes, and write $(c_1, \dots, c_k; q)_n = (c_1; q)_n \cdots (c_k; q)_n$ with the [[q-Pochhammer symbol|Y1X8ZZQ7VM]].
A pair of sequences $(\alpha_n)_{n \ge 0}$, $(\beta_n)_{n \ge 0}$ is a *Bailey pair relative to $a$* if
$$\beta_n = \sum_{r=0}^{n} \frac{\alpha_r}{(q; q)_{n-r}\, (aq; q)_{n+r}} \quad \text{for all } n \ge 0.$$
Put $c = \frac{aq}{\rho_1 \rho_2}$.
If $(\alpha_n, \beta_n)$ is a Bailey pair relative to $a$, then so is $(\alpha_n', \beta_n')$, where
$$\alpha_n' = \frac{(\rho_1, \rho_2; q)_n\, c^n}{(aq/\rho_1, aq/\rho_2; q)_n}\, \alpha_n,
\qquad
\beta_n' = \sum_{j=0}^{n} \frac{(\rho_1, \rho_2; q)_j\, (c; q)_{n-j}\, c^j}{(q; q)_{n-j}\, (aq/\rho_1, aq/\rho_2; q)_n}\, \beta_j.$$

## Remarks

Proof idea: insert the definition of $\beta_j$ into $\beta_n'$ and exchange the sums.
The inner sum over $j$ is a terminating balanced ${}_3\phi_2$ series, which the $q$-Pfaff–Saalschütz summation evaluates in closed form.
Example: the *unit Bailey pair* relative to $a$ is $\beta_n = \delta_{n0}$ with $\alpha_0 = 1$ and $\alpha_n = \frac{(1 - a q^{2n})(a; q)_n (-1)^n q^{\binom{n}{2}}}{(1 - a)(q; q)_n}$ for $n \ge 1$; applying the lemma to it produces new pairs.
Letting $\rho_1, \rho_2 \to \infty$ gives $c^n (\rho_1, \rho_2; q)_n \to a^n q^{n^2}$, and with $n \to \infty$ one gets the identity $\sum_{n \ge 0} a^n q^{n^2} \beta_n = \frac{1}{(aq; q)_\infty} \sum_{n \ge 0} a^n q^{n^2} \alpha_n$ for suitable pairs.
This limit, applied to a suitable pair with $a = 1$ or $a = q$ and combined with the [[Jacobi triple product|JFP2DGMNXT]], gives the [[Rogers–Ramanujan identities|M24H4GJPPW]].

## Explanations

### L1 human

A Bailey pair is two sequences linked by a fixed triangular sum.
Bailey's lemma is a machine: put one Bailey pair in, and a new Bailey pair comes out, with two free parameters.
Each pair gives an identity between a sum and, often, a product, so repeating the machine produces infinitely many identities.

### L2 human

Bailey proved the lemma in the 1940s, and Andrews later noticed that it can be iterated, which gives the Bailey chain.
The Bailey chain explains the Rogers–Ramanujan identities and their many generalizations, such as the Andrews–Gordon identities, in a uniform way.
The proof only needs the $q$-Pfaff–Saalschütz sum, the $q$-analogue of the [[Pfaff–Saalschütz theorem|9X6KG770GV]].
