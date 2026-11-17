---
tag: X86G2FXTPC
kind: statement
role: theorem
name: Skolem arithmetic
aliases: [decidability-of-skolem-arithmetic, theory-of-multiplication-of-natural-numbers]
msc: ["03B25", "03C10", "11U09"]
topics: [E4AVTNWE9E]
audience: research
about: [HWC687ES0Q]
uses: [HWC687ES0Q, 92SWXST1ZM, 0MWKJ44V5A, 084HH1NDCB, 4W0E9G7PPV, CY1TXHF6KQ, 9JDDFN8PT7]
history:
  first_stated: "1952"
  notes: Andrzej Mostowski proved in 1952 that weak direct powers preserve decidability, which gives the decidability of the theory of multiplication. Julia Robinson showed in 1949 that addition is definable from successor and multiplication.
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Feferman%E2%80%93Vaught_theorem
    locator: lead section
---

## Statement

Skolem arithmetic is the [[theory|92SWXST1ZM]] $\operatorname{Th}(\N, \cdot)$ of the [[natural numbers|0MWKJ44V5A]] with multiplication alone.
Let $S$ be the successor function $S(x) = x + 1$, and let $<$ be the usual order of $\N$.

1. $\operatorname{Th}(\N, \cdot)$ is a [[decidable theory|HWC687ES0Q]].
2. $\operatorname{Th}(\N, S, \cdot)$ and $\operatorname{Th}(\N, <, \cdot)$ are not decidable.

## Remarks

### Why each hypothesis is needed

- Part 1 needs the absence of $S$ and $<$, by part 2.
- Part 2 needs multiplication: the theories $\operatorname{Th}(\N, S)$ and $\operatorname{Th}(\N, <)$ are decidable, and so is [[Presburger arithmetic|4W0E9G7PPV]] $\operatorname{Th}(\N, 0, 1, +)$.
- So multiplication alone and order alone are tame, and their combination already defines addition.

### Consequences

1. Divisibility $x \mid y$ is [[definable|CY1TXHF6KQ]] by $\exists z \, (x \cdot z = y)$, so $\operatorname{Th}(\N, \mid)$ is decidable.
2. The set of [[prime numbers|01826KMG2H]] is definable in $(\N, \cdot)$. The number $1$ is the unique $u$ with $\forall y \, (u \cdot y = y)$, and $p$ is prime when $p \ne 1$, $p \ne 0$ and $\forall y \, \forall z \, (y \cdot z = p \to y = 1 \vee z = 1)$.
3. "There are infinitely many primes" is expressed by $\forall x \, (x \ne 0 \to \exists p \, (p \text{ prime} \wedge \neg (p \mid x)))$, and part 1 decides it. Statements on twin primes or on the Goldbach conjecture use $+$ and are not in the language.
4. Addition is not definable in $(\N, \cdot)$. Otherwise the theory of $(\N, +, \cdot)$ would reduce to $\operatorname{Th}(\N, \cdot)$, and it would be decidable, against part 2.

### Converse

Part 1 has a partial converse in the opposite direction: adding to $(\N, \cdot)$ a relation that is definable in $(\N, \cdot)$ keeps the theory decidable, by translation.
So the undecidability in part 2 shows that $S$ and $<$ are not definable in $(\N, \cdot)$.
This also follows from automorphisms: each permutation of the primes extends to an automorphism of $(\N, \cdot)$, so even the number $2$ is not definable.

### Generalizations

- The method gives the decidability of every weak direct power of a structure with a decidable theory, by the theorem of Mostowski. For example, $(\Q_{> 0}, \cdot)$ is a weak direct power of $(\Z, +)$, and its theory is decidable.
- The Feferman-Vaught theorem extends the method to direct products and generalized products of structures.
- The theory of $(\N, \cdot)$ with the coprimality relation, and other enrichments by relations definable in $(\N, \cdot)$, stay decidable.

## History

The theory of multiplication of natural numbers is named after Thoralf Skolem.
Mostowski proved in 1952 that the theory of a weak direct power of a structure is decidable when the theory of the structure is decidable, and this gives part 1.
Feferman and Vaught generalized the result to products of structures in 1959.
Julia Robinson showed in 1949 that addition is definable from successor and multiplication, which gives part 2.

## Explanations

### L1 human

Skolem arithmetic talks about whole numbers using only multiplication.
In this language one can say "$6$ is divisible by $3$" and "there are infinitely many prime numbers", and a computer can decide every such statement.
The reason is that a number is described by the exponents in its prime factorization, and multiplying numbers adds the exponents.
So multiplication becomes addition on many copies of the whole numbers, and addition alone is decidable.
But if one also allows "plus one", the language becomes as strong as full arithmetic, and no computer can decide all statements.

### L2 human

We check with the [[proof|CCZQ86VX9A]] that the sentence $\exists x \, \exists y \, \exists p \, (p \text{ prime} \wedge x \ne 0 \wedge x \cdot x = y \cdot y \cdot p)$ is false.
Here $x \ne 0$ is definable, since $0$ is the unique $z$ with $\forall w \, (z \cdot w = z)$.

1. If $x \ne 0$ and $x \cdot x = y \cdot y \cdot p$, then $y \ne 0$, so $x$, $y$ and $p$ are positive.
2. Under the factorization map, $x$, $y$ and $p$ become exponent sequences $e$, $f$ and $\epsilon$, where $\epsilon$ has $1$ at the prime $p$ and $0$ elsewhere.
3. Multiplication becomes addition, so the equation becomes $2 e = 2 f + \epsilon$.
4. At the prime $p$, this reads $2 e_p = 2 f_p + 1$, an equation between an even and an odd number.
5. So no solution exists, and the sentence is false: no prime has a rational square root.

The typical use of the theorem is to show that a property of numbers expressed with multiplication alone is decidable.
A trap is to think that "prime" and "divides" bring addition back; they are definable from multiplication, but "$p + 2$ is prime" is not.

### L3 human

The proof shows that $(\N_{> 0}, \cdot)$ is the weak direct power $(\N, +)^{(\omega)}$.
The theory of a weak power is controlled by the theory of the factor and by the theory of the Boolean algebra of finite and cofinite index sets.
This is the Feferman-Vaught method, which reduces sentences about products to sentences about the factors and about the index structure.
The undecidability with successor is an instance of interpretation: once addition and multiplication are definable, the [[essential undecidability|9JDDFN8PT7]] of $\mathsf{Q}$ transfers.
