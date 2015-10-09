; SICP Exercise 1.41
; Higher-order procedure

(use-modules (ice-9 format))

(define (double f)
  (lambda (x) (f (f x))))

(define (inc x) (+ x 1))

(define (square x) (* x x))

(format #t "1+1     = ~d\n" (inc 1))
(format #t "(1+1)+1 = ~d\n" ((double inc) 1))
(newline)
(format #t "2^2     = ~d\n" (square 2))
(format #t "(2^2)^2 = ~d\n" ((double square) 2))
