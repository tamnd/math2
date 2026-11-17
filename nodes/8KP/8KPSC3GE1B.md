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

Let $\mathrm{I\Sigma}_1$ be [[Peano arithmetic|0QFT7Z76N5]] with the [[induction schema|1QD0KDDGYJ]] only for $\Sigma_1$ formulas of the [[arithmetical hierarchy|7CVJCQKY41]].
As in [[the definition|C19Z3B6V4P]], we add a predicate $X$ and allow it in the $\Sigma_1$ formulas.
$\mathrm{I\Sigma}_1$ also proves induction for $\Pi_1$ formulas, a standard fact that we use.
We show $\abs{\mathrm{I\Sigma}_1} \ge \omega^\omega$ in full and cite the upper bound.

1. Notation. Code each ordinal below $\omega^\omega$ by its [[Cantor normal form|6GD30FGYDZ]] $\omega^{k-1} c_{k-1} + \cdots + \omega c_1 + c_0$, a finite list of numbers. The order $\prec$ compares the lists as in [[the comparison of Cantor normal forms|DXKWBFWCE0]], and it is primitive recursive.
2. Claim. For each $k$, $\mathrm{I\Sigma}_1$ proves: if $X$ is progressive along $\prec$, then $X(z)$ for all $z \prec \omega^k$. We prove this by induction on $k$, outside the theory.
3. Case $k = 0$. The only $z \prec \omega^0 = 1$ is $0$, and nothing lies below $0$. So progressiveness gives $X(0)$.
4. Step $k \to k + 1$. Assume that $X$ is progressive. Let $\psi(n)$ be $\forall z \, (z \prec \omega^k n \to X(z))$, a $\Pi_1$ formula in $X$.
5. $\psi(0)$ holds, since nothing lies below $0$.
6. Assume $\psi(n)$. Let $Y(x)$ be $X(\omega^k n + x)$, where the sum of codes is primitive recursive.
7. Each $z$ with $\omega^k n \preceq z \prec \omega^k (n+1)$ has the form $\omega^k n + y$ with $y \prec \omega^k$, by the Cantor normal form.
8. So if $Y(y)$ for all $y \prec x$, then $X(z)$ for all $z \prec \omega^k n + x$, by step 7 and $\psi(n)$. Progressiveness of $X$ gives $Y(x)$, so $Y$ is progressive below $\omega^k$.
9. The proof for $k$ works with $Y$ in place of $X$, since substituting a primitive recursive term into $X$ keeps the inductions $\Pi_1$. So $Y(x)$ for all $x \prec \omega^k$, which is $\psi(n + 1)$.
10. Induction for the $\Pi_1$ formula $\psi$ gives $\psi(n)$ for all $n$. Every $z \prec \omega^{k+1}$ lies below $\omega^k (c_k + 1)$, where $c_k$ is its coefficient of $\omega^k$. So $X(z)$ for all $z \prec \omega^{k+1}$.
11. Lower bound. Step 2 holds for each $k$, so $\abs{\mathrm{I\Sigma}_1} \ge \sup_k \omega^k = \omega^\omega$.
12. Upper bound (cited). $\mathrm{I\Sigma}_1$ proves the same $\Pi_2$ sentences as primitive recursive arithmetic, and the ordinal analysis of these theories gives no primitive recursive well-order of type $\omega^\omega$ or more. So $\abs{\mathrm{I\Sigma}_1} = \omega^\omega$.

## Remarks

Primitive recursive arithmetic has the same ordinal, $\abs{\mathrm{PRA}} = \omega^\omega$, and its provably total functions are the [[primitive recursive functions|5NVA2JRHPV]].
Raising the level of induction raises the ordinal by one exponential: $\abs{\mathrm{I\Sigma}_2} = \omega^{\omega^\omega}$, and in general $\abs{\mathrm{I\Sigma}_n}$ is the tower of $n + 1$ letters $\omega$.
The union of these theories is PA, and the supremum of the towers is $\varepsilon_0$.
In the proof above, each extra level $k$ needs one more induction on a $\Pi_1$ formula, but the complexity of the formula does not grow.
A proof up to $\omega^\omega$ itself would need an argument that is uniform in $k$.
The jump of [[transfinite induction in arithmetic|ZE54ABPMJ0]] is such an argument, but it raises the complexity beyond $\Pi_1$.

## Explanations

### L1 human

The theory $\mathrm{I\Sigma}_1$ is arithmetic in which induction may only be used for simple statements.
It can still prove induction along the ordinals $\omega$, $\omega^2$, $\omega^3$, and so on, one at a time.
It cannot go as far as $\omega^\omega$, the limit of these.
So its proof-theoretic ordinal is $\omega^\omega$, much smaller than the $\varepsilon_0$ of full Peano arithmetic.

### L2 human

We run the step from $k = 1$ to $k = 2$, so from $\omega$ to $\omega^2$.

1. The ordinals below $\omega^2$ are $\omega n + m$, coded by pairs $(n, m)$ and ordered by $n$ first, then $m$.
2. Assume $X$ is progressive. Let $\psi(n)$ say that $X$ holds of every $\omega n' + m$ with $n' < n$.
3. Given $\psi(n)$, let $Y(m) = X(\omega n + m)$. Everything below $\omega n + m$ is either below $\omega n$ or of the form $\omega n + m'$ with $m' < m$.
4. So $Y$ is progressive along the ordinary order of $\N$, and ordinary induction gives $Y(m)$ for all $m$. That is $\psi(n + 1)$.
5. Induction on $n$ gives $\psi(n)$ for all $n$, so $X$ holds below $\omega^2$.

The typical use is a lower bound: prove induction along $\omega^k$ by an outer induction on the coefficient and an inner induction below $\omega^{k-1}$.
The trap: this proves one theorem for each $k$; $\mathrm{I\Sigma}_1$ does not prove the single statement "for all $k$, induction along $\omega^k$".
