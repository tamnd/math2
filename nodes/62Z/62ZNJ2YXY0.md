---
tag: 62ZNJ2YXY0
kind: example
name: The totality of exponentiation has no feasibly constructive proof
msc: ["03F30"]
topics: [RA380RWEC0]
audience: research
not_instance_of:
  - target: H1B2VD0KVP
    note: the value 2^x has length x + 1, which is exponential in the length of x, so no polynomial-time function and no PV symbol computes it
uses: [FMM44KFZQT, H1B2VD0KVP, GVT2NKN37K]
sources:
  - url: https://en.wikipedia.org/wiki/Cobham%27s_thesis
    locator: lead section
---

## Example

The input $1024$ has $11$ binary digits, but $2^{1024}$ has $1025$.
Let $E(x) = 2^x$.
The usual proof of $\forall x \, \exists y \, (y = 2^x)$ uses ordinary induction on $x$ with the step $2^{x + 1} = 2^x + 2^x$.
We show that no [[feasibly constructive proof|H1B2VD0KVP]] of this statement exists, in the sense that no $\mathsf{PV}$ symbol computes $E$.
We write $\lvert x \rvert$ for the number of binary digits of $x$.

1. For each symbol $f$ of [[PV|FMM44KFZQT]] there is a polynomial $p_f$ with $\lvert f(\bar x) \rvert \le p_f(\lvert \bar x \rvert)$.
   This follows by induction on the definition of $f$, and the bounding condition of limited recursion on notation gives the step.
2. In binary, $2^x$ is $1$ followed by $x$ zeros, so $\lvert E(x) \rvert = x + 1$.
3. Take $x = 2^k$, so $\lvert x \rvert = k + 1$.
   For a fixed polynomial $p$, we have $2^k + 1 > p(k + 1)$ for all large $k$, since an exponential outgrows every polynomial.
4. For example, with $p(n) = n^3$ and $k = 12$ we get $x = 4096$ and the comparison below.
   $$\lvert E(4096) \rvert = 4097 > 2197 = 13^3 = p(13).$$
5. By steps 1 to 3, no $\mathsf{PV}$ symbol equals $E$ on all inputs.
   So the existence of $2^x$ is not witnessed by any feasibly constructive proof.

## Remarks

The non-example shows that feasibility concerns the length of the output as well as the running time.
A function with exponentially long values cannot be polynomial-time, because a machine needs one step to write each digit.

The ordinary proof by induction on $x$ is constructive, and in [[elementary function arithmetic|2JD80TE553]] it is a correct proof.
But it describes a computation with $x$ doubling steps, and $x$ is exponential in $\lvert x \rvert$.

What changes when the exponent is the length?
The function $x \mapsto 2^{\lvert x \rvert}$ has a value with $\lvert x \rvert + 1$ digits, so it is polynomial-time.
It has a feasibly constructive definition by recursion on notation.

## Explanations

### L1 human

Writing $2^{100}$ in binary needs $101$ digits.
The input $100$ needs only $7$ binary digits.
As the input grows, the output becomes much longer than any fixed power of the input length.
A fast program cannot even write down such an answer, so no fast proof can give it.

### L2 human

Let us compare the input length and the output length of $E(x) = 2^x$ for three powers of $2$.
For $x = 8$ the lengths are $\lvert 8 \rvert = 4$ and $\lvert 2^8 \rvert = 9$.
For $x = 64$ they are $\lvert 64 \rvert = 7$ and $\lvert 2^{64} \rvert = 65$.
For $x = 1024$ they are $\lvert 1024 \rvert = 11$ and $\lvert 2^{1024} \rvert = 1025$.
In general, for $x = 2^j$ we have $\lvert x \rvert = j + 1$, so the output length is the following:
$$\lvert 2^x \rvert = 2^j + 1 = 2^{\lvert x \rvert - 1} + 1.$$
That is exponential in $\lvert x \rvert$, and the comparison is a quick test of the growth condition before you look for a feasible proof.
Watch out: do not confuse $2^x$ with $2^{\lvert x \rvert}$, which lies between $x$ and $2x$ for $x \ge 1$ and is feasible.
