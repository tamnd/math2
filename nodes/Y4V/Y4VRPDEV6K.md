---
tag: Y4VRPDEV6K
kind: example
name: Coding sentences by their truth value
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
not_instance_of:
  - target: MFJXPAF0R0
    fails: [2, 3]
    note: "The map is injective, but it is not computable, and its set of codes is not decidable."
uses: [MFJXPAF0R0, YRV6SYK2BY, PPGD5KW8JC]
sources:
  - url: https://en.wikipedia.org/wiki/Tarski%27s_undefinability_theorem
    locator: lead section
---

## Example

Let $g$ be the prime-power [[Gödel numbering|MFJXPAF0R0]] of the strings of the language $\{0, S, +, \cdot\}$.
Define a new map $h$ on strings by
$$h(w) = \begin{cases} 2 g(w) & \text{if } w \text{ is a sentence true in } \mathbb{N}, \\ 2 g(w) + 1 & \text{otherwise.} \end{cases}$$
For example, $h(0 = 0) = 2 g(0 = 0)$ is even, and $h(0 = S0) = 2 g(0 = S0) + 1$ is odd.
We check which conditions of a Gödel numbering hold.

1. Injectivity holds.
   If $h(w) = h(w')$, then the two values have the same parity, and halving and rounding down gives $g(w) = g(w')$.
   Since $g$ is injective, $w = w'$.
2. Computability fails.
   Suppose that $h$ were computable.
   Then the set of true sentences would be a [[computable set|PPGD5KW8JC]]: to decide whether a sentence $w$ is true, compute $h(w)$ and check whether it is even.
3. Every computable set of numbers is definable in $\mathbb{N}$, by the formula that represents it in $\mathsf{Q}$.
   So the set of codes of true sentences would be definable in $\mathbb{N}$.
   This contradicts [[Tarski's undefinability theorem|YRV6SYK2BY]], so $h$ is not computable.
4. Decidability of the set of codes fails.
   For a sentence $w$, the number $2 g(w)$ is a value of $h$ exactly when $w$ is true.
   So a procedure that decides the set of values of $h$ would decide truth, which step 3 rules out.

## Remarks

The map $h$ carries the same information as $g$ plus one extra bit, the truth value, and that bit is not computable.
So injectivity alone does not make a Gödel numbering.
Arithmetic can describe syntax only through a numbering that is computable and has a decidable set of codes.

Change the extra bit and the picture changes.
With "provable in Peano arithmetic" in place of "true in $\mathbb{N}$", step 2 still fails, now because provability in $\mathsf{PA}$ is undecidable.
With "is a sentence" in place of "is a true sentence", the map becomes computable, because the set of sentences is decidable, and $h$ is a Gödel numbering.

## Explanations

### L1 human

Imagine a code for statements in which true statements get even numbers and false ones get odd numbers.
Different statements still get different numbers, so nothing is lost.
But to compute the code of a statement, you must first know whether it is true.
No machine can do that for all statements about whole numbers, so this code cannot be computed.

### L2 human

We compute what we can.
The sentence $0 = 0$ is true, so its value is $2 g(0 = 0)$, an even number.
The sentence $0 = S0$ is false, so its value is $2 g(0 = S0) + 1$, an odd number.
For the sentence of arithmetic that expresses the Goldbach conjecture, nobody knows today which parity to use, and Tarski's theorem says that no single procedure handles every sentence.
The typical use of this example is to separate the conditions in the definition of a Gödel numbering.
Watch out: a map defined by cases on a property is computable only when the property is decidable.
