---
tag: PCXE6QYCDR
kind: example
name: Exponentiation is provably total in IΣ1
msc: ["03F30"]
topics: [T6FK1E7GJ1]
audience: grad
instance_of: [Z742YPHPNS]
uses: [Z742YPHPNS, 1QD0KDDGYJ, CV2E6JZHVP]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_function
    locator: Relationship to recursive functions
---

## Example

To prove that $2^x$ always exists, we prove by induction that the list $1, 2, 4, \dots, 2^x$ can always be written down.
For $x = 3$ the list is $\langle 1, 2, 4, 8 \rangle$: it has length $4$, it starts at $1$, each entry is twice the one before, and its last entry is $8 = 2^3$.

We show that $x \mapsto 2^x$ is [[provably total|Z742YPHPNS]] in $\mathrm{I}\Sigma_1$.
We use a standard coding of finite sequences by numbers, with $\mathrm{lh}(s)$ for the length and $(s)_i$ for the entry $i$.

1. Let $\varphi(x, y)$ say: there is $s$ with $\mathrm{lh}(s) = x + 1$, $(s)_0 = 1$, $(s)_{i+1} = 2 \cdot (s)_i$ for all $i < x$, and $(s)_x = y$.
2. The part after "there is $s$" has only bounded quantifiers, so $\varphi$ is a [[$\Sigma_1$|CV2E6JZHVP]] formula.
3. In $\mathbb{N}$, the only such $s$ is $\langle 1, 2, 4, \dots, 2^x \rangle$, by induction on $i$.
   So $\varphi$ defines the graph of $x \mapsto 2^x$.
4. Let $\psi(x)$ be $\exists y\, \varphi(x, y)$.
   It is again $\Sigma_1$, so the [[induction schema|1QD0KDDGYJ]] of $\mathrm{I}\Sigma_1$ applies to it.
5. Base: $\psi(0)$ holds with $s = \langle 1 \rangle$ and $y = 1$.
6. Step: from $\varphi(x, y)$ with witness $s$, let $s'$ be $s$ with the entry $2y$ added at the end.
   Then $\varphi(x + 1, 2y)$ holds with witness $s'$.
7. $\mathrm{I}\Sigma_1$ proves that $s'$ exists, because appending an entry to a coded sequence is a provably total operation of the coding.
8. By $\Sigma_1$ induction, $\mathrm{I}\Sigma_1 \vdash \forall x\, \psi(x)$, so $x \mapsto 2^x$ is provably total in $\mathrm{I}\Sigma_1$.

## Remarks

The same scheme proves every primitive recursive function total in $\mathrm{I}\Sigma_1$: write a $\Sigma_1$ formula that asserts a computation, and prove by $\Sigma_1$ induction that the computation can always be extended.
The converse, that $\mathrm{I}\Sigma_1$ proves only primitive recursive functions total, is the harder half of the theorem of Parsons and Mints.

Weaken the theory and the example breaks.
Bounded induction $\mathrm{I}\Delta_0$ does not prove that $2^x$ is total, because its provably total functions are bounded by polynomials, by a theorem of Parikh.
The induction in step 8 is on $\exists s\, (\dots)$, which is not bounded, and $\mathrm{I}\Delta_0$ cannot use it.
Strengthen the function instead, and the [[Ackermann function|SXAKCZYGVE]] needs an induction on a $\Pi_2$ formula, which $\mathrm{I}\Sigma_1$ lacks.

## Explanations

### L1 human

To show that $2^x$ always exists, we write down the list $1, 2, 4, \dots$ and prove by induction that the list can always be continued.
For example, from $\langle 1, 2, 4 \rangle$ we get $\langle 1, 2, 4, 8 \rangle$ by doubling the last entry.
The induction is on a statement of the form "there exists a list", and $\mathrm{I}\Sigma_1$ allows exactly this kind of induction.

### L2 human

We run the induction for $x = 0, 1, 2$ to see each step at work.
At $x = 0$ the witness is $s = \langle 1 \rangle$, with $(s)_0 = 1 = 2^0$.
The step doubles the last entry and appends it, so the witness for $x = 1$ is $\langle 1, 2 \rangle$ and the witness for $x = 2$ is $\langle 1, 2, 4 \rangle$.
Each witness checks the bounded part of $\varphi$: the length is $x + 1$, and each entry is twice the one before.
The example shows the typical use: one step of a primitive recursion is one step of an induction on a $\Sigma_1$ statement.
The trap is to forget that the computation must be coded as a single number $s$, since only then is the induction formula $\Sigma_1$.
