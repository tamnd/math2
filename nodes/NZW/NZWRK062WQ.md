---
tag: NZWRK062WQ
kind: object
name: Takeuti-Feferman-Buchholz ordinal
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
uses: [E7WEFRMQTB, C72RBH0CDR, 5VNT564Y2W, PQSHBKCE7V, DC60FYCSPM, 9APRFM0G7F]
sources:
  - url: https://en.wikipedia.org/wiki/Takeuti%E2%80%93Feferman%E2%80%93Buchholz_ordinal
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Buchholz_psi_functions
    locator: Ordinal notation
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
  - url: https://en.wikipedia.org/wiki/Buchholz_hydra
    locator: lead section
---

## Description

In [[Buchholz's system|E7WEFRMQTB]], the term $\psi_0(\Omega)$ is $\varepsilon_0$, the ordinal of Peano arithmetic, and $\psi_0(\Omega_2)$ is the Bachmann-Howard ordinal, the ordinal of $\mathrm{ID}_1$.
Push the argument as far as the system allows, and you reach its last value:
$$\psi_0(\varepsilon_{\Omega_\omega + 1}).$$
This countable ordinal is the Takeuti-Feferman-Buchholz ordinal.

Here $\Omega_\omega = \aleph_\omega$, and $\varepsilon_{\Omega_\omega + 1}$ is the least [[epsilon number|PQSHBKCE7V]] above $\Omega_\omega$, the limit of
$$\Omega_\omega + 1, \quad \omega^{\Omega_\omega + 1}, \quad \omega^{\omega^{\Omega_\omega + 1}}, \quad \dots$$
In Feferman's notation the same ordinal is $\theta_{\varepsilon_{\Omega_\omega + 1}}(0)$.
It is the order type of the countable part of Buchholz's notation system, the terms below the term for $\Omega_1$.
By the table of ordinal analyses, it is the [[proof-theoretic ordinal|C72RBH0CDR]] of the theory $\Pi^1_1\text{-}\mathrm{CA} + \mathrm{BI}$ of [[second-order arithmetic|DC60FYCSPM]], and of the theory $\mathrm{ID}_\omega$ of $\omega$-times [[iterated inductive definitions|5VNT564Y2W]].
Here $\mathrm{BI}$ is bar induction, transfinite induction along every well-founded relation for every formula, and the proof-theoretic ordinal is the supremum of the order types of the primitive recursive well-orderings that the theory proves well-founded.

## Remarks

### Why it is the last value

Why can no argument go further?
Write $E = \varepsilon_{\Omega_\omega + 1}$, and use the fact from the Wikipedia article that $\psi_\omega(\xi) = \omega^{\Omega_\omega + \xi}$ for $\xi < E$.

1. We show that every member of every $C_0(\alpha)$ is below $E$, by induction on the construction.
   The start $\{ 0 \}$ is below $E$, and $E$ is closed under addition.
2. A value $\psi_\mu(\xi)$ with $\mu < \omega$ is below $\Omega_{\mu + 1} < E$.
3. A value $\psi_\omega(\xi)$ has $\xi$ already in the set, so $\xi < E$, and then $\omega^{\Omega_\omega + \xi} < E$ because $E$ is an epsilon number.
4. So no argument $\xi \ge E$ is ever named, and $C_0(\alpha) = C_0(E)$ for all $\alpha \ge E$.
   Hence $\psi_0(\alpha) = \psi_0(E)$ for all $\alpha \ge E$.

### The values below it

The ordinals of the familiar theories sit below this one.
For $1 \le \nu < \omega$, the value $\psi_0(\Omega_\nu)$ is the ordinal of $\mathrm{ID}_{<\nu}$, the union of the theories $\mathrm{ID}_\mu$ for $\mu < \nu$.
For $\nu = 1$ this is $\varepsilon_0$, and for $\nu = 2$ it is $\psi_0(\Omega_2) = \psi_0(\varepsilon_{\Omega + 1})$, the [[Bachmann-Howard ordinal|QH3ENXFRSV]].
At the top of the tower, $\psi_0(\Omega_\omega)$ is the ordinal of $\mathrm{ID}_{<\omega}$ and of [[Π¹₁-comprehension|2MGJJTSRFD]] $\Pi^1_1\text{-}\mathrm{CA}_0$, and it is smaller than the Takeuti-Feferman-Buchholz ordinal.
The gap between $\Pi^1_1\text{-}\mathrm{CA}_0$ and $\Pi^1_1\text{-}\mathrm{CA} + \mathrm{BI}$ is the strength of induction: the first theory has induction only for sets, the second transfinite induction for all formulas.

### Watch out

Do not give this ordinal to $\mathrm{ID}_{<\omega}$ or to $\Pi^1_1\text{-}\mathrm{CA}_0$.
Their ordinal is the smaller $\psi_0(\Omega_\omega)$, the limit of $\psi_0(\Omega_n)$ for finite $n$.
The Takeuti-Feferman-Buchholz ordinal belongs to $\mathrm{ID}_\omega$, where the definitions are iterated through all finite levels at once, and to $\Pi^1_1\text{-}\mathrm{CA} + \mathrm{BI}$.

### The Buchholz hydra

The [[Buchholz hydra|9APRFM0G7F]] is a game on finite rooted trees whose labels are the indices $\nu \le \omega$ of Buchholz's functions.
Each hydra matches a term of the notation system, and each move of the game lowers the term.
So every hydra game ends, but $\Pi^1_1\text{-}\mathrm{CA} + \mathrm{BI}$ cannot prove this.
The ordinal thus gives a natural combinatorial statement that the theory leaves open.

### The name

The ordinal is named after three proof theorists.
Gaisi Takeuti gave the first consistency proof of $\Pi^1_1$-comprehension, with ordinal diagrams.
Solomon Feferman introduced the $\theta$ functions, and Wilfried Buchholz introduced the $\psi$ functions that give the short name above.

## Explanations

### L1 human

Proof theorists measure the strength of a theory by a countable ordinal.
Stronger theories need larger ordinals, and better names for them.
Buchholz's functions give names with a ladder of infinities $\Omega_1, \Omega_2, \dots$ and its top $\Omega_\omega$.
The Takeuti-Feferman-Buchholz ordinal is the largest ordinal that these names reach.
It measures a strong part of second-order arithmetic, in which one can form sets defined by one quantifier over all sets.

### L2 human

We place the ordinal in the list of values of $\psi_0$, from the bottom up.
First, $\psi_0(\Omega) = \varepsilon_0$ is the ordinal of Peano arithmetic.
Next, $\psi_0(\Omega_2)$ is the Bachmann-Howard ordinal, the ordinal of $\mathrm{ID}_1$.
Then $\psi_0(\Omega_\omega)$ is the ordinal of $\Pi^1_1\text{-}\mathrm{CA}_0$.
Finally, the argument $\varepsilon_{\Omega_\omega + 1}$ ends the system, since larger arguments give the same value, and $\psi_0(\varepsilon_{\Omega_\omega + 1})$ is the ordinal of $\mathrm{ID}_\omega$.

The ordinal serves as a benchmark.
An ordinal analysis of a new theory places its ordinal below, at or above it, and beyond it one needs stronger notations such as [[Rathjen's psi function|M7D1HEJQVH]].
