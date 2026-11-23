---
tag: YZHC2B7YT5
kind: example
name: Concatenation of codes is primitive recursive
msc: ["03F40", "03D20"]
topics: [HXHHWY3328]
audience: grad
instance_of: [6M12VR1GT6]
uses: [MFJXPAF0R0, 5NVA2JRHPV, QQQRJA90EP]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_function
    locator: lead section
  - book: isbn:9780521857840
---

## Example

The string $0$ has code $2^{13}$ and the string $= 0$ has code $2^{7} 3^{13}$, and joining them should give $0 = 0$, with code $2^{13} 3^{7} 5^{13}$.
We define the operation on codes that does this in general, and we show that it is [[primitive recursive|5NVA2JRHPV]].

We use the prime-power [[Gödel numbering|MFJXPAF0R0]]: a string $s_1 \cdots s_n$ has code $p_1^{c(s_1)} \cdots p_n^{c(s_n)}$, where $p_1 = 2, p_2 = 3, \ldots$ are the primes and each $c(s) \ge 1$.
Write $(x)_i$ for the exponent of $p_i$ in $x$, and $\mathrm{lh}(x)$ for the number of primes that divide $x$.
Concatenation of codes is
$$x * y = x \cdot \prod_{i = 1}^{\mathrm{lh}(y)} p_{\mathrm{lh}(x) + i}^{(y)_i}.$$

### The pieces are primitive recursive

1. The relation "$z$ is prime" is primitive recursive.
   It says $z \ge 2$ and $\forall u < z \, \forall v < z \, (u \cdot v \ne z)$, and bounded quantifiers keep primitive recursiveness.
2. The function $i \mapsto p_i$ is primitive recursive.
   We have $p_1 = 2$, and $p_{i+1}$ is the least prime $z$ with $p_i < z \le p_i ! + 1$.
   Euclid's argument shows that $p_i ! + 1$ has a prime factor above $p_i$, so the search is bounded.
3. The function $(x)_i$ is primitive recursive.
   For $x \ge 1$ it is the least $e < x$ such that $p_i^{e+1}$ does not divide $x$, a bounded search.
4. The function $\mathrm{lh}(x)$ is primitive recursive.
   It is the bounded sum over $i \le x$ of $1$ when $p_i$ divides $x$ and $0$ otherwise.

### The product does the joining

5. For a string code $x$ of length $n$, the primes that divide $x$ are exactly $p_1, \ldots, p_n$, because each exponent $c(s_j)$ is at least $1$.
   So $\mathrm{lh}(x) = n$.
6. Bounded products of primitive recursive functions are primitive recursive, so $x * y$ is primitive recursive.
7. If $x$ codes $s_1 \cdots s_n$ and $y$ codes $t_1 \cdots t_m$, the product puts the exponent $c(t_i)$ on $p_{n+i}$.
   So $x * y$ codes $s_1 \cdots s_n t_1 \cdots t_m$.
8. In the opening case, $x = 2^{13}$ has $\mathrm{lh}(x) = 1$, and $y = 2^{7} 3^{13}$ has $(y)_1 = 7$ and $(y)_2 = 13$.
   The formula gives
   $$x * y = 2^{13} \cdot 3^{7} \cdot 5^{13},$$
   which is the code of $0 = 0$.

## Remarks

Every search in steps 1 to 4 stops below a number that we can compute in advance.
That is the whole reason for primitive recursiveness, and the same pattern works for the other syntactic functions of the [[arithmetization of syntax|6M12VR1GT6]].
For example, with the codes $9$, $3$ and $11$ for $($, $\to$ and $)$, the code of $(\varphi \to \psi)$ is
$$2^{9} * x * 2^{3} * y * 2^{11},$$
where $x$ and $y$ are the codes of $\varphi$ and $\psi$.

The formula depends on the numbering.
With the [[bijective base-k numbering|4QSK8112QQ]], concatenation is $x * y = x \cdot k^{\ell(y)} + y$, where $\ell(y)$ is the length of the string coded by $y$.
It is primitive recursive for the same reason.

Watch out: the shift uses $\mathrm{lh}(x)$, the length of the first string.
If we shifted by $\mathrm{lh}(y)$ instead, the case above would give $2^{13} \cdot 5^{7} \cdot 7^{13}$, which has a gap at the prime $3$ and is no code at all.

## Explanations

### L1 human

Joining two pieces of text corresponds to an operation on their code numbers.
With prime-power codes, we move the primes of the second code past the primes of the first, and then multiply.
For example, "0" and "=0" join to "0=0", and the codes $2^{13}$ and $2^{7} \cdot 3^{13}$ give $2^{13} \cdot 3^{7} \cdot 5^{13}$.
Each step uses only counting, multiplying and dividing, so a simple program computes it.

### L2 human

We join the term $S0$, with code $2^{15} 3^{13}$, to the string $= 0$, with code $2^{7} 3^{13}$.
The first code has length $\mathrm{lh}(x) = 2$, so the exponents of $y$ move to the primes $p_3 = 5$ and $p_4 = 7$.
This gives
$$2^{15} \cdot 3^{13} * 2^{7} \cdot 3^{13} = 2^{15} \cdot 3^{13} \cdot 5^{7} \cdot 7^{13},$$
the code of the formula $S0 = 0$.
Building the code of a compound formula from the codes of its parts is the typical use, and it is how a theory of arithmetic describes the formation rules of formulas.
