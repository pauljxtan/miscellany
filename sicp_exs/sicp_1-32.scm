; SICP Exercise 1.32
; Generalized accumulation function (abstraction of sum, product, etc.)

(use-modules (ice-9 format))

(define (accumulate combiner null-value term a next b)
  (if (> a b)
    null-value
    (combiner (term a)
              (accumulate combiner null-value term (next a) next b))))

; Define (sum) as call to accumulate:
(define (sum term a next b)
  (define (add x y) (+ x y))
  (accumulate add 0 term a next b))

; Define (product) as call to accumulate:
(define (product term a next b)
  (define (multiply x y) (* x y))
  (accumulate multiply 1 term a next b))

(define (sum-to n)
  (define (term x) x)
  (define (next x) (+ x 1))
  (sum term 1 next n))

(define (factorial n)
  (define (term x) x)
  (define (next x) (+ x 1))
  (product term 1 next n))

(format #t "sum-to(8)  = ~d\n" (sum-to 8))
(format #t "sum-to(16) = ~d\n" (sum-to 16))
(format #t "sum-to(32) = ~d\n" (sum-to 32))
(newline)
(format #t "2! = ~d\n" (factorial 2))
(format #t "4! = ~d\n" (factorial 4))
(format #t "8! = ~d\n" (factorial 8))
