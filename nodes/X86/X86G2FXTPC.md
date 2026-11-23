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

Arithmetic with multiplication but without addition is decidable: a machine can settle every sentence about the natural numbers that uses only $\cdot$ and equality.
For example, it decides that there are infinitely many prime numbers, because "prime" and "divides" can be said with multiplication alone.

Skolem arithmetic is the [[theory|92SWXST1ZM]] $\operatorname{Th}(\mathbb{N}, \cdot)$ of the [[natural numbers|0MWKJ44V5A]] with multiplication alone.
Let $S$ be the successor function $S(x) = x + 1$, and let $<$ be the usual order of $\mathbb{N}$.

1. Decidability.
   $\operatorname{Th}(\mathbb{N}, \cdot)$ is a [[decidable theory|HWC687ES0Q]].
2. Undecidability with successor or order.
   $\operatorname{Th}(\mathbb{N}, S, \cdot)$ and $\operatorname{Th}(\mathbb{N}, <, \cdot)$ are not decidable.

The [[proof|CCZQ86VX9A]] uses prime factorization for part 1 and a polynomial identity for part 2.

## Remarks

### A first decision

Take the sentence $\exists x \, \exists y \, \exists p \, (p \text{ prime} \wedge x \ne 0 \wedge x \cdot x = y \cdot y \cdot p)$.
Here $x \ne 0$ can be said with multiplication, since $0$ is the only $z$ with $\forall w \, (z \cdot w = z)$.
If $x \ne 0$, then $y \ne 0$, so $x$, $y$ and $p$ are positive.

Write each positive number by the exponents in its prime factorization: $x$, $y$ and $p$ become exponent sequences $e$, $f$ and $\epsilon$.
The sequence $\epsilon$ has $1$ at the prime $p$ and $0$ elsewhere.
Multiplication becomes addition of exponents, so the equation becomes $2 e = 2 f + \epsilon$.
At the prime $p$ this reads $2 e_p = 2 f_p + 1$, which says that an even number equals an odd number.
So the sentence is false: no prime has a rational square root.
Check: for $p = 2$, the squares $x \cdot x$ have an even exponent of $2$, while $y \cdot y \cdot 2$ has an odd one.

### Why each hypothesis is needed

Part 1 needs the absence of $S$ and $<$, by part 2.

Part 2 needs multiplication.
The theories $\operatorname{Th}(\mathbb{N}, S)$ and $\operatorname{Th}(\mathbb{N}, <)$ are decidable, and so is [[Presburger arithmetic|4W0E9G7PPV]] $\operatorname{Th}(\mathbb{N}, 0, 1, +)$.
So multiplication alone and order alone are tame, but together they define addition.

### What it gives you

Divisibility $x \mid y$ is [[definable|CY1TXHF6KQ]] by $\exists z \, (x \cdot z = y)$, so $\operatorname{Th}(\mathbb{N}, \mid)$ is decidable.

The set of [[prime numbers|01826KMG2H]] is definable in $(\mathbb{N}, \cdot)$.
The number $1$ is the only $u$ with $\forall y \, (u \cdot y = y)$.
A number $p$ is prime when $p \ne 0$, $p \ne 1$ and $\forall y \, \forall z \, (y \cdot z = p \to y = 1 \vee z = 1)$.

The sentence $\forall x \, (x \ne 0 \to \exists p \, (p \text{ prime} \wedge \neg (p \mid x)))$ says that there are infinitely many primes.
If there were only finitely many, their product $x$ would be divisible by all of them.
Part 1 decides this sentence.

Addition is not definable in $(\mathbb{N}, \cdot)$.
If it were, the theory of $(\mathbb{N}, +, \cdot)$ would reduce to $\operatorname{Th}(\mathbb{N}, \cdot)$ and would be decidable, against part 2.

### Definable and not definable

If a relation is definable in $(\mathbb{N}, \cdot)$, then adding it to the structure keeps the theory decidable, because each new atom can be replaced by its definition.
So part 2 shows that $S$ and $<$ are not definable in $(\mathbb{N}, \cdot)$.
Automorphisms show this directly.
Each permutation of the primes extends to an automorphism of $(\mathbb{N}, \cdot)$, so not even the number $2$ is definable.
But $2 = S(S(0))$, and $S$ is definable from $<$, so neither $S$ nor $<$ is definable.

### Watch out

"Prime" and "divides" do not bring addition back.
They are definable from multiplication, but "$p + 2$ is prime" is not, so statements about twin primes or the Goldbach conjecture are outside the language.

The number $0$ behaves differently from the positive numbers, since $0 \cdot x = 0$ for all $x$.
The factorization argument works for the positive numbers, and the proof treats $0$ by a separate case split.

### Generalizations

The method gives the decidability of every weak direct power of a structure with a decidable theory, by the theorem of Mostowski.
For example, $(\mathbb{Q}_{> 0}, \cdot)$ is a weak direct power of $(\mathbb{Z}, +)$, with one factor for each prime, and its theory is decidable.
The Feferman-Vaught theorem extends the method to direct products and generalized products of structures.

### Try it

Is the sentence $\forall x \, \exists y \, (y \cdot y = x)$ true in $(\mathbb{N}, \cdot)$?
No: $2$ is not a square, since its exponent of $2$ is odd.

Is the set of powers of $2$ definable in $(\mathbb{N}, \cdot)$?
No: the automorphism that swaps the primes $2$ and $3$ maps $4$ to $9$, and a definable set is mapped to itself.

## History

The theory of multiplication of natural numbers is named after Thoralf Skolem.
Mostowski proved in 1952 that the theory of a weak direct power of a structure is decidable when the theory of the structure is decidable, and this gives part 1.
Feferman and Vaught generalized the method to products of structures in 1959.
Julia Robinson showed in 1949 that addition is definable from successor and multiplication, and this gives part 2.

## Explanations

### L1 human

Skolem arithmetic talks about whole numbers using only multiplication.
In this language one can say "$6$ is divisible by $3$" and "there are infinitely many prime numbers", and a computer can decide every such statement.
The reason is that a number is described by the exponents in its prime factorization, and multiplying numbers adds the exponents.
So multiplication becomes addition on many copies of the whole numbers, and addition alone is decidable.
But if one also allows "plus one", the language becomes as strong as full arithmetic, and no computer can decide all statements.

### L2 human

We decide $\forall x \, \forall y \, (x \cdot x = y \cdot y \to x = y)$ in $(\mathbb{N}, \cdot)$, with the method of the [[proof|CCZQ86VX9A]].
First split off the number $0$.
If $x = 0$, then $y \cdot y = 0$, so $y = 0 = x$, and the same holds if $y = 0$.
If $x$ and $y$ are positive, they become exponent sequences $e$ and $f$, and the equation becomes $2 e = 2 f$.
Then $e = f$ at every prime, so $x = y$.
So the sentence is true.
Check: in $\mathbb{Z}$ it would fail, with $x = 1$ and $y = -1$, but $\mathbb{N}$ has no negative numbers.

The typical use of the theorem is to show that a property of numbers expressed with multiplication alone is decidable.
Watch out: the reduction to exponents works only for positive numbers, so the case $0$ always needs its own check.

### L3 human

The proof shows that $(\mathbb{N}_{> 0}, \cdot)$ is the weak direct power $(\mathbb{N}, +)^{(\omega)}$.
The theory of a weak power is controlled by the theory of the factor and by the theory of the Boolean algebra of finite and cofinite index sets.
This is the Feferman-Vaught method, which reduces sentences about products to sentences about the factors and about the index structure.
The undecidability with successor is an instance of interpretation: once addition and multiplication are definable, the [[essential undecidability|9JDDFN8PT7]] of $\mathsf{Q}$ transfers.
