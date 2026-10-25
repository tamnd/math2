module

public import Mathlib.Basic.Real.Basic
public import Mathlib.Order.MinMax
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# Interval certificates

An interval certificate shows that a polynomial with rational coefficients is positive at each real point of a closed interval. The polynomial is a list of coefficients, the constant first, and `eval` computes it by the Horner rule.

The checker uses interval arithmetic on exact rationals, so it has no rounding error. It cuts the interval at the points of the certificate. On each piece it computes an interval that holds all the values of the polynomial, and it checks that the lower end of that interval is positive. The certificate is only the list of cut points. A tool finds the cut points, and the checker does not trust it.

A computation node with an interval certificate reaches E5 when `decide +kernel` proves `check p lo hi cuts = true`. Do not use `native_decide`, because it adds `Lean.ofReduceBool`.
-/

@[expose] public section

namespace Math2.Cert.Interval

/-- A closed interval with rational ends. -/
structure Box where
  /-- The lower end. -/
  lo : ℚ
  /-- The upper end. -/
  hi : ℚ
deriving Repr, DecidableEq

/-- `X.Mem x` says that the real number `x` is in `X`. -/
def Box.Mem (X : Box) (x : ℝ) : Prop :=
  (X.lo : ℝ) ≤ x ∧ x ≤ X.hi

/-- The interval sum. -/
def Box.add (X Y : Box) : Box :=
  ⟨X.lo + Y.lo, X.hi + Y.hi⟩

/-- The interval product. Its ends are the least and the greatest product of two ends. -/
def Box.mul (X Y : Box) : Box :=
  ⟨min (min (X.lo * Y.lo) (X.lo * Y.hi)) (min (X.hi * Y.lo) (X.hi * Y.hi)),
   max (max (X.lo * Y.lo) (X.lo * Y.hi)) (max (X.hi * Y.lo) (X.hi * Y.hi))⟩

/-- The value at `x` of the polynomial with the coefficients `p`, the constant first. -/
noncomputable def eval : List ℚ → ℝ → ℝ
  | [], _ => 0
  | c :: p, x => c + x * eval p x

/-- `evalBox p X` is an interval that holds the values of `p` on `X`. It follows the Horner rule. -/
def evalBox : List ℚ → Box → Box
  | [], _ => ⟨0, 0⟩
  | c :: p, X => Box.add ⟨c, c⟩ (Box.mul X (evalBox p X))

/-- `checkFrom p a hi cuts` checks that `p` is positive on `[a, hi]`, with the cut points `cuts`. -/
def checkFrom (p : List ℚ) (a hi : ℚ) : List ℚ → Bool
  | [] => decide (0 < (evalBox p ⟨a, hi⟩).lo)
  | t :: cuts => decide (0 < (evalBox p ⟨a, t⟩).lo) && checkFrom p t hi cuts

/-- `check p lo hi cuts` is true when the cut points `cuts` show that `p` is positive on `[lo, hi]`. The pieces are `[lo, t₁]`, `[t₁, t₂]` and so on to `[tₖ, hi]`. -/
def check (p : List ℚ) (lo hi : ℚ) (cuts : List ℚ) : Bool :=
  checkFrom p lo hi cuts

theorem Box.mem_add {X Y : Box} {x y : ℝ} (hx : X.Mem x) (hy : Y.Mem y) :
    (X.add Y).Mem (x + y) := by
  simp only [Box.Mem, Box.add, Rat.cast_add] at *
  constructor <;> linarith [hx.1, hx.2, hy.1, hy.2]

/-- A product `x * y` with `x` in `[a, b]` is between `a * y` and `b * y`. -/
theorem mul_between {a b x : ℝ} (ha : a ≤ x) (hb : x ≤ b) (y : ℝ) :
    min (a * y) (b * y) ≤ x * y ∧ x * y ≤ max (a * y) (b * y) := by
  rcases le_total 0 y with hy | hy
  · exact ⟨min_le_of_left_le (by nlinarith), le_max_of_le_right (by nlinarith)⟩
  · exact ⟨min_le_of_right_le (by nlinarith), le_max_of_le_left (by nlinarith)⟩

theorem Box.mem_mul {X Y : Box} {x y : ℝ} (hx : X.Mem x) (hy : Y.Mem y) :
    (X.mul Y).Mem (x * y) := by
  have h := mul_between hx.1 hx.2 y
  have hl := mul_between hy.1 hy.2 (X.lo : ℝ)
  have hh := mul_between hy.1 hy.2 (X.hi : ℝ)
  simp only [mul_comm _ (X.lo : ℝ), mul_comm _ (X.hi : ℝ)] at hl hh
  simp only [Box.Mem, Box.mul, Rat.cast_min, Rat.cast_max, Rat.cast_mul]
  exact ⟨(min_le_min hl.1 hh.1).trans h.1, h.2.trans (max_le_max hl.2 hh.2)⟩

theorem mem_evalBox {X : Box} {x : ℝ} (hx : X.Mem x) (p : List ℚ) :
    (evalBox p X).Mem (eval p x) := by
  induction p with
  | nil => simp [Box.Mem, evalBox, eval]
  | cons c p ih =>
    exact Box.mem_add (x := (c : ℝ)) ⟨le_rfl, le_rfl⟩ (Box.mem_mul hx ih)

theorem checkFrom_sound {p : List ℚ} {a hi : ℚ} {cuts : List ℚ}
    (h : checkFrom p a hi cuts = true) {x : ℝ} (ha : (a : ℝ) ≤ x) (hh : x ≤ hi) :
    0 < eval p x := by
  induction cuts generalizing a with
  | nil =>
    simp only [checkFrom, decide_eq_true_eq] at h
    have := (mem_evalBox (X := ⟨a, hi⟩) ⟨ha, hh⟩ p).1
    exact lt_of_lt_of_le (by exact_mod_cast h) this
  | cons t cuts ih =>
    simp only [checkFrom, Bool.and_eq_true, decide_eq_true_eq] at h
    rcases le_total x t with hx | hx
    · exact lt_of_lt_of_le (by exact_mod_cast h.1) (mem_evalBox (X := ⟨a, t⟩) ⟨ha, hx⟩ p).1
    · exact ih h.2 hx

/-- The checker is sound: when it accepts, `p` is positive at each real point of `[lo, hi]`. -/
theorem sound {p : List ℚ} {lo hi : ℚ} {cuts : List ℚ} (h : check p lo hi cuts = true)
    {x : ℝ} (hlo : (lo : ℝ) ≤ x) (hhi : x ≤ hi) : 0 < eval p x :=
  checkFrom_sound h hlo hhi

end Math2.Cert.Interval
