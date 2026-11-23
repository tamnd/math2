---
tag: XQMNJF241J
kind: statement
role: theorem
name: Goodstein's theorem
msc: ["03F30", "03F15"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [0QFT7Z76N5, MPSCREYC3M, 0YSCSX5YZC, 6GD30FGYDZ, KT50SMH3EC, 0ZHQMQ2C1N]
about: [MPSCREYC3M, KT50SMH3EC]
history:
  first_stated: "1944"
  notes: "Goodstein proved termination in 1944 (J. Symbolic Logic, 'On the restricted ordinal theorem'). Kirby and Paris proved the unprovability in PA in 1982 (Bull. London Math. Soc., 'Accessible independence results for Peano arithmetic')."
sources:
  - url: https://en.wikipedia.org/wiki/Goodstein's_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Goodstein's_theorem
    locator: Sequence length as a function of the starting value
same_as:
  wikidata: Q1149185
  wikipedia: Goodstein's theorem
---

## Statement

Goodstein's theorem says that a simple game on whole numbers always ends, although the numbers first grow beyond all imagination, and that Peano arithmetic cannot prove this.

Let $b \ge 2$ be an integer.
Every integer $n \ge 1$ has a unique expansion $n = b^{e_1} c_1 + b^{e_2} c_2 + \cdots + b^{e_r} c_r$ with $e_1 > e_2 > \cdots > e_r \ge 0$ and $0 < c_i < b$.
The *hereditary base-$b$ notation* of $n$ is this expansion, with each exponent $e_i$ again written in hereditary base-$b$ notation.
Let $B_b(n)$ be the number that we get when we replace every $b$ in the hereditary base-$b$ notation of $n$ by $b + 1$, and let $B_b(0) = 0$.
The *Goodstein sequence* of $m \in \mathbb{N}$ is defined by $G_1 = m$ and $G_{k+1} = B_{k+1}(G_k) - 1$ as long as $G_k > 0$.
So the term $G_k$ is read in base $k + 1$.

**Theorem.**

1. For every $m \in \mathbb{N}$ the Goodstein sequence of $m$ reaches $0$: there is a $k$ with $G_k = 0$.
2. Statement 1, written as a $\Pi_2$ sentence of first-order arithmetic, is not provable in [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$.
3. Statement 1 is provable in $\mathsf{PA}$ plus [[transfinite induction|0ZHQMQ2C1N]] up to [[epsilon nought|KT50SMH3EC]] $\varepsilon_0$, and so it is provable in $\mathsf{ZFC}$.

The [[proof|J1NTZCSPPM]] proves parts 1 and 3 in full, and it gives part 2 with the cited lemmas marked.

## Remarks

### The sequence that starts at 3

Start with $G_1 = 3$ and write it in hereditary base $2$:
$$G_1 = 3 = 2^1 + 1.$$
Replace every $2$ by $3$ and subtract $1$:
$$G_2 = (3^1 + 1) - 1 = 3 = 3^1.$$
Now replace every $3$ by $4$ and subtract $1$:
$$G_3 = 4^1 - 1 = 3.$$
In base $4$ the number $3$ is a single digit, so a change of base does nothing to it.
From here on, each step only subtracts $1$, so $G_4 = 2$, $G_5 = 1$ and $G_6 = 0$.
The whole sequence is $3, 3, 3, 2, 1, 0$, and it ends at step $6$.

Notice what happened.
The number did not go down in the first two steps, but its notation became simpler: $2^1 + 1$, then $3^1$, then a single digit.
The proof turns this "simpler notation" into an ordinal that goes down at every step.

### The sequence that starts at 4

Now start with $G_1 = 4 = 2^{2^1}$, where even the exponent is written in base $2$.
The first step gives
$$G_2 = 3^{3^1} - 1 = 26 = 2 \cdot 3^2 + 2 \cdot 3 + 2.$$
The next steps change every $3$ into a $4$, then every $4$ into a $5$, and so on:
$$G_3 = (2 \cdot 4^2 + 2 \cdot 4 + 2) - 1 = 41, \qquad G_4 = (2 \cdot 5^2 + 2 \cdot 5 + 1) - 1 = 60.$$
Check: $32 + 8 + 2 - 1 = 41$ and $50 + 10 + 1 - 1 = 60$.
The sequence goes on $4, 26, 41, 60, 83, 109, 139, 173, \dots$ and grows for a very long time.

Why does it take so long?
Each step lowers only the last digit by $1$, while the base grows by $1$.
When the last digit is $0$, the next subtraction borrows from the digit before it, and the last digit refills to the new base minus $1$.
At base $5$ the number is $2 \cdot 5^2 + 2 \cdot 5 + 0$.
One step later, at base $6$, it is $2 \cdot 6^2 + 1 \cdot 6 + 5$, so $5$ more steps are needed before the next borrow.

### Why the base doubles

Follow the digits from base $5$ on.
At base $6$ the number is $2 \cdot 6^2 + 1 \cdot 6 + 5 = 83$.
The last digit runs down to $0$ at base $11$, where the number is $2 \cdot 11^2 + 11 = 253$.
The next borrow gives $2 \cdot 12^2 + 0 \cdot 12 + 11$, and the last digit runs down to $0$ at base $23$.
Each borrow from the middle digit takes the base from $b$ to about $2b$.

At base $24$ the top digit must lend:
$$2 \cdot 24^2 - 1 = 1151 = 1 \cdot 24^2 + 23 \cdot 24 + 23.$$
Check: $576 + 552 + 23 = 1151$.
Now the middle digit is $23$, and each of its $23$ borrows doubles the base again.
After them the base is $24 \cdot 2^{23} = 3 \cdot 2^{26}$, and one more run of the last digit brings the number to $b^2$ at base $b = 3 \cdot 2^{27} - 1 = 402653183$.
The term $b^2$ then needs about $b$ more doublings.
The sequence of $4$ reaches $0$ at base $3 \cdot 2^{402653211} - 1$, so after $3 \cdot 2^{402653211} - 2$ steps, a number with $121210695$ decimal digits.

### Why each hypothesis is needed

The theory in part 2 is $\mathsf{PA}$, and not every theory.
Part 3 shows that $\mathsf{PA}$ plus transfinite induction up to $\varepsilon_0$ proves the statement, and so does $\mathsf{ZFC}$.
So "independent" here always means "independent of $\mathsf{PA}$".

The notation must be hereditary.
If we write only the digits in base $b$ and leave the exponents alone, we get the *weak Goodstein sequence*.
Its ordinals stay below $\omega^\omega$, and $\mathsf{PA}$ proves that it reaches $0$.

The bases must not decrease.
A digit of base $b$ can be too large for a smaller base, and then the step has no meaning.
Every nondecreasing sequence of bases works, by the [[extended Goodstein theorem|3RVB1T9YDT]].

The subtraction of $1$ is needed.
Without it, $B_b$ alone never makes a positive number smaller, and the sequence $2, 3, 4, 5, \dots$ of $m = 2$ grows for ever.

### What it gives you

Let $L(m)$ be the least $k$ with $G_k = 0$.
Then $L(3) = 6$, and $L(4) = 3 \cdot 2^{402653211} - 2$, as computed above.
The [[Hardy hierarchy|X8RKXQASR9]] gives an exact formula,
$$L(m) = H_{o_2(m)}(3) - 2,$$
where $o_2(m)$ replaces every $2$ in the hereditary base-$2$ notation of $m$ by $\omega$.
For $m = 3$ this is $H_{\omega + 1}(3) - 2 = H_\omega(4) - 2 = 8 - 2 = 6$.
The [[proof|J1NTZCSPPM]] derives the formula.

The function $L$ is total and computable, but it is not [[provably total|Z742YPHPNS]] in $\mathsf{PA}$.
No function that $\mathsf{PA}$ proves total bounds it from some point on.
So the theorem gives a true $\Pi_2$ sentence about numbers, with no mention of logic or coding, that $\mathsf{PA}$ does not prove.
It is a concrete case of [[Gödel's incompleteness theorems|X9WYNYE29C]].

### The converse and single instances

Part 1 has no hypothesis except $m \in \mathbb{N}$, so it has no converse in the usual sense.
The useful contrast is between the general statement and its instances.
For a fixed numeral $m$, the sentence "the sequence of $m$ reaches $0$" is a true $\Sigma_1$ sentence.
$\mathsf{PA}$ proves every true $\Sigma_1$ sentence, so it proves each instance, for example the one for $m = 4$.
What $\mathsf{PA}$ cannot do is prove all instances with one proof.

### Generalizations

The [[extended Goodstein theorem|3RVB1T9YDT]] replaces the bases $2, 3, 4, \dots$ by any nondecreasing sequence of bases with $b_1 \ge 2$.
The [[Kirby-Paris hydra|C028FF4TWM]] and [[Beklemishev's worm principle|MHDZGDNEPS]] are other processes whose termination needs the ordinals up to $\varepsilon_0$.
The [[Buchholz hydra|9APRFM0G7F]] needs much larger ordinals, and its termination is not provable even in $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$.

### Watch out

The numbers $G_k$ do not decrease, so you cannot prove termination with a measure in $\mathbb{N}$.
In the sequence of $3$ the first three terms are all $3$, and in the sequence of $4$ the terms grow for more than $10^8$ steps.
The measure that works is the ordinal of the notation, which goes down at every step.

A second slip is to read part 2 as "Goodstein's theorem cannot be proved".
It has a short proof in $\mathsf{ZFC}$, given in the [[proof|J1NTZCSPPM]].
It is unprovable only in $\mathsf{PA}$.

### Try it

First, compute the sequence of $m = 2$.
The answer is $G_1 = 2 = 2^1$, then $G_2 = 3^1 - 1 = 2$, then $G_3 = 1$ and $G_4 = 0$, so $L(2) = 4$.

Second, check $L(2)$ with the formula.
Here $o_2(2) = \omega$, and $H_\omega(3) = H_3(3) = 6$, so $L(2) = 6 - 2 = 4$.

## History

Reuben Goodstein proved part 1 in 1944, in a paper on the "restricted ordinal theorem" in the Journal of Symbolic Logic.
Laurence Kirby and Jeff Paris proved part 2 in 1982, in "Accessible independence results for Peano arithmetic", the same paper that introduced the hydra game.
Their proof used non-standard models of arithmetic.
In 1983 Cichon gave a shorter proof through the Hardy hierarchy and the provably total functions of $\mathsf{PA}$.

## Explanations

### L1 human

Write $4$ with powers of $2$ only, even inside the exponents: $4 = 2^2$.
Change every $2$ into a $3$ and subtract $1$: $3^3 - 1 = 26$.
Write $26$ with powers of $3$, change every $3$ into a $4$ and subtract $1$, and you get $41$.
The numbers grow for a very long time, but the theorem says that they always come back to $0$ in the end.
For the start value $4$ this takes a number of steps with more than a hundred million digits.
The usual axioms of arithmetic cannot prove this fact, although it is true.

### L2 human

We run the ordinal method on the sequence of $3$.
Write each $G_k$ in hereditary base $k + 1$ and replace the base by $\omega$.
This gives an [[ordinal|0YSCSX5YZC]] $\alpha_k$ in [[Cantor normal form|6GD30FGYDZ]].
The term $G_1 = 2 + 1$ gives $\alpha_1 = \omega + 1$, and $G_2 = 3^1$ in base $3$ gives $\alpha_2 = \omega$.
The term $G_3 = 3$ is a digit in base $4$, so $\alpha_3 = 3$, and then $\alpha_4 = 2$, $\alpha_5 = 1$, $\alpha_6 = 0$.
The ordinals form the chain
$$\omega + 1 > \omega > 3 > 2 > 1 > 0,$$
which goes down at every step, although the numbers $3, 3, 3$ do not.
The example shows the typical use of ordinals: a process ends when some measure goes down at each step in a well-ordered set.

### L3 human

Goodstein's theorem is the well-foundedness of $\varepsilon_0$ along one primitive recursive descending path, written in the language of numbers.
The length function equals $H_{\alpha}(3) - 2$ with $\alpha < \varepsilon_0$, and this ties the theorem to the [[proof-theoretic ordinal|C72RBH0CDR]] $\varepsilon_0$ of $\mathsf{PA}$.
The same pattern, termination by ordinals and unprovability by growth rate, returns for the [[Kirby-Paris hydra|C028FF4TWM]], for [[worms|MHDZGDNEPS]] and in the [[Paris-Harrington theorem|509ZWA0R26]].
Stronger theories match larger ordinals, as in the [[Buchholz hydra|9APRFM0G7F]] and in [[Friedman's finite form of Kruskal's theorem|12XRGBWH59]].
Behind all of them stands [[Gentzen's consistency proof|QPV0HNP22S]] of 1936, which proved the consistency of $\mathsf{PA}$ by induction up to $\varepsilon_0$, and the [[ordinal analysis|C5E5TG8PGP]] that grew from it.
