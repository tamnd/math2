---
tag: TKDKW5MENB
kind: example
name: The language of Presburger arithmetic is not the language of arithmetic
msc: ["03F30", "03B25"]
topics: [QHCRN4JVG0]
audience: ug2
not_instance_of:
  - target: D8SD54M5PN
    note: the signature has no symbol for multiplication, and multiplication is not definable from 0, S, + and < in the natural numbers
uses: [329ZG1Z0G5, 4W0E9G7PPV, CY1TXHF6KQ]
sources:
  - url: https://en.wikipedia.org/wiki/Presburger_arithmetic
    locator: Presburger-definable integer relation
  - book: isbn:9780122384523
---

## Example

Let $L_P$ be the signature $\{0, S, +, <\}$, and let $\mathfrak{P} = (\mathbb{N}, 0, S, +, <)$ be its standard structure.
$L_P$ is the language of [[Presburger arithmetic|4W0E9G7PPV]], up to the choice of $S$ or a constant $1$.
It is a part of the [[language of arithmetic|D8SD54M5PN]] $L_A$, but more than a symbol is missing: no $L_P$-formula defines multiplication in $\mathfrak{P}$.
We prove this with the perfect squares.

We use Presburger's quantifier elimination as a known fact.
Add to $L_P$ a binary relation symbol $\equiv_n$ for each $n \ge 2$, read as congruence modulo $n$.
In this expansion of $\mathfrak{P}$, every formula is equivalent to a quantifier-free formula.
Call a set $A \subseteq \mathbb{N}$ eventually periodic if there are $N$ and $p \ge 1$ with $a \in A \leftrightarrow a + p \in A$ for all $a \ge N$.

1. A term in one variable $x$ of the expanded language has the value $k x + c$ for some $k, c \in \mathbb{N}$.
2. An atomic formula $k x + c = k' x + c'$ defines a set with at most one element or all of $\mathbb{N}$, so it is eventually periodic with $p = 1$.
3. An atomic formula $k x + c < k' x + c'$ defines a finite set or a set that contains all large $x$, so it is eventually periodic with $p = 1$.
4. An atomic formula $k x + c \equiv_n k' x + c'$ defines a set with period $n$, since replacing $x$ by $x + n$ adds multiples of $n$ to both sides.
5. If $A$ and $B$ are eventually periodic with data $(N, p)$ and $(N', p')$, then $A \cap B$ and $\mathbb{N} \setminus A$ are eventually periodic, with threshold $\max(N, N')$ and period $p p'$.
6. By quantifier elimination and steps 2 to 5, every subset of $\mathbb{N}$ definable in $\mathfrak{P}$ is eventually periodic.
7. Suppose that an $L_P$-formula $\mu(x, y, z)$ defines the relation $x \cdot y = z$ in $\mathfrak{P}$.
   Then $\exists y\, \mu(y, y, x)$ defines the set $Q$ of squares.
8. Take any $N$ and $p \ge 1$, and choose $k \ge \max(N, p)$.
   Then $k^2 \in Q$ and $k^2 \ge N$.
9. The next square after $k^2$ is $k^2 + 2k + 1 > k^2 + p$, so $k^2 + p \notin Q$.
10. So $Q$ is not eventually periodic, which contradicts step 6.
    Hence no such $\mu$ exists.

## Remarks

The example shows that $\cdot$ is the decisive symbol of $L_A$.
Without it, the true sentences of $\mathfrak{P}$ form a decidable set, by Presburger's theorem.
With it, the true sentences of $\mathfrak{N}$ form a set that is not even arithmetical, by [[Tarski's undefinability theorem|YRV6SYK2BY]].
So passing from $\{0, S, +, <\}$ to $L_A$ is not an [[extension by definitions|GCK0NN60E4]].
Adding $<$ to $\{0, S, +, \cdot\}$ is one, in contrast, since $\exists v\, (v + S x = y)$ defines $x < y$.

Step 6 also shows that the set of primes is not definable in $\mathfrak{P}$.
An infinite eventually periodic set has bounded gaps, and the gaps between primes are unbounded.

## Explanations

### L1 human

Presburger arithmetic talks about whole numbers with zero, "next", plus and "less than", but without "times".
You might hope to write "times" as repeated plus.
That fails: "$x$ times $y$" needs a number of additions that depends on $y$, and a formula has a fixed length.
In fact the only sets of numbers that this language can describe repeat with a fixed period from some point on.
The perfect squares $0, 1, 4, 9, 16, \ldots$ do not repeat like that, because the gaps between them keep growing.

### L2 human

Multiplication by a fixed number is still expressible.
The formula $z = x + x + x$ says $z = 3 x$, and it is an $L_P$-formula, since $3$ is fixed.
A formula for $z = x \cdot y$ would need $y$ copies of $x$, and $y$ varies.
The proof shows that no clever formula avoids this, because such a formula would define the squares.
Their gaps are
$$1 - 0 = 1, \quad 4 - 1 = 3, \quad 9 - 4 = 5, \quad 16 - 9 = 7, \ldots,$$
and they grow without bound, so the squares are not eventually periodic.

This is why the incompleteness theorems need multiplication.
Watch out: missing symbols are not always harmless.
You can drop $<$ from $L_A$ without loss, but you cannot drop $\cdot$.
