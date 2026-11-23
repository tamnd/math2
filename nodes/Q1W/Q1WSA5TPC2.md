---
tag: Q1WSA5TPC2
kind: example
name: The doubling indicator is not an indicator for models of PA
msc: ["03C62"]
topics: [T6FK1E7GJ1]
audience: research
not_instance_of:
  - target: JWTZ8NVVGK
    note: the doubling indicator is non-standard on some pairs that no initial segment satisfying PA separates, so it is not an indicator for the class of models of PA
uses: [JWTZ8NVVGK, K470Y7R628, 1QWN5CV4CG, MPSCREYC3M]
sources:
  - url: https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic
    locator: Structure of countable non-standard models
---

## Example

Between an infinite number $c$ and its square $c^2$ there is room for infinitely many doublings, but there is no room for a model of arithmetic.
So the doubling count reports a gap where no model of $\mathsf{PA}$ fits.

Let $M$ be a countable [[non-standard model|1QWN5CV4CG]] of [[Peano arithmetic|MPSCREYC3M]], and let $\mathcal{K}$ be the class of the cuts $I$ of $M$ with $I \models \mathsf{PA}$, where $I$ carries the operations of $M$.
Let $Y(a, b) = \max \{ c : a \cdot 2^c \le b \}$ be the [[doubling indicator|K470Y7R628]], for $1 \le a \le b$.
We check that $Y$ is not an [[indicator|JWTZ8NVVGK]] for $\mathcal{K}$, because condition 3 of the definition fails.

1. Let $c \in M$ be non-standard, so $c \ge 2$.
   Put $a = c$ and $b = c^2$.
2. Dividing by $c$, the condition $c \cdot 2^k \le c^2$ is the same as $2^k \le c$.
   So $Y(c, c^2)$ is the greatest $k$ with $2^k \le c$.
3. Each standard $k$ has $2^k$ standard, so $2^k < c$.
   So $Y(c, c^2) \ge k$ for each standard $k$, and $Y(c, c^2)$ is non-standard.
4. Let $I$ be a cut with $c \in I$ and $I \models \mathsf{PA}$.
   Then $I$ is closed under multiplication, so $c^2 = c \cdot c \in I$.
5. So no $I \in \mathcal{K}$ has $c \in I < c^2$, although $Y(c, c^2)$ is non-standard.
6. This breaks condition 3 of the definition, so $Y$ is not an indicator for $\mathcal{K}$.

## Remarks

The other direction of condition 3 still holds.
Every cut that is a model of $\mathsf{PA}$ is closed under doubling, so the [[doubling indicator|K470Y7R628]] is non-standard whenever such a cut separates $a$ from $b$.
So $Y$ errs in one direction only: it reports a gap where there is no model of $\mathsf{PA}$.

The same failure happens for any indicator built from one fixed fast function.
Let $E(x) = 2^x$, and count how many times we can apply $E$ to $a$ and stay at or below $b$.
The pair $(c, E^c(c))$, with $E$ applied $c$ times, gives the non-standard count $c$.
But $\mathsf{PA}$ proves that $x \mapsto E^x(x)$ is total, so every model of $\mathsf{PA}$ that contains $c$ also contains $E^c(c)$.
A model of $\mathsf{PA}$ is closed under every function that $\mathsf{PA}$ proves total, and no single such function is enough to detect it.
That is why the indicator for $\mathcal{K}$ in the [[Paris-Harrington proof|D0Q498H0R5]] needs a principle that $\mathsf{PA}$ does not prove.

## Explanations

### L1 human

The doubling count between $c$ and $c^2$ is infinite when $c$ is infinite, because $c$ can be halved again and again, any finite number of times.
But a model of arithmetic that contains $c$ must contain $c \cdot c$.
So this count sees a gap where no model of arithmetic fits, and it cannot detect such models.

### L2 human

The check uses one pair, $(c, c^2)$, and one closure property of models of $\mathsf{PA}$, closure under multiplication.
We can see the size of $Y(c, c^2)$ on ordinary numbers too: for $c = 1000$ the greatest $k$ with $2^k \le 1000$ is $9$, since $2^9 = 512$ and $2^{10} = 1024$.
So $Y(c, c^2)$ is about $\log_2 c$, which is infinite when $c$ is infinite.

The typical use is to see why an indicator for models of $\mathsf{PA}$ needs a strong principle such as the Paris-Harrington principle.
The trap is to think that the doubling indicator is wrong: it is correct for its own class of cuts, and it fails only for the smaller class of models of $\mathsf{PA}$.
