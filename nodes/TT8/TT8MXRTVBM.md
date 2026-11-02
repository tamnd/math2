---
tag: TT8MXRTVBM
kind: definition
name: Robinson arithmetic
msc: [03F30]
defines: 3K1AKGXF8A
uses: [92SWXST1ZM, WDVVEYD6AT, 0QFT7Z76N5]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
---

## Definition

Let $L$ be the [[signature|WDVVEYD6AT]] with a constant symbol $0$, a unary function symbol $S$, and binary function symbols $+$ and $\cdot$.
*Robinson arithmetic* $\mathsf{Q}$ is the first-order [[theory|92SWXST1ZM]] in $L$ whose axioms are the universal closures of these seven formulas:

1. $S x \ne 0$;
2. $S x = S y \to x = y$;
3. $x \ne 0 \to \exists y\, (x = S y)$;
4. $x + 0 = x$;
5. $x + S y = S(x + y)$;
6. $x \cdot 0 = 0$;
7. $x \cdot S y = (x \cdot y) + x$.

## Remarks

Example: the natural numbers $\N$ with $0$, $S(n) = n + 1$, and the usual addition and multiplication satisfy all seven axioms, so they form a model of $\mathsf{Q}$.

Non-example: the integers $\Z$ with $S(n) = n + 1$ and the usual operations are not a model of $\mathsf{Q}$.
Axiom 1 fails, because $S(-1) = 0$.

$\mathsf{Q}$ is the [[Peano axioms|0QFT7Z76N5]] without the induction scheme, with axiom 3 added in its place.
$\mathsf{Q}$ does not prove $\forall x\, \forall y\, (x + y = y + x)$; there are models of $\mathsf{Q}$ in which addition is not commutative.
$\mathsf{Q}$ proves every true sentence of the form $\exists x_1 \cdots \exists x_n\, \varphi$ with $\varphi$ quantifier-free, and every computable function is representable in $\mathsf{Q}$.
