; SICP Exercise 1.31
; Product of function values over a given range

(use-modules (ice-9 format))

(define (product term a next b)
  (if (> a b)
    1
    (* (term a)
       (product term (next a) next b))))

(define (factorial n)
  (define (term x) x)
  (define (next x) (+ x 1))
  (product term 1 next n))

; (pi/4) = [2/3 * 4/3] * [4/5 * 6/5] * [6/7 * 8/7] * ...
; (pi/2) = 2/1 * [2/3 * 4/3] * [4/5 * 6/5] * [6/7 * 8/7] * ...
;        = [2/1 * 2/3] * [4/3 * 4/5] * [6/5 * 6/7] * ...
;        = PRODUCT{i=1 to inf} [(2*i)/(2*i-1) * (2*i)/(2*i+1)]
;     pi = 2 * PRODUCT{i=1 to inf} [(2*i)/(2*i-1) * (2*i)/(2*i+1)]
(define (approx-pi n-terms)
  (define (term x) (* (/ (* 2 x) 
                         (- (* 2 x) 1))
                       (/ (* 2 x) 
                          (+ (* 2 x) 1))))
  (define (next x) (+ x 1))
  (* 2
     (product term 1 next n-terms)))

(format #t "1! = ~d\n" (factorial 1))
(format #t "2! = ~d\n" (factorial 2))
(format #t "3! = ~d\n" (factorial 3))
(format #t "4! = ~d\n" (factorial 4))
(format #t "5! = ~d\n" (factorial 5))
(newline)
(format #t "(64   terms) pi = ~f\n" (approx-pi 64))
(format #t "(128  terms) pi = ~f\n" (approx-pi 128))
(format #t "(256  terms) pi = ~f\n" (approx-pi 256))
(format #t "(512  terms) pi = ~f\n" (approx-pi 512))
(format #t "(1024 terms) pi = ~f\n" (approx-pi 1024))
