---
tag: 8KPSC3GE1B
kind: example
name: The proof-theoretic ordinal of IΣ1 is ω^ω
msc: ["03F15", "03F30"]
topics: [XTTKZTYDSD]
audience: grad
instance_of: [C72RBH0CDR]
uses: [C19Z3B6V4P, 1QD0KDDGYJ, 7CVJCQKY41, 6GD30FGYDZ, DXKWBFWCE0, 0QFT7Z76N5, 5NVA2JRHPV]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
---

## Example

The theory $\mathrm{I\Sigma}_1$ is [[Peano arithmetic|0QFT7Z76N5]] with the [[induction schema|1QD0KDDGYJ]] only for $\Sigma_1$ formulas of the [[arithmetical hierarchy|7CVJCQKY41]].
As in [[the definition|C19Z3B6V4P]], we add a predicate $X$ and allow it in these formulas.
We use the standard fact that $\mathrm{I\Sigma}_1$ also proves induction for $\Pi_1$ formulas.
We show $\lvert \mathrm{I\Sigma}_1 \rvert \ge \omega^\omega$ in full, and we cite the upper bound.

### The claim

Code each ordinal below $\omega^\omega$ by its [[Cantor normal form|6GD30FGYDZ]] $\omega^{k-1} c_{k-1} + \cdots + \omega c_1 + c_0$, a finite list of numbers.
The order $\prec$ compares two lists as in [[the comparison of Cantor normal forms|DXKWBFWCE0]], and it is primitive recursive.

Claim: for each $k$, $\mathrm{I\Sigma}_1$ proves that if $X$ is progressive along $\prec$ on the elements below $\omega^k$, then $X(z)$ for all $z \prec \omega^k$.
We prove the claim by induction on $k$, outside the theory.
For $k = 0$, the only $z \prec \omega^0 = 1$ is $0$, and nothing lies below $0$, so progressiveness gives $X(0)$.

### The induction step

We go from $k$ to $k + 1$.

1. Assume that $X$ is progressive below $\omega^{k+1}$, and let $\psi(n)$ be $\forall z \, (z \prec \omega^k n \to X(z))$.
   This is a $\Pi_1$ formula in $X$.
2. The formula $\psi(0)$ holds, since nothing lies below $0$.
3. Assume $\psi(n)$, and let $Y(x)$ be $X(\omega^k n + x)$.
   The sum of two codes is a primitive recursive function, so $Y$ is again a formula of the same form.
4. Each $z$ with $\omega^k n \preceq z \prec \omega^k (n+1)$ is $\omega^k n + y$ for some $y \prec \omega^k$, by the Cantor normal form.
5. If $Y(y)$ holds for all $y \prec x$, then $X(z)$ holds for all $z \prec \omega^k n + x$, by step 4 and $\psi(n)$.
   Progressiveness of $X$ then gives $Y(x)$, so $Y$ is progressive below $\omega^k$.
6. The claim for $k$ works with $Y$ in place of $X$, and it gives $Y(x)$ for all $x \prec \omega^k$.
   That is $\psi(n + 1)$.
7. Induction for the $\Pi_1$ formula $\psi$ gives $\psi(n)$ for all $n$.
   Every $z \prec \omega^{k+1}$ lies below $\omega^k (c + 1)$, where $c$ is its coefficient of $\omega^k$, so $X(z)$ for all $z \prec \omega^{k+1}$.

### The value

The claim holds for each $k$, so $\lvert \mathrm{I\Sigma}_1 \rvert \ge \sup_k \omega^k = \omega^\omega$.
For the upper bound we cite the ordinal analysis of $\mathrm{I\Sigma}_1$: it proves induction along no primitive recursive well-order of type $\omega^\omega$ or more.
So $\lvert \mathrm{I\Sigma}_1 \rvert = \omega^\omega$.

## Remarks

### What the example shows

Each extra power of $\omega$ costs one more induction on a $\Pi_1$ formula, but the complexity of the formula does not grow.
So $\mathrm{I\Sigma}_1$ reaches every $\omega^k$, one proof for each $k$.
A proof up to $\omega^\omega$ itself would need one argument for all $k$ at once.
Gentzen's jump in [[transfinite induction in arithmetic|ZE54ABPMJ0]] is such an argument, but it raises the complexity of the formulas beyond $\Pi_1$.

### Changing the amount of induction

Primitive recursive arithmetic has the same ordinal, $\lvert \mathrm{PRA} \rvert = \omega^\omega$, and its provably total functions are the [[primitive recursive functions|5NVA2JRHPV]].
More induction raises the ordinal by one exponential: $\lvert \mathrm{I\Sigma}_2 \rvert = \omega^{\omega^\omega}$, and $\lvert \mathrm{I\Sigma}_n \rvert$ is the tower of $n + 1$ letters $\omega$.
The union of the theories $\mathrm{I\Sigma}_n$ is PA, and the supremum of the towers is $\varepsilon_0 = \lvert \mathrm{PA} \rvert$.

## Explanations

### L1 human

The theory $\mathrm{I\Sigma}_1$ is arithmetic in which induction may only be used for simple statements.
It can still prove induction along $\omega$, $\omega^2$, $\omega^3$, and so on, one at a time.
It cannot reach $\omega^\omega$, the limit of these, so its proof-theoretic ordinal is $\omega^\omega$.
That is much smaller than the $\varepsilon_0$ of full Peano arithmetic.

### L2 human

We run the step from $k = 1$ to $k = 2$, so from $\omega$ to $\omega^2$.

1. The ordinals below $\omega^2$ are $\omega n + m$, coded by pairs $(n, m)$ and ordered by $n$ first, then by $m$.
2. Assume that $X$ is progressive, and let $\psi(n)$ say that $X$ holds at every $\omega n' + m$ with $n' < n$.
3. Given $\psi(n)$, let $Y(m)$ be $X(\omega n + m)$.
   Everything below $\omega n + m$ is either below $\omega n$ or of the form $\omega n + m'$ with $m' < m$.
4. So $Y$ is progressive along the usual order of $\mathbb{N}$, and ordinary induction gives $Y(m)$ for all $m$, which is $\psi(n + 1)$.
5. Induction on $n$ gives $\psi(n)$ for all $n$, so $X$ holds below $\omega^2$.

The typical use is a lower bound: an outer induction on the leading coefficient and an inner induction below the lower power.
Watch out: this gives one theorem for each $k$, and $\mathrm{I\Sigma}_1$ does not prove the single statement "for all $k$, induction holds below $\omega^k$".
That single statement would give induction below $\omega^\omega$.
