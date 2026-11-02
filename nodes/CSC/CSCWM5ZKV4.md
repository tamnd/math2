---
tag: CSCWM5ZKV4
kind: statement
role: theorem
name: Dougall's formula
msc: [33C20]
uses: [VDBAW9PN88, YZHM3HSM0F]
about: [VDBAW9PN88]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_hypergeometric_function
---

## Statement

Let $m$ be a nonnegative integer and let $a, b, c, d, e$ be complex numbers with
$$1 + 2a = b + c + d + e - m.$$
Assume that none of the lower parameters $\frac{a}{2}, 1 + a - b, 1 + a - c, 1 + a - d, 1 + a - e, 1 + a + m$ lies in $\set{0, -1, \dots, 1 - m}$, and that $(1 + a - b - c - d)_m \ne 0$.
Write $(x)_k = x (x + 1) \cdots (x + k - 1)$ for the [[Pochhammer symbol|YZHM3HSM0F]].
Then the terminating [[generalized hypergeometric series|VDBAW9PN88]] ${}_7F_6$ at $1$ is
$${}_7F_6\left( \begin{matrix} a,\ 1 + \frac{a}{2},\ b,\ c,\ d,\ e,\ -m \\ \frac{a}{2},\ 1 + a - b,\ 1 + a - c,\ 1 + a - d,\ 1 + a - e,\ 1 + a + m \end{matrix} ; 1 \right) = \frac{(1 + a)_m\, (1 + a - b - c)_m\, (1 + a - b - d)_m\, (1 + a - c - d)_m}{(1 + a - b)_m\, (1 + a - c)_m\, (1 + a - d)_m\, (1 + a - b - c - d)_m}.$$

## Remarks

The series is *very well-poised*: each upper parameter plus the matching lower parameter gives $1 + a$, and the pair $1 + \frac{a}{2}, \frac{a}{2}$ is present.
The condition $1 + 2a = b + c + d + e - m$ says that the series is $2$-balanced: the lower parameters sum to $2$ more than the upper ones.
One proof applies [[Whipple's transformation|QNGGCTXK9S]], which turns the ${}_7F_6$ into a multiple of ${}_4F_3(-m, d, e, 1 + a - b - c; 1 + a - b, 1 + a - c, d + e - a - m; 1)$.
Under the condition $1 + 2a = b + c + d + e - m$ one has $d + e - a - m = 1 + a - b - c$, so this ${}_4F_3$ reduces to a balanced ${}_3F_2$.
The [[Pfaff–Saalschütz theorem|9X6KG770GV]] then sums it, and the product on the right comes out.
For $m = 0$ both sides equal $1$.
Letting $m \to \infty$ term by term gives the summation of the well-poised ${}_5F_4$ with upper parameters $a, 1 + \frac{a}{2}, b, c, d$, which in turn contains part 3 of [[Dixon's identity|QC4TP5D6HE]].

## Explanations

### L1 human

Dougall's formula evaluates a finite sum of ratios of rising factorials with seven parameters on top and six on the bottom.
The parameters must follow a rigid pattern, and one linear relation must hold among them.
When they do, the whole sum is a single product, which is rare for sums of this size.

### L2 human

Dougall's formula sits near the top of the classical summation formulas for hypergeometric series at $1$.
Specialising parameters gives many other summations, which is why it is a hub in tables of identities.
Its $q$-analogue is Jackson's summation for a very well-poised ${}_8\phi_7$.
