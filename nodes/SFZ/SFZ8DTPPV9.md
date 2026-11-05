---
tag: SFZ8DTPPV9
kind: proof
name: Proof of Gauss's lemma (primitivity)
msc: [13F20]
proves: N20H6ZBTQR
sources:
  - wikipedia: en:2310971@r1354460683
    locator: Gauss's lemma (polynomials), section The lemma over the integers
    note: adopted
    mention: wikipedia://en/2310971#3TCP
    sections: [Proof]
---

## Proof

**Proof:** Clearly the product *f*(*x*)*g*(*x*) of two primitive polynomials has integer coefficients. Therefore, if it is not primitive, there must be a prime *p* which is a common divisor of all its coefficients. But *p* cannot divide all the coefficients of either *f*(*x*) or *g*(*x*) (otherwise they would not be primitive). Let *a*<sub>*r*</sub>*x*<sup>*r*</sup> be the first term of *f*(*x*) not divisible by *p* and let *b*<sub>*s*</sub>*x*<sup>*s*</sup> be the first term of *g*(*x*) not divisible by *p*. Now consider the term *x*<sup>*r*+*s*</sup> in the product, whose coefficient is

$$\cdots + a_{r+2} b_{s-2} + a_{r+1} b_{s-1} + a_r b_s + a_{r-1} b_{s+1} + a_{r-2} b_{s+2} + \cdots .$$

The term *a*<sub>*r*</sub>*b*<sub>*s*</sub> is not divisible by *p* (because *p* is prime), yet all the remaining ones are, so the entire sum cannot be divisible by *p*. By assumption all coefficients in the product are divisible by *p*, leading to a contradiction. Therefore, the coefficients of the product can have no common divisor and are thus primitive. $\square$

The proof is given below for the more general case. Note that an [[irreducible element|052SDEPZH7]] of **Z** (a prime number) is still irreducible when viewed as constant polynomial in **Z**\[*X*\]; this explains the need for "non-constant" in the statement.
