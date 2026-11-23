---
tag: VK6WWSDMXK
kind: example
name: The closed terms of zero and successor are the numerals
msc: ["03B10", "03F30"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [6D3WA7N2W4]
uses: [6D3WA7N2W4, BQQ0FPFZ67, 12MQ2NJ29A, 0QFT7Z76N5, 2BVB7YDEV4]
sources:
  - url: https://en.wikipedia.org/wiki/Term_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: lead section
---

## Example

With only "zero" and "the next number" you can name every natural number, and nothing else.
Let $\sigma = \{ 0, S \}$, with a constant symbol $0$ and a unary function symbol $S$.
For $n \in \mathbb{N}$ let the *numeral* $\underline{n}$ be the string $S(S(\cdots S(0) \cdots))$ with $n$ copies of $S$, so $\underline{3} = S(S(S(0)))$.
We check that the closed [[terms|6D3WA7N2W4]] of $\sigma$ are exactly the numerals.

1. The numeral $\underline{0}$ is $0$, a term by the clause for constant symbols.
2. If $\underline{n}$ is a term, then $\underline{n+1} = S(\underline{n})$ is a term by the clause for function symbols.
   By induction on $n$, every numeral is a term.
3. Numerals contain no variables, so they are closed terms.
4. Conversely, let $t$ be a closed term, and use [[structural induction|12MQ2NJ29A]] on $t$ by the clauses of the [[definition|BQQ0FPFZ67]].
5. The variable clause does not apply, because $t$ is closed.
6. If $t$ is the constant symbol $0$, then $t = \underline{0}$.
7. If $t = S(t')$, then $t'$ is closed, so by the induction hypothesis $t' = \underline{n}$ for some $n$, and $t = \underline{n+1}$.
8. Different $n$ give different strings, since $\underline{n}$ has exactly $n$ copies of $S$.

So $n \mapsto \underline{n}$ is a bijection from $\mathbb{N}$ onto the closed terms of $\sigma$.

## Remarks

In the standard structure $\mathbb{N}$, the value of $\underline{n}$ is the number $n$, as induction on $n$ shows.
In the language of [[Peano arithmetic|0QFT7Z76N5]], with $+$ and $\cdot$ added, there are many more closed terms, such as $\underline{2} + \underline{3}$.
Each of them has the same value in $\mathbb{N}$ as some numeral, but as a string it is not a numeral.
The set of closed terms is the [[Herbrand universe|2BVB7YDEV4]] of $\sigma$.
If we drop the constant $0$, the signature $\{ S \}$ has no closed terms at all, because every term then has a variable at its bottom leaf.

## Explanations

### L1 human

With the symbols $0$ and $S$ for "zero" and "the next number", you can write $0$, $S(0)$, $S(S(0))$ and so on.
These strings are names for $0, 1, 2, \dots$.
Without variables, nothing else can be written.
So the closed terms are exactly these names.

### L2 human

We list the closed terms of $\sigma$ by height, where the height counts the nested copies of $S$.
At height $0$ the only closed term is $0$.
At height $1$ the only one is $S(0)$, because the argument of $S$ must be a closed term of height $0$.
At height $2$ the only one is $S(S(0))$, and in the same way each height has exactly one closed term, the numeral of that height.
The typical use of numerals is to name natural numbers inside formal arithmetic, for example in Gödel numbering, where $\underline{n}$ stands for the code $n$.
Watch out: $\underline{2} + \underline{3}$ and $\underline{5}$ are different terms with the same value.
