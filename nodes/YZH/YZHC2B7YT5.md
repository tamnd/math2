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

We use the prime-power [[Gödel numbering|MFJXPAF0R0]]: a string $s_1 \cdots s_n$ has code $p_1^{c(s_1)} \cdots p_n^{c(s_n)}$, where $p_1 = 2, p_2 = 3, \ldots$ are the primes and each $c(s) \ge 1$.
Define the concatenation function on codes by
$$x * y = x \cdot \prod_{i = 1}^{\mathrm{lh}(y)} p_{\mathrm{lh}(x) + i}^{(y)_i},$$
where $(x)_i$ is the exponent of $p_i$ in $x$ and $\mathrm{lh}(x)$ is the number of primes that divide $x$.
We show that $*$ is [[primitive recursive|5NVA2JRHPV]] and that it computes the code of the concatenated string.

1. The relation "$z$ is prime" is primitive recursive, since it says $z \ge 2$ and $\forall u < z \, \forall v < z \, (u \cdot v \ne z)$, with bounded quantifiers.
2. The function $i \mapsto p_i$ is primitive recursive: $p_1 = 2$ and $p_{i+1}$ is the least prime $z$ with $p_i < z \le p_i ! + 1$. Euclid's argument shows that such a $z$ exists, so the search is bounded.
3. The function $(x)_i$ is primitive recursive: it is the least $e < x$ such that $p_i^{e+1}$ does not divide $x$, a bounded search for $x \ge 1$.
4. The function $\mathrm{lh}(x)$ is primitive recursive: it is the bounded sum over $i \le x$ of $1$ when $p_i$ divides $x$ and $0$ otherwise.
5. For a string code $x$ of length $n$, the primes that divide $x$ are exactly $p_1, \ldots, p_n$, because each exponent $c(s_j)$ is at least $1$. So $\mathrm{lh}(x) = n$.
6. Bounded products of primitive recursive functions are primitive recursive, so the product in the definition is primitive recursive, and so is $x * y$.
7. If $x$ codes $s_1 \cdots s_n$ and $y$ codes $t_1 \cdots t_m$, the product puts the exponent $c(t_i)$ on $p_{n+i}$. So $x * y$ codes $s_1 \cdots s_n t_1 \cdots t_m$.
8. Check on a small case: $x = 2^{13}$ codes $0$, and $y = 2^{7} 3^{13}$ codes $= 0$. Then $\mathrm{lh}(x) = 1$, and $x * y = 2^{13} \cdot 3^{7} \cdot 5^{13}$, the code of $0 = 0$.

## Remarks

The same pattern shows that the other syntactic functions of [[arithmetization of syntax|6M12VR1GT6]] are primitive recursive.
For example, the code of $(\varphi \to \psi)$ is $2^{9} * x * 2^{3} * y * 2^{11}$, where $x$ and $y$ are the codes of $\varphi$ and $\psi$.
Every search in steps 1 to 4 is bounded by a number computed in advance, which is the reason for primitive recursiveness.
With the bijective base-$k$ numbering, concatenation is $x * y = x \cdot k^{\ell(y)} + y$, where $\ell(y)$ is the length, and it is primitive recursive in the same way.

## Explanations

### L1 human

Joining two pieces of text corresponds to an operation on their code numbers.
With prime-power codes, we shift the primes of the second code past the primes of the first and multiply.
For example, "0" and "=0" join to "0=0", and the codes $2^{13}$ and $2^{7} \cdot 3^{13}$ give $2^{13} \cdot 3^{7} \cdot 5^{13}$.
Each step uses only counting, multiplying and dividing, so a simple program computes it.

### L2 human

1. Read the exponents of $y = 2^{7} 3^{13}$: $(y)_1 = 7$ and $(y)_2 = 13$, and $\mathrm{lh}(y) = 2$.
2. Read the length of $x = 2^{13}$: $\mathrm{lh}(x) = 1$.
3. Put the exponent $7$ on $p_2 = 3$ and the exponent $13$ on $p_3 = 5$.
4. Multiply: $2^{13} \cdot 3^{7} \cdot 5^{13}$.

The typical use is to build the code of a compound formula from the codes of its parts.
A trap: the formula needs $\mathrm{lh}(x)$ for the first code, not the second, because the second string is shifted.
